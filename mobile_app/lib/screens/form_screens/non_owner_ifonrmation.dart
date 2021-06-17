import 'package:flutter/material.dart';
// import 'package:more_pro_ui_qr/screens/form_screens/check_boxes.dart';

class DriversInormation extends StatefulWidget {
  @override
  _DriversInormationState createState() => _DriversInormationState();
}

class _DriversInormationState extends State<DriversInormation> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 70,
        title: Text('Filling the form'),
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
      body: Center(
        child: SingleChildScrollView(
          child: Column(
            children: <Widget>[
              Text(
                'Please enter your information',
                style: TextStyle(
                    fontSize: 20,
                    color: Colors.blueAccent,
                    fontWeight: FontWeight.bold),
              ),
              SizedBox(height: 30),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20),
                child: TextFormField(
                  decoration: InputDecoration(
                    border: OutlineInputBorder(
                      borderRadius: const BorderRadius.all(
                        const Radius.circular(50),
                      ),
                    ),
                    contentPadding: EdgeInsets.all(15),
                    suffixIcon: Icon(Icons.person, size: 35),
                    hintText: "First Name",
                  ),
                ),
              ),
              SizedBox(height: 20),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20),
                child: TextFormField(
                  decoration: InputDecoration(
                    border: OutlineInputBorder(
                      borderRadius: const BorderRadius.all(
                        const Radius.circular(50),
                      ),
                    ),
                    contentPadding: EdgeInsets.all(15),
                    suffixIcon: Icon(Icons.person, size: 35),
                    hintText: "Last Name",
                  ),
                ),
              ),
              SizedBox(height: 20),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20),
                child: TextFormField(
                  decoration: InputDecoration(
                    border: OutlineInputBorder(
                      borderRadius: const BorderRadius.all(
                        const Radius.circular(50),
                      ),
                    ),
                    contentPadding: EdgeInsets.all(15),
                    suffixIcon: Icon(Icons.payment, size: 35),
                    hintText: "Driver's license number",
                  ),
                ),
              ),
              SizedBox(height: 20),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20),
                child: TextFormField(
                  decoration: InputDecoration(
                    border: OutlineInputBorder(
                      borderRadius: const BorderRadius.all(
                        const Radius.circular(50),
                      ),
                    ),
                    contentPadding: EdgeInsets.all(15),
                    suffixIcon: Icon(Icons.payment, size: 35),
                    hintText: "ID card number",
                  ),
                ),
              ),
              SizedBox(height: 20),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20),
                child: TextFormField(
                  decoration: InputDecoration(
                    border: OutlineInputBorder(
                      borderRadius: const BorderRadius.all(
                        const Radius.circular(50),
                      ),
                    ),
                    contentPadding: EdgeInsets.all(15),
                    suffixIcon: Icon(Icons.home, size: 35),
                    hintText: "Adress",
                  ),
                ),
              ),
              SizedBox(height: 40),
              Container(
                height: 50,
                width: 180,
                child: ElevatedButton(
                  onPressed: () {},
                  child: Text('Submit'),
                  style: ElevatedButton.styleFrom(
                      primary: Colors.blueAccent,
                      onPrimary: Colors.white,
                      shape: (RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(50),
                      ))),
                ),
              ),
              SizedBox(height: 50),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  Container(
                    height: 50,
                    width: 150,
                    child: ElevatedButton(
                      onPressed: () {
                        Navigator.of(context).pop();
                      },
                      child: Text('<<  Back'),
                      style: ElevatedButton.styleFrom(
                          primary: Colors.blueAccent,
                          onPrimary: Colors.white,
                          shape: (RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(50),
                          ))),
                    ),
                  ),
                  Container(
                    height: 50,
                    width: 150,
                    child: ElevatedButton(
                      onPressed: () {
                        // Navigator.of(context).push(MaterialPageRoute(
                        //     builder: (context) => CheckBoxes()));
                      },
                      child: Text('Next  >>'),
                      style: ElevatedButton.styleFrom(
                          primary: Colors.blueAccent,
                          onPrimary: Colors.white,
                          shape: (RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(50),
                          ))),
                    ),
                  )
                ],
              )
            ],
          ),
        ),
      ),
    );
  }
}
