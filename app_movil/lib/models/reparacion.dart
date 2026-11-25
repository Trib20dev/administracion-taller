class Reparacion {
  final String id;
  final String cliente;
  final String? tecnico;
  final String equipo;
  final String descripcion;
  final double coste;
  final String estado;

  Reparacion({
    required this.id,
    required this.cliente,
    this.tecnico,
    required this.equipo,
    required this.descripcion,
    required this.coste,
    required this.estado,
  });

  double get costeConIva => coste * 1.21;

  factory Reparacion.fromJson(Map<String, dynamic> json) {
    return Reparacion(
      id: json['id'] as String,
      cliente: json['cliente'] as String,
      tecnico: json['tecnico'] as String?,
      equipo: json['equipo'] as String,
      descripcion: json['descripcion'] as String,
      coste: (json['coste'] as num).toDouble(),
      estado: json['estado'] as String,
    );
  }
}