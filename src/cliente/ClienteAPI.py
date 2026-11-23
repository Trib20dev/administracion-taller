# src/cliente/cliente_api.py
from uuid import UUID
import requests
from compartido.esquemas import ClienteCreate, ClienteOut, TallerAuth


class ErrorAPI(Exception):
    """Excepción propia para que la ventana muestre un QMessageBox limpio."""
    pass


class ClienteAPI:
    def __init__(self, url_base: str = "http://127.0.0.1:8000"):
        self.url_base = url_base
        self._token: str | None = None

    @property
    def _headers(self) -> dict[str, str]:
        if not self._token:
            return {}
        return {"Authorization": f"Bearer {self._token}"}

    def _manejar_respuesta(self, respuesta: requests.Response):
        if respuesta.status_code == 401:
            self._token = None
            raise ErrorAPI("Sesión caducada o no autorizada. Vuelve a iniciar sesión.")
        if not respuesta.ok:
            # Extrae el 'detail' que devuelve FastAPI en los HTTPException
            detalle = respuesta.json().get("detail", "Error desconocido en el servidor")
            raise ErrorAPI(str(detalle))
        return respuesta.json()

    # --- Autenticación ---
    def login(self, nombre: str, contrasena: str) -> None:
        datos = TallerAuth(nombre=nombre, contrasena=contrasena)
        res = requests.post(f"{self.url_base}/login", json=datos.model_dump())
        data = self._manejar_respuesta(res)
        self._token = data["access_token"]

    def registrar_taller(self, nombre: str, contrasena: str) -> None:
        datos = TallerAuth(nombre=nombre, contrasena=contrasena)
        res = requests.post(f"{self.url_base}/talleres", json=datos.model_dump())
        self._manejar_respuesta(res)

    def cerrar_sesion(self) -> None:
        self._token = None

    # --- Clientes (ejemplo) ---
    def listar_clientes(self) -> list[ClienteOut]:
        res = requests.get(f"{self.url_base}/clientes", headers=self._headers)
        data = self._manejar_respuesta(res)
        return [ClienteOut(**item) for item in data]

    def crear_cliente(self, cliente: ClienteCreate) -> ClienteOut:
        res = requests.post(
            f"{self.url_base}/clientes",
            json=cliente.model_dump(mode="json"),
            headers=self._headers
        )
        data = self._manejar_respuesta(res)
        return ClienteOut(**data)

    def borrar_cliente(self, cliente_id: UUID) -> None:
        res = requests.delete(f"{self.url_base}/clientes/{cliente_id}", headers=self._headers)
        self._manejar_respuesta(res)