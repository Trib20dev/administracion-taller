# Administracion de taller

## Pequeña explicación
Aplicación de escritorio desarrollada en Python que permite gestionar de forma sencilla la información de un taller de reparación. Facilita la administración de clientes, técnicos y reparaciones, ofreciendo operaciones para crear, consultar y modificar registros, así como almacenar los datos de forma persistente mediante archivos `.store`.

## Estructura
Esta compuesto por pocos archivos, y se lanza con el comando normal de python empleando el archivo `main.py` ubicado en la raiz del proyecto

``` text
ProyectoRepasoGráfico/
│
├── main.py
├── datos/
├── src/
│   ├── vista/
│   │   ├── ui_ventana.py
│   │   ├── Ventana.py
│   │   └── Ventana.ui
│   ├── modelos.py
│   └── persistencia.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Instalación y jecucion
1. Instala las dependencias necesarias
``` bash 
python -m pip install -r requirements.txt
```
2. Para iniciar la aplicación, ejecuta desde el directorio raiz el comando
``` bash
python main.py
```

## Persistencia
El programa se inicia cargando el archivo `MI TALLER.store` si este existe.
En caso contrario, al guardar sin abrir un fichero diferente, utiliza un nuevo archivo con ese nombre.

Por defecto, el archivo se encuentra en el directorio de almacenamiento
`datos`, el cual no se puede alterar.

Puedes abrir otro archivo con el mismo final `.store` empleando la accion **Cargar tienda** o pulsando `ctrl + o`.
Internamente ese fichero es un json sin encriptar, así que puede ser analizado comodamente con un editor de texto.

## Decisiones de diseño
La ventana principal es una `QMainWindow`, con un único elemento principal, un `QStackedWidget` el cual cambia la página visible en base a la accion presionada en el menú superior.

El menu en cuestion se conforma por 4 apartados:
- **Fichero**:
Funciones de persistencia y llamado a la ventana de estadísticas
- **Administrar clientes**
- **Administrar técnicos**
- **Administrar reparaciones**

Los menus de administración contienen las mismas tres opciones:
- **Crear**:
Que contiene una página con un formulario para crear un nuevo elemento
- **Actualizar**: Que te permite seleccionar un elemento y modificar sus campos
- **Tabla**: Te lleva a una pagina con una tabla en la que puedes ver el conjunto de registros de forma clara y visual

## Mejoras incorporadas
Se incluyo la posibilidad de emplear filtros en las distintas tablas, concretamente:
- Clientes: filtro por nombre
- Tecnicos: filtro por nombre y especialidad
- Reparaciones: filtro por nombre de tecnico, cliente asignado y estado de la reparación

Se implemento también una pregunta de seguridad al intentar cerrar o abrir un nuevo archivo sin guardar los cambios realizados

Se puede apreciar de forma visual si actualmente hay cambios sin guardar porque se implemento en el título la habitual funcionalidad de hacer aparecer `*` junto al título al estar el archivo modificado

Como última adición destacable, se añadio la posibilidad de ordenar las reparaciones en base a distintos campos:
- Fecha de inserción
- Coste
- Cliente
- Tecnico
- Estado

## Realización de pruebas
Para poder realizar pruebas de la funcionalidad de la aplicacion se añadio a datos el archivo `Transatlantique.store`, generado con unos 50 elementos para cada campo.

## Pendiente de incorporar
- **Integridad de referencias**: Puedes eliminar clientes o técnicos aunque esten incluidos en reparaciones, lo cual lanzara un error al intentar acceder a la tabla de reparaciones posteriormente

- **Exhaustiva corrección de campos**: El correo solo comprueba que tenga una arroba, y el número no comprueba absolutamente nada