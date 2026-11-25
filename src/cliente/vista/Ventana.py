# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ventana.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTableView,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(630, 390)
        MainWindow.setMinimumSize(QSize(630, 390))
        self.action_guardar = QAction(MainWindow)
        self.action_guardar.setObjectName(u"action_guardar")
        self.action_abrir_tienda = QAction(MainWindow)
        self.action_abrir_tienda.setObjectName(u"action_abrir_tienda")
        self.action_salir = QAction(MainWindow)
        self.action_salir.setObjectName(u"action_salir")
        self.action_consultar_Modificar_cliente = QAction(MainWindow)
        self.action_consultar_Modificar_cliente.setObjectName(u"action_consultar_Modificar_cliente")
        self.action_consultar_clientes = QAction(MainWindow)
        self.action_consultar_clientes.setObjectName(u"action_consultar_clientes")
        self.action_consultar_Modificar_tecnico = QAction(MainWindow)
        self.action_consultar_Modificar_tecnico.setObjectName(u"action_consultar_Modificar_tecnico")
        self.action_consultar_tecnicos = QAction(MainWindow)
        self.action_consultar_tecnicos.setObjectName(u"action_consultar_tecnicos")
        self.action_consultar_Modificar_reparacion = QAction(MainWindow)
        self.action_consultar_Modificar_reparacion.setObjectName(u"action_consultar_Modificar_reparacion")
        self.action_consultar_reparaciones = QAction(MainWindow)
        self.action_consultar_reparaciones.setObjectName(u"action_consultar_reparaciones")
        self.action_crear_cliente = QAction(MainWindow)
        self.action_crear_cliente.setObjectName(u"action_crear_cliente")
        self.action_crear_tecnico = QAction(MainWindow)
        self.action_crear_tecnico.setObjectName(u"action_crear_tecnico")
        self.action_crear_reparacion = QAction(MainWindow)
        self.action_crear_reparacion.setObjectName(u"action_crear_reparacion")
        self.action_estadisticas = QAction(MainWindow)
        self.action_estadisticas.setObjectName(u"action_estadisticas")
        self.action_cerrar_sesion = QAction(MainWindow)
        self.action_cerrar_sesion.setObjectName(u"action_cerrar_sesion")
        self.action_import = QAction(MainWindow)
        self.action_import.setObjectName(u"action_import")
        self.action_export = QAction(MainWindow)
        self.action_export.setObjectName(u"action_export")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page_crear_cliente = QWidget()
        self.page_crear_cliente.setObjectName(u"page_crear_cliente")
        self.page_crear_cliente.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.page_crear_cliente)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lab_nombre_cliente = QLabel(self.page_crear_cliente)
        self.lab_nombre_cliente.setObjectName(u"lab_nombre_cliente")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lab_nombre_cliente)

        self.line_nombre_cliente = QLineEdit(self.page_crear_cliente)
        self.line_nombre_cliente.setObjectName(u"line_nombre_cliente")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.line_nombre_cliente)

        self.lab_email_cliente = QLabel(self.page_crear_cliente)
        self.lab_email_cliente.setObjectName(u"lab_email_cliente")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lab_email_cliente)

        self.line_email_cliente = QLineEdit(self.page_crear_cliente)
        self.line_email_cliente.setObjectName(u"line_email_cliente")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.line_email_cliente)

        self.lab_numero_cliente = QLabel(self.page_crear_cliente)
        self.lab_numero_cliente.setObjectName(u"lab_numero_cliente")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lab_numero_cliente)

        self.line_numero_cliente = QLineEdit(self.page_crear_cliente)
        self.line_numero_cliente.setObjectName(u"line_numero_cliente")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.line_numero_cliente)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.but_guardar_creacion_cliente = QPushButton(self.page_crear_cliente)
        self.but_guardar_creacion_cliente.setObjectName(u"but_guardar_creacion_cliente")
        self.but_guardar_creacion_cliente.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.but_guardar_creacion_cliente)

        self.but_limpiar_creacion_cliente = QPushButton(self.page_crear_cliente)
        self.but_limpiar_creacion_cliente.setObjectName(u"but_limpiar_creacion_cliente")

        self.horizontalLayout_2.addWidget(self.but_limpiar_creacion_cliente)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.stackedWidget.addWidget(self.page_crear_cliente)
        self.page_crear_tecnico = QWidget()
        self.page_crear_tecnico.setObjectName(u"page_crear_tecnico")
        self.verticalLayout = QVBoxLayout(self.page_crear_tecnico)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lab_nombre_tecnico = QLabel(self.page_crear_tecnico)
        self.lab_nombre_tecnico.setObjectName(u"lab_nombre_tecnico")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lab_nombre_tecnico)

        self.line_nombre_tecnico = QLineEdit(self.page_crear_tecnico)
        self.line_nombre_tecnico.setObjectName(u"line_nombre_tecnico")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.line_nombre_tecnico)

        self.lab_especialidad = QLabel(self.page_crear_tecnico)
        self.lab_especialidad.setObjectName(u"lab_especialidad")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lab_especialidad)

        self.combo_especialidad = QComboBox(self.page_crear_tecnico)
        self.combo_especialidad.addItem("")
        self.combo_especialidad.addItem("")
        self.combo_especialidad.setObjectName(u"combo_especialidad")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.combo_especialidad)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.but_guardar_creacion_tecnico = QPushButton(self.page_crear_tecnico)
        self.but_guardar_creacion_tecnico.setObjectName(u"but_guardar_creacion_tecnico")
        self.but_guardar_creacion_tecnico.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.but_guardar_creacion_tecnico)

        self.but_limpiar_creacion_tecnico = QPushButton(self.page_crear_tecnico)
        self.but_limpiar_creacion_tecnico.setObjectName(u"but_limpiar_creacion_tecnico")

        self.horizontalLayout_3.addWidget(self.but_limpiar_creacion_tecnico)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.page_crear_tecnico)
        self.page_crear_reparacion = QWidget()
        self.page_crear_reparacion.setObjectName(u"page_crear_reparacion")
        self.verticalLayout_4 = QVBoxLayout(self.page_crear_reparacion)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.lab_crear_reparacion_cliente = QLabel(self.page_crear_reparacion)
        self.lab_crear_reparacion_cliente.setObjectName(u"lab_crear_reparacion_cliente")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lab_crear_reparacion_cliente)

        self.widget_crear_reparacion_cliente = QWidget(self.page_crear_reparacion)
        self.widget_crear_reparacion_cliente.setObjectName(u"widget_crear_reparacion_cliente")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_crear_reparacion_cliente)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.line_crear_reparacion_cliente = QLineEdit(self.widget_crear_reparacion_cliente)
        self.line_crear_reparacion_cliente.setObjectName(u"line_crear_reparacion_cliente")
        self.line_crear_reparacion_cliente.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.line_crear_reparacion_cliente)

        self.but_crear_reparacion_cliente = QToolButton(self.widget_crear_reparacion_cliente)
        self.but_crear_reparacion_cliente.setObjectName(u"but_crear_reparacion_cliente")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.but_crear_reparacion_cliente.setIcon(icon)
        self.but_crear_reparacion_cliente.setAutoRaise(True)

        self.horizontalLayout_7.addWidget(self.but_crear_reparacion_cliente)


        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.widget_crear_reparacion_cliente)

        self.lab_crear_reparacion_tecnico = QLabel(self.page_crear_reparacion)
        self.lab_crear_reparacion_tecnico.setObjectName(u"lab_crear_reparacion_tecnico")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lab_crear_reparacion_tecnico)

        self.widget_crear_reparacion_tecnico = QWidget(self.page_crear_reparacion)
        self.widget_crear_reparacion_tecnico.setObjectName(u"widget_crear_reparacion_tecnico")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_crear_reparacion_tecnico)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.line_crear_reparacion_tecnico = QLineEdit(self.widget_crear_reparacion_tecnico)
        self.line_crear_reparacion_tecnico.setObjectName(u"line_crear_reparacion_tecnico")
        self.line_crear_reparacion_tecnico.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.line_crear_reparacion_tecnico)

        self.but_crear_reparacion_tecnico = QToolButton(self.widget_crear_reparacion_tecnico)
        self.but_crear_reparacion_tecnico.setObjectName(u"but_crear_reparacion_tecnico")
        self.but_crear_reparacion_tecnico.setIcon(icon)
        self.but_crear_reparacion_tecnico.setAutoRaise(True)

        self.horizontalLayout_8.addWidget(self.but_crear_reparacion_tecnico)


        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.widget_crear_reparacion_tecnico)

        self.lab_crear_reparacion_equipo = QLabel(self.page_crear_reparacion)
        self.lab_crear_reparacion_equipo.setObjectName(u"lab_crear_reparacion_equipo")

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lab_crear_reparacion_equipo)

        self.line_crear_reparacion_equipo = QLineEdit(self.page_crear_reparacion)
        self.line_crear_reparacion_equipo.setObjectName(u"line_crear_reparacion_equipo")

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.FieldRole, self.line_crear_reparacion_equipo)

        self.lab_crear_reparacion_descripcion = QLabel(self.page_crear_reparacion)
        self.lab_crear_reparacion_descripcion.setObjectName(u"lab_crear_reparacion_descripcion")

        self.formLayout_4.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lab_crear_reparacion_descripcion)

        self.line_crear_reparacion_descripcion = QLineEdit(self.page_crear_reparacion)
        self.line_crear_reparacion_descripcion.setObjectName(u"line_crear_reparacion_descripcion")

        self.formLayout_4.setWidget(3, QFormLayout.ItemRole.FieldRole, self.line_crear_reparacion_descripcion)

        self.lab_crear_reparacion_coste = QLabel(self.page_crear_reparacion)
        self.lab_crear_reparacion_coste.setObjectName(u"lab_crear_reparacion_coste")

        self.formLayout_4.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lab_crear_reparacion_coste)

        self.line_crear_reparacion_coste = QLineEdit(self.page_crear_reparacion)
        self.line_crear_reparacion_coste.setObjectName(u"line_crear_reparacion_coste")

        self.formLayout_4.setWidget(4, QFormLayout.ItemRole.FieldRole, self.line_crear_reparacion_coste)


        self.verticalLayout_4.addLayout(self.formLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.layout_crear_reparacion_botones = QHBoxLayout()
        self.layout_crear_reparacion_botones.setObjectName(u"layout_crear_reparacion_botones")
        self.but_crear_reparacion_guardar = QPushButton(self.page_crear_reparacion)
        self.but_crear_reparacion_guardar.setObjectName(u"but_crear_reparacion_guardar")
        self.but_crear_reparacion_guardar.setEnabled(False)

        self.layout_crear_reparacion_botones.addWidget(self.but_crear_reparacion_guardar)

        self.but_crear_reparacion_limpiar = QPushButton(self.page_crear_reparacion)
        self.but_crear_reparacion_limpiar.setObjectName(u"but_crear_reparacion_limpiar")

        self.layout_crear_reparacion_botones.addWidget(self.but_crear_reparacion_limpiar)


        self.verticalLayout_4.addLayout(self.layout_crear_reparacion_botones)

        self.lab_crear_reparacion_aviso = QLabel(self.page_crear_reparacion)
        self.lab_crear_reparacion_aviso.setObjectName(u"lab_crear_reparacion_aviso")

        self.verticalLayout_4.addWidget(self.lab_crear_reparacion_aviso)

        self.stackedWidget.addWidget(self.page_crear_reparacion)
        self.page_tabla_clientes = QWidget()
        self.page_tabla_clientes.setObjectName(u"page_tabla_clientes")
        self.verticalLayout_5 = QVBoxLayout(self.page_tabla_clientes)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lab_filter_cliente_nombre = QLabel(self.page_tabla_clientes)
        self.lab_filter_cliente_nombre.setObjectName(u"lab_filter_cliente_nombre")

        self.horizontalLayout_12.addWidget(self.lab_filter_cliente_nombre)

        self.line_filter_cliente_nombre = QLineEdit(self.page_tabla_clientes)
        self.line_filter_cliente_nombre.setObjectName(u"line_filter_cliente_nombre")

        self.horizontalLayout_12.addWidget(self.line_filter_cliente_nombre)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.table_clientes = QTableView(self.page_tabla_clientes)
        self.table_clientes.setObjectName(u"table_clientes")

        self.verticalLayout_5.addWidget(self.table_clientes)

        self.widget_botones_clientes = QWidget(self.page_tabla_clientes)
        self.widget_botones_clientes.setObjectName(u"widget_botones_clientes")
        self.widget_botones_clientes.setEnabled(True)
        self.horizontalLayout_9 = QHBoxLayout(self.widget_botones_clientes)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.but_select_clientes = QPushButton(self.widget_botones_clientes)
        self.but_select_clientes.setObjectName(u"but_select_clientes")
        self.but_select_clientes.setEnabled(False)

        self.horizontalLayout_9.addWidget(self.but_select_clientes)

        self.but_cancelar_clientes = QPushButton(self.widget_botones_clientes)
        self.but_cancelar_clientes.setObjectName(u"but_cancelar_clientes")

        self.horizontalLayout_9.addWidget(self.but_cancelar_clientes)


        self.verticalLayout_5.addWidget(self.widget_botones_clientes)

        self.stackedWidget.addWidget(self.page_tabla_clientes)
        self.page_tabla_tecnicos = QWidget()
        self.page_tabla_tecnicos.setObjectName(u"page_tabla_tecnicos")
        self.verticalLayout_6 = QVBoxLayout(self.page_tabla_tecnicos)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lab_filter_tecnico_nombre = QLabel(self.page_tabla_tecnicos)
        self.lab_filter_tecnico_nombre.setObjectName(u"lab_filter_tecnico_nombre")

        self.horizontalLayout_11.addWidget(self.lab_filter_tecnico_nombre)

        self.line_filter_tecnico_nombre = QLineEdit(self.page_tabla_tecnicos)
        self.line_filter_tecnico_nombre.setObjectName(u"line_filter_tecnico_nombre")

        self.horizontalLayout_11.addWidget(self.line_filter_tecnico_nombre)

        self.lab_filter_tecnico_especialidad = QLabel(self.page_tabla_tecnicos)
        self.lab_filter_tecnico_especialidad.setObjectName(u"lab_filter_tecnico_especialidad")

        self.horizontalLayout_11.addWidget(self.lab_filter_tecnico_especialidad)

        self.combo_filter_tecnico_especialidad = QComboBox(self.page_tabla_tecnicos)
        self.combo_filter_tecnico_especialidad.addItem("")
        self.combo_filter_tecnico_especialidad.addItem("")
        self.combo_filter_tecnico_especialidad.addItem("")
        self.combo_filter_tecnico_especialidad.setObjectName(u"combo_filter_tecnico_especialidad")

        self.horizontalLayout_11.addWidget(self.combo_filter_tecnico_especialidad)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.table_tecnicos = QTableView(self.page_tabla_tecnicos)
        self.table_tecnicos.setObjectName(u"table_tecnicos")

        self.verticalLayout_6.addWidget(self.table_tecnicos)

        self.widget_botones_tecnicos = QWidget(self.page_tabla_tecnicos)
        self.widget_botones_tecnicos.setObjectName(u"widget_botones_tecnicos")
        self.widget_botones_tecnicos.setEnabled(True)
        self.horizontalLayout_10 = QHBoxLayout(self.widget_botones_tecnicos)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.but_select_tecnicos = QPushButton(self.widget_botones_tecnicos)
        self.but_select_tecnicos.setObjectName(u"but_select_tecnicos")
        self.but_select_tecnicos.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.but_select_tecnicos)

        self.but_cancelar_tecnicos = QPushButton(self.widget_botones_tecnicos)
        self.but_cancelar_tecnicos.setObjectName(u"but_cancelar_tecnicos")

        self.horizontalLayout_10.addWidget(self.but_cancelar_tecnicos)


        self.verticalLayout_6.addWidget(self.widget_botones_tecnicos)

        self.stackedWidget.addWidget(self.page_tabla_tecnicos)
        self.page_estadisticas = QWidget()
        self.page_estadisticas.setObjectName(u"page_estadisticas")
        self.verticalLayout_2 = QVBoxLayout(self.page_estadisticas)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.lab_estad_titulo_clientes = QLabel(self.page_estadisticas)
        self.lab_estad_titulo_clientes.setObjectName(u"lab_estad_titulo_clientes")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.lab_estad_titulo_clientes.setFont(font)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lab_estad_titulo_clientes)

        self.lab_estad_client_regist = QLabel(self.page_estadisticas)
        self.lab_estad_client_regist.setObjectName(u"lab_estad_client_regist")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lab_estad_client_regist)

        self.line_estad_client_regist = QLineEdit(self.page_estadisticas)
        self.line_estad_client_regist.setObjectName(u"line_estad_client_regist")
        self.line_estad_client_regist.setReadOnly(True)

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.line_estad_client_regist)

        self.lab_estad_titulo_tecnicos = QLabel(self.page_estadisticas)
        self.lab_estad_titulo_tecnicos.setObjectName(u"lab_estad_titulo_tecnicos")
        self.lab_estad_titulo_tecnicos.setFont(font)

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lab_estad_titulo_tecnicos)

        self.lab_estad_tecn_regist = QLabel(self.page_estadisticas)
        self.lab_estad_tecn_regist.setObjectName(u"lab_estad_tecn_regist")

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lab_estad_tecn_regist)

        self.line_estad_tecn_regist = QLineEdit(self.page_estadisticas)
        self.line_estad_tecn_regist.setObjectName(u"line_estad_tecn_regist")
        self.line_estad_tecn_regist.setReadOnly(True)

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.FieldRole, self.line_estad_tecn_regist)

        self.lab_estad_titulo_reparaciones = QLabel(self.page_estadisticas)
        self.lab_estad_titulo_reparaciones.setObjectName(u"lab_estad_titulo_reparaciones")
        self.lab_estad_titulo_reparaciones.setFont(font)

        self.formLayout_3.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lab_estad_titulo_reparaciones)

        self.lab_estad_rep_pendientes = QLabel(self.page_estadisticas)
        self.lab_estad_rep_pendientes.setObjectName(u"lab_estad_rep_pendientes")

        self.formLayout_3.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lab_estad_rep_pendientes)

        self.line_estad_rep_pendientes = QLineEdit(self.page_estadisticas)
        self.line_estad_rep_pendientes.setObjectName(u"line_estad_rep_pendientes")
        self.line_estad_rep_pendientes.setReadOnly(True)

        self.formLayout_3.setWidget(5, QFormLayout.ItemRole.FieldRole, self.line_estad_rep_pendientes)

        self.lab_estad_rep_en_proceso = QLabel(self.page_estadisticas)
        self.lab_estad_rep_en_proceso.setObjectName(u"lab_estad_rep_en_proceso")

        self.formLayout_3.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lab_estad_rep_en_proceso)

        self.line_estad_rep_en_proceso = QLineEdit(self.page_estadisticas)
        self.line_estad_rep_en_proceso.setObjectName(u"line_estad_rep_en_proceso")
        self.line_estad_rep_en_proceso.setReadOnly(True)

        self.formLayout_3.setWidget(6, QFormLayout.ItemRole.FieldRole, self.line_estad_rep_en_proceso)

        self.lab_estad_rep_finalizadas = QLabel(self.page_estadisticas)
        self.lab_estad_rep_finalizadas.setObjectName(u"lab_estad_rep_finalizadas")

        self.formLayout_3.setWidget(7, QFormLayout.ItemRole.LabelRole, self.lab_estad_rep_finalizadas)

        self.line_estad_rep_finalizadas = QLineEdit(self.page_estadisticas)
        self.line_estad_rep_finalizadas.setObjectName(u"line_estad_rep_finalizadas")
        self.line_estad_rep_finalizadas.setReadOnly(True)

        self.formLayout_3.setWidget(7, QFormLayout.ItemRole.FieldRole, self.line_estad_rep_finalizadas)

        self.lab_estad_rep_registradas = QLabel(self.page_estadisticas)
        self.lab_estad_rep_registradas.setObjectName(u"lab_estad_rep_registradas")

        self.formLayout_3.setWidget(8, QFormLayout.ItemRole.LabelRole, self.lab_estad_rep_registradas)

        self.line_estad_rep_registradas = QLineEdit(self.page_estadisticas)
        self.line_estad_rep_registradas.setObjectName(u"line_estad_rep_registradas")
        self.line_estad_rep_registradas.setReadOnly(True)

        self.formLayout_3.setWidget(8, QFormLayout.ItemRole.FieldRole, self.line_estad_rep_registradas)

        self.lab_estad_rep_ganancias = QLabel(self.page_estadisticas)
        self.lab_estad_rep_ganancias.setObjectName(u"lab_estad_rep_ganancias")

        self.formLayout_3.setWidget(9, QFormLayout.ItemRole.LabelRole, self.lab_estad_rep_ganancias)

        self.line_estad_rep_ganancias = QLineEdit(self.page_estadisticas)
        self.line_estad_rep_ganancias.setObjectName(u"line_estad_rep_ganancias")
        self.line_estad_rep_ganancias.setReadOnly(True)

        self.formLayout_3.setWidget(9, QFormLayout.ItemRole.FieldRole, self.line_estad_rep_ganancias)


        self.verticalLayout_2.addLayout(self.formLayout_3)

        self.stackedWidget.addWidget(self.page_estadisticas)
        self.page_actualizacion_cliente = QWidget()
        self.page_actualizacion_cliente.setObjectName(u"page_actualizacion_cliente")
        self.verticalLayout_8 = QVBoxLayout(self.page_actualizacion_cliente)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.but_update_cliente_seleccionar = QPushButton(self.page_actualizacion_cliente)
        self.but_update_cliente_seleccionar.setObjectName(u"but_update_cliente_seleccionar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_update_cliente_seleccionar.sizePolicy().hasHeightForWidth())
        self.but_update_cliente_seleccionar.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.but_update_cliente_seleccionar)


        self.verticalLayout_8.addLayout(self.horizontalLayout_16)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.lab_update_cliente_nombre = QLabel(self.page_actualizacion_cliente)
        self.lab_update_cliente_nombre.setObjectName(u"lab_update_cliente_nombre")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lab_update_cliente_nombre)

        self.line_update_cliente_nombre = QLineEdit(self.page_actualizacion_cliente)
        self.line_update_cliente_nombre.setObjectName(u"line_update_cliente_nombre")
        self.line_update_cliente_nombre.setEnabled(False)

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.FieldRole, self.line_update_cliente_nombre)

        self.lab_update_cliente_email = QLabel(self.page_actualizacion_cliente)
        self.lab_update_cliente_email.setObjectName(u"lab_update_cliente_email")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lab_update_cliente_email)

        self.line_update_cliente_email = QLineEdit(self.page_actualizacion_cliente)
        self.line_update_cliente_email.setObjectName(u"line_update_cliente_email")
        self.line_update_cliente_email.setEnabled(False)

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.FieldRole, self.line_update_cliente_email)

        self.lab_update_cliente_numero = QLabel(self.page_actualizacion_cliente)
        self.lab_update_cliente_numero.setObjectName(u"lab_update_cliente_numero")

        self.formLayout_5.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lab_update_cliente_numero)

        self.line_update_cliente_numero = QLineEdit(self.page_actualizacion_cliente)
        self.line_update_cliente_numero.setObjectName(u"line_update_cliente_numero")
        self.line_update_cliente_numero.setEnabled(False)

        self.formLayout_5.setWidget(2, QFormLayout.ItemRole.FieldRole, self.line_update_cliente_numero)


        self.verticalLayout_8.addLayout(self.formLayout_5)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.but_update_cliente_actualizar = QPushButton(self.page_actualizacion_cliente)
        self.but_update_cliente_actualizar.setObjectName(u"but_update_cliente_actualizar")
        self.but_update_cliente_actualizar.setEnabled(False)

        self.horizontalLayout_15.addWidget(self.but_update_cliente_actualizar)

        self.but_update_cliente_eliminar = QPushButton(self.page_actualizacion_cliente)
        self.but_update_cliente_eliminar.setObjectName(u"but_update_cliente_eliminar")
        self.but_update_cliente_eliminar.setEnabled(False)

        self.horizontalLayout_15.addWidget(self.but_update_cliente_eliminar)


        self.verticalLayout_8.addLayout(self.horizontalLayout_15)

        self.stackedWidget.addWidget(self.page_actualizacion_cliente)
        self.page_actualizacion_tecnico = QWidget()
        self.page_actualizacion_tecnico.setObjectName(u"page_actualizacion_tecnico")
        self.verticalLayout_9 = QVBoxLayout(self.page_actualizacion_tecnico)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.but_update_tecnico_seleccionar = QPushButton(self.page_actualizacion_tecnico)
        self.but_update_tecnico_seleccionar.setObjectName(u"but_update_tecnico_seleccionar")
        sizePolicy.setHeightForWidth(self.but_update_tecnico_seleccionar.sizePolicy().hasHeightForWidth())
        self.but_update_tecnico_seleccionar.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.but_update_tecnico_seleccionar)


        self.verticalLayout_9.addLayout(self.horizontalLayout_17)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.lab_update_tecnico_nombre = QLabel(self.page_actualizacion_tecnico)
        self.lab_update_tecnico_nombre.setObjectName(u"lab_update_tecnico_nombre")

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lab_update_tecnico_nombre)

        self.line_update_tecnico_nombre = QLineEdit(self.page_actualizacion_tecnico)
        self.line_update_tecnico_nombre.setObjectName(u"line_update_tecnico_nombre")
        self.line_update_tecnico_nombre.setEnabled(False)

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.FieldRole, self.line_update_tecnico_nombre)

        self.lab_update_tecnico_especialidad = QLabel(self.page_actualizacion_tecnico)
        self.lab_update_tecnico_especialidad.setObjectName(u"lab_update_tecnico_especialidad")

        self.formLayout_6.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lab_update_tecnico_especialidad)

        self.combo_update_tecnico_especialidad = QComboBox(self.page_actualizacion_tecnico)
        self.combo_update_tecnico_especialidad.addItem("")
        self.combo_update_tecnico_especialidad.addItem("")
        self.combo_update_tecnico_especialidad.setObjectName(u"combo_update_tecnico_especialidad")
        self.combo_update_tecnico_especialidad.setEnabled(False)

        self.formLayout_6.setWidget(1, QFormLayout.ItemRole.FieldRole, self.combo_update_tecnico_especialidad)


        self.verticalLayout_9.addLayout(self.formLayout_6)

        self.verticalSpacer_5 = QSpacerItem(20, 135, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_5)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.but_update_tecnico_actualizar = QPushButton(self.page_actualizacion_tecnico)
        self.but_update_tecnico_actualizar.setObjectName(u"but_update_tecnico_actualizar")
        self.but_update_tecnico_actualizar.setEnabled(False)

        self.horizontalLayout_18.addWidget(self.but_update_tecnico_actualizar)

        self.but_update_tecnico_eliminar = QPushButton(self.page_actualizacion_tecnico)
        self.but_update_tecnico_eliminar.setObjectName(u"but_update_tecnico_eliminar")
        self.but_update_tecnico_eliminar.setEnabled(False)

        self.horizontalLayout_18.addWidget(self.but_update_tecnico_eliminar)


        self.verticalLayout_9.addLayout(self.horizontalLayout_18)

        self.stackedWidget.addWidget(self.page_actualizacion_tecnico)
        self.page_actualizacion_reparacion = QWidget()
        self.page_actualizacion_reparacion.setObjectName(u"page_actualizacion_reparacion")
        self.verticalLayout_10 = QVBoxLayout(self.page_actualizacion_reparacion)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.but_update_reparacion_seleccionar = QPushButton(self.page_actualizacion_reparacion)
        self.but_update_reparacion_seleccionar.setObjectName(u"but_update_reparacion_seleccionar")
        sizePolicy.setHeightForWidth(self.but_update_reparacion_seleccionar.sizePolicy().hasHeightForWidth())
        self.but_update_reparacion_seleccionar.setSizePolicy(sizePolicy)

        self.horizontalLayout_20.addWidget(self.but_update_reparacion_seleccionar)


        self.verticalLayout_10.addLayout(self.horizontalLayout_20)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.lab_update_reparacion_cliente = QLabel(self.page_actualizacion_reparacion)
        self.lab_update_reparacion_cliente.setObjectName(u"lab_update_reparacion_cliente")

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lab_update_reparacion_cliente)

        self.widget_update_reparacion_cliente = QWidget(self.page_actualizacion_reparacion)
        self.widget_update_reparacion_cliente.setObjectName(u"widget_update_reparacion_cliente")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_update_reparacion_cliente)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.line_update_reparacion_cliente = QLineEdit(self.widget_update_reparacion_cliente)
        self.line_update_reparacion_cliente.setObjectName(u"line_update_reparacion_cliente")
        self.line_update_reparacion_cliente.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.line_update_reparacion_cliente)

        self.but_update_reparacion_cliente = QToolButton(self.widget_update_reparacion_cliente)
        self.but_update_reparacion_cliente.setObjectName(u"but_update_reparacion_cliente")
        self.but_update_reparacion_cliente.setEnabled(False)
        self.but_update_reparacion_cliente.setIcon(icon)
        self.but_update_reparacion_cliente.setAutoRaise(True)

        self.horizontalLayout_21.addWidget(self.but_update_reparacion_cliente)


        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.FieldRole, self.widget_update_reparacion_cliente)

        self.lab_update_reparacion_tecnico = QLabel(self.page_actualizacion_reparacion)
        self.lab_update_reparacion_tecnico.setObjectName(u"lab_update_reparacion_tecnico")

        self.formLayout_7.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lab_update_reparacion_tecnico)

        self.widget_update_alquiler_tecnico = QWidget(self.page_actualizacion_reparacion)
        self.widget_update_alquiler_tecnico.setObjectName(u"widget_update_alquiler_tecnico")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_update_alquiler_tecnico)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.line_update_reparacion_tecnico = QLineEdit(self.widget_update_alquiler_tecnico)
        self.line_update_reparacion_tecnico.setObjectName(u"line_update_reparacion_tecnico")
        self.line_update_reparacion_tecnico.setReadOnly(True)

        self.horizontalLayout_22.addWidget(self.line_update_reparacion_tecnico)

        self.but_update_reparacion_tecnico = QToolButton(self.widget_update_alquiler_tecnico)
        self.but_update_reparacion_tecnico.setObjectName(u"but_update_reparacion_tecnico")
        self.but_update_reparacion_tecnico.setEnabled(False)
        self.but_update_reparacion_tecnico.setIcon(icon)
        self.but_update_reparacion_tecnico.setAutoRaise(True)

        self.horizontalLayout_22.addWidget(self.but_update_reparacion_tecnico)


        self.formLayout_7.setWidget(1, QFormLayout.ItemRole.FieldRole, self.widget_update_alquiler_tecnico)

        self.lab_update_reparacion_equipo = QLabel(self.page_actualizacion_reparacion)
        self.lab_update_reparacion_equipo.setObjectName(u"lab_update_reparacion_equipo")

        self.formLayout_7.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lab_update_reparacion_equipo)

        self.line_update_reparacion_equipo = QLineEdit(self.page_actualizacion_reparacion)
        self.line_update_reparacion_equipo.setObjectName(u"line_update_reparacion_equipo")
        self.line_update_reparacion_equipo.setEnabled(False)

        self.formLayout_7.setWidget(3, QFormLayout.ItemRole.FieldRole, self.line_update_reparacion_equipo)

        self.lab_update_reparacion_descripcion = QLabel(self.page_actualizacion_reparacion)
        self.lab_update_reparacion_descripcion.setObjectName(u"lab_update_reparacion_descripcion")

        self.formLayout_7.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lab_update_reparacion_descripcion)

        self.line_update_reparacion_descripcion = QLineEdit(self.page_actualizacion_reparacion)
        self.line_update_reparacion_descripcion.setObjectName(u"line_update_reparacion_descripcion")
        self.line_update_reparacion_descripcion.setEnabled(False)

        self.formLayout_7.setWidget(4, QFormLayout.ItemRole.FieldRole, self.line_update_reparacion_descripcion)

        self.lab_update_reparacion_coste = QLabel(self.page_actualizacion_reparacion)
        self.lab_update_reparacion_coste.setObjectName(u"lab_update_reparacion_coste")

        self.formLayout_7.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lab_update_reparacion_coste)

        self.line_update_reparacion_coste = QLineEdit(self.page_actualizacion_reparacion)
        self.line_update_reparacion_coste.setObjectName(u"line_update_reparacion_coste")
        self.line_update_reparacion_coste.setEnabled(False)

        self.formLayout_7.setWidget(5, QFormLayout.ItemRole.FieldRole, self.line_update_reparacion_coste)

        self.lab_update_reparacion_estado = QLabel(self.page_actualizacion_reparacion)
        self.lab_update_reparacion_estado.setObjectName(u"lab_update_reparacion_estado")

        self.formLayout_7.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lab_update_reparacion_estado)

        self.combo_update_reparacion_estado = QComboBox(self.page_actualizacion_reparacion)
        self.combo_update_reparacion_estado.addItem("")
        self.combo_update_reparacion_estado.addItem("")
        self.combo_update_reparacion_estado.addItem("")
        self.combo_update_reparacion_estado.setObjectName(u"combo_update_reparacion_estado")
        self.combo_update_reparacion_estado.setEnabled(False)

        self.formLayout_7.setWidget(2, QFormLayout.ItemRole.FieldRole, self.combo_update_reparacion_estado)


        self.verticalLayout_10.addLayout(self.formLayout_7)

        self.verticalSpacer_6 = QSpacerItem(20, 39, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_6)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.but_update_reparacion_actualizar = QPushButton(self.page_actualizacion_reparacion)
        self.but_update_reparacion_actualizar.setObjectName(u"but_update_reparacion_actualizar")
        self.but_update_reparacion_actualizar.setEnabled(False)

        self.horizontalLayout_19.addWidget(self.but_update_reparacion_actualizar)

        self.but_update_reparacion_eliminar = QPushButton(self.page_actualizacion_reparacion)
        self.but_update_reparacion_eliminar.setObjectName(u"but_update_reparacion_eliminar")
        self.but_update_reparacion_eliminar.setEnabled(False)

        self.horizontalLayout_19.addWidget(self.but_update_reparacion_eliminar)


        self.verticalLayout_10.addLayout(self.horizontalLayout_19)

        self.stackedWidget.addWidget(self.page_actualizacion_reparacion)
        self.page_tabla_reparaciones = QWidget()
        self.page_tabla_reparaciones.setObjectName(u"page_tabla_reparaciones")
        self.verticalLayout_7 = QVBoxLayout(self.page_tabla_reparaciones)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lab_filter_reparacion_cliente = QLabel(self.page_tabla_reparaciones)
        self.lab_filter_reparacion_cliente.setObjectName(u"lab_filter_reparacion_cliente")

        self.horizontalLayout_14.addWidget(self.lab_filter_reparacion_cliente)

        self.line_filter_reparacion_cliente = QLineEdit(self.page_tabla_reparaciones)
        self.line_filter_reparacion_cliente.setObjectName(u"line_filter_reparacion_cliente")

        self.horizontalLayout_14.addWidget(self.line_filter_reparacion_cliente)

        self.lab_filter_reparacion_tecnico = QLabel(self.page_tabla_reparaciones)
        self.lab_filter_reparacion_tecnico.setObjectName(u"lab_filter_reparacion_tecnico")

        self.horizontalLayout_14.addWidget(self.lab_filter_reparacion_tecnico)

        self.line_filter_reparacion_tecnico = QLineEdit(self.page_tabla_reparaciones)
        self.line_filter_reparacion_tecnico.setObjectName(u"line_filter_reparacion_tecnico")

        self.horizontalLayout_14.addWidget(self.line_filter_reparacion_tecnico)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lab_filter_reparacion_estado = QLabel(self.page_tabla_reparaciones)
        self.lab_filter_reparacion_estado.setObjectName(u"lab_filter_reparacion_estado")

        self.horizontalLayout_5.addWidget(self.lab_filter_reparacion_estado)

        self.combo_filter_reparacion_estado = QComboBox(self.page_tabla_reparaciones)
        self.combo_filter_reparacion_estado.addItem("")
        self.combo_filter_reparacion_estado.addItem("")
        self.combo_filter_reparacion_estado.addItem("")
        self.combo_filter_reparacion_estado.addItem("")
        self.combo_filter_reparacion_estado.setObjectName(u"combo_filter_reparacion_estado")
        sizePolicy.setHeightForWidth(self.combo_filter_reparacion_estado.sizePolicy().hasHeightForWidth())
        self.combo_filter_reparacion_estado.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.combo_filter_reparacion_estado)

        self.lab_filte_reparacion_orden = QLabel(self.page_tabla_reparaciones)
        self.lab_filte_reparacion_orden.setObjectName(u"lab_filte_reparacion_orden")

        self.horizontalLayout_5.addWidget(self.lab_filte_reparacion_orden)

        self.combo_filter_reparacion_orden = QComboBox(self.page_tabla_reparaciones)
        self.combo_filter_reparacion_orden.addItem("")
        self.combo_filter_reparacion_orden.addItem("")
        self.combo_filter_reparacion_orden.addItem("")
        self.combo_filter_reparacion_orden.addItem("")
        self.combo_filter_reparacion_orden.addItem("")
        self.combo_filter_reparacion_orden.setObjectName(u"combo_filter_reparacion_orden")
        sizePolicy.setHeightForWidth(self.combo_filter_reparacion_orden.sizePolicy().hasHeightForWidth())
        self.combo_filter_reparacion_orden.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.combo_filter_reparacion_orden)

        self.but_filter_reparacion_direccion = QPushButton(self.page_tabla_reparaciones)
        self.but_filter_reparacion_direccion.setObjectName(u"but_filter_reparacion_direccion")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.but_filter_reparacion_direccion.sizePolicy().hasHeightForWidth())
        self.but_filter_reparacion_direccion.setSizePolicy(sizePolicy1)
        self.but_filter_reparacion_direccion.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_5.addWidget(self.but_filter_reparacion_direccion)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.table_reparacion = QTableView(self.page_tabla_reparaciones)
        self.table_reparacion.setObjectName(u"table_reparacion")

        self.verticalLayout_7.addWidget(self.table_reparacion)

        self.widget_botones_reparaciones = QWidget(self.page_tabla_reparaciones)
        self.widget_botones_reparaciones.setObjectName(u"widget_botones_reparaciones")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_botones_reparaciones)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.but_select_reparacion = QPushButton(self.widget_botones_reparaciones)
        self.but_select_reparacion.setObjectName(u"but_select_reparacion")
        self.but_select_reparacion.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.but_select_reparacion)

        self.but_cancelar_reparacion = QPushButton(self.widget_botones_reparaciones)
        self.but_cancelar_reparacion.setObjectName(u"but_cancelar_reparacion")

        self.horizontalLayout_4.addWidget(self.but_cancelar_reparacion)


        self.verticalLayout_7.addWidget(self.widget_botones_reparaciones)

        self.stackedWidget.addWidget(self.page_tabla_reparaciones)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 630, 33))
        self.menuFichero = QMenu(self.menubar)
        self.menuFichero.setObjectName(u"menuFichero")
        self.menuAdministrar_clientes = QMenu(self.menubar)
        self.menuAdministrar_clientes.setObjectName(u"menuAdministrar_clientes")
        self.menuAdministrar_t_cnicos = QMenu(self.menubar)
        self.menuAdministrar_t_cnicos.setObjectName(u"menuAdministrar_t_cnicos")
        self.menuAdministrar_reparaciones = QMenu(self.menubar)
        self.menuAdministrar_reparaciones.setObjectName(u"menuAdministrar_reparaciones")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFichero.menuAction())
        self.menubar.addAction(self.menuAdministrar_clientes.menuAction())
        self.menubar.addAction(self.menuAdministrar_t_cnicos.menuAction())
        self.menubar.addAction(self.menuAdministrar_reparaciones.menuAction())
        self.menuFichero.addAction(self.action_estadisticas)
        self.menuFichero.addAction(self.action_import)
        self.menuFichero.addAction(self.action_export)
        self.menuFichero.addAction(self.action_salir)
        self.menuAdministrar_clientes.addAction(self.action_crear_cliente)
        self.menuAdministrar_clientes.addAction(self.action_consultar_Modificar_cliente)
        self.menuAdministrar_clientes.addAction(self.action_consultar_clientes)
        self.menuAdministrar_t_cnicos.addAction(self.action_crear_tecnico)
        self.menuAdministrar_t_cnicos.addAction(self.action_consultar_Modificar_tecnico)
        self.menuAdministrar_t_cnicos.addAction(self.action_consultar_tecnicos)
        self.menuAdministrar_reparaciones.addAction(self.action_crear_reparacion)
        self.menuAdministrar_reparaciones.addAction(self.action_consultar_Modificar_reparacion)
        self.menuAdministrar_reparaciones.addAction(self.action_consultar_reparaciones)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(9)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_guardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.action_guardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_abrir_tienda.setText(QCoreApplication.translate("MainWindow", u"Abrir tienda", None))
#if QT_CONFIG(shortcut)
        self.action_abrir_tienda.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
#if QT_CONFIG(shortcut)
        self.action_salir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_consultar_Modificar_cliente.setText(QCoreApplication.translate("MainWindow", u"Consultar/Modificar", None))
        self.action_consultar_clientes.setText(QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.action_consultar_Modificar_tecnico.setText(QCoreApplication.translate("MainWindow", u"Consultar/Modificar", None))
        self.action_consultar_tecnicos.setText(QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.action_consultar_Modificar_reparacion.setText(QCoreApplication.translate("MainWindow", u"Consultar/Modificar", None))
        self.action_consultar_reparaciones.setText(QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.action_crear_cliente.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.action_crear_tecnico.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.action_crear_reparacion.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.action_estadisticas.setText(QCoreApplication.translate("MainWindow", u"Estad\u00edsticas", None))
        self.action_cerrar_sesion.setText(QCoreApplication.translate("MainWindow", u"Cerrar sesion", None))
        self.action_import.setText(QCoreApplication.translate("MainWindow", u"Import from json", None))
        self.action_export.setText(QCoreApplication.translate("MainWindow", u"Export as json", None))
#if QT_CONFIG(tooltip)
        self.stackedWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lab_nombre_cliente.setText(QCoreApplication.translate("MainWindow", u"Nombre: ", None))
        self.lab_email_cliente.setText(QCoreApplication.translate("MainWindow", u"Email: ", None))
        self.line_email_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"email@example.com", None))
        self.lab_numero_cliente.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.line_numero_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"123-456-789", None))
        self.but_guardar_creacion_cliente.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.but_limpiar_creacion_cliente.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.lab_nombre_tecnico.setText(QCoreApplication.translate("MainWindow", u"Nombre: ", None))
        self.lab_especialidad.setText(QCoreApplication.translate("MainWindow", u"Especialidad", None))
        self.combo_especialidad.setItemText(0, QCoreApplication.translate("MainWindow", u"Software", None))
        self.combo_especialidad.setItemText(1, QCoreApplication.translate("MainWindow", u"Hardware", None))

        self.but_guardar_creacion_tecnico.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.but_limpiar_creacion_tecnico.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.lab_crear_reparacion_cliente.setText(QCoreApplication.translate("MainWindow", u"Cliente:*", None))
        self.line_crear_reparacion_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pendiente de elegir", None))
        self.but_crear_reparacion_cliente.setText(QCoreApplication.translate("MainWindow", u"Elegir", None))
        self.lab_crear_reparacion_tecnico.setText(QCoreApplication.translate("MainWindow", u"T\u00e9cnico:", None))
        self.line_crear_reparacion_tecnico.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pendiente de elegir...", None))
        self.but_crear_reparacion_tecnico.setText(QCoreApplication.translate("MainWindow", u"Elegir", None))
        self.lab_crear_reparacion_equipo.setText(QCoreApplication.translate("MainWindow", u"Equipo:*", None))
        self.line_crear_reparacion_equipo.setPlaceholderText("")
        self.lab_crear_reparacion_descripcion.setText(QCoreApplication.translate("MainWindow", u"Descripcion:*", None))
        self.line_crear_reparacion_descripcion.setPlaceholderText("")
        self.lab_crear_reparacion_coste.setText(QCoreApplication.translate("MainWindow", u"Coste:*", None))
        self.but_crear_reparacion_guardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.but_crear_reparacion_limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.lab_crear_reparacion_aviso.setText(QCoreApplication.translate("MainWindow", u"Los campos marcados con * son obligatorios", None))
        self.lab_filter_cliente_nombre.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.line_filter_cliente_nombre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre a filtrar...", None))
        self.but_select_clientes.setText(QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.but_cancelar_clientes.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.lab_filter_tecnico_nombre.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.line_filter_tecnico_nombre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre a filtrar...", None))
        self.lab_filter_tecnico_especialidad.setText(QCoreApplication.translate("MainWindow", u"Especialidad", None))
        self.combo_filter_tecnico_especialidad.setItemText(0, QCoreApplication.translate("MainWindow", u"*", None))
        self.combo_filter_tecnico_especialidad.setItemText(1, QCoreApplication.translate("MainWindow", u"Software", None))
        self.combo_filter_tecnico_especialidad.setItemText(2, QCoreApplication.translate("MainWindow", u"Hardware", None))

        self.but_select_tecnicos.setText(QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.but_cancelar_tecnicos.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.lab_estad_titulo_clientes.setText(QCoreApplication.translate("MainWindow", u"CLIENTES", None))
        self.lab_estad_client_regist.setText(QCoreApplication.translate("MainWindow", u"CLIENTES REGISTRADOS:", None))
        self.lab_estad_titulo_tecnicos.setText(QCoreApplication.translate("MainWindow", u"TECNICOS", None))
        self.lab_estad_tecn_regist.setText(QCoreApplication.translate("MainWindow", u"TECNICOS REGISTRADOS:", None))
        self.lab_estad_titulo_reparaciones.setText(QCoreApplication.translate("MainWindow", u"REPARACIONES", None))
        self.lab_estad_rep_pendientes.setText(QCoreApplication.translate("MainWindow", u"REPARACIONES PENDIENTES", None))
        self.lab_estad_rep_en_proceso.setText(QCoreApplication.translate("MainWindow", u"REPARACIONES EN PROCESO", None))
        self.lab_estad_rep_finalizadas.setText(QCoreApplication.translate("MainWindow", u"REPARACIONES FINALIZADAS:", None))
        self.lab_estad_rep_registradas.setText(QCoreApplication.translate("MainWindow", u"REPARACIONES REGISTRADAS:", None))
        self.lab_estad_rep_ganancias.setText(QCoreApplication.translate("MainWindow", u"TOTAL REPARACIONES FACTURADAS:", None))
        self.but_update_cliente_seleccionar.setText(QCoreApplication.translate("MainWindow", u"Seleccionar cliente", None))
        self.lab_update_cliente_nombre.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.lab_update_cliente_email.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.lab_update_cliente_numero.setText(QCoreApplication.translate("MainWindow", u"Numero:", None))
        self.but_update_cliente_actualizar.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.but_update_cliente_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.but_update_tecnico_seleccionar.setText(QCoreApplication.translate("MainWindow", u"Seleccionar t\u00e9cnico", None))
        self.lab_update_tecnico_nombre.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.lab_update_tecnico_especialidad.setText(QCoreApplication.translate("MainWindow", u"Especialidad:", None))
        self.combo_update_tecnico_especialidad.setItemText(0, QCoreApplication.translate("MainWindow", u"Software", None))
        self.combo_update_tecnico_especialidad.setItemText(1, QCoreApplication.translate("MainWindow", u"Hardware", None))

        self.but_update_tecnico_actualizar.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.but_update_tecnico_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.but_update_reparacion_seleccionar.setText(QCoreApplication.translate("MainWindow", u"Seleccionar reparacion", None))
        self.lab_update_reparacion_cliente.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.line_update_reparacion_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pendiente de elegir...", None))
        self.but_update_reparacion_cliente.setText(QCoreApplication.translate("MainWindow", u"Elegir", None))
        self.lab_update_reparacion_tecnico.setText(QCoreApplication.translate("MainWindow", u"T\u00e9cnico:", None))
        self.line_update_reparacion_tecnico.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pendiente de elegir...", None))
        self.but_update_reparacion_tecnico.setText(QCoreApplication.translate("MainWindow", u"Elegir", None))
        self.lab_update_reparacion_equipo.setText(QCoreApplication.translate("MainWindow", u"Equipo:", None))
        self.lab_update_reparacion_descripcion.setText(QCoreApplication.translate("MainWindow", u"Descripcion:", None))
        self.lab_update_reparacion_coste.setText(QCoreApplication.translate("MainWindow", u"Coste:", None))
        self.lab_update_reparacion_estado.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.combo_update_reparacion_estado.setItemText(0, QCoreApplication.translate("MainWindow", u"pendiente", None))
        self.combo_update_reparacion_estado.setItemText(1, QCoreApplication.translate("MainWindow", u"en proceso", None))
        self.combo_update_reparacion_estado.setItemText(2, QCoreApplication.translate("MainWindow", u"finalizada", None))

        self.but_update_reparacion_actualizar.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.but_update_reparacion_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.lab_filter_reparacion_cliente.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.line_filter_reparacion_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre...", None))
        self.lab_filter_reparacion_tecnico.setText(QCoreApplication.translate("MainWindow", u"T\u00e9cnico:", None))
        self.line_filter_reparacion_tecnico.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre...", None))
        self.lab_filter_reparacion_estado.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.combo_filter_reparacion_estado.setItemText(0, QCoreApplication.translate("MainWindow", u"*", None))
        self.combo_filter_reparacion_estado.setItemText(1, QCoreApplication.translate("MainWindow", u"pendiente", None))
        self.combo_filter_reparacion_estado.setItemText(2, QCoreApplication.translate("MainWindow", u"en proceso", None))
        self.combo_filter_reparacion_estado.setItemText(3, QCoreApplication.translate("MainWindow", u"finalizada", None))

        self.lab_filte_reparacion_orden.setText(QCoreApplication.translate("MainWindow", u"Orden:", None))
        self.combo_filter_reparacion_orden.setItemText(0, QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.combo_filter_reparacion_orden.setItemText(1, QCoreApplication.translate("MainWindow", u"Coste", None))
        self.combo_filter_reparacion_orden.setItemText(2, QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.combo_filter_reparacion_orden.setItemText(3, QCoreApplication.translate("MainWindow", u"Tecnico", None))
        self.combo_filter_reparacion_orden.setItemText(4, QCoreApplication.translate("MainWindow", u"Estado", None))

        self.but_filter_reparacion_direccion.setText(QCoreApplication.translate("MainWindow", u"Descendiente", None))
        self.but_select_reparacion.setText(QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.but_cancelar_reparacion.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.menuFichero.setTitle(QCoreApplication.translate("MainWindow", u"Fichero", None))
        self.menuAdministrar_clientes.setTitle(QCoreApplication.translate("MainWindow", u"Administrar clientes", None))
        self.menuAdministrar_t_cnicos.setTitle(QCoreApplication.translate("MainWindow", u"Administrar t\u00e9cnicos", None))
        self.menuAdministrar_reparaciones.setTitle(QCoreApplication.translate("MainWindow", u"Administrar reparaciones", None))
    # retranslateUi

