import 'package:flutter/material.dart';
import 'package:dio/dio.dart';
import 'package:shared_preferences/shared_preferences.dart';

class Item {
  // ignore: non_constant_identifier_names
  var car_id;
  var mark;
  var type;
  Item(String id, String mark, String type) {
    this.car_id = id;
    this.mark = mark;
    this.type = type;
  }
  // const Item(this.name);
  // final String name;
}

class SelectyourCar extends StatefulWidget {
  const SelectyourCar({Key? key}) : super(key: key);

  @override
  _SelectyourCarState createState() => _SelectyourCarState();
}

class _SelectyourCarState extends State<SelectyourCar> {
  List cars = [];

  fetchCars() async {
    var url = 'http://102.37.113.211/api/client/cars';
    SharedPreferences prefs = await SharedPreferences.getInstance();
    dynamic to = prefs.getString('jwt');
    print(to);
    String? token = 'Bearer ' + to;
    var response = await Dio().get(
      url,
      options: Options(headers: {
        'Content-Type': 'application/json',
        'Authorization': token
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

  Item? selectedCar;
  List<Item> carsList = [];
  @override
  void initState() {
    fetchCars().then((data) {
      setState(() {
        cars = mapToList(data);

        carsList = [
          Item(cars[0]['id'], cars[0]['Mark'], cars[0]['type_c']),
          Item(cars[1]['id'], cars[1]['Mark'], cars[1]['type_c'])
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
        hint: Text('Select your car ID'),
        value: selectedCar,
        onChanged: (value) {
          setState(() {
            selectedCar = value;
          });
          savePref(value);
       
        },
        items: carsList.map((car) {
          return DropdownMenuItem(
            value: car,
            child: Row(children: [
              Text(car.mark + " " + car.type),
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
      preferences.setString("CarId", car.car_id);
        // ignore: deprecated_member_use
        preferences.commit();
  }

}
