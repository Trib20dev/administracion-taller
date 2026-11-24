from PySide6.QtWidgets import QDialog

from cliente.cliente_api import ClienteAPI
from cliente.vista.login_register import Ui_Dialog


class VentanaLogin(QDialog):
    def __init__(self, api: ClienteAPI):
        super().__init__()

        self.api = api
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.connect_events()

    def check_login(self):
        pass

    def check_register(self):
        pass

    def login(self):
        pass

    def register(self):
        pass

    def connect_events(self):
        pass