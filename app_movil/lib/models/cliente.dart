class Cliente {
  final String id;
  final String nombre;
  final String numero;
  final String email;

  Cliente({
    required this.id,
    required this.nombre,
    required this.numero,
    required this.email,
  });

  factory Cliente.fromJson(Map<String, dynamic> json) {
    return Cliente(
      id: json['id'] as String,
      nombre: json['nombre'] as String,
      numero: json['numero'] as String,
      email: json['email'] as String,
    );
  }
}