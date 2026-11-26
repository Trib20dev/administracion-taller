import 'package:app_movil/providers/taller_provider.dart';
import 'package:app_movil/services/api_service.dart';
import 'package:flutter/material.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:provider/provider.dart';
import 'core/mi_material.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await dotenv.load(fileName: '.env');

  final apiUrl = dotenv.env['API_URL'] ?? 'http://127.0.0.1:8000';
  final apiService = ApiService(baseUrl: apiUrl);

  runApp(
    ChangeNotifierProvider(
      create: (_) => TallerProvider(apiService),
      child: const MiMaterial(),
    ),
  );
}