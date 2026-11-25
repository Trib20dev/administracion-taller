import json
import uuid
from pathlib import Path
from uuid import UUID
from typing import override, Literal, Self
from servidor import persistencia


class PersonaNoExisteError(Exception):
    pass

class PersonaDuplicadaError(Exception):
    pass

class Persona:
    """
    En la creacion de una persona su ID autogenerado se guarda en el listado estatico
    Y los nombre se guardan en lowercase
    """
    def __init__(self, nombre:str, uid: UUID | None = None):
        self._id = uid if uid is not None else uuid.uuid4()
        self.nombre = nombre.lower()

    @property
    def id(self):
        return self._id

    def info(self) -> None:
        print(f'{self.nombre}')

    def to_dict(self) -> dict:
        return {
            "nombre": self.nombre
        }

class Cliente(Persona):
    def __init__(self, nombre:str, email:str, numero:str, uid: UUID | None = None):
        super().__init__(nombre, uid=uid)
        self.email = email
        self.numero = numero

    @classmethod
    def from_dict(cls, key:str, value:dict) -> Self:
        return cls(uid=UUID(key), **value)


    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value,Cliente):
            return False
        return (self._id == value._id and
                self.nombre == value.nombre and
                self.email == value.email and
                self.numero == value.numero)

    @override
    def info(self):
        print(f'{self.nombre} - {self.email} - {self.numero}')

    def to_dict(self) -> dict:
        datos = super().to_dict()
        datos.update({
            "email": self.email,
            "numero": self.numero
        })
        return datos


class Tecnico(Persona):
    def __init__(self, nombre:str,especialidad:Literal["software", "hardware"], uid: UUID | None = None):
        super().__init__(nombre,uid=uid)
        self.especialidad = especialidad

    @classmethod
    def from_dict(cls, key: str, value: dict) -> Self:
        return cls(uid=UUID(key), **value)

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value,Tecnico):
            return False
        condicion = self._id == value._id and self.nombre == value.nombre and self.especialidad == value.especialidad
        return condicion

    @override
    def info(self):
        print(f'{self.nombre} - {self.especialidad}')

    def to_dict(self) -> dict:
        datos = super().to_dict()
        datos["especialidad"] = self.especialidad
        return datos

class Reparacion:
    def __init__(self, cliente:UUID, equipo:str, descripcion:str, coste:float, tecnico:UUID | None = None, estado:str | None = 'pendiente',uid: UUID | None = None):
        self._id = uid if uid is not None else uuid.uuid4()
        self.cliente = cliente if isinstance(cliente, UUID) else UUID(str(cliente))
        self.equipo = equipo
        self.descripcion = descripcion
        self.tecnico = (
            None if tecnico is None
            else (tecnico if isinstance(tecnico, UUID) else UUID(str(tecnico)))
        )
        self.estado = estado
        if coste < 0:
            raise ValueError('Coste negativo no valido')
        self.coste = coste

    @classmethod
    def from_dict(cls, key: str, value: dict) -> Self:
        return cls(uid=UUID(key), **value)

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value,Reparacion):
            return False
        return (
            self._id == value._id and
            self.cliente == value.cliente and
            self.tecnico == value.tecnico and
            self.equipo == value.equipo and
            self.descripcion == value.descripcion and
            self.estado == value.estado and
            self.coste == value.coste
        )

    @property
    def id(self):
        return self._id

    def to_dict(self) -> dict:
        return {
            "cliente": str(self.cliente),
            "equipo": self.equipo,
            "descripcion": self.descripcion,
            "tecnico": str(self.tecnico) if self.tecnico is not None else None,            "estado": self.estado,
            "coste": self.coste
        }

    def __str__(self):
        return f'{self.id}'


    def change_state(self, estado:str) -> None:
        if estado != 'pendiente' and estado != 'en proceso' and estado != 'finalizada':
            raise NameError('Estado no valido')
        self.estado = estado

    def change_price_to(self, new_price: float) -> None:
        if new_price < 0:
            raise ValueError('Precio negativo no valido')
        self.coste = new_price

    def get_with_iva(self) -> float:
        return self.coste * 1.21

    def asignar_tecnico(self,tecnico):
        self.tecnico = UUID(tecnico)

    def modificar_estado(self, estado:str):
        self.estado = estado

    def modificar_coste(self,coste:str):
        try:
            coste_parseado = float(coste)
            if coste_parseado < 0:
                raise ValueError('Coste negativo no valido')
            self.coste = float(coste_parseado)
        except ValueError as e:
            print(f'No me seas melon: {e}')

    def info(self):
        print(f'Reparacion:\nCliente: {self.cliente} - Tecnico: {self.tecnico} - Equipo:{self.equipo} - Coste (IVA aplicado){self.get_with_iva()}')

class Taller:
    def __init__(self, nombre:str):

        self.nombre = nombre
        self.clientes: dict[UUID, Cliente] = {}
        self.tecnicos: dict[UUID, Tecnico] = {}
        self.reparaciones: dict[UUID, Reparacion] = {}

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, Taller):
            return False
        condicion = (self.nombre == value.nombre and
                     self.clientes == value.clientes and
                     self.tecnicos == value.tecnicos and
                     self.reparaciones == value.reparaciones
                     )
        return condicion


    def _set_clientes(self, clientes: dict[UUID, Cliente]) -> None:
        self.clientes = clientes

    def _set_tecnicos(self, tecnicos: dict[UUID, Tecnico]) -> None:
        self.tecnicos = tecnicos

    def _set_reparaciones(self, reparaciones: dict[UUID, Reparacion]) -> None:
        self.reparaciones = reparaciones

    def add_client(self, cliente: Cliente) -> None:
        self.clientes.update({
            cliente.id: cliente
        })

    def add_tecnico(self, tecnico: Tecnico) -> None:
        self.tecnicos.update({
            tecnico.id: tecnico
        })

    def add_reparacion(self, reparacion: Reparacion) -> None:
        self.reparaciones.update({
            reparacion.id: reparacion
        })

    def alta_cliente(self,nombre:str,email:str,numero:str):
        """
            Funcion encargada de pedir los datos para dar de
            alta a un cliente.
            :return: El id del cliente y el cliente como tupla
        """
        try:
            cliente = Cliente(nombre, email, numero)
        except PersonaDuplicadaError as e:
            raise e
            print(f'No se pudo crear el cliente: {e}')
        self.clientes[cliente.id] = cliente
        # for cliente in self.clientes.values():
        #     cliente.info()

    def alta_tecnico(self,nombre:str,especialidad:Literal["software", "hardware"]):
        """
            Funcion encargada de pedir los datos para dar de
            alta a un tecnico.
            :return: El id del tecnico y el tecnico como tupla
        """
        try:
            tecnico = Tecnico(nombre, especialidad)
        except PersonaDuplicadaError as e:
            raise e
        self.tecnicos[tecnico.id] = tecnico
        # for tecnico in self.tecnicos.values():
        #     tecnico.info()

    def registrar_reparacion(self, cliente:UUID,equipo:str,descripcion:str,tecnico:UUID|None,coste:str):
        try:
            coste_parseado = float(coste)
            reparacion = Reparacion(cliente, equipo, descripcion, coste_parseado, tecnico)
        except (PersonaNoExisteError, ValueError) as e:
            print(f'No se pudo crear la reparacion: {e}')
            return

        self.reparaciones[reparacion.id] = reparacion

    # def guardar(self):
    #     from src import persistencia
    #     persistencia.guardar_datos(self.nombre,self.clientes,self.tecnicos,self.reparaciones)

    def imprimir_personas(self):
        """
        Imprime los clientes y tecnicos del taller
        """
        print('Clientes:')
        for cliente in self.clientes.values():
            cliente.info()
        print('Tecnicos:')
        for tecnico in self.tecnicos.values():
            tecnico.info()

    def print_filtered_repairs(self, estado:str) -> None:
        filtered_list = [reparacion for reparacion in self.reparaciones.values() if reparacion.estado == estado]
        for reparacion in filtered_list:
            reparacion.info()

    def get_total_repaired_gain(self):
        return sum(reparacion.get_with_iva() for reparacion in self.reparaciones.values() if reparacion.estado == 'finalizada')

    def existe_reparacion(self, reparacion):
        existe = False
        try:
            existe = self.reparaciones[UUID(reparacion)] is not None
        except ValueError as e:
            print('Introdujiste un id no valido')
        return existe

    def obtener_reparacion(self, reparacion):
        return self.reparaciones[UUID(reparacion)]

    def existe_tecnico(self, tecnico):
        existe = False
        try:
            existe = self.tecnicos[UUID(tecnico)] is not None
        except ValueError as e:
            print('Introdujiste un id no valido')
        return existe

    def imprimir_por_estado(self, estado):
        for reparacion in [reparacion for reparacion in self.reparaciones.values() if reparacion.estado == estado]:
            reparacion.info()

    def ganancia_total_reparadas(self):
        print(self.get_total_repaired_gain())

    def imprimir_estadisticas(self):
        print(f'Total de reparaciones: {len(self.reparaciones)}')
        print('Reparaciones por estado:')
        print(f'Pendiente:  {len([reparacion for reparacion in self.reparaciones.values() if reparacion.estado == 'pendiente'])}')
        print(f'En proceso: {len([reparacion for reparacion in self.reparaciones.values() if reparacion.estado == 'en proceso'])}')
        print(f'Finalizada: {len([reparacion for reparacion in self.reparaciones.values() if reparacion.estado == 'finalizada'])}')
        clientes = []
        for reparacion in self.reparaciones.values():
            if reparacion.cliente not in clientes:
                clientes.append(reparacion.cliente)
        print(f'Hay {len(clientes)} clientes con reparaciones')