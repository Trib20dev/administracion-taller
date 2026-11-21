import sys

from PySide6.QtWidgets import QApplication

from cliente.vista import MiVentanaPrincipal


def main():
    app = QApplication(sys.argv)
    ventana = MiVentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()