import 'package:flutter/material.dart';
import '../models/cliente.dart';
import '../models/tecnico.dart';
import '../models/reparacion.dart';
import '../services/api_service.dart';

class TallerProvider extends ChangeNotifier {
  final ApiService _apiService;

  TallerProvider(this._apiService);

  String? _nombreTaller;
  bool _cargando = false;
  String? _error;

  Map<String, Cliente> _clientes = {};
  Map<String, Tecnico> _tecnicos = {};
  List<Reparacion> _reparaciones = [];

  String? get nombreTaller => _nombreTaller;
  bool get cargando => _cargando;
  String? get error => _error;

  Map<String, Cliente> get clientes => _clientes;
  Map<String, Tecnico> get tecnicos => _tecnicos;
  List<Reparacion> get reparaciones => _reparaciones;

  String obtenerNombreCliente(String clienteId) {
    return _clientes[clienteId]?.nombre ?? 'Cliente desconocido';
  }

  String obtenerNombreTecnico(String? tecnicoId) {
    if (tecnicoId == null) return 'Sin asignar';
    return _tecnicos[tecnicoId]?.nombre ?? 'Técnico desconocido';
  }

  double get ingresosTotales =>
      _reparaciones.fold(0.0, (suma, r) => suma + r.coste);

  int contarPorEstado(String estado) => _reparaciones
      .where((r) => r.estado.toLowerCase() == estado.toLowerCase())
      .length;

  Future<bool> iniciarSesion(String nombre, String contrasena) async {
    _cargando = true;
    _error = null;
    notifyListeners();

    try {
      await _apiService.login(nombre, contrasena);
      _nombreTaller = nombre;
      await cargarDatos();
      return true;
    } catch (e) {
      _error = e.toString().replaceFirst('Exception: ', '');
      _cargando = false;
      notifyListeners();
      return false;
    }
  }

  Future<void> cargarDatos() async {
    _cargando = true;
    _error = null;
    notifyListeners();

    try {
      final resultados = await Future.wait([
        _apiService.getClientes(),
        _apiService.getTecnicos(),
        _apiService.getReparaciones(),
      ]);

      final listaClientes = resultados[0] as List<Cliente>;
      final listaTecnicos = resultados[1] as List<Tecnico>;
      final listaReparaciones = resultados[2] as List<Reparacion>;

      _clientes = {for (var c in listaClientes) c.id: c};
      _tecnicos = {for (var t in listaTecnicos) t.id: t};
      _reparaciones = listaReparaciones;
    } catch (e) {
      _error = e.toString().replaceFirst('Exception: ', '');
    } finally {
      _cargando = false;
      notifyListeners();
    }
  }

  void cerrarSesion() {
    _apiService.setToken(null);
    _nombreTaller = null;
    _clientes = {};
    _tecnicos = {};
    _reparaciones = [];
    _error = null;
    notifyListeners();
  }
}