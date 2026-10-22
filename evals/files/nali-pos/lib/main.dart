import 'package:flutter/material.dart';
import 'checkout_screen.dart';

void main() => runApp(const NaliPosApp());

class NaliPosApp extends StatelessWidget {
  const NaliPosApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Nali Market POS',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(colorSchemeSeed: Colors.deepPurple, useMaterial3: true),
      home: const CheckoutScreen(),
    );
  }
}
