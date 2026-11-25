# Administración de Taller

## Pequeña explicación
Aplicación cliente-servidor desarrollada en Python que permite gestionar de forma multiusuario la información de distintos talleres de reparación. Facilita la administración de clientes, técnicos y reparaciones a través de una interfaz gráfica de escritorio (PySide6) conectada mediante peticiones HTTP a una API REST propia (FastAPI), garantizando la persistencia y el aislamiento de datos por taller.

## Estructura
El proyecto se divide en tres paquetes principales dentro de `src/` (`cliente`, `servidor` y `compartido`), además de los archivos necesarios para su despliegue mediante contenedores Docker:

```text
administracion-taller/
│
├── main.py                     # Punto de entrada de la aplicación cliente
├── Dockerfile                  # Imagen Docker para el servidor FastAPI
├── docker-compose.yml          # Orquestación del servicio y volúmenes
├── requirements.txt            # Dependencias del proyecto
├── .env.example                # Plantilla de variables de entorno
├── .dockerignore
├── .gitignore
├── README.md
│
├── datos/                      # Almacenamiento persistente aislado por UUID de taller
│   └── <uuid-taller>/
│       ├── clientes.json
│       ├── tecnicos.json
│       └── reparaciones.json
│
└── src/
    ├── cliente/                # Lógica de conexión HTTP y vistas PySide6
    │   ├── cliente_api.py
    │   └── vista/
    ├── servidor/               # API REST, autenticación JWT, modelos y persistencia
    │   ├── api.py
    │   ├── modelos.py
    │   ├── persistencia.py
    │   └── seguridad.py
    └── compartido/             # Esquemas Pydantic compartidos entre cliente y servidor
        └── esquemas.py
```

## Instalación y ejecución en local

### 1. Configuración previa
Instala las dependencias necesarias en tu entorno virtual:
```bash
python -m pip install -r requirements.txt
```
Crea un archivo `.env` en la raíz del proyecto tomando como referencia `.env.example` para definir la URL del servidor y la clave secreta de firma de tokens:
```env
API_URL=[http://127.0.0.1:8000](http://127.0.0.1:8000)
SECRET_KEY=tu_clave_secreta_segura
```

### 2. Ejecución del servidor
Inicia el backend con Uvicorn apuntando al directorio `src`:
```bash
uvicorn servidor.api:app --host 0.0.0.0 --port 8000 --app-dir src --reload
```

### 3. Ejecución del cliente de escritorio
Desde el directorio raíz, ejecuta:
```bash
python main.py
```

## Despliegue en producción (Docker, Portainer y Nginx)

El servidor está preparado para ejecutarse en un contenedor aislado y exponerse de forma segura mediante HTTPS detrás de un proxy inverso.

### 1. Despliegue en Portainer desde Git
1. Accede a **Portainer** $\rightarrow$ **Stacks** $\rightarrow$ **+ Add stack**.
2. Selecciona **Repository**, introduce la URL del repositorio de GitHub, indica la rama (`master`) y establece `docker-compose.yml` como ruta del archivo (*Compose path*).
3. En la sección **Environment variables**, añade la variable `SECRET_KEY` con una clave segura (no es necesario subir ningún archivo `.env` al repositorio).
4. Pulsa **Deploy the stack**. El contenedor construirá la imagen desde el `Dockerfile`, mapeará el puerto local `127.0.0.1:8095` al puerto `8000` interno de Uvicorn y montará un volumen persistente en `/app/datos`.

*(Para actualizar la aplicación tras nuevos cambios en el repositorio, basta con entrar al Stack y pulsar **Pull and redeploy**).*

### 2. Configuración del proxy inverso (Nginx + SSL)
1. Crea el bloque de servidor en `/etc/nginx/sites-available/api-taller`:
   ```nginx
   server {
       listen 80;
       listen [::]:80;
       server_name api.tudominio.com;

       location / {
           proxy_pass [http://127.0.0.1:8095](http://127.0.0.1:8095);
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```
2. Habilita el sitio y recarga Nginx:
   ```bash
   sudo ln -s /etc/nginx/sites-available/api-taller /etc/nginx/sites-enabled/
   sudo nginx -t && sudo systemctl reload nginx
   ```
3. Genera e instala el certificado SSL con Certbot:
   ```bash
   sudo certbot --nginx -d api.tudominio.com
   ```

### 3. Conexión del cliente de escritorio al servidor desplegado
En el equipo donde se ejecute la interfaz gráfica, configura el archivo `.env` apuntando al dominio público con HTTPS (sin incluir `SECRET_KEY`):
```env
API_URL=[https://api.tudominio.com](https://api.tudominio.com)
```

## Persistencia y arquitectura cliente-servidor
A diferencia de la versión anterior basada en archivos locales `.store`, toda la persistencia recae ahora en el servidor:

* **Aislamiento multi-taller:** Al iniciar la aplicación cliente aparece un diálogo de inicio de sesión y registro (`LoginDialog`). Cada taller registrado recibe un identificador único (`UUID`) y un directorio exclusivo dentro de `datos/<uuid-taller>/` con sus propios ficheros `clientes.json`, `tecnicos.json` y `reparaciones.json`.
* **Autenticación JWT:** Tras autenticarse, el servidor emite un token *Bearer* que el cliente adjunta automáticamente en las cabeceras de cada petición (`ClienteAPI`), asegurando que cada taller solo pueda consultar y modificar sus propios registros.
* **Validación compartida:** Tanto el cliente como el servidor utilizan los mismos esquemas de Pydantic (`src/compartido/esquemas.py`), validando tipos (`UUID`), longitudes mínimas y restricciones (como costes no negativos o especialidades válidas) antes y después de viajar por la red.

## Decisiones de diseño
La ventana principal sigue siendo una `QMainWindow` con un `QStackedWidget` central cuya página visible cambia según la acción seleccionada en la barra de menú superior, ahora alimentada de forma dinámica desde la API:

El menú se conforma por 4 apartados:
* **Fichero**: Acceso a estadísticas, opciones de importación/exportación (en desarrollo) y cierre de la aplicación (`Ctrl+Q`).
* **Administrar clientes**
* **Administrar técnicos**
* **Administrar reparaciones**

Cada menú de administración mantiene las tres vistas principales:
* **Crear**: Formulario que valida los datos mediante esquemas Pydantic y envía una petición `POST` al servidor.
* **Actualizar**: Selector de registros existentes para modificar sus campos (`PUT`) o eliminarlos (`DELETE`).
* **Tabla**: Vista tabular sincronizada con los datos del servidor (`GET`).

## Mejoras incorporadas
* **Integridad referencial en el servidor:** El backend impide eliminar clientes o técnicos (`HTTP 400`) si tienen reparaciones asociadas, evitando referencias rotas en la tabla de reparaciones.
* **Despliegue contenerizado:** Preparación completa mediante `Dockerfile` y `docker-compose.yml` para despliegue automatizado desde repositorio Git en Portainer y publicación segura tras Nginx.
* **Filtros y ordenación en tablas:**
  * *Clientes:* filtro por nombre.
  * *Técnicos:* filtro por nombre y especialidad (`software` / `hardware`).
  * *Reparaciones:* filtro por nombre de técnico, cliente asignado y estado, además de ordenación por fecha, coste, cliente, técnico o estado.
* **Indicador visual de sesión:** El título de la ventana principal muestra el taller activo conectado en ese momento (por ejemplo, `Tabla Reparaciones - hector`).

## Pendiente de incorporar
* **Cerrar sesión (`Logout`):** Añadir una acción en el menú *Fichero* que limpie el token activo en el cliente y permita volver al diálogo de inicio de sesión para cambiar de taller sin tener que reiniciar la aplicación.
* **Importar y exportar datos en JSON (`Import from json` / `Export as json`):** Aunque las acciones ya figuran en el menú *Fichero*, queda pendiente conectar su lógica para realizar copias de seguridad locales o cargas masivas contra los endpoints de la API.
* **Ventana o indicador de carga:** Incorporar un diálogo de espera o barra de progreso durante las peticiones HTTP iniciales y operaciones de red para mejorar la respuesta visual ante conexiones lentas.
* **Validación exhaustiva de campos:** Ampliar las comprobaciones de formato en correo electrónico y números de teléfono en los esquemas de validación.