import json
from pathlib import Path
from typing import Any

from src.modelos import Taller


class Persistencia:

    def __init__(self, nombre: str) -> None:
        self.taller = Path('./datos/'+nombre)
        self.taller.mkdir(parents = True, exist_ok = True)

    def guadar_clientes(self, datos: dict[str,Any]):
        ruta = self.taller / "clientes.json"
        with open(ruta, 'w', encoding="utf-8") as json_file:
            json.dump(datos, json_file, indent = 4, ensure_ascii = False)

    def guadar_tecnicos(self, datos: dict[str,Any]):
        ruta = self.taller / "tecnicos.json"
        with open(ruta, 'w', encoding="utf-8") as json_file:
            json.dump(datos, json_file, indent = 4, ensure_ascii = False)

    def guadar_reparaciones(self, datos: dict[str,Any]):
        with open(str(self.taller.absolute()) + '/reparaciones.json', 'w', encoding="utf-8") as json_file:
            json.dump(datos, json_file, indent = 4, ensure_ascii = False)


    def guardar_datos(nombre:str, datos: dict[str,Any]):
        with open(f'./datos/{nombre}.store', 'w', encoding="utf-8") as json_file:
            json.dump(datos, json_file, indent=4,ensure_ascii=False)

    def cargar_taller(nombre:str) ->  Taller:
        ruta = Path(f"./datos/{nombre}.store")

        if not ruta.exists():
            return Taller(nombre)
        else:
            return Taller.importar(nombre,ruta)