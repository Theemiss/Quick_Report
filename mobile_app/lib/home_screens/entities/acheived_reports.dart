class Report {
  late String reportId;
  late String insurance_id;
  late String first_name;
  late String last_name;
  late String driversName;
  late String cin;
  late String adress;
  late String permit_id;
  late String mark;
  late String permit_validation;
  Report(this.reportId);
  Report.fromJson(Map<String, dynamic> json) {
    this.reportId = json['reportID'];
    this.insurance_id = json['insurance_id'];
    this.first_name = json['first_name'];
    this.last_name = json['last_name'];
    this.driversName = json['driversName'];
    this.cin = json['CIN'];
    this.adress = json['adresse'];
    this.permit_id = json['permit_id'];
    this.permit_validation = json['permit_validation'];
  }
}
