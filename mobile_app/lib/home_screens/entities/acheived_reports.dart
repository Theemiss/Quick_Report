// import 'package:flutter/cupertino.dart';

class Report {
  var reportId;
  // ignore: non_constant_identifier_names
  var insurance_id;
  // ignore: non_constant_identifier_names
  var first_name;
  // ignore: non_constant_identifier_names
  var last_name;
  var driversName;
  var cin;
  var adress;
  // ignore: non_constant_identifier_names
  var permit_id;
  var mark;
  var phone;
  // ignore: non_constant_identifier_names
  var permit_validation;
  Report(
      {required this.reportId,
      // ignore: non_constant_identifier_names
      required this.insurance_id,
      // ignore: non_constant_identifier_names
      required this.first_name,
      // ignore: non_constant_identifier_names
      required this.last_name,
      required this.driversName,
      required this.cin,
      required this.adress,
      // ignore: non_constant_identifier_names
      required this.permit_id,
      required this.mark,
      required this.phone,
      // ignore: non_constant_identifier_names
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
