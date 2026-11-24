import json
import uuid
from pathlib import Path
from typing import Type, TypeVar
from uuid import UUID

import bcrypt

from servidor.modelos import Reparacion, Tecnico, Cliente

T = TypeVar("T", Cliente, Tecnico, Reparacion)

# Resuelve siempre a la carpeta 'datos/' en la raíz del proyecto, sin importar desde dónde ejecutes
BASE_DATOS = Path(__file__).resolve().parents[2] / "datos"


class GestorTaller:

    def __init__(self):
        self.ruta = BASE_DATOS / "talleres.json"
        self.ruta.parent.mkdir(parents=True, exist_ok=True)

    def crear_taller(self, nombre: str, contrasena: str):
        talleres = {}
        if self.ruta.exists():
            with open(self.ruta, "r", encoding="utf-8") as json_file:
                talleres = json.load(json_file)

        if nombre in talleres:
            raise ValueError("El taller ya existe")

        id_taller = str(uuid.uuid4())
        talleres[nombre] = {
            "id": id_taller,
            "nombre": nombre,
            "contrasena": bcrypt.hashpw(contrasena.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        }

        (BASE_DATOS / id_taller).mkdir(parents=True, exist_ok=True)
        with open(self.ruta, "w", encoding="utf-8") as json_file:
            json.dump(talleres, json_file, indent=4, ensure_ascii=False)

        db = PersistenciaTaller(nombre)
        db.guardar_clientes({})
        db.guardar_tecnicos({})
        db.guardar_reparaciones({})

    def validar_taller(self, nombre: str, contrasena: str) -> bool:
        if not self.ruta.exists():
            return False

        with open(self.ruta, "r", encoding="utf-8") as json_file:
            talleres = json.load(json_file)

        taller = talleres.get(nombre)
        if taller is None:
            return False

        contrasena_hasheada = taller["contrasena"]
        return bcrypt.checkpw(contrasena.encode("utf-8"), contrasena_hasheada.encode("utf-8"))


class PersistenciaTaller:

    def __init__(self, nombre: str) -> None:
        with open(BASE_DATOS / "talleres.json", "r", encoding="utf-8") as json_file:
            talleres = json.load(json_file)
        self.id = talleres[nombre]["id"]
        self.taller = BASE_DATOS / self.id

    def _guardar(self, nombre_fichero: str, datos: dict):
        ruta = self.taller / nombre_fichero
        with open(ruta, "w", encoding="utf-8") as json_file:
            json.dump(
                {str(uid): objeto.to_dict() for uid, objeto in datos.items()},
                json_file,
                indent=4,
                ensure_ascii=False
            )

    def _cargar(self, nombre_fichero: str, clase: Type[T]) -> dict[UUID, T]:
        ruta = self.taller / nombre_fichero
        if not ruta.exists():
            return {}
        with open(ruta, "r", encoding="utf-8") as json_file:
            datos = json.load(json_file)
        return {UUID(uid_str): clase.from_dict(uid_str, item) for uid_str, item in datos.items()}

    def guardar_clientes(self, datos: dict[UUID, Cliente]):
        self._guardar("clientes.json", datos)

    def guardar_tecnicos(self, datos: dict[UUID, Tecnico]):
        self._guardar("tecnicos.json", datos)

    def guardar_reparaciones(self, datos: dict[UUID, Reparacion]):
        self._guardar("reparaciones.json", datos)

    def cargar_clientes(self) -> dict[UUID, Cliente]:
        return self._cargar("clientes.json", Cliente)

    def cargar_tecnicos(self) -> dict[UUID, Tecnico]:
        return self._cargar("tecnicos.json", Tecnico)

    def cargar_reparaciones(self) -> dict[UUID, Reparacion]:
        return self._cargar("reparaciones.json", Reparacion)