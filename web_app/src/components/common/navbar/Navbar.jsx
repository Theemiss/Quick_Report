import React from 'react';
import { Link } from 'react-router-dom';

import './Navbar.css'

function Navbar () {

  return (
    <section className="navbar">
      <Link to="/" className="navbar-item nav-link">Home</Link>
      <Link to="/clients" className="navbar-item nav-link">Client</Link>
      <Link to="/reports" className="navbar-item nav-link">Reports</Link>
      <Link to="/contact" className="navbar-item nav-link">Contact</Link>
      <Link to="/about" className="navbar-item nav-link">About Us</Link>
      <Link to="/logout"className="navbar-item nav-link"> logout</Link>
  </section>
  )

}
export default Navbar;