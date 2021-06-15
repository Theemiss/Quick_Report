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
      <h3>Client N° :<h5>{data.id} </h5></h3>
       adresse: {data.adresse} <br />
        email :{data.email} <br />
       Name : {data.first_name}  <br />
       last name : {data.last_name} <br />
       permit id: {data.permit_id} <br />
       permit valid : {data.permit_validation} <br />
       phone : {data.phone} <br />
      CIN : {data.CIN} <br />

    </div>
  )
};


