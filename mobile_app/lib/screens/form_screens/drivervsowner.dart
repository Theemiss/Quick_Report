// Module that difines if the user is the car owner or not

import 'package:flutter/material.dart';
import 'package:more_pro_ui_qr/Navigation/navigation_drawer.dart';
import 'package:more_pro_ui_qr/screens/form_screens/date.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:dio/dio.dart';

// stateful widget class
class DriverVsOwner extends StatefulWidget {
  @override
  _DriverVsOwnerState createState() => _DriverVsOwnerState();
}

class _DriverVsOwnerState extends State<DriverVsOwner> {
  @override
  // Build the class's design
  Widget build(BuildContext context) {
    return Scaffold(
      drawer: NavigationDrawerWidget(),
      extendBodyBehindAppBar: true,
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
        elevation: 30,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.vertical(
            bottom: Radius.circular(25),
          ),
        ),
      ),
      body: Center(
        child: SingleChildScrollView(
          child: Column(
            children: [
              Text(
                'Is the damaged vehicle yours ?',
                style: TextStyle(
                  color: Colors.blueAccent,
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                ),
              ),
              SizedBox(height: 100),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20.0),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Container(
                      height: 50,
                      width: 150,
                      child: ElevatedButton(
                        onPressed: () {
                          user(context).then((data) => {report(data, context)});
                        },
                        child: Text('Yes'),
                        style: ElevatedButton.styleFrom(
                          primary: Colors.blueAccent,
                          onPrimary: Colors.black,
                          shape: (RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(50),
                          )),
                        ),
                      ),
                    ),
                    Container(
                      height: 50,
                      width: 150,
                      child: ElevatedButton(
                        onPressed: () {
                          Navigator.of(context).push(MaterialPageRoute(
                              builder: (context) => DateScreen()));
                        },
                        child: Text('No'),
                        style: ElevatedButton.styleFrom(
                          primary: Colors.redAccent,
                          onPrimary: Colors.black,
                          shape: (RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(50),
                          )),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

// http request
user(BuildContext context) async {
  var url = 'http://102.37.113.211/api/client';
  SharedPreferences prefs = await SharedPreferences.getInstance();
  dynamic to = prefs.getString('jwt');
  print(to);
  String? token = 'Bearer ' + to;
  var response = await Dio().get(
    url,
    options: Options(
        headers: {'Content-Type': 'application/json', 'Authorization': token}),
  );

  return response.data;
}

// sending the report information
report(data, BuildContext context) async {
  WidgetsFlutterBinding.ensureInitialized();
  SharedPreferences prefs = await SharedPreferences.getInstance();
  dynamic carid = prefs.getString('CarId');
  dynamic token = prefs.getString('jwt');
  // ignore: non_constant_identifier_names
  String Token = "Bearer " + token;
  Map user = {
    'DriverName': data['first_name'],
    'DriverLastName': data['last_name'],
    "DriverPermit": data['permit_id'],
    "DriverPermitValidation": data[''],
    "DriverAdresse": data['adresse'],
    "CarId": carid
  };
  var url = Uri.parse('http://102.37.113.211/api/client/report');
  final response = await http.post(url,
      headers: {'Content-Type': 'application/json', "Authorization": Token},
      body: jsonEncode(user));
  if (response.statusCode == 201) {
    // ignore: unused_local_variable
    Map mapresposne = jsonDecode(response.body);
    //print(Mapresposne);
    WidgetsFlutterBinding.ensureInitialized();
    // ignore: unused_local_variable
    SharedPreferences prefs = await SharedPreferences.getInstance();
    Navigator.pushNamed(context, '/fourthPage');
  }
}
