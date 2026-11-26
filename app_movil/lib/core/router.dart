import '../screens/screens.dart';
import 'package:go_router/go_router.dart';

class MiRouter{

  static const String login = 'login';
  static const String home = 'home';

  static GoRouter crearRouter() =>
    GoRouter(routes: [
      GoRoute(path: '/',     name: login,builder: (_, state) => const LoginScreen()),
      GoRoute(path: '/home', name: home, builder: (_, state) => const HomeScreen()),
    ]);
    
  
}