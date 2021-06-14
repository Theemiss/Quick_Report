import React, { useEffect, useState } from 'react';
//import { Header, Footer } from '../common';
import useToken from '../app/useToken';
import './client.css';
import Menu from '../common/menu'

import {Table} from 'reactstrap';



export default function Reports() {
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

    return (
        <div className="body-pd">
<Menu></Menu>
            <h2 className='Title'>All Reports</h2>

            <Table responsive>
    <thead>
        <tr>
            <th className="text-center">#</th>
            <th>ID</th>
            <th>CAR</th>
            <th className="text-center">Driver</th>
            <th className="text-right">User</th>
            <th className="text-right">Actions</th>
        </tr>
    </thead>
    <tbody>
   
 
   
    </tbody>
</Table>
            </div>
    )
};