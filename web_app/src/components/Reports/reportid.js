import React, { useEffect, useState } from "react";
//import { Header, Footer } from '../common';
import Menu from "../common/menu";
import useToken from "../app/useToken";
import "./client.css";
import { useParams } from "react-router-dom";

//import {Button} from 'reactstrap';

export default function ReportId() {
  // eslint-disable-next-line
  const { token, setToken } = useToken();
  const [data, setData] = useState({});
  const Token = "Bearer ".concat(token);
  const { id } = useParams();

  const url = "http://102.37.113.211/api/report/" + id;
  useEffect(() => {
    const fetchUserInfo = async () => {
      const response = await fetch(url, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: Token,
        },
      });

      const email = await response.json();

      setData(email);
    };
    fetchUserInfo();
    // eslint-disable-next-line
  }, []);

  return (
    <div className="body-pd">
      <Menu />
      <h3 className="Title" id="1">
        Report N° : <small class="text-muted">{data.id} </small>{" "}
      </h3>
      <h5>
        Date : <small class="text-muted">{data.updated_at} </small>{" "}
      </h5>

      <div className="container-fluid">
        <div className="row">
          <div className="col box center">
            <h4>Car A</h4>

            <ul className="shadow p-3  rounded question-a">
              <div className="sub-title">Driver Info</div>
              <li>
                Driver: {data.driver_name} {data.driver_lastname}{" "}
              </li>
              <li>Permit :{data.driver_permit}</li>
              <li> Permit Valid : {data.driver_permit_valid}</li>
            </ul>
            <ul className="shadow p-3 question-a rounded">
              <div className="sub-title">Client Info</div>
              <li>Address: {data.adresse}</li>
              <li>Email :{data.email} </li>
              <li>Name : {data.first_name}</li>
              <li>Last Name : {data.last_name}</li>
              <li> Permit: {data.permit_id}</li>
              <li> Permit valid : {data.permit_validation}</li>
              <li> Phone : {data.phone}</li>
              <li>CIN : {data.CIN}</li>
            </ul>
            <ul className="shadow p-3 question-a rounded">
              <div className="sub-title">Car Info</div>
              <li>Matricule:{data.car_id}</li>
              <li>Type : {data.type_c}</li>
              <li> Mark : {data.Mark}</li>
            </ul>
          </div>

          <div className="col box center">
            <h4>Circumstance</h4>
            <ul className="question">
              <li>Parked / stationary</li>
              <br />
              <li>*Leaving a parking space / opening a door</li>
              <br />
              <li>entering a parking space (at the roadside)</li>
              <br />
              <li>emerging from a car park, from private grounds,</li>
              <br />
              <li>entering a car park, private grounds, a track</li>
              <br />
              <li>entering a roundabout or similar traffic system</li>
              <br />
              <li>driving on roundabout etc</li>
              <br />
              <li>
                Hit the rear end, driving in same direction in a same file
                (lane)
              </li>
              <br />
              <li>going in the same direction but a different lane</li>
              <br />
              <li>changing files (lanes)</li>
              <br />
              <li>overtaking</li>
              <br />
              <li>turning to the right</li>
              <br />
              <li>turning to the left</li>
              <br />
              <li>encroaching upon the lane reserved for opposite traffic</li>
              <br />
              <li>coming from the right on intersection</li>
              <br />
              <li> Failing to stop at sign</li>
              <br />
            </ul>
          </div>

          <div className="col box center">
            <h4>Car B</h4>

            <ul className="shadow p-3  rounded question-a">
              <div className="sub-title">Driver Info</div>
              <li>
                Driver: {data.driver_name} {data.driver_lastname}{" "}
              </li>
              <li>Permit :{data.driver_permit}</li>
              <li> Permit Valid : {data.driver_permit_valid}</li>
            </ul>
            <ul className="shadow p-3 question-a rounded">
              <div className="sub-title">Client Info</div>
              <li>Address: {data.adresse}</li>
              <li>Email :{data.email} </li>
              <li>Name : {data.first_name}</li>
              <li>Last Name : {data.last_name}</li>
              <li> Permit: {data.permit_id}</li>
              <li> Permit valid : {data.permit_validation}</li>
              <li> Phone : {data.phone}</li>
              <li>CIN : {data.CIN}</li>
            </ul>
            <ul className="shadow p-3 question-a rounded">
              <div className="sub-title">Car Info</div>
              <li> Matricule:{data.car_id}</li>
              <li>Type : {data.type_c}</li>
              <li> Mark : {data.Mark}</li>
            </ul>
          </div>
        </div>
      </div>
        <div className="container-fluid">
          <div className='row'>
          <div className='col box'>
          <div className='row'>

            <div className='container'>
           <h5>Remarks :</h5>
            .......................................................................................<br />
            .......................................................................................<br />
            .......................................................................................<br />
            .......................................................................................<br />
            </div>
            <div className='container'>
           <h5>Signatures of the driver A</h5> 
            </div>
            </div>
          </div>
          <div className='col-6 box center'>
          <h4> Accident sketch</h4>
          <img  className="sketch" alt='sketch' src="https://thumbs.dreamstime.com/b/square-mesh-pastel-tone-sketch-art-board-background-design-element-grid-paper-design-element-grid-paper-91830034.jpg">

          </img>
          </div>
          <div className='col box '>
          <div className='row'>

            <div className='container'>
           <h5>Remarks :</h5>
            .......................................................................................<br />
            .......................................................................................<br />
            .......................................................................................<br />
            .......................................................................................<br />
            </div>
            <div className='container'>
           <h5>Signatures of the driver B</h5> 
            </div>
            </div>
          </div>
          </div>
        </div>
      <div class="mb-3 box">
        <form>
          <label for="exampleFormControlTextarea1" class="form-label Title">
            <h5>Feedback</h5>
          </label>
          <textarea
            class="form-control"
            id="exampleFormControlTextarea1"
            rows="3"
          ></textarea>
          <input class="btn btn-primary" type="submit" value="Submit"></input>
        </form>
      </div>
    </div>
  );
}
