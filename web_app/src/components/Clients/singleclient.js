import React, { useEffect, useState } from 'react';
//import { Header, Footer } from '../common';
import Menu from '../common/menu'
import useToken from '../app/useToken';
import './client.css';
//import { Link } from 'react-router-dom'
import ListGroup from 'react-bootstrap/ListGroup'
import { Tab, Row, Col, Card } from 'react-bootstrap'
//import {Button} from 'reactstrap';







export default function Clients() {
    const { token, setToken } = useToken();
    const [data, setData] = useState({});
    const Token = "Bearer ".concat(token)
  
    useEffect(() => {
  
      const fetchUserEmail = async () => {
  
        const response = await fetch('http://102.37.113.211/api/company/clients', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': Token
          }
        });
  
        const email = await response.json();
  
        setData(email);
  
      };
  
      fetchUserEmail();
  
    }, []);
    const arr = []
    for (const x in data) {
      arr.push(data[x])
    }
    let num = arr.length
    return (
      <div className="body-pd" >
        <Menu />
        
  
      </div>
    )
  };
  
  
  