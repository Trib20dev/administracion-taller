import json
from pathlib import Path
from typing import Any

from src.modelos import Taller

def guardar_datos(nombre:str, datos: dict[str,Any]):
    with open(f'./datos/{nombre}.store', 'w', encoding="utf-8") as json_file:
        json.dump(datos, json_file, indent=4,ensure_ascii=False)

def cargar_taller(nombre:str) ->  Taller:
    ruta = Path(f"./datos/{nombre}.store")

    if not ruta.exists():
        return Taller(nombre)
    else:
        return Taller.importar(nombre,ruta)