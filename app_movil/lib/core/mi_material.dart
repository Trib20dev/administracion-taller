import 'package:app_movil/core/router.dart';
import 'package:flutter/material.dart';

class MiMaterial extends StatelessWidget {
  const MiMaterial({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      title: 'Administración de Taller',
      theme: ThemeData(
        colorSchemeSeed: Colors.blueGrey,
        useMaterial3: true,
      ),
      debugShowCheckedModeBanner: false,
      routerConfig: MiRouter.crearRouter(),
    );
  }
}