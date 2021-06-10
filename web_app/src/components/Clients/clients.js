import React, { useEffect, useState } from 'react';
import { Header, Footer } from '../common';
import useToken from '../app/useToken';
import './client.css';
import { Link } from 'react-router-dom'
import ListGroup from 'react-bootstrap/ListGroup'
import { Tab, Row, Col, Card, Container,Button } from 'react-bootstrap'










export default function Clients() {
  const { token, setToken } = useToken();
  const [data, setData] = useState({});
  const Token = "Bearer ".concat(token)
  const mystyle = {
    BorderColor : 'blue'  };
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

  return (
    <div>
      <Header />

      <h2 className='Title'>All Client</h2>

      <Tab.Container id="list-group-tabs-example" >
        <Row>
          <Col sm={6}>
            {arr.map((user) => (<ListGroup className='nayek'>

              <ListGroup.Item  className='nayek shadow-lg p-3 mb-2 bg-white rounded' action href={"#" + user.id}>
                {user.email}
              </ListGroup.Item>            </ListGroup>



            ))}   </Col>


          <Col sm={6}>

            {arr.map((user) => (
              <Tab.Content>
                <Tab.Pane eventKey={"#" + user.id}>
                  <Card  className="border shadow p-3 mb-5 rounded">
                    <Card.Body className="matme">
                      <Card.Title>{user.email}</Card.Title>
                      <Card.Subtitle className="mb-2 text-muted">{user.id}</Card.Subtitle>
                      <ListGroup.Item className="border-2">CIN : {user.CIN}</ListGroup.Item>
                      <ListGroup.Item className="border-2">Name : {user.first_name}</ListGroup.Item>
                      <ListGroup.Item className="border-2">Last Name : {user.last_name}</ListGroup.Item>
                      <ListGroup.Item className="border-2">Phone : {user.phone}</ListGroup.Item>
                      <ListGroup.Item className="border-2">Email : {user.email}</ListGroup.Item>
                      <ListGroup.Item className="border-2">permit : {user.permit_id}</ListGroup.Item>
                      <ListGroup.Item className="border-2">permit Validation : {user.permit_validation}</ListGroup.Item>
                      <button type="button" className="btn btn-lg btn-block shadow-lg p-3 mb-2  rounded" size="lg"> Report</button>
                    </Card.Body>
                  </Card>

                </Tab.Pane>
              </Tab.Content>
            ))}
          </Col>

        </Row>
      </Tab.Container>
      <Footer /></div>
  )
};


