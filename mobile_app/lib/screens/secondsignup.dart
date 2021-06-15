import 'package:flutter/material.dart';

class SecondSignUpPage extends StatefulWidget {
  @override
  _SecondSignUpPageState createState() => _SecondSignUpPageState();
}

class _SecondSignUpPageState extends State<SecondSignUpPage> {
  @override
  Widget build(BuildContext context) {
    // ignore: unused_local_variable
    String? firstName,
        // ignore: unused_local_variable
        lastName,
        // ignore: unused_local_variable
        userAdress,
        // ignore: unused_local_variable
        phoneNumber,
        // ignore: unused_local_variable
        driverLicense,
        // ignore: unused_local_variable
        licenseDate;
    TextEditingController _firstNameController = TextEditingController();
    TextEditingController _lastNameController = TextEditingController();
    TextEditingController _userAdressController = TextEditingController();
    TextEditingController _phoneNumberController = TextEditingController();
    TextEditingController _driverLicenseController = TextEditingController();
    TextEditingController _licenseDateController = TextEditingController();
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
                    Container(
                      height: 100,
                      width: double.infinity,
                      child: Center(
                        child: Text("Please provide information",
                            style: TextStyle(
                                fontSize: 20,
                                fontWeight: FontWeight.bold,
                                color: Colors.blueAccent)),
                      ),
                    ),
                    Card(
                      shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(50)),
                      child: TextFormField(
                        controller: _firstNameController,
                        onSaved: (val) {
                          firstName = val;
                        },
                        decoration: InputDecoration(
                          border: OutlineInputBorder(
                              borderRadius: const BorderRadius.all(
                                  const Radius.circular(50))),
                          contentPadding: EdgeInsets.all(15),
                          suffixIcon: Icon(Icons.person, size: 35),
                          labelText: "First name",
                          hintText: "Enter your name",
                        ),
                        keyboardType: TextInputType.text,
                      ),
                    ),
                    SizedBox(height: 20),
                    Card(
                      shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(50)),
                      child: TextFormField(
                        controller: _lastNameController,
                        onSaved: (val) {
                          lastName = val;
                        },
                        decoration: InputDecoration(
                          border: OutlineInputBorder(
                              borderRadius: const BorderRadius.all(
                                  const Radius.circular(50))),
                          contentPadding: EdgeInsets.all(15),
                          suffixIcon: Icon(Icons.person, size: 35),
                          labelText: "Last name",
                          hintText: "Enter your Last name",
                        ),
                        keyboardType: TextInputType.text,
                      ),
                    ),
                    SizedBox(height: 20),
                    Card(
                      shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(50)),
                      child: TextFormField(
                        controller: _userAdressController,
                        onSaved: (val) {
                          userAdress = val;
                        },
                        decoration: InputDecoration(
                          border: OutlineInputBorder(
                              borderRadius: const BorderRadius.all(
                                  const Radius.circular(50))),
                          contentPadding: EdgeInsets.all(15),
                          suffixIcon: Icon(Icons.home, size: 35),
                          labelText: "Adress",
                          hintText: "Enter your adress",
                        ),
                        keyboardType: TextInputType.text,
                      ),
                    ),
                    SizedBox(height: 20),
                    Card(
                      shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(50)),
                      child: TextFormField(
                        controller: _phoneNumberController,
                        onSaved: (val) {
                          phoneNumber = val;
                        },
                        decoration: InputDecoration(
                          border: OutlineInputBorder(
                              borderRadius: const BorderRadius.all(
                                  const Radius.circular(50))),
                          contentPadding: EdgeInsets.all(15),
                          suffixIcon: Icon(Icons.phone, size: 35),
                          labelText: "Phone number",
                          hintText: "Enter your phone number",
                        ),
                        keyboardType: TextInputType.number,
                      ),
                    ),
                    SizedBox(height: 20),
                    Card(
                      shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(50)),
                      child: TextFormField(
                        controller: _driverLicenseController,
                        onSaved: (val) {
                          driverLicense = val;
                        },
                        decoration: InputDecoration(
                          border: OutlineInputBorder(
                              borderRadius: const BorderRadius.all(
                                  const Radius.circular(50))),
                          contentPadding: EdgeInsets.all(15),
                          suffixIcon: Icon(Icons.payment, size: 35),
                          labelText: "Driver's license",
                          hintText: "Enter your driver's license number",
                        ),
                        keyboardType: TextInputType.emailAddress,
                      ),
                    ),
                    SizedBox(height: 20),
                    Card(
                      shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(50)),
                      child: TextFormField(
                        controller: _licenseDateController,
                        onSaved: (val) {
                          licenseDate = val;
                        },
                        decoration: InputDecoration(
                          border: OutlineInputBorder(
                              borderRadius: const BorderRadius.all(
                                  const Radius.circular(50))),
                          contentPadding: EdgeInsets.all(15),
                          suffixIcon: Icon(Icons.payment, size: 35),
                          labelText: "Driver's license date",
                          hintText: "Enter your driver's license validity date",
                        ),
                        keyboardType: TextInputType.datetime,
                      ),
                    ),
                    SizedBox(height: 40),
                    Container(
                      height: 50,
                      width: double.infinity,
                      child: ElevatedButton(
                        onPressed: () {},
                        child: Text('Register'),
                        style: ElevatedButton.styleFrom(
                            primary: Colors.blueAccent,
                            onPrimary: Colors.white,
                            shape: (RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(50),
                            ))),
                      ),
                    ),
                    SizedBox(height: 40),
                    GestureDetector(
                      onTap: () {
                        Navigator.pop(context);
                      },
                      child: Text.rich(
                        TextSpan(
                          text: "",
                          children: [
                            TextSpan(
                              text: "Previous",
                              style: TextStyle(color: Colors.blueAccent),
                            ),
                          ],
                        ),
                      ),
                    ),
                  ],
                ),
              )),
        ),
      ),
    );
  }
}
