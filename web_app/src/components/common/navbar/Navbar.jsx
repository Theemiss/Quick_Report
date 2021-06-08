import React from 'react';
import { Link } from 'react-router-dom';

import './Navbar.css'

function Navbar () {

  return (
    <section className="navbar">
      <Link to="/" className="navbar-item">Home</Link>
      <Link to="/clients" className="navbar-item">Client</Link>
      <Link to="/reports" className="navbar-item">Reports</Link>
      <Link to="/contact" className="navbar-item">Contact</Link>
      <Link to="/about" className="navbar-item">About Us</Link>
  </section>
  )

}
export default Navbar;