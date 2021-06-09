import 'package:flutter/material.dart';

class Item {
  const Item(this.name);
  final String name;
}

class DropDownMenue extends StatefulWidget {
  const DropDownMenue({Key? key}) : super(key: key);

  @override
  _DropDownMenueState createState() => _DropDownMenueState();
}

class _DropDownMenueState extends State<DropDownMenue> {
  Item? selectedCompany;

  List<Item> companies = [
    Item('Company 1'),
    Item('Company 2'),
    Item('Company 3'),
    Item('Company 4'),
    Item('Company 5'),
  ];

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
        },
        items: companies.map((company) {
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
