import 'package:flutter/material.dart';

class NavigationDrawerWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: Material(
        color: Colors.blueAccent,
        child: ListView(
          children: <Widget>[
            const SizedBox(height: 48),
            buildMenueItem(
              text: 'My Profile',
              icon: Icons.person,
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
      onTap: () {},
    );
  }
}
