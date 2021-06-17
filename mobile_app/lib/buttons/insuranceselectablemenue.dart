import 'package:flutter/material.dart';
import 'package:dio/dio.dart';
import 'package:shared_preferences/shared_preferences.dart';

class Item {
  // ignore: non_constant_identifier_names
  var id;
  var name;
  Item(String name, String id) {
    this.name = name;
    this.id = id;
  }
}

class DropDownMenue extends StatefulWidget {
  const DropDownMenue({Key? key}) : super(key: key);

  @override
  _DropDownMenueState createState() => _DropDownMenueState();
}

class _DropDownMenueState extends State<DropDownMenue> {
  List company = [];

  fetchcompany() async {
    var url = 'http://102.37.113.211/api/hidden';
   
    var response = await Dio().get(
      url,
      options: Options(headers: {
        'Content-Type': 'application/json'
      }),
    );
    // print(response.data);
    return response.data;
  }

  List mapToList(Map data) {
    List carsList = [];
    data.forEach((a, b) => carsList.add(b));
    return carsList;
  }




  Item? selectedCompany;
   List<Item> companylist = [];
  @override
  void initState() {
    fetchcompany().then((data) {
      setState(() {
        company = mapToList(data);

        companylist = [
          Item(company[0]['name'], company[0]['id']),
          Item(company[1]['name'], company[1]['id'])
        ];
      });
    });
    super.initState();
  }



  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      child: DropdownButton<Item>(
        hint: Text('Select your insurance company'),
        value: selectedCompany,
        onChanged: (value) {
          setState(() {
            selectedCompany = value;
          });
          savePref(value);

        },
        items: companylist.map((company) {
          return DropdownMenuItem(
            value: company,
            child: Row(children: [
              Text(company.name),
            ]),
          );
        }).toList(),
      ),
    );
  }
}

savePref(Item? car) async {
  SharedPreferences preferences = await SharedPreferences.getInstance();
  if (car != null){
      preferences.setString("companyId", car.id);
        // ignore: deprecated_member_use
        preferences.commit();
  }

}
