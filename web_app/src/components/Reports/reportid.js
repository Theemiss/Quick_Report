import React, { useEffect, useState } from 'react';
//import { Header, Footer } from '../common';
import Menu from '../common/menu'
import useToken from '../app/useToken';
import './client.css';
import { Link, useParams } from 'react-router-dom'


//import {Button} from 'reactstrap';







export default function ReportId() {
  const { token, setToken } = useToken();
  const [data, setData] = useState({});
  const [car, setCar] = useState({});
  const Token = "Bearer ".concat(token)
  const { id } = useParams();

  const url = 'http://102.37.113.211/api/report/' + id
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
      <h3 className="Title">Rapport N° : <small class="text-muted">{data.id} </small> </h3>

      <div class="container-fluid">
  <div className="row">
    
    <div className="container-fluid">
    <ul className="shadow p-3  rounded"><div className="sub-title">Client Info</div>
       <li>Adresse: {data.adresse}</li> 
       <li >Email :{data.email} </li> 
       <li >Name : {data.first_name}</li>
       <li >Last Name : {data.last_name}</li>
       <li > Permit: {data.permit_id}</li>
       <li > Permit valid : {data.permit_validation}</li>
       <li > Phone : {data.phone}</li>
       <li >CIN : {data.CIN}</li>
      </ul>
    </div>
    <div className="container-fluid">
      <ul className="shadow p-3  rounded"><div className="sub-title">Driver Info</div>
        <li>Driver: {data.driver_name} {data.driver_lastname} </li>
        <li>Permit :{data.driver_permit}</li>
        <li> Permit Valid : {data.driver_permit_valid}</li>

      </ul>
    </div>
  </div>
  <div className="row">
  <div className="container-fluid">
    <ul className="shadow p-3  rounded"><div className="sub-title">Car Info</div>
      <li> Matricule : {data.car_id}</li>
      <li>Type : {data.type_c}</li>
      <li> Mark : {data.Mark}</li>

      
    </ul>
   
     </div>
      </div>

</div>
    
      
      <div class="mb-3">
        <form>
  <label for="exampleFormControlTextarea1" class="form-label">Feedback</label>
  <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
  <input class="btn btn-primary" type="submit" value="Submit"></input>
  </form>
</div>


    </div>
  )
};


