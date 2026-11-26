# Administración de Taller

## Pequeña explicación
Sistema multiplataforma con arquitectura cliente-servidor para la gestión multiusuario de talleres de reparación. Permite administrar clientes, técnicos y reparaciones mediante una API REST propia (FastAPI) con aislamiento de datos por taller, acompañada de un cliente de escritorio completo (PySide6) y una aplicación móvil de consulta (Flutter).

## Estructura del proyecto
El repositorio sigue una estructura unificada (*monorepo*) dividida en el backend/cliente de escritorio en Python (`src/`) y la aplicación móvil en Dart/Flutter (`app_movil/`):

```text
administracion-taller/
│
├── main.py                     # Punto de entrada del cliente de escritorio (PySide6)
├── Dockerfile                  # Imagen Docker para el servidor FastAPI
├── docker-compose.yml          # Orquestación del contenedor y volúmenes persistentes
├── requirements.txt            # Dependencias de Python (servidor y escritorio)
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
├── src/
│   ├── cliente/                # Lógica HTTP y vistas gráficas de escritorio (PySide6)
│   │   ├── cliente_api.py
│   │   └── vista/
│   ├── servidor/               # API REST, seguridad JWT, modelos y persistencia
│   │   ├── api.py
│   │   ├── modelos.py
│   │   ├── persistencia.py
│   │   └── seguridad.py
│   └── compartido/             # Esquemas Pydantic compartidos entre cliente y servidor
│       └── esquemas.py
│
└── app_movil/                  # Aplicación móvil de consulta (Flutter / Dart)
    ├── pubspec.yaml
    ├── .env.example
    └── lib/
        ├── main.dart
        ├── core/
        │   ├── mi_material.dart
        │   ├── router.dart
        │   ├── models/         # Modelos de datos (Cliente, Tecnico, Reparacion)
        │   ├── providers/      # Gestión de estado con Provider (TallerProvider)
        │   └── services/       # Cliente HTTP con Dio e interceptor JWT (ApiService)
        └── screens/            # Pantallas de acceso y consulta (LoginScreen, HomeScreen)
```

## Instalación y ejecución en local

### 1. Backend (FastAPI) y Cliente de Escritorio (PySide6)
1. Instala las dependencias de Python en tu entorno virtual:
   ```bash
   python -m pip install -r requirements.txt
   ```
2. Crea un archivo `.env` en la raíz tomando como referencia `.env.example`:
   ```env
   API_URL=[http://127.0.0.1:8000](http://127.0.0.1:8000)
   SECRET_KEY=tu_clave_secreta_segura
   ```
3. Arranca el servidor en local:
   ```bash
   uvicorn servidor.api:app --host 0.0.0.0 --port 8000 --app-dir src --reload
   ```
4. En otra terminal, lanza la interfaz de escritorio:
   ```bash
   python main.py
   ```

### 2. Aplicación Móvil (Flutter)
1. Accede al directorio de la app móvil e instala las dependencias de Dart (`dio`, `provider`, `go_router`, `flutter_dotenv`):
   ```bash
   cd app_movil
   flutter pub get
   ```
2. Crea su archivo `.env` a partir de `app_movil/.env.example` indicando la URL del servidor (incluyendo el protocolo `http://` o `https://`):
   ```env
   API_URL=[https://api.tudominio.com](https://api.tudominio.com)
   ```
3. Ejecuta la aplicación en un emulador o dispositivo físico:
   ```bash
   flutter run
   ```

## Despliegue del servidor con Docker

El backend está contenerizado y preparado para desplegarse con **Docker Compose** en cualquier servidor o máquina con Docker instalado.

1. Clona el repositorio en el servidor:
   ```bash
   git clone [https://github.com/Trib20dev/administracion-taller.git](https://github.com/Trib20dev/administracion-taller.git)
   cd administracion-taller
   ```
2. Crea el archivo `.env` en la raíz (o define la variable en el entorno del sistema/orquestador) con la clave secreta para la firma de tokens JWT:
   ```env
   SECRET_KEY=tu_clave_secreta_segura
   ```
3. Construye la imagen y levanta el contenedor en segundo plano:
   ```bash
   docker compose up -d --build
   ```
   * El contenedor ejecuta Uvicorn en el puerto interno `8000` (mapeado al puerto local configurado en `docker-compose.yml`).
   * Los datos de los talleres se almacenan de forma persistente en el volumen Docker asociado a `/app/datos`.
4. *(Opcional — Producción)* Para exponer la API en internet mediante HTTPS, coloca un proxy inverso (como **Nginx**, **Caddy** o **Traefik**) delante del puerto local del contenedor y apunta el `API_URL` del cliente de escritorio y de la app móvil al dominio configurado.

## Arquitectura y decisiones de diseño

### Backend y Persistencia Multi-taller
* **Aislamiento por UUID:** Cada taller registrado recibe un identificador único (`UUID`) y un directorio exclusivo en `datos/<uuid-taller>/` con sus propios ficheros `clientes.json`, `tecnicos.json` y `reparaciones.json`.
* **Autenticación JWT:** El endpoint `/login` emite un token *Bearer* que tanto el cliente de escritorio como la app móvil adjuntan automáticamente en cada petición.
* **Integridad referencial:** El servidor impide eliminar clientes o técnicos (`HTTP 400`) mientras tengan reparaciones asociadas.

### Cliente de Escritorio (PySide6)
* Basado en una `QMainWindow` con un `QStackedWidget` central y barra de menú superior (*Fichero*, *Administrar clientes*, *Administrar técnicos*, *Administrar reparaciones*).
* Incluye formularios de creación (`POST`), modificación/borrado (`PUT`/`DELETE`), tablas sincronizadas (`GET`) con filtros dinámicos, ordenación de reparaciones y ventana de estadísticas.

### Aplicación Móvil de Consulta (Flutter)
* **Arquitectura desacoplada:** Separación entre capa de red (`ApiService` con `Dio` e interceptor automático del token JWT) y gestión de estado (`TallerProvider` con `ChangeNotifier`), cargando clientes, técnicos y reparaciones en paralelo (`Future.wait`) y cruzando sus nombres mediante mapas indexados por UUID.
* **Navegación y diseño:** Enrutamiento declarativo con `GoRouter` (`LoginScreen` y `HomeScreen`). La pantalla principal utiliza un `PageView` sincronizado con una barra inferior (`NavigationBar`) dividido en 4 vistas:
  * **Reparaciones:** Tarjetas compactas con filtro rápido por estado (`ChoiceChip`), recarga *pull-to-refresh* y hoja modal inferior (`showModalBottomSheet`) con el detalle completo de cada avería.
  * **Clientes:** Listado con datos de contacto.
  * **Técnicos:** Listado con especialidad asignada.
  * **Resumen:** Panel de estadísticas con ingresos totales, conteo de registros y desglose de reparaciones por estado.

## Pendiente de incorporar
* **Cerrar sesión (`Logout`) en escritorio:** Añadir la opción en el menú *Fichero* de PySide6 para limpiar el token activo y volver al diálogo de inicio de sesión sin cerrar la aplicación.
* **Importar y exportar datos en JSON (`Import from json` / `Export as json`):** Conectar las opciones ya presentes en el menú *Fichero* del cliente de escritorio para generar y restaurar copias de seguridad completas del taller.
* **Indicador de carga en escritorio:** Añadir un diálogo o cursor de espera durante las peticiones de red en PySide6.
* **Validación exhaustiva de campos:** Reforzar la validación de formatos de correo electrónico y teléfono en `src/compartido/esquemas.py`.