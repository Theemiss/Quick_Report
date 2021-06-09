import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';

class MyLogInPage extends StatefulWidget {
  @override
  _MyLogInPageState createState() => _MyLogInPageState();
}

class _MyLogInPageState extends State<MyLogInPage> {
  @override
  Widget build(BuildContext context) {
    String? email, password;
    bool isLoading = false;
    TextEditingController _emailController = new TextEditingController();
    TextEditingController _passwordController = new TextEditingController();
    final _key = GlobalKey<FormState>();
    return Scaffold(
      body: Center(
        child: SingleChildScrollView(
          child: Padding(
            padding: EdgeInsets.all(20),
            child: Form(
              key: _key,
              child: Column(
                children: <Widget>[
                  Image(
                    image: AssetImage('assets/login-icon-3047.png'),
                    height: 150,
                  ),
                  SizedBox(height: 20),
                  Card(
                    shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(50)),
                    child: TextFormField(
                      // validator: (e) =>
                      //     e.isEmpty ? "Please enter your email adress" : null,
                      controller: _emailController,
                      onSaved: (val) {
                        email = val;
                      },
                      decoration: InputDecoration(
                        border: OutlineInputBorder(
                          borderRadius: const BorderRadius.all(
                            const Radius.circular(50),
                          ),
                        ),
                        contentPadding: EdgeInsets.all(15),
                        suffixIcon: Icon(Icons.email, size: 35),
                        labelText: "Login",
                        hintText: "Email",
                      ),
                      //keyboardType: TextInputType.emailAddress,
                    ),
                  ),
                  SizedBox(height: 20),
                  Card(
                    shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(50)),
                    child: TextFormField(
                      // validator: (e) =>
                      //     e.isEmpty ? "Please enter your password" : null,
                      controller: _passwordController,
                      onSaved: (val) {
                        password = val;
                      },
                      obscureText: true,
                      decoration: InputDecoration(
                        border: OutlineInputBorder(
                            borderRadius: const BorderRadius.all(
                                const Radius.circular(50))),
                        contentPadding: EdgeInsets.all(15),
                        suffixIcon: Icon(Icons.visibility_off, size: 35),
                        labelText: "Password",
                        hintText: "Type your password",
                      ),
                      keyboardType: TextInputType.text,
                    ),
                  ),
                  SizedBox(height: 20),
                  Container(
                    height: 50,
                    width: double.infinity,
                    child: ElevatedButton(
                      onPressed: () {
                        login(_emailController.text, _passwordController.text,
                            context);
                      },
                      child: Text('Login'),
                      style: ElevatedButton.styleFrom(
                          primary: Colors.blueAccent,
                          onPrimary: Colors.white,
                          shape: (RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(50),
                          ))),
                    ),
                  ),
                  SizedBox(height: 80),
                  GestureDetector(
                    onTap: () {
                      Navigator.pushNamed(context, '/secondPage');
                    },
                    child: Text.rich(
                      TextSpan(
                        text: "Don't have an account? ",
                        children: [
                          TextSpan(
                            text: "Sign Up",
                            style: TextStyle(color: Colors.blueAccent),
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}

savePref(String jwt) async {
  SharedPreferences preferences = await SharedPreferences.getInstance();

  preferences.setString("jwt", jwt);
  preferences.setBool("isLogged", true);

  preferences.commit();
}

login(email, password, BuildContext context) async {
  Map user = {'Email': email, 'Password': password};
  var url = Uri.parse('http://102.37.113.211/api/login');
  final response = await http.post(url,
      headers: {'Content-Type': 'application/json'}, body: jsonEncode(user));
  if (response.statusCode == 200) {
    Map Mapresposne = jsonDecode(response.body);
    //print(Mapresposne);
    savePref(Mapresposne['token']);
    WidgetsFlutterBinding.ensureInitialized();
    SharedPreferences prefs = await SharedPreferences.getInstance();
    Navigator.pushNamed(context, '/fourthPage');
    //print(prefs.get('jwt'));

  } else {
    ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Please check your Email or your password')));
  }
}
