import os
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, Depends

import jwt
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.openapi.models import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials
from jwt import InvalidTokenError

from servidor.persistencia import GestorTaller, PersistenciaTaller

load_dotenv() #Cargar el .env

SECRET_KEY = os.getenv("SECRET_KEY") #Carga la clave secreta de cifrado
ALGORITMO = "HS256"
HORAS_EXPIRACION = 8

app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)
gestor = GestorTaller() #El gestor de datitos de mi taller
esquema_bearer = HTTPBearer() #esquema de autenticación mediante Bearer Token

@app.get("/")
def read_root():
    return None

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


def obtener_db(
    credenciales: HTTPAuthorizationCredentials = Depends(esquema_bearer)
) -> PersistenciaTaller:
    nombre_taller = verificar_token_jwt(credenciales.credentials)
    return PersistenciaTaller(nombre_taller)