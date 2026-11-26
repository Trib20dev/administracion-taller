import 'package:dio/dio.dart';
import '../models/cliente.dart';
import '../models/tecnico.dart';
import '../models/reparacion.dart';

class ApiService {
  final Dio _dio;
  String? _token;

  ApiService({required String baseUrl})
      : _dio = Dio(
          BaseOptions(
            baseUrl: baseUrl,
            connectTimeout: const Duration(seconds: 10),
            receiveTimeout: const Duration(seconds: 10),
            headers: {'Content-Type': 'application/json'},
          ),
        ) {
    _dio.interceptors.add(
      InterceptorsWrapper(
        onRequest: (options, handler) {
          if (_token != null) {
            options.headers['Authorization'] = 'Bearer $_token';
          }
          return handler.next(options);
        },
      ),
    );
  }

  void setToken(String? token) {
    _token = token;
  }

  String _extraerMensajeError(DioException e) {
    if (e.response?.data is Map && e.response?.data['detail'] != null) {
      return e.response!.data['detail'].toString();
    }
    if (e.type == DioExceptionType.connectionTimeout ||
        e.type == DioExceptionType.connectionError) {
      return 'No se pudo conectar con el servidor';
    }
    return 'Error de red (${e.response?.statusCode ?? 'desconocido'})';
  }

  Future<String> login(String nombre, String contrasena) async {
    try {
      final response = await _dio.post(
        '/login',
        data: {'nombre': nombre, 'contrasena': contrasena},
      );
      final token = response.data['access_token'] as String;
      setToken(token);
      return token;
    } on DioException catch (e) {
      throw Exception(_extraerMensajeError(e));
    }
  }

  Future<List<Cliente>> getClientes() async {
    try {
      final response = await _dio.get('/clientes');
      return (response.data as List)
          .map((json) => Cliente.fromJson(json as Map<String, dynamic>))
          .toList();
    } on DioException catch (e) {
      throw Exception(_extraerMensajeError(e));
    }
  }

  Future<List<Tecnico>> getTecnicos() async {
    try {
      final response = await _dio.get('/tecnicos');
      return (response.data as List)
          .map((json) => Tecnico.fromJson(json as Map<String, dynamic>))
          .toList();
    } on DioException catch (e) {
      throw Exception(_extraerMensajeError(e));
    }
  }

  Future<List<Reparacion>> getReparaciones() async {
    try {
      final response = await _dio.get('/reparaciones');
      return (response.data as List)
          .map((json) => Reparacion.fromJson(json as Map<String, dynamic>))
          .toList();
    } on DioException catch (e) {
      throw Exception(_extraerMensajeError(e));
    }
  }
}