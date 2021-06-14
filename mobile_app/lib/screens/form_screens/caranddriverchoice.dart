import 'package:flutter/material.dart';
import 'package:more_pro_ui_qr/Navigation/navigation_drawer.dart';
import 'package:more_pro_ui_qr/buttons/cardropdownbutton.dart';
import 'package:more_pro_ui_qr/screens/form_screens/drivervsowner.dart';

class FirstChoices extends StatefulWidget {
  @override
  _FirstChoicesState createState() => _FirstChoicesState();
}

class _FirstChoicesState extends State<FirstChoices> {
  @override
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
          child: Column(
            children: [
              Text(
                'Select your car ID',
                style: TextStyle(
                  color: Colors.blueAccent,
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                ),
              ),
              SizedBox(height: 80),
              Padding(
                padding: const EdgeInsets.all(20),
                child: Form(
                    child: Card(
                  shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(50)),
                  child: Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 15),
                    child: SelectyourCar(),
                  ),
                )),
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
                          Navigator.of(context).push(MaterialPageRoute(
                              builder: (context) => DriverVsOwner()));
                        },
                        child: Text('Vehicle A'),
                        style: ElevatedButton.styleFrom(
                          primary: Colors.yellowAccent,
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
                        onPressed: () {},
                        child: Text('Vehicle B'),
                        style: ElevatedButton.styleFrom(
                          primary: Colors.blueAccent,
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
