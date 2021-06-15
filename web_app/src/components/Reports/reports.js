import React, { useEffect, useState } from 'react';
//import { Header, Footer } from '../common';
import useToken from '../app/useToken';
import './client.css';
import Menu from '../common/menu'
import { Link } from 'react-router-dom';

import {Table} from 'reactstrap';


export default function Reports() {
    const { token, setToken } = useToken();
    const [data, setData] = useState({});
    const Token = "Bearer ".concat(token)

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
    let i = 0;
    return (
        <div className="body-pd">
<Menu></Menu>
            <h2 className='Title'>All Reports</h2>

            <Table >
    <thead>
        <tr>
            <th  >#</th>
            <th >Client</th>
            <th >CAR</th>
            <th >Driver</th>
            <th >Time</th>
        </tr>
    </thead>
    <tbody>
    {arr.map((user) => (
         <tr>
            <th ><a href={"http://102.37.113.211/api/client/report/pdf/" + "f8ff4b7c-c06b-4b3e-95d4-0ab902b3917a"}>{i++}</a></th>
            <th ><Link to={{pathname: `/${user.client_id}`}}>{user.first_name} {user.last_name}</Link></th>
            <th >{user.Mark} {user.type_c}</th>
            <th >{user.driver_name} {user.driver_lastname}</th>
            <th >{user.created_at}</th>
        </tr>
      
 
    ))}
 
   
    </tbody>
</Table>
            </div>
    )
};