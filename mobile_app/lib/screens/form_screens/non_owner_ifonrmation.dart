import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';

// import 'package:more_pro_ui_qr/screens/form_screens/check_boxes.dart';

class DriversInormation extends StatefulWidget {
  @override
  _DriversInormationState createState() => _DriversInormationState();
}

class _DriversInormationState extends State<DriversInormation> {
  @override
  Widget build(BuildContext context) {
    String? name, name2, driverpermit, validation, addre;
    TextEditingController _name = new TextEditingController();
    TextEditingController _name2 = new TextEditingController();
    TextEditingController _driverpermit = new TextEditingController();
    TextEditingController _driveradresse = new TextEditingController();
    TextEditingController _validation = new TextEditingController();

    final _key = GlobalKey<FormState>();
    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 70,
        title: Text('Filling the form'),
        centerTitle: true,
        actions: [
          IconButton(
            onPressed: () {},
            icon: Icon(Icons.notifications),
          ),
        ],
        flexibleSpace: Container(
          decoration: BoxDecoration(
            borderRadius: BorderRadius.vertical(
              bottom: Radius.circular(25),
            ),
            gradient: LinearGradient(
              colors: [Colors.redAccent, Colors.blueAccent],
              begin: Alignment.bottomRight,
              end: Alignment.topLeft,
            ),
          ),
        ),
        elevation: 30,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.vertical(
            bottom: Radius.circular(25),
          ),
        ),
      ),
      body: Center(
        child: SingleChildScrollView(
            child: Form(
          key: _key,
          child: Column(
            children: <Widget>[
              Text(
                'Please enter your information',
                style: TextStyle(
                    fontSize: 20,
                    color: Colors.blueAccent,
                    fontWeight: FontWeight.bold),
              ),
              SizedBox(height: 30),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20),
                child: TextFormField(
                  controller: _name,
                  decoration: InputDecoration(
                    border: OutlineInputBorder(
                      borderRadius: const BorderRadius.all(
                        const Radius.circular(50),
                      ),
                    ),
                    contentPadding: EdgeInsets.all(15),
                    suffixIcon: Icon(Icons.person, size: 35),
                    hintText: "First Name",
                  ),
                  onSaved: (val) {
                    name = val;
                  },
                ),
              ),
              SizedBox(height: 20),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20),
                child: TextFormField(
                  controller: _name2,
                  onSaved: (val) {
                    name2 = val;
                  },
                  decoration: InputDecoration(
                    border: OutlineInputBorder(
                      borderRadius: const BorderRadius.all(
                        const Radius.circular(50),
                      ),
                    ),
                    contentPadding: EdgeInsets.all(15),
                    suffixIcon: Icon(Icons.person, size: 35),
                    hintText: "Last Name",
                  ),
                ),
              ),
              SizedBox(height: 20),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20),
                child: TextFormField(
                  controller: _driverpermit,
                  onSaved: (val) {
                    driverpermit = val;
                  },
                  decoration: InputDecoration(
                    border: OutlineInputBorder(
                      borderRadius: const BorderRadius.all(
                        const Radius.circular(50),
                      ),
                    ),
                    contentPadding: EdgeInsets.all(15),
                    suffixIcon: Icon(Icons.payment, size: 35),
                    hintText: "Driver's license number",
                  ),
                ),
              ),
              SizedBox(height: 20),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20),
                child: TextFormField(
                  controller: _validation,
                  onSaved: (val) {
                    validation = val;
                  },
                  decoration: InputDecoration(
                    border: OutlineInputBorder(
                      borderRadius: const BorderRadius.all(
                        const Radius.circular(50),
                      ),
                    ),
                    contentPadding: EdgeInsets.all(15),
                    suffixIcon: Icon(Icons.payment, size: 35),
                    hintText: "Permit Validation",
                  ),
                ),
              ),
              SizedBox(height: 20),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20),
                child: TextFormField(
                  controller: _driveradresse,
                  onSaved: (val) {
                    addre = val;
                  },
                  decoration: InputDecoration(
                    border: OutlineInputBorder(
                      borderRadius: const BorderRadius.all(
                        const Radius.circular(50),
                      ),
                    ),
                    contentPadding: EdgeInsets.all(15),
                    suffixIcon: Icon(Icons.home, size: 35),
                    hintText: "Adress",
                  ),
                ),
              ),
              SizedBox(height: 40),
              Container(
                height: 50,
                width: 180,
                child: ElevatedButton(
                  onPressed: () {
                    report(_name.text,_name2.text,_driverpermit.text,_validation.text,_driveradresse.text,context);
                  },
                  child: Text('Submit'),
                  style: ElevatedButton.styleFrom(
                      primary: Colors.blueAccent,
                      onPrimary: Colors.white,
                      shape: (RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(50),
                      ))),
                ),
              ),
              SizedBox(height: 50),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  Container(
                    height: 50,
                    width: 150,
                    child: ElevatedButton(
                      onPressed: () {
                        Navigator.of(context).pop();
                      },
                      child: Text('<<  Back'),
                      style: ElevatedButton.styleFrom(
                          primary: Colors.blueAccent,
                          onPrimary: Colors.white,
                          shape: (RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(50),
                          ))),
                    ),
                  ),
                  Container(
                    height: 50,
                    width: 150,
                    child: ElevatedButton(
                      onPressed: () {
                        // Navigator.of(context).push(MaterialPageRoute(
                        //     builder: (context) => CheckBoxes()));
                      },
                      child: Text('Next  >>'),
                      style: ElevatedButton.styleFrom(
                          primary: Colors.blueAccent,
                          onPrimary: Colors.white,
                          shape: (RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(50),
                          ))),
                    ),
                  )
                ],
              )
            ],
          ),
        )),
      ),
    );
  }
}

report(name, name2, permit, permit_vald, adress, BuildContext context) async {
  WidgetsFlutterBinding.ensureInitialized();
  SharedPreferences prefs = await SharedPreferences.getInstance();
  dynamic carid = prefs.getString('CarId');
  dynamic token = prefs.getString('jwt');
  String Token = "Bearer " + token;
  Map user = {
    'DriverName': name,
    'DriverLastName': name2,
    "DriverPermit": permit,
    "DriverPermitValidation": permit_vald,
    "DriverAdresse": adress,
    "CarId": carid
  };
  var url = Uri.parse('http://102.37.113.211/api/client/report');
  final response = await http.post(url,
      headers: {'Content-Type': 'application/json', "Authorization": Token},
      body: jsonEncode(user));
  if (response.statusCode == 201) {
    Map mapresposne = jsonDecode(response.body);
    //print(Mapresposne);
    WidgetsFlutterBinding.ensureInitialized();
    // ignore: unused_local_variable
    SharedPreferences prefs = await SharedPreferences.getInstance();
    Navigator.pushNamed(context, '/');
  } else {
    ScaffoldMessenger.of(context)
        .showSnackBar(SnackBar(content: Text('Wrong Data')));
  }
}
