// import 'package:flutter/cupertino.dart';

class Report {
  var reportId;
  var insurance_id;
  var first_name;
  var last_name;
  var driversName;
  var cin;
  var adress;
  var permit_id;
  var mark;
  var phone;
  var permit_validation;
  Report(
      {required this.reportId,
      required this.insurance_id,
      required this.first_name,
      required this.last_name,
      required this.driversName,
      required this.cin,
      required this.adress,
      required this.permit_id,
      required this.mark,
      required this.phone,
      required this.permit_validation});
  Report.fromJson(String key, Map<String, dynamic> json) {
    this.reportId = key;
    this.insurance_id = json["insurance_id"];
    this.first_name = json["first_name"];
    this.last_name = json["last_name"];
    this.driversName = json["DriverName"];
    this.cin = json["CIN"];
    this.adress = json["adresse"];
    this.permit_id = json["permit_id"];
    this.phone = json["phone"];
    this.permit_validation = json["permit_validation"];
  }
  // factory Report.fromJson(Map<String, dynamic> json) {
  //   return Report(
  //     reportId: Key,
  //     insurance_id: json["insurance_id"],
  //     first_name: json["first_name"],
  //     last_name: json["last_name"],
  //     driversName: json["DriverName"],
  //     cin: json["CIN"],
  //     adress: json["adresse"],
  //     permit_id: json["permit_id"],
  //     mark: json["mark"],
  //     phone: json["phone"],
  //     permit_validation: json["permit_validation"],
  //   );
  // }
}
