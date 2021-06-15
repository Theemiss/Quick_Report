import 'package:flutter/material.dart';

// ignore: unused_import
import 'package:more_pro_ui_qr/home_screens/entities/acheived_reports.dart';

// ignore: must_be_immutable
class GeneratedReports extends StatelessWidget {
  List _reports;
  GeneratedReports(this._reports);
  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      itemCount: _reports.length,
      itemBuilder: (context, index) {
        return Card(
          child: Padding(
            padding: const EdgeInsets.all(28),
            child: Column(
              // crossAxisAlignment: CrossAxisAlignment.start,r
              children: [
                Text(_reports[0]['id'].toString()),
              ],
            ),
          ),
        );
      },
    );
  }
}
