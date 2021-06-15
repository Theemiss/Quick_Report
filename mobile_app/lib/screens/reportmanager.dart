import 'dart:convert';
import 'dart:async';
import 'package:flutter/material.dart';
import 'package:more_pro_ui_qr/Navigation/navigation_drawer.dart';
import 'package:more_pro_ui_qr/home_screens/entities/acheived_reports.dart';
import 'package:more_pro_ui_qr/home_screens/generated_reports.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'form_screens/caranddriverchoice.dart';
import 'package:http/http.dart' as http;

class ReportManager extends StatefulWidget {
  @override
  _ReportManagerState createState() => _ReportManagerState();
}

class _ReportManagerState extends State<ReportManager> {
  Future<List<Report>> fetchReports() async {
    var url = Uri.parse('http://102.37.113.211/api/client/report');
    SharedPreferences prefs = await SharedPreferences.getInstance();
    dynamic to = prefs.getString('jwt');
    print(to);
    String? token = 'Bearer ' + to;
    final response = await http.get(url,
        headers: {'Content-Type': 'application/json', 'Authorization': token});
    print(response.statusCode);
    if (response.statusCode == 200) {
      print(jsonDecode(response.body));
      for (var item in jsonDecode(response.body)) {
        print(item);
      }
    }
    return [];
  }

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    var futureReports = fetchReports();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      drawer: NavigationDrawerWidget(),
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        toolbarHeight: 70,
        title: Text('Reports History'),
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
      body: GeneratedReports([
        Report("azerazerazerazer"),
        Report("earaerazrazeraezr"),
        Report("earaerazrazeraezr"),
      ]),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {
          Navigator.of(context)
              .push(MaterialPageRoute(builder: (context) => FirstChoices()));
        },
        label: const Text('Create new report'),
        icon: const Icon(Icons.add),
        backgroundColor: Colors.blueAccent,
      ),
    );
  }
}
