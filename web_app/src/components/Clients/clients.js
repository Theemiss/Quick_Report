import React ,{useEffect,useState} from 'react';
import { Header, Footer } from '../common';
import useToken from '../app/useToken';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import {Link} from 'react-router-dom'

  

export default  function  Clients (){
    const { token, setToken } = useToken();
    const [data, setData] =useState({});
    const Token = "Bearer ".concat(token)

    useEffect(() => {

        const fetchUserEmail = async () => {
    
          const response = await fetch('http://102.37.113.211/api/company/clients', {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
              'Authorization' :  Token
            }
          });
    
          const  email  = await response.json();
    
          setData(email);
    
        };
    
        fetchUserEmail();
    
      }, []);
    console.log(data)
    const arr = []
      for (const x in data){
          arr.push(data[x])
      }

    return (
        <div>
        <Header />

            <h2 className='Title'>All Client</h2>

            <TableContainer component={Paper}>
      <Table aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>ID</TableCell>
            <TableCell align="right">Name</TableCell>
            <TableCell align="right">Last Name</TableCell>
            <TableCell align="right">Phone</TableCell>
            <TableCell align="right">Email</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {arr.map((user) => (
            <TableRow key={user.first_name}>
              <TableCell component="th" scope="row">
         <Link to={'client/${user.id} '} activeClassName="current" params={{id : user.id}}>  {user.id}</Link>
              </TableCell>
              <TableCell align="right">{user.first_name} </TableCell>
              <TableCell align="right">{user.last_name}</TableCell>
              <TableCell align="right">{user.phone}</TableCell>
              <TableCell align="right">{user.email}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
            <Footer /></div>
    )
};