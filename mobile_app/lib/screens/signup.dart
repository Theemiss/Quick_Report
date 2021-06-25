// This module shows the first sign up screen
//
// First user's information entry

import 'package:flutter/material.dart';
import 'package:more_pro_ui_qr/buttons/insuranceselectablemenue.dart';
import 'package:shared_preferences/shared_preferences.dart';

//Stateful widget of the signup screen
// geting input inormation from user
class FirstSignUpPage extends StatefulWidget {
  @override
  _FirstSignUpPageState createState() => _FirstSignUpPageState();
}

class _FirstSignUpPageState extends State<FirstSignUpPage> {
  @override
  Widget build(BuildContext context) {
    // ignore: unused_local_variable
    String? email, password, idCard, insuranceCompany;
    // ignore: unused_local_variable
    bool isLogged = false;
    TextEditingController _emailController = TextEditingController();
    TextEditingController _passwordController = TextEditingController();
    TextEditingController _idCardController = TextEditingController();
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
                    image: AssetImage('assets/register.png'),
                    height: 150,
                  ),
                  SizedBox(height: 40),
                  Card(
                    shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(50)),
                    child: TextFormField(
                      controller: _emailController,
                      onSaved: (val) {
                        email = val;
                      },
                      decoration: InputDecoration(
                        border: OutlineInputBorder(
                            borderRadius: const BorderRadius.all(
                                const Radius.circular(50))),
                        contentPadding: EdgeInsets.all(15),
                        suffixIcon: Icon(Icons.email, size: 35),
                        labelText: "Email",
                        hintText: "Enter your email adress",
                      ),
                      keyboardType: TextInputType.emailAddress,
                    ),
                  ),
                  SizedBox(height: 20),
                  Card(
                    shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(50)),
                    child: TextFormField(
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
                        hintText: "Enter your password",
                      ),
                      keyboardType: TextInputType.text,
                    ),
                  ),
                  SizedBox(height: 20),
                  Card(
                    shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(50)),
                    child: TextFormField(
                      controller: _idCardController,
                      onSaved: (val) {
                        idCard = val;
                      },
                      decoration: InputDecoration(
                        border: OutlineInputBorder(
                            borderRadius: const BorderRadius.all(
                                const Radius.circular(50))),
                        contentPadding: EdgeInsets.all(15),
                        suffixIcon: Icon(Icons.payment, size: 35),
                        labelText: "ID card",
                        hintText: "Enter your ID card number",
                      ),
                      keyboardType: TextInputType.number,
                    ),
                  ),
                  SizedBox(height: 20),
                  Card(
                    // borderOnForeground:
                    shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(50)),
                    child: Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 15),
                      child: DropDownMenue(),
                    ),
                  ),
                  SizedBox(height: 40),
                  Container(
                    height: 50,
                    width: double.infinity,
                    child: ElevatedButton(
                      onPressed: () {
                        savePref(_emailController.text, _idCardController.text,
                            _passwordController.text);
                        Navigator.pushNamed(context, '/thirdPage');
                      },
                      child: Text('Move to the next step'),
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
                      Navigator.pop(context);
                    },
                    child: Text.rich(
                      TextSpan(
                        text: "Already have an account? ",
                        children: [
                          TextSpan(
                            text: "Sign In",
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

// saving the users data in the cache memory of the phone
savePref(String email, cin, password) async {
  SharedPreferences preferences = await SharedPreferences.getInstance();

  preferences.setString("email", email);
  preferences.setString("cin", cin);
  preferences.setString("password", password);

  // ignore: deprecated_member_use
  preferences.commit();
}
