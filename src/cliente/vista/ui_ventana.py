from PySide6.QtCore import Qt, QLocale
from PySide6.QtGui import QStandardItemModel, QStandardItem, QDoubleValidator
from PySide6.QtWidgets import QMainWindow, QWidget, QHeaderView, QMessageBox, QAbstractItemView, \
    QTableView

from cliente.cliente_api import ClienteAPI, ErrorAPI
from compartido.esquemas import ClienteOut, TecnicoOut, ReparacionOut, ClienteCreate, TecnicoCreate, ReparacionCreate
from cliente.vista.Ventana import Ui_MainWindow

def warning_box(parent,text):
    QMessageBox.warning(parent,"Ocurrio un error",text, QMessageBox.StandardButton.Ok)

class MiVentanaPrincipal(QMainWindow):
    def __init__(self, api: ClienteAPI):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.api = api
        self.taller = self.api.nombre_taller

        self.ventana_actual = "page_tabla_reparaciones"
        self.ventana_previa = ""

        #Manera que me comento la IA que valida q el coste sea double
        self.validador_coste = QDoubleValidator(0.0, 99999.99, 2,self)  # min, max, decimales, padre
        self.validador_coste.setNotation(QDoubleValidator.Notation.StandardNotation)
        self.validador_coste.setLocale(QLocale.c())
        self.ui.line_crear_reparacion_coste.setValidator(self.validador_coste)
        self.ui.line_update_reparacion_coste.setValidator(self.validador_coste)

        #Objetos a descargar
        self.clientes = self.api.listar_clientes_dict()
        self.tecnicos = self.api.listar_tecnicos_dict()
        self.reparaciones = self.api.listar_reparaciones_dict()

        #Para la operacion de eliminar y updatear
        self.cliente: ClienteOut | None = None
        self.tecnico: TecnicoOut | None = None
        self.reparacion: ReparacionOut | None = None

        self.definir_tablas()
        self.rellenar_tablas()
        self.connect_events()

        self.establecer_ventana(ventana_objetivo="page_tabla_reparaciones",ventana_origen=self.ventana_actual)



    """ Igual se reutiliza, pero en deshuso actual
    def guardado(self) -> bool:
        '''
        Metodo empleado para comprobar si actualmente esta guardado el taller
        :return: True si esta guardado, False si no
        '''
        return self.taller == self.taller_guardado
    """

    def actualizar_titulo(self, nombre_pagina:str) -> None:
        """
        Construccion y establecimiento del titulo
        :param nombre_pagina:  El nombre de la pagina que debe mostrar, normalmente sera self.ventana_actual
        """
        titulo = f"{nombre_pagina.replace('page', '').replace('_', ' ').title()} - {self.taller}"
        self.setWindowTitle(titulo)

    def conf_general_tabla(self,tabla:QTableView):
        """
        Configuración habitual por todas las tablas, juntada en una función para mejor lectura y eficiencia
        :param tabla: La tabla que debe configurar
        """
        # Colorcitos
        tabla.setAlternatingRowColors(True)

        tabla.setStyleSheet("""
                   QTableView {
                       background-color: white;
                       alternate-background-color: #e8f0fe;
                       selection-background-color: #2196F3;
                       color: black;
                       gridline-color: #cccccc;
                   }
               """)

        # Eleccion lineal
        tabla.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )
        # Eleccion unica
        tabla.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )
        # No editable
        tabla.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        tabla.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

    # --  METODOS PARA TRATAR TABLAS

    # -   METODOS PARA DEFINIR TABLAS

    def definir_tabla_clientes(self):
        tabla = self.ui.table_clientes
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Nombre","Email","Numero"])
        tabla.setModel(model)

        self.conf_general_tabla(tabla)

    def definir_tabla_tecnicos(self):
        tabla = self.ui.table_tecnicos
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Nombre", "Especialidad"])
        tabla.setModel(model)
        self.conf_general_tabla(tabla)

    def definir_tabla_reparaciones(self):
        tabla = self.ui.table_reparacion
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Cliente", "Técnico", "Equipo","Descripcion","Estado","Coste sin iva","Coste con iva"])
        tabla.setModel(model)
        self.conf_general_tabla(tabla)

    def definir_tablas(self):
        #Poner en invisible por defecto los select de las tablas
        self.definir_tabla_clientes()
        self.definir_tabla_tecnicos()
        self.definir_tabla_reparaciones()

    # -  FUNCIONES ENCARGADAS DE RELLENAR LAS TABLAS

    #   RELLENAR FILAS
    def rellenar_fila_cliente(self,cliente: ClienteOut):
        model = self.ui.table_clientes.model()
        nombre_con_id = QStandardItem(cliente.nombre)
        nombre_con_id.setData(cliente.id, Qt.ItemDataRole.UserRole)
        model.appendRow([nombre_con_id,QStandardItem(cliente.email),QStandardItem(cliente.numero)])

    def rellenar_fila_tecnico(self, tecnico: TecnicoOut):
        model = self.ui.table_tecnicos.model()
        nombre_con_id = QStandardItem(tecnico.nombre)
        nombre_con_id.setData(tecnico.id, Qt.ItemDataRole.UserRole)
        model.appendRow([nombre_con_id,QStandardItem(tecnico.especialidad)])

    def rellenar_fila_reparacion(self, reparacion: ReparacionOut):
        model = self.ui.table_reparacion.model()
        nombre_con_id = QStandardItem(self.clientes[reparacion.cliente].nombre)
        nombre_con_id.setData(reparacion.id, Qt.ItemDataRole.UserRole)
        model.appendRow([nombre_con_id,
                         QStandardItem(self.tecnicos[reparacion.tecnico].nombre) if reparacion.tecnico is not None else QStandardItem(""),
                         QStandardItem(reparacion.equipo),
                         QStandardItem(reparacion.descripcion),
                         QStandardItem(reparacion.estado or ""),
                         QStandardItem(str(reparacion.coste)),
                         QStandardItem(f'{reparacion.get_with_iva():.2f}')
                         ])

    #   RELLENAR TABLA ÚNICA

    def rellenar_tabla_clientes(self):
        nombre = self.ui.line_filter_cliente_nombre.text().strip().lower()
        model = self.ui.table_clientes.model()
        model.removeRows(0, model.rowCount())

        self.clientes = self.api.listar_clientes_dict()

        for cliente in self.clientes.values():
            if nombre == "" or nombre.lower() in cliente.nombre:
                self.rellenar_fila_cliente(cliente)

    def rellenar_tabla_tecnicos(self):
        nombre = self.ui.line_filter_tecnico_nombre.text().strip().lower()
        especialidad = self.ui.combo_filter_tecnico_especialidad.currentText().lower()
        model = self.ui.table_tecnicos.model()
        model.removeRows(0, model.rowCount())

        self.tecnicos = self.api.listar_tecnicos_dict()

        for tecnico in self.tecnicos.values():
            if (nombre == "" or nombre.lower() in tecnico.nombre) and \
                    (especialidad == "*" or tecnico.especialidad == especialidad.lower()):
                self.rellenar_fila_tecnico(tecnico)

    def rellenar_tabla_reparaciones(self):
        filtro_cliente = self.ui.line_filter_reparacion_cliente.text().strip().lower()
        filtro_tecnico = self.ui.line_filter_reparacion_tecnico.text().strip().lower()
        filtro_estado = self.ui.combo_filter_reparacion_estado.currentText().lower()

        model = self.ui.table_reparacion.model()
        model.removeRows(0, model.rowCount())

        # Redescarga de los datos
        self.clientes = self.api.listar_clientes_dict()
        self.tecnicos = self.api.listar_tecnicos_dict()
        self.reparaciones = self.api.listar_reparaciones_dict()

        # Lógica ordenacion compacta

        campo = self.ui.combo_filter_reparacion_orden.currentText()
        direccion = self.ui.but_filter_reparacion_direccion.text()

        ordenaciones = {  # Relacion campo -> propiedad
            'Coste': lambda r: r.coste,
            'Cliente': lambda r: self.clientes[r.cliente].nombre,
            'Tecnico': lambda r: self.tecnicos[r.tecnico].nombre if r.tecnico is not None else "",
            'Estado': lambda r: r.estado,
        }



        reparaciones = list(self.reparaciones.values()) #Copia de la lista, para no modificar la original

        if campo == 'Fecha': #Si el campo es fecha y es pa abajo lo revierte
            if direccion == "Descendiente":
                reparaciones.reverse()
        else: #Si no es fecha lanza el algoritmo general
            reparaciones.sort(
                key=ordenaciones[campo], #El atributo por el cual se ordena
                reverse=(direccion == 'Descendiente')
            )

        for reparacion in reparaciones:
            if (filtro_cliente == "" or filtro_cliente.lower() in self.clientes[reparacion.cliente].nombre) and \
                    (filtro_tecnico == "" or (reparacion.tecnico is not None and filtro_tecnico.lower() in self.tecnicos[reparacion.tecnico].nombre)) and \
                    (filtro_estado == "*" or filtro_estado == reparacion.estado):
                self.rellenar_fila_reparacion(reparacion)

    #Pequeño apartado, funcion para el boton de direccion:
    def alterar_direccion(self):
        if self.ui.but_filter_reparacion_direccion.text() == 'Descendiente':
            self.ui.but_filter_reparacion_direccion.setText('Ascendiente')
        else:
            self.ui.but_filter_reparacion_direccion.setText('Descendiente')
        self.rellenar_tabla_reparaciones()

    #   RELLENAR TODAS LAS TABLAS

    def rellenar_tablas(self):
        self.rellenar_tabla_clientes()
        self.rellenar_tabla_tecnicos()
        self.rellenar_tabla_reparaciones()

    # -- FUNCION ENCARGADA DE LIMPIAR LA PAGINA INDICADA

    def limpiar_ventana(self, ventana:str) -> None:
        """
        Limpia la ventana indicada
        :param ventana: Nombre de la pagina que debe limpiar
        """
        match ventana:
            case "page_tabla_clientes":
                self.ui.table_clientes.selectionModel().clearSelection()
                self.ui.line_filter_cliente_nombre.clear()
            case "page_tabla_tecnicos":
                self.ui.table_tecnicos.selectionModel().clearSelection()
                self.ui.line_filter_tecnico_nombre.clear()
                self.ui.combo_filter_tecnico_especialidad.setCurrentText("*")
            case "page_tabla_reparaciones":
                self.ui.table_reparacion.selectionModel().clearSelection()
                self.ui.line_filter_reparacion_cliente.clear()
                self.ui.line_filter_reparacion_tecnico.clear()
                self.ui.combo_filter_reparacion_estado.setCurrentText("*")
                self.ui.combo_filter_reparacion_orden.setCurrentText("Fecha")
                self.ui.but_filter_reparacion_direccion.setText("Descendiente")
            case "page_crear_cliente":
                self.ui.line_nombre_cliente.clear()
                self.ui.line_email_cliente.clear()
                self.ui.line_numero_cliente.clear()
            case "page_crear_tecnico":
                self.ui.line_nombre_tecnico.clear()
                self.ui.combo_especialidad.setCurrentText("Software")
            case "page_crear_reparacion":
                self.ui.line_crear_reparacion_cliente.clear()
                self.ui.line_crear_reparacion_tecnico.clear()
                self.ui.line_crear_reparacion_equipo.clear()
                self.ui.line_crear_reparacion_descripcion.clear()
                self.ui.line_crear_reparacion_coste.clear()
            case "page_actualizacion_cliente":
                self.ui.line_update_cliente_nombre.clear()
                self.ui.line_update_cliente_email.clear()
                self.ui.line_update_cliente_numero.clear()
                self.set_cliente_enabled(False)
                self.cliente = None
            case "page_actualizacion_tecnico":
                self.ui.line_update_tecnico_nombre.clear()
                self.ui.combo_update_tecnico_especialidad.setCurrentText("Software")
                self.set_tecnico_enabled(False)
                self.tecnico = None
            case "page_actualizacion_reparacion":
                self.ui.line_update_reparacion_cliente.clear()
                self.ui.line_update_reparacion_tecnico.clear()
                self.ui.line_update_reparacion_equipo.clear()
                self.ui.line_update_reparacion_descripcion.clear()
                self.ui.line_update_reparacion_coste.clear()
                self.set_reparacion_enabled(False)
                self.reparacion = None
            case "page_estadisticas": pass
            case _: print("Que estupidez me pediste que limpiase??")

    # -- FUNCION ENCARGADA DE DESPLAZARSE POR EL STACKED_WIDGET

    def establecer_ventana(self,ventana_objetivo: str, ventana_origen:str, select_intention: bool = False):
        #Se cambia el titulo para que sea acorde a la nueva pagina
        self.actualizar_titulo(ventana_objetivo)

        #Limpia la ventana de origen a no ser que deba reusarla a continuacion
        if not select_intention:
            self.limpiar_ventana(ventana_origen)
            self.ui.widget_botones_clientes.hide()
            self.ui.widget_botones_tecnicos.hide()
            self.ui.widget_botones_reparaciones.hide()
        else:
            self.ui.widget_botones_clientes.show()
            self.ui.widget_botones_tecnicos.show()
            self.ui.widget_botones_reparaciones.show()


        self.ventana_actual = ventana_objetivo
        if ventana_origen is not None:
            self.ventana_previa = ventana_origen
        self.ui.stackedWidget.setCurrentWidget(self.ui.stackedWidget.findChild(QWidget, ventana_objetivo))

    # -- METODOS DE MODIFICACION DE HABILITADO DE UPDATE
    # - Apartado clientes
    def set_cliente_enabled(self,habilitado: bool):
        self.ui.line_update_cliente_nombre.setEnabled(habilitado)
        self.ui.line_update_cliente_email.setEnabled(habilitado)
        self.ui.line_update_cliente_numero.setEnabled(habilitado)
    # - Apartado tecnicos
    def set_tecnico_enabled(self,habilitado: bool):
        self.ui.line_update_tecnico_nombre.setEnabled(habilitado)
        self.ui.combo_update_tecnico_especialidad.setEnabled(habilitado)
    # - Apartado reparaciones
    def set_reparacion_enabled(self,habilitado: bool):
        self.ui.but_update_reparacion_cliente.setEnabled(habilitado)
        self.ui.but_update_reparacion_tecnico.setEnabled(habilitado)
        self.ui.combo_update_reparacion_estado.setEnabled(habilitado)
        self.ui.line_update_reparacion_equipo.setEnabled(habilitado)
        self.ui.line_update_reparacion_descripcion.setEnabled(habilitado)
        self.ui.line_update_reparacion_coste.setEnabled(habilitado)
        self.ui.but_update_reparacion_cliente.setEnabled(habilitado)
        self.ui.but_update_reparacion_tecnico.setEnabled(habilitado)

    # -- LOGICA DEL SELECT PARA OBTENER DATOS
    # - BOTON SELECT CLIENTES
    def check_select_cliente(self):
        self.ui.but_select_clientes.setEnabled(bool(self.ui.table_clientes.selectionModel().selectedRows()))
    def accion_select_cliente(self):
        id_cliente = self.ui.table_clientes.selectionModel().selectedRows()[0].data(Qt.ItemDataRole.UserRole)
        cliente = self.clientes[id_cliente]

        if   self.ventana_previa == "page_crear_reparacion":
            self.ui.line_crear_reparacion_cliente.setText(cliente.nombre)
            self.ui.line_crear_reparacion_cliente.setProperty("UUID",cliente.id)
        elif self.ventana_previa == "page_actualizacion_cliente":
            self.set_cliente_enabled(True)
            self.cliente = cliente
            self.ui.line_update_cliente_nombre.setText(cliente.nombre)
            self.ui.line_update_cliente_nombre.setProperty("UUID",cliente.id)
            self.ui.line_update_cliente_email.setText(cliente.email)
            self.ui.line_update_cliente_numero.setText(cliente.numero)
        elif self.ventana_previa == "page_actualizacion_reparacion":
            self.ui.line_update_reparacion_cliente.setText(cliente.nombre)
            self.ui.line_update_reparacion_cliente.setProperty("UUID",cliente.id)

        self.establecer_ventana(self.ventana_previa,ventana_origen=self.ventana_actual)
    # - BOTON SELECT TECNICOS
    def check_select_tecnico(self):
        self.ui.but_select_tecnicos.setEnabled(bool(self.ui.table_tecnicos.selectionModel().selectedRows()))
    def accion_select_tecnico(self):
        id_tecnico = self.ui.table_tecnicos.selectionModel().selectedRows()[0].data(Qt.ItemDataRole.UserRole)
        tecnico = self.tecnicos[id_tecnico]

        if self.ventana_previa == "page_crear_reparacion":
            self.ui.line_crear_reparacion_tecnico.setText(tecnico.nombre)
            self.ui.line_crear_reparacion_tecnico.setProperty("UUID",tecnico.id)
        elif self.ventana_previa == "page_actualizacion_tecnico":
            self.set_tecnico_enabled(True)
            self.tecnico = tecnico
            self.ui.line_update_tecnico_nombre.setText(tecnico.nombre)
            self.ui.line_update_tecnico_nombre.setProperty("UUID", tecnico.id)
            self.ui.combo_update_tecnico_especialidad.setCurrentText(tecnico.especialidad.capitalize())
        elif self.ventana_previa == "page_actualizacion_reparacion":
            self.ui.line_update_reparacion_tecnico.setText(tecnico.nombre)
            self.ui.line_update_reparacion_tecnico.setProperty("UUID", tecnico.id)
        self.establecer_ventana(self.ventana_previa,ventana_origen=self.ventana_actual)
    # - BOTON SELECT REPARACIONES
    def check_select_reparacion(self):
        self.ui.but_select_reparacion.setEnabled(bool(self.ui.table_reparacion.selectionModel().selectedRows()))
    def accion_select_reparacion(self):
        self.set_reparacion_enabled(True)
        id_reparacion = self.ui.table_reparacion.selectionModel().selectedRows()[0].data(Qt.ItemDataRole.UserRole)
        reparacion = self.reparaciones[id_reparacion]
        self.reparacion = reparacion
        self.ui.line_update_reparacion_cliente.setText(self.clientes[reparacion.cliente].nombre)
        self.ui.line_update_reparacion_cliente.setProperty("UUID",reparacion.cliente)
        self.ui.line_update_reparacion_tecnico.setText(self.tecnicos[reparacion.tecnico].nombre if reparacion.tecnico is not None else "")
        if reparacion.tecnico is not None:
            self.ui.line_update_reparacion_tecnico.setProperty("UUID",reparacion.tecnico)
        self.ui.combo_update_reparacion_estado.setCurrentText(reparacion.estado)
        self.ui.line_update_reparacion_equipo.setText(reparacion.equipo)
        self.ui.line_update_reparacion_descripcion.setText(reparacion.descripcion)
        self.ui.line_update_reparacion_coste.setText(str(reparacion.coste))

        self.establecer_ventana(self.ventana_previa,ventana_origen=self.ventana_actual)

    # -- FUNCIONES DE CREACION DE ELEMENTOS
    # - CREACION DE CLIENTES
    def check_crear_cliente(self):
        ui = self.ui
        condicion = ui.line_nombre_cliente.text() != "" and ui.line_email_cliente.text().__contains__('@') and ui.line_numero_cliente.text() != ""
        ui.but_guardar_creacion_cliente.setEnabled(condicion)
    def crear_cliente(self):
        nombre = self.ui.line_nombre_cliente.text().lower().strip()
        email =  self.ui.line_email_cliente.text().lower().strip()
        numero = self.ui.line_numero_cliente.text().lower().strip()
        try:
            self.api.crear_cliente(ClienteCreate(nombre=nombre,email=email,numero=numero))
        except ErrorAPI as e :
            warning_box(self,str(e))
        self.limpiar_ventana(self.ventana_actual)
        self.rellenar_tabla_clientes()
        self.actualizar_titulo(self.ventana_actual)

    # - CREACION DE TECNICO
    def check_crear_tecnico(self):
        ui = self.ui
        condicion = ui.line_nombre_tecnico.text() != ""
        ui.but_guardar_creacion_tecnico.setEnabled(condicion)
    def crear_tecnico(self):
        nombre = self.ui.line_nombre_tecnico.text().lower().strip()
        especialidad =  self.ui.combo_especialidad.currentText().lower()
        try:
            self.api.crear_tecnico(TecnicoCreate(nombre=nombre,especialidad=especialidad))
        except ErrorAPI as e:
            warning_box(self,str(e))
        self.limpiar_ventana(self.ventana_actual)
        self.rellenar_tabla_tecnicos()
        self.actualizar_titulo(self.ventana_actual)

    # - CREACION DE LA REPARACION
    def check_crear_reparacion(self):
        ui = self.ui
        condicion = (ui.line_crear_reparacion_cliente.text().strip() != "" and
                     ui.line_crear_reparacion_equipo.text().strip() != "" and
                     ui.line_crear_reparacion_descripcion.text() != "" and
                     ui.line_crear_reparacion_coste.text() != ""
                     )
        ui.but_crear_reparacion_guardar.setEnabled(condicion)
    def crear_reparacion(self):
        cliente = self.ui.line_crear_reparacion_cliente.property("UUID")
        tecnico = self.ui.line_crear_reparacion_tecnico.property("UUID")
        equipo = self.ui.line_crear_reparacion_equipo.text().lower().strip()
        descripcion = self.ui.line_crear_reparacion_descripcion.text().lower().strip()
        coste = float(self.ui.line_crear_reparacion_coste.text().lower().strip())
        try:
            self.api.crear_reparacion(ReparacionCreate(cliente=cliente,tecnico=tecnico,equipo=equipo,descripcion=descripcion,coste=coste))
        except ErrorAPI as e:
            warning_box(self,str(e))
        self.limpiar_ventana(self.ventana_actual)
        self.rellenar_tabla_reparaciones()
        self.actualizar_titulo(self.ventana_actual)

    # -- FUNCIONES DE ACTUALIZACION DE ELEMENTOS
    # - ACTUALIZACION DE CLIENTE
    def check_actualizacion_cliente(self):
        condicion = ((self.ui.line_update_cliente_nombre.text() != self.cliente.nombre and self.ui.line_update_cliente_nombre.text() != "")or
                     (self.ui.line_update_cliente_email.text() != self.cliente.email and self.ui.line_update_cliente_email.text().__contains__('@'))or
                     self.ui.line_update_cliente_numero.text() != self.cliente.numero
                     )
        self.ui.but_update_cliente_actualizar.setEnabled(condicion)
    def actualizar_cliente(self):
        cli_id = self.cliente.id
        nombre = self.ui.line_update_cliente_nombre.text().lower()
        email = self.ui.line_update_cliente_email.text().lower()
        numero = self.ui.line_update_cliente_numero.text()
        try:
            self.api.actualizar_cliente(cliente_id=cli_id, cliente=ClienteCreate(nombre=nombre,email=email,numero=numero))
        except ErrorAPI as e:
            warning_box(self, str(e))
        self.check_actualizacion_cliente()
        self.rellenar_tabla_clientes()
    # - ACTUALIZACION DE TECNICO
    def check_actualizacion_tecnico(self):
        condicion = (
            self.ui.line_update_tecnico_nombre.text() != self.tecnico.nombre or
            self.ui.combo_update_tecnico_especialidad.currentText().lower() != self.tecnico.especialidad
        )
        self.ui.but_update_tecnico_actualizar.setEnabled(condicion)
    def actualizar_tecnico(self):
        tec_id = self.tecnico.id
        nombre = self.ui.line_update_tecnico_nombre.text().lower()
        especialidad = self.ui.combo_update_tecnico_especialidad.currentText().lower()
        try:
            self.api.actualizar_tecnico(tecnico_id=tec_id, tecnico=TecnicoCreate(nombre=nombre,especialidad=especialidad))
        except ErrorAPI as e:
            warning_box(self, str(e))
        self.check_actualizacion_tecnico()
        self.rellenar_tabla_tecnicos()

    # - ACTUALIZACION DE REPARACION
    def check_actualizacion_reparacion(self): #TODO revisar entero
        condicion = (
            self.ui.line_update_reparacion_cliente.property("UUID") != self.reparacion.cliente or
            self.ui.line_update_reparacion_tecnico.property("UUID") != self.reparacion.tecnico or
            self.ui.combo_update_reparacion_estado.currentText().lower() != self.reparacion.estado or
            (self.ui.line_update_reparacion_equipo.text() != self.reparacion.equipo and self.ui.line_update_reparacion_equipo.text() != "") or
            (self.ui.line_update_reparacion_descripcion.text() != self.reparacion.descripcion and self.ui.line_update_reparacion_descripcion.text() != "") or
            (self.ui.line_update_reparacion_coste.text() != str(self.reparacion.coste) and self.ui.line_update_reparacion_coste.text() != "")        )
        self.ui.but_update_reparacion_actualizar.setEnabled(condicion)
    def actualizar_reparacion(self):
        rep_id = self.reparacion.id
        cliente = self.ui.line_update_reparacion_cliente.property("UUID")
        tecnico = self.ui.line_update_reparacion_tecnico.property("UUID")
        estado = self.ui.combo_update_reparacion_estado.currentText().lower()
        equipo = self.ui.line_update_reparacion_equipo.text().strip()
        descripcion = self.ui.line_update_reparacion_descripcion.text().strip()
        coste = float(self.ui.line_update_reparacion_coste.text().strip())
        try:
            self.api.actualizar_reparacion(reparacion_id=rep_id, reparacion=ReparacionCreate(cliente=cliente, tecnico=tecnico, equipo=equipo, descripcion=descripcion, coste=coste, estado=estado))
        except ErrorAPI as e:
            warning_box(self, str(e))
        self.check_actualizacion_reparacion()
        self.rellenar_tabla_reparaciones()

    # -- FUNCIONES DE ELIMINACION DE ELEMENTOS
    # - PREGUNTA PARA CONFIRMACION DE ELMINAR
    def confirmar_eliminacion(self):
        return QMessageBox.question(
            self,
            'Eliminando el elemento',
            '¿Estas seguro de que quieres eliminar de forma permanente?',
            QMessageBox.StandardButton.Apply | QMessageBox.StandardButton.Cancel
        )
    # - ELIMINACION DE CLIENTE
    def check_eliminar_cliente(self):
        """
        Activa el boton de eliminacion cuando el line de update de cliente es habilitado
        """
        condicion = self.ui.line_update_cliente_nombre.isEnabled()
        self.ui.but_update_cliente_eliminar.setEnabled(condicion)
    def eliminar_cliente(self):
        respuesta = self.confirmar_eliminacion()
        if respuesta == QMessageBox.StandardButton.Cancel:
            return
        try:
            self.api.borrar_cliente(self.cliente.id)
        except ErrorAPI as e:
            warning_box(self, str(e))
        self.limpiar_ventana(self.ventana_actual)
        self.rellenar_tabla_clientes()
        self.actualizar_titulo(self.ventana_actual)
    # - ELIMINACION DE TECNICO
    def check_eliminar_tecnico(self):
        condicion = self.ui.line_update_tecnico_nombre.isEnabled()
        self.ui.but_update_tecnico_eliminar.setEnabled(condicion)
    def eliminar_tecnico(self):
        respuesta = self.confirmar_eliminacion()
        if respuesta == QMessageBox.StandardButton.Cancel:
            return
        try:
            self.api.borrar_tecnico(self.tecnico.id)
        except ErrorAPI as e:
            warning_box(self, str(e))
        self.limpiar_ventana(self.ventana_actual)
        self.rellenar_tabla_tecnicos()
        self.actualizar_titulo(self.ventana_actual)
    # - ELIMINACION DE LA REPARACION
    def check_eliminar_reparacion(self):
        condicion = self.ui.line_update_reparacion_cliente.isEnabled()
        self.ui.but_update_reparacion_eliminar.setEnabled(condicion)
    def eliminar_reparacion(self):
        respuesta = self.confirmar_eliminacion()
        if respuesta == QMessageBox.StandardButton.Cancel:
            return
        try:
            self.api.borrar_reparacion(self.reparacion.id)
        except ErrorAPI as e:
            warning_box(self, str(e))
        self.limpiar_ventana(self.ventana_actual)
        self.rellenar_tabla_reparaciones()
        self.actualizar_titulo(self.ventana_actual)


    # -- FUNCION ENCARGADA DE PONER LA VENTANA DE ESTADISTICAS Y COMPLETAR LOS CAMPOS
    def estadisticas(self):
        #Parte registrados
        self.ui.line_estad_client_regist.setText(str(len(self.clientes)))
        self.ui.line_estad_tecn_regist.setText(str(len(self.tecnicos)))
        self.ui.line_estad_rep_registradas.setText(str(len(self.reparaciones)))
        #Parte estados
        self.ui.line_estad_rep_pendientes.setText(str(len([reparacion for reparacion in self.reparaciones.values() if reparacion.estado == "pendiente"])))
        self.ui.line_estad_rep_en_proceso.setText(str(len([reparacion for reparacion in self.reparaciones.values() if reparacion.estado == "en proceso"])))
        self.ui.line_estad_rep_finalizadas.setText(str(len([reparacion for reparacion in self.reparaciones.values() if reparacion.estado == "finalizada"])))
        #Para facturacion
        self.ui.line_estad_rep_ganancias.setText(f'{sum([reparacion.get_with_iva() for reparacion in self.reparaciones.values() if reparacion.estado == "finalizada"]):.2f} €')

        self.establecer_ventana('page_estadisticas',self.ventana_actual)

    # - PERSISTENCIA -
    def importar(self): #TODO pendiente de implementar
        pass

    def exportar(self): #TODO pendiente de implementar
        pass

    """ Igual se reutiliza, pero en deshuso actual
    # -- FUNCIONES DE PERSISTENCIA
    def dialogo_confirmacion_no_guardado(self) -> QMessageBox.StandardButton:
        return QMessageBox.question(
            self,
            'Taller sin guardar',
            'Estas a punto de cerrar la ventana sin haber guardado los cambios realizados\n'
            'Se perderan los cambios si continuas sin guardar',
            QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel,
        )

    def guardar(self):
        try:
            self.taller.exportar()
            self.taller_guardado = copy.deepcopy(self.taller)
        except:
            print('Hubo un error raro al guardar, resuelvelo')

    def abrir(self):
        #Comprobacion de que este guardado
        if not self.guardado():
            respuesta = self.dialogo_confirmacion_no_guardado()


            if respuesta == QMessageBox.StandardButton.Save:
                self.guardar()
            elif respuesta == QMessageBox.StandardButton.Discard:
                pass #Se abre el siguiente archivo y listo
            else:
                return #Se cancela la apertura

        ruta, _ = QFileDialog.getOpenFileName(
            self,
            'Abrir archivo',
            './datos/',
            'Archivos de tienda (*.store);',

        )

        if ruta == "":
            return

        self.taller = persistencia.cargar_taller(ruta.split('/')[-1].replace('.store', ''))
        self.taller_guardado = copy.deepcopy(self.taller)

        self.rellenar_tablas()

        self.establecer_ventana("page_tabla_reparaciones","")
        self.actualizar_titulo(self.ventana_actual)

    def closeEvent(self, event: PySide6.QtGui.QCloseEvent, /) -> None:
        # Comprobacion de que este guardado
        if not self.guardado():
            respuesta = self.dialogo_confirmacion_no_guardado()

            if respuesta == QMessageBox.StandardButton.Save:
                self.guardar()
                event.accept()
            elif respuesta == QMessageBox.StandardButton.Discard:
                event.accept()
            else:
                event.ignore()
    """
    # -- FUNCIONES AGRUPACION CONEXIONES
    # - CONEXIONES DE LAS ACCIONES
    def conectar_acciones(self):
        """
        Conecta las acciones a los métodos correspondientes
        """
        #Administracion
        self.ui.action_crear_cliente.triggered.connect(lambda: self.establecer_ventana("page_crear_cliente",self.ventana_actual))
        self.ui.action_crear_tecnico.triggered.connect(lambda: self.establecer_ventana("page_crear_tecnico",self.ventana_actual))
        self.ui.action_crear_reparacion.triggered.connect(lambda: self.establecer_ventana("page_crear_reparacion",self.ventana_actual))
        self.ui.action_consultar_clientes.triggered.connect(lambda: self.establecer_ventana("page_tabla_clientes",self.ventana_actual))
        self.ui.action_consultar_tecnicos.triggered.connect(lambda: self.establecer_ventana("page_tabla_tecnicos",self.ventana_actual))
        self.ui.action_consultar_reparaciones.triggered.connect(lambda: self.establecer_ventana("page_tabla_reparaciones",self.ventana_actual))
        self.ui.action_consultar_Modificar_cliente.triggered.connect(lambda: self.establecer_ventana("page_actualizacion_cliente",self.ventana_actual))
        self.ui.action_consultar_Modificar_tecnico.triggered.connect(lambda: self.establecer_ventana("page_actualizacion_tecnico",self.ventana_actual))
        self.ui.action_consultar_Modificar_reparacion.triggered.connect(lambda: self.establecer_ventana("page_actualizacion_reparacion",self.ventana_actual))
        #Persistencia
        """
        self.ui.action_guardar.triggered.connect(self.guardar)
        self.ui.action_abrir_tienda.triggered.connect(self.abrir)
        """
        self.ui.action_import.triggered.connect(self.importar)
        self.ui.action_export.triggered.connect(self.exportar)
        self.ui.action_salir.triggered.connect(self.close) #Utilizo el propio evento de salir
        #Estadisticas
        self.ui.action_estadisticas.triggered.connect(self.estadisticas)
    # - CONEXIONES DE LOS FILTROS
    def conectar_filtros(self) -> None:
        """
        Conecta los filtros a los campos encargados de ello
        """
        #Filtro clientes
        self.ui.line_filter_cliente_nombre.textChanged.connect(self.rellenar_tabla_clientes)
        #Filtro tecnicos
        self.ui.line_filter_tecnico_nombre.textChanged.connect(self.rellenar_tabla_tecnicos)
        self.ui.combo_filter_tecnico_especialidad.currentTextChanged.connect(self.rellenar_tabla_tecnicos)
        #Filtro reparacion
        self.ui.line_filter_reparacion_cliente.textChanged.connect(self.rellenar_tabla_reparaciones)
        self.ui.line_filter_reparacion_tecnico.textChanged.connect(self.rellenar_tabla_reparaciones)
        self.ui.combo_filter_reparacion_estado.currentTextChanged.connect(self.rellenar_tabla_reparaciones)
        self.ui.combo_filter_reparacion_orden.currentTextChanged.connect(self.rellenar_tabla_reparaciones)
        self.ui.but_filter_reparacion_direccion.clicked.connect(self.alterar_direccion)
    # - CONEXIONES DE CREACION
    def conectar_creacion(self):
        #Creacion cliente
        self.ui.line_nombre_cliente.textChanged.connect(self.check_crear_cliente)
        self.ui.line_email_cliente.textChanged.connect(self.check_crear_cliente)
        self.ui.line_numero_cliente.textChanged.connect(self.check_crear_cliente)
        self.ui.but_guardar_creacion_cliente.clicked.connect(self.crear_cliente)
        self.ui.but_limpiar_creacion_cliente.clicked.connect(lambda: self.limpiar_ventana("page_crear_cliente"))
        #Creacion del tecnico
        self.ui.line_nombre_tecnico.textChanged.connect(self.check_crear_tecnico)
        self.ui.combo_especialidad.currentIndexChanged.connect(self.check_crear_tecnico)
        self.ui.but_guardar_creacion_tecnico.clicked.connect(self.crear_tecnico)
        self.ui.but_limpiar_creacion_tecnico.clicked.connect(lambda: self.limpiar_ventana("page_crear_tecnico"))
        #Creacion de la reparacion
        self.ui.line_crear_reparacion_cliente.textChanged.connect(self.check_crear_reparacion)
        self.ui.line_crear_reparacion_tecnico.textChanged.connect(self.check_crear_reparacion)
        self.ui.line_crear_reparacion_equipo.textChanged.connect(self.check_crear_reparacion)
        self.ui.line_crear_reparacion_descripcion.textChanged.connect(self.check_crear_reparacion)
        self.ui.line_crear_reparacion_coste.textChanged.connect(self.check_crear_reparacion)
        self.ui.but_crear_reparacion_guardar.clicked.connect(self.crear_reparacion)
        self.ui.but_crear_reparacion_limpiar.clicked.connect(lambda: self.limpiar_ventana("page_crear_reparacion"))
    # - CONEXIONES DE CONSULTA DE CLIENTE, TECNICO, Y REPARACION
    def conectar_consultas(self):
        # PARTE DE CREACION DE REPARACION
        #Cliente
        self.ui.but_crear_reparacion_cliente.clicked.connect(lambda: self.establecer_ventana(ventana_objetivo="page_tabla_clientes", ventana_origen=self.ventana_actual, select_intention=True))
        #Técnico
        self.ui.but_crear_reparacion_tecnico.clicked.connect(lambda: self.establecer_ventana(ventana_objetivo="page_tabla_tecnicos", ventana_origen=self.ventana_actual,select_intention=True))



        #PARTE DE ACTUALIZACION
        #Cliente
        self.ui.but_update_cliente_seleccionar.clicked.connect(lambda: self.establecer_ventana(ventana_objetivo="page_tabla_clientes", ventana_origen=self.ventana_actual, select_intention=True))
        #Tecnico
        self.ui.but_update_tecnico_seleccionar.clicked.connect(lambda: self.establecer_ventana(ventana_objetivo="page_tabla_tecnicos", ventana_origen=self.ventana_actual,select_intention=True))
        #Reparacion
        self.ui.but_update_reparacion_cliente.clicked.connect(lambda: self.establecer_ventana(ventana_objetivo="page_tabla_clientes", ventana_origen=self.ventana_actual,select_intention=True))
        self.ui.but_update_reparacion_tecnico.clicked.connect(lambda: self.establecer_ventana(ventana_objetivo="page_tabla_tecnicos", ventana_origen=self.ventana_actual,select_intention=True))
        self.ui.but_update_reparacion_seleccionar.clicked.connect(lambda: self.establecer_ventana(ventana_objetivo="page_tabla_reparaciones", ventana_origen=self.ventana_actual,select_intention=True))


        # GENERAL
        #Select row check
        self.ui.table_clientes.selectionModel().selectionChanged.connect(self.check_select_cliente)
        self.ui.table_tecnicos.selectionModel().selectionChanged.connect(self.check_select_tecnico)
        self.ui.table_reparacion.selectionModel().selectionChanged.connect(self.check_select_reparacion)
        #Select button
        self.ui.but_select_clientes.clicked.connect(self.accion_select_cliente)
        self.ui.but_select_tecnicos.clicked.connect(self.accion_select_tecnico)
        self.ui.but_select_reparacion.clicked.connect(self.accion_select_reparacion)
        #Cancel
        self.ui.but_cancelar_clientes.clicked.connect(lambda: self.establecer_ventana(ventana_objetivo=self.ventana_previa,ventana_origen=self.ventana_actual))
        self.ui.but_cancelar_tecnicos.clicked.connect(lambda: self.establecer_ventana(ventana_objetivo=self.ventana_previa, ventana_origen=self.ventana_actual))
        self.ui.but_cancelar_reparacion.clicked.connect(lambda: self.establecer_ventana(ventana_objetivo=self.ventana_previa, ventana_origen=self.ventana_actual))
    # - CONEXIONES DE UPDATE
    def conectar_actualizacion(self):
        #Cliente
        self.ui.line_update_cliente_nombre.textChanged.connect(self.check_actualizacion_cliente)
        self.ui.line_update_cliente_email .textChanged.connect(self.check_actualizacion_cliente)
        self.ui.line_update_cliente_numero.textChanged.connect(self.check_actualizacion_cliente)
        self.ui.but_update_cliente_actualizar.clicked.connect(self.actualizar_cliente)
        #Update tecnico
        self.ui.line_update_tecnico_nombre.textChanged.connect(self.check_actualizacion_tecnico)
        self.ui.combo_update_tecnico_especialidad.currentTextChanged.connect(self.check_actualizacion_tecnico)
        self.ui.but_update_tecnico_actualizar.clicked.connect(self.actualizar_tecnico)
        #Update reparacion
        self.ui.line_update_reparacion_cliente.textChanged.connect(self.check_actualizacion_reparacion)
        self.ui.line_update_reparacion_tecnico.textChanged.connect(self.check_actualizacion_reparacion)
        self.ui.combo_update_reparacion_estado.currentTextChanged.connect(self.check_actualizacion_reparacion)
        self.ui.line_update_reparacion_equipo.textChanged.connect(self.check_actualizacion_reparacion)
        self.ui.line_update_reparacion_descripcion.textChanged.connect(self.check_actualizacion_reparacion)
        self.ui.line_update_reparacion_coste.textChanged.connect(self.check_actualizacion_reparacion)
        self.ui.but_update_reparacion_actualizar.clicked.connect(self.actualizar_reparacion)
    # - CONEXIONES DE ELIMINACION
    def conectar_eliminacion(self):
        #Cliente
        self.ui.line_update_cliente_nombre.textChanged.connect(self.check_eliminar_cliente)
        self.ui.but_update_cliente_eliminar.clicked.connect(self.eliminar_cliente)
        #Tecnico
        self.ui.line_update_tecnico_nombre.textChanged.connect(self.check_eliminar_tecnico)
        self.ui.but_update_tecnico_eliminar.clicked.connect(self.eliminar_tecnico)
        #Reparacion
        self.ui.line_update_reparacion_cliente.textChanged.connect(self.check_eliminar_reparacion)
        self.ui.but_update_reparacion_eliminar.clicked.connect(self.eliminar_reparacion)


    # - METODO QUE LLAMA A TODOS LOS INDIVIDUALES Y QUE ES EMPLEADO POR EL INIT
    def connect_events(self):
        #Conexion de las acciones
        self.conectar_acciones()
        #Conexion de los filtros
        self.conectar_filtros()
        #Conectar creacion
        self.conectar_creacion()
        #Conectar consultas
        self.conectar_consultas()
        #Conectar actualizaciones
        self.conectar_actualizacion()
        #Conectar eliminaciones
        self.conectar_eliminacion()