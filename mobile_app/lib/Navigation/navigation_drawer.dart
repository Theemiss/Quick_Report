import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:more_pro_ui_qr/home_screens/myprofile.dart';
import 'package:more_pro_ui_qr/home_screens/aboutapp.dart';
import 'package:more_pro_ui_qr/screens/reportmanager.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:more_pro_ui_qr/screens/login.dart';

class NavigationDrawerWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: Material(
        color: Colors.blueAccent,
        child: ListView(
          children: <Widget>[
            const SizedBox(height: 200),
            buildMenueItem(
              text: 'My Home',
              icon: Icons.home,
              onClicked: () => selectedItem(context, 0),
            ),
            const SizedBox(height: 40),
            buildMenueItem(
              text: 'My Profile',
              icon: Icons.person,
              onClicked: () => selectedItem(context, 1),
            ),
            const SizedBox(height: 40),
            buildMenueItem(
              text: 'About Quick Report',
              icon: Icons.help_outline,
              onClicked: () => selectedItem(context, 2),
            ),
            const SizedBox(height: 150),
            Divider(color: Colors.white70),
            const SizedBox(height: 60),
            buildMenueItem(
              text: 'Logout',
              icon: Icons.logout,
              onClicked: () => logoutFunction(context),
            ),
          ],
        ),
      ),
    );
  }

  // Building menue items
  Widget buildMenueItem({
    required String text,
    required IconData icon,
    VoidCallback? onClicked,
  }) {
    final color = Colors.white;
    final hovercolor = Colors.white70;
    return ListTile(
      leading: Icon(icon, color: color),
      title: Text(
        text,
        style: TextStyle(color: color),
      ),
      hoverColor: hovercolor,
      onTap: onClicked,
    );
  }

  void selectedItem(BuildContext context, int index) {
    Navigator.of(context).pop();
    switch (index) {
      case 0:
        Navigator.of(context).push(
          MaterialPageRoute(
            builder: (context) => ReportManager(),
          ),
        );
        break;
      case 1:
        Navigator.of(context).push(
          MaterialPageRoute(
            builder: (context) => MyProfile(),
          ),
        );
        break;
      case 2:
        Navigator.of(context).push(
          MaterialPageRoute(
            builder: (context) => AboutTheApp(),
          ),
        );
        break;
    }
  }

  logoutFunction(BuildContext context) async {
    var url = Uri.parse('http://102.37.113.211/api/logout');

    SharedPreferences prefs = await SharedPreferences.getInstance();
    dynamic to = prefs.getString('jwt');
    print(to);
    String? token = 'Bearer ' + to;
    final response = await http.post(url,
        headers: {'Content-Type': 'application/json', 'Authorization': token});
    if (response.statusCode == 202) {
      prefs.remove('jwt');
      prefs.setBool('isLogged', false);
      prefs.commit();
      Navigator.of(context)
          .push(MaterialPageRoute(builder: (context) => MyLogInPage()));
    }
  }
}
