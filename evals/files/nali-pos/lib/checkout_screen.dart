import 'package:flutter/material.dart';

class CartLine {
  final String name;
  final int qty;
  final int price; // IQD
  CartLine(this.name, this.qty, this.price);
}

class CheckoutScreen extends StatefulWidget {
  const CheckoutScreen({super.key});

  @override
  State<CheckoutScreen> createState() => _CheckoutScreenState();
}

class _CheckoutScreenState extends State<CheckoutScreen> {
  final List<CartLine> lines = [
    CartLine('شیر - ١ لیتر', 2, 1500),
    CartLine('نانی سەمون', 10, 250),
    CartLine('پەنیری سپی', 1, 4750),
    CartLine('چای ئەحمەد', 1, 6000),
  ];
  int received = 0;

  int get total => lines.fold(0, (s, l) => s + l.qty * l.price);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF3F4F6),
      appBar: AppBar(
        backgroundColor: Colors.deepPurple,
        title: const Text('پارەدان', style: TextStyle(color: Colors.white, fontSize: 18, letterSpacing: 1.2)),
      ),
      body: Row(
        children: [
          Expanded(
            flex: 3,
            child: ListView.builder(
              itemCount: lines.length,
              itemBuilder: (context, i) {
                final l = lines[i];
                return Container(
                  margin: const EdgeInsets.only(left: 16, right: 8, top: 8),
                  padding: const EdgeInsets.fromLTRB(12, 10, 12, 10),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(20),
                    boxShadow: [BoxShadow(color: Colors.black12, blurRadius: 12)],
                  ),
                  child: Row(
                    children: [
                      Expanded(
                        child: Text(l.name, textAlign: TextAlign.left, style: const TextStyle(fontSize: 13, color: Color(0xFF374151))),
                      ),
                      Text('x${l.qty}', style: const TextStyle(fontSize: 12, color: Colors.grey)),
                      const SizedBox(width: 12),
                      Text('${l.qty * l.price} IQD', style: const TextStyle(fontSize: 13, fontWeight: FontWeight.bold, color: Color(0xFF111827))),
                      IconButton(
                        icon: const Icon(Icons.delete, size: 16, color: Colors.red),
                        onPressed: () => setState(() => lines.removeAt(i)),
                      ),
                    ],
                  ),
                );
              },
            ),
          ),
          Expanded(
            flex: 2,
            child: Container(
              color: Colors.white,
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Align(
                    alignment: Alignment.centerLeft,
                    child: Text('کۆی گشتی', style: TextStyle(fontSize: 14, color: Colors.grey[600])),
                  ),
                  Text('$total IQD', style: const TextStyle(fontSize: 28, fontWeight: FontWeight.w800, color: Colors.deepPurple)),
                  const SizedBox(height: 16),
                  Text('وەرگیراو: $received', style: const TextStyle(fontSize: 14)),
                  Text('گەڕاوە: ${received - total}', style: const TextStyle(fontSize: 14, color: Colors.green)),
                  const SizedBox(height: 16),
                  Wrap(
                    spacing: 6,
                    runSpacing: 6,
                    children: [1000, 5000, 10000, 25000, 50000].map((v) {
                      return ElevatedButton(
                        style: ElevatedButton.styleFrom(
                          minimumSize: const Size(36, 36),
                          backgroundColor: Colors.purple[50],
                          foregroundColor: Colors.deepPurple,
                        ),
                        onPressed: () => setState(() => received += v),
                        child: Text('$v', style: const TextStyle(fontSize: 12)),
                      );
                    }).toList(),
                  ),
                  const Spacer(),
                  Positioned(
                    left: 0,
                    child: TextButton(
                      onPressed: () => setState(() => received = 0),
                      child: const Text('سڕینەوە'),
                    ),
                  ),
                  SizedBox(
                    width: double.infinity,
                    child: ElevatedButton(
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.deepPurple,
                        foregroundColor: Colors.white,
                        padding: const EdgeInsets.symmetric(vertical: 14),
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(30)),
                      ),
                      onPressed: received >= total ? () {} : null,
                      child: const Text('تەواوکردن', style: TextStyle(fontSize: 16)),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
