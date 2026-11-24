from PySide6.QtWidgets import QDialog

from cliente.cliente_api import ClienteAPI, ErrorAPI
from cliente.vista.login_register import Ui_Dialog


class VentanaLogin(QDialog):
    def __init__(self, api: ClienteAPI):
        super().__init__()

        self.api = api
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.connect_events()
        self.hide_error()

    def hide_error(self):
        self.ui.widget_login.hide()
        self.ui.widget_register.hide()

    def check_login(self):
        condicion = self.ui.line_login_nombre.text() != "" and self.ui.line_login_password.text() != ""
        self.ui.but_login_login.setEnabled(condicion)

    def check_register(self):
        condicion = self.ui.line_register_nombre.text() != "" and self.ui.line_register_password.text() != ""
        self.ui.but_register_register.setEnabled(condicion)

    def login(self):
        try:
            self.api.login(self.ui.but_login_login.text(), self.ui.but_register_register.text())
            self.accept()
        except ErrorAPI as e:
            self.ui.widget_login.setVisible(True)
            self.ui.widget_login.setText(str(e))

    def register(self):
        try:
            self.api.registrar_taller(self.ui.line_register_nombre.text(), self.ui.line_register_password.text())
            self.api.login(self.ui.line_register_nombre.text(), self.ui.line_register_password.text())
            self.accept()
        except ErrorAPI as e:
            self.ui.widget_login.setVisible(True)
            self.ui.widget_login.setText(str(e))

    def connect_events(self):
        #Login
        self.ui.line_login_nombre.textChanged.connect(self.check_login)
        self.ui.line_login_password.textChanged.connect(self.check_login)
        self.ui.but_login_login.clicked.connect(self.login)
        #Password
        self.ui.line_register_nombre.textChanged.connect(self.check_register)
        self.ui.line_register_password.textChanged.connect(self.check_register)
        self.ui.but_register_register.clicked.connect(self.register)