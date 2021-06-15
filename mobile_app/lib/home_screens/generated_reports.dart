import 'package:flutter/material.dart';
import 'package:more_pro_ui_qr/home_screens/entities/acheived_reports.dart';

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
            padding: const EdgeInsets.all(18),
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
