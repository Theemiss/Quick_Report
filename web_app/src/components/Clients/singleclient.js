import React, { useEffect, useState } from 'react';
//import { Header, Footer } from '../common';
import Menu from '../common/menu'
import useToken from '../app/useToken';
import './client.css';
import { Link, useParams } from 'react-router-dom'


//import {Button} from 'reactstrap';







export default function ClientsId() {
  const { token, setToken } = useToken();
  const [data, setData] = useState({});
  const [car, setCar] = useState({});
  const Token = "Bearer ".concat(token)
  const { id } = useParams();

  const url = 'http://102.37.113.211/api/company/clients/' + id
  useEffect(() => {

    const fetchUserInfo = async () => {

      const response = await fetch(url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': Token
        }
      });

      const email = await response.json();

      setData(email);

    };
    fetchUserInfo();

  }, []);






  return (
    <div className="body-pd" >
      <Menu />
      <div class="card shadow-lg p-3 mb-5 rounded">
      <div className="container-fluid">
        <div className="row">
        <ul>Client N° :{data.id}
          <li>
          adresse: {data.adresse} 
          </li>
          <li>
          email :{data.email} 
          </li>
          <li>
          Name : {data.first_name}
          </li>
          <li>
          last name : {data.last_name}
          </li>
          <li>
          permit id: {data.permit_id}
          </li>
          <li>
          permit valid : {data.permit_validation}
          </li>
          <li>
          phone : {data.phone}
          </li>
          <li>
          CIN : {data.CIN}
          </li>
        </ul>
      </div>


        </div>
      </div>
      </div>
    
  )
};


