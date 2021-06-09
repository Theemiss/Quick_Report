import 'package:flutter/material.dart';
import 'package:more_pro_ui_qr/buttons/insuranceselectablemenue.dart';

class FirstSignUpPage extends StatefulWidget {
  @override
  _FirstSignUpPageState createState() => _FirstSignUpPageState();
}

class _FirstSignUpPageState extends State<FirstSignUpPage> {
  @override
  Widget build(BuildContext context) {
    String? email, password, idCard, insuranceCompany;
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
