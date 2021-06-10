import 'dart:ui';

import 'package:flutter/material.dart';
import 'package:more_pro_ui_qr/Navigation/navigation_drawer.dart';

class AboutTheApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      extendBodyBehindAppBar: true,
      drawer: NavigationDrawerWidget(),
      appBar: AppBar(
        toolbarHeight: 70,
        title: Text('About Quick Report'),
        centerTitle: true,
        flexibleSpace: Container(
          decoration: BoxDecoration(
              borderRadius: BorderRadius.vertical(
                bottom: Radius.circular(25),
              ),
              gradient: LinearGradient(
                colors: [Colors.redAccent, Colors.blueAccent],
                begin: Alignment.bottomRight,
                end: Alignment.topLeft,
              )),
        ),
        elevation: 30,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.vertical(
            bottom: Radius.circular(25),
          ),
        ),
      ),
      body: SingleChildScrollView(
        child: Column(
          children: <Widget>[
            SizedBox(height: 80),
            Container(
              height: 150,
              child: Center(
                child: Text('Welcom to Quick Report',
                    style: TextStyle(
                        fontSize: 30,
                        fontWeight: FontWeight.bold,
                        color: Colors.blueAccent)),
              ),
            ),
            SizedBox(height: 20),
            Text(
              'Vesrion:',
              style: TextStyle(fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 20),
            Container(child: Text('1.0.0')),
            SizedBox(height: 50),
            Text(
              'About Quick Report',
              style: TextStyle(fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 20),
            Container(
              child: Text(
                  'Have you ever thought about how long it will take to fill and transmit papers about traffic accidents in Tunisia? The answer is  DAYS … and probably WEEKS\n\nThis app finds a solution for that.\n\nActually, the current way to fill a traffic accident report to insurance companies could last a long time, especially with the high number of car crashes that make the procedure heavy. Besides, there is a high error occurrence risk.\n\nHowever, the app cannot be used outside the Tunisian territory or for vehicles insured by foreign insurance companies. Also, the app cannot be used in case of human damage (even slight damage).\n\n'),
            ),
            SizedBox(height: 50),
            Text(
              'Authors:',
              style: TextStyle(fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 20),
            Column(
              children: <Widget>[
                Align(
                  alignment: Alignment.centerLeft,
                  child: Container(
                    child: Text('Ahmed Belhaj:',
                        style: TextStyle(fontWeight: FontWeight.bold)),
                  ),
                ),
              ],
            ),
            SizedBox(height: 15),
            Column(
              children: <Widget>[
                Align(
                  alignment: Alignment.centerLeft,
                  child: Container(
                    child: Text(
                      'Software Engineering Student at Holberton School',
                    ),
                  ),
                ),
              ],
            ),
            SizedBox(height: 40),
            Column(
              children: <Widget>[
                Align(
                  alignment: Alignment.centerLeft,
                  child: Container(
                    child: Text('Mohamed Chedli:',
                        style: TextStyle(fontWeight: FontWeight.bold)),
                  ),
                ),
              ],
            ),
            SizedBox(height: 15),
            Column(
              children: <Widget>[
                Align(
                  alignment: Alignment.centerLeft,
                  child: Container(
                    child: Text(
                      'Software Engineering Student at Holberton School',
                    ),
                  ),
                ),
              ],
            ),
            SizedBox(height: 40),
            Column(
              children: <Widget>[
                Align(
                  alignment: Alignment.centerLeft,
                  child: Container(
                    child: Text('Med Amin Bondi:',
                        style: TextStyle(fontWeight: FontWeight.bold)),
                  ),
                ),
              ],
            ),
            SizedBox(height: 15),
            Column(
              children: <Widget>[
                Align(
                  alignment: Alignment.centerLeft,
                  child: Container(
                    child: Text(
                      'Software Engineering Student at Holberton School',
                    ),
                  ),
                ),
              ],
            ),
            SizedBox(height: 50),
            // SizedBox(height: 30),
          ],
        ),
      ),
    );
  }
}
