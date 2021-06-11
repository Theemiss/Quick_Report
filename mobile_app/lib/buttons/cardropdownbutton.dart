import 'package:flutter/material.dart';

class Item {
  const Item(this.name);
  final String name;
}

class SelectyourCar extends StatefulWidget {
  const SelectyourCar({Key? key}) : super(key: key);

  @override
  _SelectyourCarState createState() => _SelectyourCarState();
}

class _SelectyourCarState extends State<SelectyourCar> {
  Item? selectedCompany;
  List<Item> cars = [
    Item('Car 1'),
    Item('Car 2'),
    Item('Car 3'),
    Item('Car 4'),
    Item('Car 5'),
  ];
  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      child: DropdownButton<Item>(
        hint: Text('Select your car ID'),
        value: selectedCompany,
        onChanged: (value) {
          setState(() {
            selectedCompany = value;
          });
        },
        items: cars.map((company) {
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
