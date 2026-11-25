import sys

from PySide6.QtWidgets import QApplication

from cliente.cliente_api import ClienteAPI
from cliente.vista import MiVentanaPrincipal
from cliente.vista.ui_login import DialogoLogin


def main():
    app = QApplication(sys.argv)
    api = ClienteAPI()
    if DialogoLogin(api).exec():
        ventana = MiVentanaPrincipal(api)
        ventana.show()
        sys.exit(app.exec())
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()