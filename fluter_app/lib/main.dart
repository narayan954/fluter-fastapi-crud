import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Image Processing App',
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  TextEditingController imageUrlController = TextEditingController();

  Future<void> processImage() async {
    final response = await http.post(
      Uri.parse('http://127.0.0.1:8000/process_image'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode({'image_url': imageUrlController.text}),
    );

    if (response.statusCode == 200) {
      print('Image processing successful');
      // Handle the response as needed
    } else {
      print('Failed to process image');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Image Processing App'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            TextField(
              controller: imageUrlController,
              decoration: InputDecoration(labelText: 'Enter Image URL'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                processImage();
              },
              child: Text('Process Image'),
            ),
          ],
        ),
      ),
    );
  }
}
