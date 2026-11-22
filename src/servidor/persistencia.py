import json
from pathlib import Path
from uuid import UUID

from modelos import Reparacion, Tecnico, Cliente, Persona
from src.modelos import Taller


class Persistencia:

    def __init__(self, nombre: str) -> None:
        self.taller = Path('./datos/'+nombre)
        self.taller.mkdir(parents = True, exist_ok = True)

    def guadar_clientes(self, datos: dict[UUID,Cliente]):
        ruta = self.taller / "clientes.json"
        with open(ruta, 'w', encoding="utf-8") as json_file:
            json.dump({'clientes': {str(cliente.id): cliente.to_dict() for cliente in datos.values()}},
                      json_file,
                      indent = 4,
                      ensure_ascii = False)

    def guadar_tecnicos(self, datos: dict[UUID,Tecnico]):
        ruta = self.taller / "tecnicos.json"
        with open(ruta, 'w', encoding="utf-8") as json_file:
            json.dump({'tecnicos': {str(tecnico.id): tecnico.to_dict() for tecnico in datos.values()}},
                      json_file,
                      indent=4,
                      ensure_ascii=False)

    def guadar_reparaciones(self, datos: dict[UUID,Reparacion]):
        ruta = self.taller / "reparaciones.json"
        with open(ruta, 'w', encoding="utf-8") as json_file:
            json.dump({'reparaciones': {str(reparacion.id): reparacion.to_dict() for reparacion in datos.values()}},
                      json_file,
                      indent=4,
                      ensure_ascii=False)

    def cargar_clientes(self) -> dict[UUID,Cliente]:
        ruta = self.taller / "clientes.json"
        if not ruta.exists():
            return {}
        with open(ruta, 'r', encoding="utf-8") as json_file:
            datos = json.load(json_file)
        clientes = {uuid: Cliente.from_dict(uuid,cliente) for uuid, cliente in datos.items()}
        return clientes

    def cargar_tecnicos(self) -> dict[UUID,Tecnico]:
        ruta = self.taller / "tecnicos.json"
        if not ruta.exists():
            return {}
        with open(ruta, 'r', encoding="utf-8") as json_file:
            datos = json.load(json_file)
        tecnicos = {uuid: Tecnico.from_dict(uuid,tecnico) for uuid, tecnico in datos.items()}
        return tecnicos

    def cargar_reparaciones(self) -> dict[UUID,Reparacion]:
        ruta = self.taller / "reparaciones.json"
        if not ruta.exists():
            return {}
        with open(ruta, 'r', encoding="utf-8") as json_file:
            datos = json.load(json_file)
        reparaciones = {uuid: Reparacion.from_dict(uuid,reparacion) for uuid, reparacion in datos.items()}
        return reparaciones