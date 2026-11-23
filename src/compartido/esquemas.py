from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field


# ==========================================
# 1. AUTENTICACIÓN Y TALLERES
# ==========================================

class TallerAuth(BaseModel):
    nombre: str = Field(..., min_length=1)
    contrasena: str = Field(..., min_length=4)

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ==========================================
# 2. CLIENTES
# ==========================================

# Lo que manda el cliente en POST /clientes o PUT /clientes/{id}
class ClienteCreate(BaseModel):
    nombre: str = Field(..., min_length=1)
    telefono: str
    email: str

# Lo que responde el servidor en GET /clientes (hereda los campos de arriba y suma el id)
class ClienteOut(ClienteCreate):
    id: UUID


# ==========================================
# 3. TÉCNICOS
# ==========================================

class TecnicoCreate(BaseModel):
    nombre: str = Field(..., min_length=1)
    telefono: str
    email: str
    especialidad: str

class TecnicoOut(TecnicoCreate):
    id: UUID


# ==========================================
# 4. REPARACIONES
# ==========================================

class ReparacionCreate(BaseModel):
    cliente_id: UUID
    tecnico_id: UUID
    descripcion: str = Field(..., min_length=1)
    coste: float = Field(..., ge=0)  # ge=0 impide costes negativos automáticamente
    estado: str = "Pendiente"

class ReparacionOut(ReparacionCreate):
    id: UUID
    fecha: datetime