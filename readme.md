# Image Processing App

This repository contains a Flutter app for image processing and a FastAPI server for handling image processing requests.

## Flutter App

### Requirements

- Flutter SDK
- Dart SDK
- Android Studio / Xcode (for mobile device testing)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/narayan954/flutter-fastapi.git
   cd flutter-fastapi
   ```

2. Open the Flutter app:

   ```bash
   cd flutter_app
   ```

3. Install dependencies:

   ```bash
   flutter pub get
   ```

### Usage

1. Run the Flutter app:

   ```bash
   flutter run
   ```

2. Enter the image URL and press the "Process Image" button.

### Generating APK

To generate an APK for your Flutter app, run:

```bash
flutter build apk
```

Find the generated APK in `build/app/outputs/flutter-apk`.

## FastAPI Server

### Requirements

- Python
- FastAPI
- Uvicorn

### Installation

1. Open the FastAPI server:

   ```bash
   cd fastapi_server
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

2. The server will be running at `http://127.0.0.1:8000`. Update the Flutter app code to use this URL if hosted externally.

### Hosting FastAPI Server

1. Choose a hosting provider (e.g., Heroku, PythonAnywhere).

2. Deploy your FastAPI server according to the hosting provider's instructions.

3. Update the Flutter app code to use the hosted FastAPI server URL.

### Note

- Ensure both Flutter app and FastAPI server are running simultaneously for the app to function correctly.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
