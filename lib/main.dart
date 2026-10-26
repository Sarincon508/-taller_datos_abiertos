import 'package:flutter/material.dart';
import 'config/environment.dart';
import 'routes/app_router.dart';
import 'themes/app_theme.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // Initialize environment variables from .env
  await Environment.init();

  runApp(const ColombiaOpenDataApp());
}

/// Root application widget configuring theme, router, and title.
class ColombiaOpenDataApp extends StatelessWidget {
  const ColombiaOpenDataApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      title: Environment.appName,
      debugShowCheckedModeBanner: false,
      theme: AppTheme.lightTheme,
      darkTheme: AppTheme.darkTheme,
      themeMode: ThemeMode.system,
      routerConfig: AppRouter.router,
    );
  }
}
