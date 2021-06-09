import 'package:flutter/material.dart';
import 'package:more_pro_ui_qr/Navigation/navigation_drawer.dart';

class ReportManager extends StatefulWidget {
  const ReportManager({Key? key}) : super(key: key);

  @override
  _ReportManagerState createState() => _ReportManagerState();
}

class _ReportManagerState extends State<ReportManager> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      drawer: NavigationDrawerWidget(),
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        toolbarHeight: 70,
        title: Text('Reports History'),
        centerTitle: true,
        // leading: IconButton(
        //   onPressed: () {},
        //   icon: Icon(Icons.menu),
        // ),
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
    );
  }
}
