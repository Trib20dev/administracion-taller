import os
from datetime import datetime, timedelta, timezone

from fastapi import HTTPException, Depends
from fastapi import status
import jwt
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials
from jwt import InvalidTokenError

from compartido.esquemas import ClienteOut, TecnicoOut, ReparacionOut, ClienteCreate, TecnicoCreate, ReparacionCreate, \
    TokenResponse, TallerAuth
from servidor.persistencia import GestorTaller, PersistenciaTaller
from servidor.modelos import *

load_dotenv() #Cargar el .env

SECRET_KEY = os.getenv("SECRET_KEY")#Carga la clave secreta de cifrado
if not SECRET_KEY:
    raise RuntimeError("Falta definir SECRET_KEY en el archivo .env")
ALGORITMO = "HS256"
HORAS_EXPIRACION = 8

app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)
gestor = GestorTaller() #El gestor de datitos de mi taller
esquema_bearer = HTTPBearer() #esquema de autenticación mediante Bearer Token

def crear_token_jwt(nombre_taller: str) -> str:
    expiracion = datetime.now(timezone.utc) + timedelta(hours=HORAS_EXPIRACION)
    payload = {
        "sub": nombre_taller,  # Aquí va grabado el nombre del taller
        "exp": expiracion      # Caducidad automática
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITMO)

def verificar_token_jwt(token: str) -> str:
    """Valida el JWT y devuelve el nombre del taller, o lanza HTTPException 401."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITMO])
        nombre_taller: str | None = payload.get("sub")
        if not nombre_taller:
            raise HTTPException(status_code=401, detail="Token sin identificador de taller")
        return nombre_taller
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido o caducado")


def obtener_db(credenciales: HTTPAuthorizationCredentials = Depends(esquema_bearer)) -> PersistenciaTaller:
    nombre_taller = verificar_token_jwt(credenciales.credentials)
    return PersistenciaTaller(nombre_taller)

# -- ENDPOINTS --

# -  Autenticación y Registro de Talleres  -
@app.post("/talleres", status_code=status.HTTP_201_CREATED)
def registrar_taller(datos: TallerAuth):
    try:
        gestor.crear_taller(datos.nombre, datos.contrasena)
        return {"mensaje": f"Taller '{datos.nombre}' registrado correctamente"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/login", response_model=TokenResponse)
def login(datos: TallerAuth):
    if not gestor.validar_taller(datos.nombre, datos.contrasena):
        raise HTTPException(status_code=401, detail="Taller o contraseña incorrectos")

    token = crear_token_jwt(datos.nombre)
    return TokenResponse(access_token=token)


# -  Crear Entidades -
@app.post("/clientes", response_model=ClienteOut, status_code=status.HTTP_201_CREATED)
def create_cliente(datos: ClienteCreate, db: PersistenciaTaller = Depends(obtener_db)):
    clientes = db.cargar_clientes()
    nuevo_cliente = Cliente(
        nombre=datos.nombre,
        numero=datos.numero,
        email=datos.email
    )

    clientes[nuevo_cliente.id] = nuevo_cliente
    db.guardar_clientes(clientes)

    return ClienteOut(id=nuevo_cliente.id, **nuevo_cliente.to_dict())


@app.post("/tecnicos", response_model=TecnicoOut, status_code=status.HTTP_201_CREATED)
def create_tecnico(datos: TecnicoCreate, db: PersistenciaTaller = Depends(obtener_db)):
    tecnicos = db.cargar_tecnicos()
    nuevo_tecnico = Tecnico(
        nombre=datos.nombre,
        especialidad=datos.especialidad
    )
    tecnicos[nuevo_tecnico.id] = nuevo_tecnico
    db.guardar_tecnicos(tecnicos)

    return TecnicoOut(id=nuevo_tecnico.id, **nuevo_tecnico.to_dict())


@app.post("/reparaciones", response_model=ReparacionOut, status_code=status.HTTP_201_CREATED)
def create_reparacion(datos: ReparacionCreate, db: PersistenciaTaller = Depends(obtener_db)):
    # Verificamos integridad referencial antes de crear
    if datos.cliente not in db.cargar_clientes():
        raise HTTPException(status_code=404, detail="El cliente asignado no existe")
    if datos.tecnico not in db.cargar_tecnicos():
        raise HTTPException(status_code=404, detail="El técnico asignado no existe")

    reparaciones = db.cargar_reparaciones()
    nueva_reparacion = Reparacion(
        cliente=datos.cliente,
        tecnico=datos.tecnico,
        equipo=datos.equipo,
        descripcion=datos.descripcion,
        coste=datos.coste,
        estado=datos.estado
    )
    reparaciones[nueva_reparacion.id] = nueva_reparacion
    db.guardar_reparaciones(reparaciones)

    return ReparacionOut(id=nueva_reparacion.id, **nueva_reparacion.to_dict())

# -  Obtener  -
@app.get("/clientes")
def read_clientes(db: PersistenciaTaller = Depends(obtener_db)):
    clientes = db.cargar_clientes()
    return [ClienteOut(id=uid, **cliente.to_dict()) for uid, cliente in clientes.items()]

@app.get("/tecnicos")
def read_tecnicos(db: PersistenciaTaller = Depends(obtener_db)):
    tecnicos = db.cargar_tecnicos()
    return [TecnicoOut(id=uid, **tecnico.to_dict()) for uid, tecnico in tecnicos.items()]

@app.get("/reparaciones")
def read_reparaciones(db: PersistenciaTaller = Depends(obtener_db)):
    reparaciones = db.cargar_reparaciones()
    return [ReparacionOut(id=uid, **reparacion.to_dict()) for uid, reparacion in reparaciones.items()]

# -  Actualizar  -
@app.put("/clientes/{cliente}", response_model=ClienteOut)
def update_cliente(
    cliente: UUID,
    datos: ClienteCreate,
    db: PersistenciaTaller = Depends(obtener_db)
    ):
    clientes = db.cargar_clientes()
    if cliente not in clientes:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    # Reconstruimos el cliente conservando su cliente original
    cliente_actualizado = Cliente(
        nombre=datos.nombre,
        numero=datos.numero,
        email=datos.email,
        uid=cliente
    )
    clientes[cliente] = cliente_actualizado
    db.guardar_clientes(clientes)

    return ClienteOut(id=cliente, **cliente_actualizado.to_dict())


@app.put("/tecnicos/{tecnico}", response_model=TecnicoOut)
def update_tecnico(
    tecnico: UUID,
    datos: TecnicoCreate,
    db: PersistenciaTaller = Depends(obtener_db)
):
    tecnicos = db.cargar_tecnicos()
    if tecnico not in tecnicos:
        raise HTTPException(status_code=404, detail="Técnico no encontrado")

    tecnico_actualizado = Tecnico(
        nombre=datos.nombre,
        especialidad=datos.especialidad,
        uid=tecnico
    )
    tecnicos[tecnico] = tecnico_actualizado
    db.guardar_tecnicos(tecnicos)

    return TecnicoOut(id=tecnico, **tecnico_actualizado.to_dict())


@app.put("/reparaciones/{reparacion}", response_model=ReparacionOut)
def update_reparacion(
    reparacion: UUID,
    datos: ReparacionCreate,
    db: PersistenciaTaller = Depends(obtener_db)
):
    reparaciones = db.cargar_reparaciones()
    if reparacion not in reparaciones:
        raise HTTPException(status_code=404, detail="Reparación no encontrada")

    # Verificamos que el cliente y el técnico asignados sigan existiendo en el taller
    if datos.cliente not in db.cargar_clientes():
        raise HTTPException(status_code=404, detail="El cliente asignado no existe")
    if datos.tecnico not in db.cargar_tecnicos():
        raise HTTPException(status_code=404, detail="El técnico asignado no existe")

    reparacion_actualizada = Reparacion(
        cliente=datos.cliente,
        tecnico=datos.tecnico,
        equipo=datos.equipo,
        descripcion=datos.descripcion,
        coste=datos.coste,
        estado=datos.estado,
        uid=reparacion
    )
    reparaciones[reparacion] = reparacion_actualizada
    db.guardar_reparaciones(reparaciones)

    return ReparacionOut(id=reparacion, **reparacion_actualizada.to_dict())

# -  Eliminar  -
@app.delete("/clientes/{cliente}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cliente(cliente: UUID, db: PersistenciaTaller = Depends(obtener_db)):
    clientes = db.cargar_clientes()
    if cliente not in clientes:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    reparaciones = db.cargar_reparaciones()
    if any(r.cliente == cliente for r in reparaciones.values()):
        raise HTTPException(status_code=400, detail="No se puede borrar: el cliente tiene reparaciones asignadas")

    del clientes[cliente]

    db.guardar_clientes(clientes)


@app.delete("/tecnicos/{tecnico}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tecnico(tecnico: UUID, db: PersistenciaTaller = Depends(obtener_db)):
    tecnicos = db.cargar_tecnicos()
    if tecnico not in tecnicos:
        raise HTTPException(status_code=404, detail="Técnico no encontrado")

    reparaciones = db.cargar_reparaciones()
    if any(r.tecnico == tecnico for r in reparaciones.values()):
        raise HTTPException(status_code=400, detail="No se puede borrar: el técnico tiene reparaciones asignadas")

    del tecnicos[tecnico]
    db.guardar_tecnicos(tecnicos)


@app.delete("/reparaciones/{reparacion}", status_code=status.HTTP_204_NO_CONTENT)
def delete_reparacion(reparacion: UUID, db: PersistenciaTaller = Depends(obtener_db)):
    reparaciones = db.cargar_reparaciones()
    if reparacion not in reparaciones:
        raise HTTPException(status_code=404, detail="Reparación no encontrada")

    del reparaciones[reparacion]
    db.guardar_reparaciones(reparaciones)
