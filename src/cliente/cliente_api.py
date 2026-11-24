# src/cliente/cliente_api.py
from uuid import UUID
import requests
from compartido.esquemas import ClienteCreate, ClienteOut, TallerAuth, TecnicoOut, TecnicoCreate, ReparacionOut, \
    ReparacionCreate


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
            try:
                detalle = respuesta.json().get("detail", "Error desconocido en el servidor")
            except ValueError:
                detalle = f"Error del servidor ({respuesta.status_code}): {respuesta.text}"
            raise ErrorAPI(str(detalle))

        if respuesta.status_code == 204 or not respuesta.content:
            return None

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

    # --- Clientes ---
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

    def actualizar_cliente(self, cliente_id: UUID, cliente: ClienteCreate) -> ClienteOut:
        res = requests.put(
            f"{self.url_base}/clientes/{cliente_id}",
            json=cliente.model_dump(mode="json"),
            headers=self._headers
        )
        data = self._manejar_respuesta(res)
        return ClienteOut(**data)

    def borrar_cliente(self, cliente_id: UUID) -> None:
        res = requests.delete(f"{self.url_base}/clientes/{cliente_id}", headers=self._headers)
        self._manejar_respuesta(res)

    # --- Tecnicos ---
    def listar_tecnicos(self) -> list[TecnicoOut]:
        res = requests.get(f"{self.url_base}/tecnicos", headers=self._headers)
        data = self._manejar_respuesta(res)
        return [TecnicoOut(**item) for item in data]

    def crear_tecnico(self, tecnico: TecnicoCreate) -> TecnicoOut:
        res = requests.post(
            f"{self.url_base}/tecnicos",
            json=tecnico.model_dump(mode="json"),
            headers=self._headers
        )
        data = self._manejar_respuesta(res)
        return TecnicoOut(**data)

    def actualizar_tecnico(self, tecnico_id: UUID, tecnico: TecnicoCreate) -> TecnicoOut:
        res = requests.put(
            f"{self.url_base}/tecnicos/{tecnico_id}",
            json=tecnico.model_dump(mode="json"),
            headers=self._headers
        )
        data = self._manejar_respuesta(res)
        return TecnicoOut(**data)

    def borrar_tecnico(self, tecnico_id: UUID) -> None:
        res = requests.delete(f"{self.url_base}/tecnicos/{tecnico_id}", headers=self._headers)
        self._manejar_respuesta(res)

    # --- Reparaciones ---
    def listar_reparaciones(self) -> list[ReparacionOut]:
        res = requests.get(f"{self.url_base}/reparaciones", headers=self._headers)
        data = self._manejar_respuesta(res)
        return [ReparacionOut(**item) for item in data]

    def crear_reparacion(self, reparacion: ReparacionCreate) -> ReparacionOut:
        res = requests.post(
            f"{self.url_base}/reparaciones",
            json=reparacion.model_dump(mode="json"),
            headers=self._headers
        )
        data = self._manejar_respuesta(res)
        return ReparacionOut(**data)

    def actualizar_reparacion(self, reparacion_id: UUID, reparacion: ReparacionCreate) -> ReparacionOut:
        res = requests.put(
            f"{self.url_base}/reparaciones/{reparacion_id}",
            json=reparacion.model_dump(mode="json"),
            headers=self._headers
        )
        data = self._manejar_respuesta(res)
        return ReparacionOut(**data)

    def borrar_reparacion(self, reparacion_id: UUID) -> None:
        res = requests.delete(f"{self.url_base}/reparaciones/{reparacion_id}", headers=self._headers)
        self._manejar_respuesta(res)