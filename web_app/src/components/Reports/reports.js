import React, { useEffect, useState } from 'react';
import { Header, Footer } from '../common';
import useToken from '../app/useToken';
import './client.css';
import { Link } from 'react-router-dom'
import ListGroup from 'react-bootstrap/ListGroup'
import { Tab, Row, Col, Card, Container, Button } from 'react-bootstrap'



export default function Reports() {
    const { token, setToken } = useToken();
    const [data, setData] = useState({});
    const Token = "Bearer ".concat(token)
    const mystyle = {
        BorderColor: 'blue'
    };
    useEffect(() => {

        const fetchUserEmail = async () => {

            const response = await fetch('http://102.37.113.211/api/company/reports', {
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

            <h2 className='Title'>All Reports</h2>

            <Tab.Container id="list-group-tabs-example" >
                <Row>
                    <Col sm={12}>
                        {arr.map((user) => (<ListGroup className='nayek'>

                            <Link to="/">  <ListGroup.Item className='nayek shadow-lg p-3 mb-2 bg-white rounded'>
                                DATA
                            </ListGroup.Item>    </Link>     </ListGroup>



                        ))}   </Col>




                </Row>
            </Tab.Container>
            <Footer /></div>
    )
};