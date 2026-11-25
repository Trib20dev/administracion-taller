class Tecnico {
  final String id;
  final String nombre;
  final String especialidad;

  Tecnico({
    required this.id,
    required this.nombre,
    required this.especialidad,
  });

  factory Tecnico.fromJson(Map<String, dynamic> json) {
    return Tecnico(
      id: json['id'] as String,
      nombre: json['nombre'] as String,
      especialidad: json['especialidad'] as String,
    );
  }
}