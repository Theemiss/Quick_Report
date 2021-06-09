import 'package:flutter/material.dart';
import 'screens/login.dart';
import 'screens/signup.dart';
import 'screens/reportmanager.dart';
import 'screens/secondsignup.dart';
import 'package:shared_preferences/shared_preferences.dart';

var home;
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  SharedPreferences prefs = await SharedPreferences.getInstance();
  bool isLogged = (prefs.getBool('isLogged') ?? false);

  if (isLogged)
    home = ReportManager();
  else
    home = MyLogInPage();
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      initialRoute: '/',
      routes: {
        '/': (context) => home,
        '/secondPage': (context) => FirstSignUpPage(),
        '/thirdPage': (context) => SecondSignUpPage(),
        '/fourthPage': (context) => ReportManager(),
      },
    );
  }
}
