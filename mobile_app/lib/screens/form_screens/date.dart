import 'package:flutter/material.dart';
import 'package:more_pro_ui_qr/screens/form_screens/non_owner_ifonrmation.dart';
import 'package:more_pro_ui_qr/Navigation/navigation_drawer.dart';

class DateScreen extends StatefulWidget {
  const DateScreen({Key? key}) : super(key: key);

  @override
  _DateScreenState createState() => _DateScreenState();
}

class _DateScreenState extends State<DateScreen> {
  DateTime? _dateTime;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      extendBodyBehindAppBar: true,
      drawer: NavigationDrawerWidget(),
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
        // flexibleSpace: Container(
        //   decoration: BoxDecoration(
        //     borderRadius: BorderRadius.vertical(
        //       bottom: Radius.circular(25),
        //     ),
        //     gradient: LinearGradient(
        //       colors: [Colors.redAccent, Colors.blueAccent],
        //       begin: Alignment.bottomRight,
        //       end: Alignment.topLeft,
        //     ),
        //   ),
        // ),
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
            children: <Widget>[
              Text(
                _dateTime == null ? "Please pick a date" : _dateTime.toString(),
                style: TextStyle(fontSize: 17),
              ),
              SizedBox(height: 40),
              Container(
                height: 50,
                width: 180,
                child: ElevatedButton(
                  onPressed: () {
                    showDatePicker(
                            context: context,
                            initialDate: DateTime.now(),
                            firstDate: DateTime(2000),
                            lastDate: DateTime(2150))
                        .then((date) {
                      setState(() {
                        _dateTime = date;
                      });
                    });
                  },
                  child: Text('choose a date here'),
                  style: ElevatedButton.styleFrom(
                      primary: Colors.blueAccent,
                      onPrimary: Colors.white,
                      shape: (RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(50),
                      ))),
                ),
              ),
              SizedBox(height: 180),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: <Widget>[
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
                        Navigator.of(context).push(MaterialPageRoute(
                            builder: (context) => DriversInormation()));
                      },
                      child: Text('Next  >>'),
                      style: ElevatedButton.styleFrom(
                          primary: Colors.blueAccent,
                          onPrimary: Colors.white,
                          shape: (RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(50),
                          ))),
                    ),
                  ),
                ],
              )
            ],
          ),
        ),
      ),
    );
  }
}
