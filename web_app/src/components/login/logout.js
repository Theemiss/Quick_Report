import React ,{useEffect} from 'react';
import { useHistory } from "react-router-dom";
import useToken from '../app/useToken';

export default function Logout(){
let history = useHistory();
const { token, setToken } = useToken();
const Token = "Bearer ".concat(token)
useEffect(() => {

    const fetchUserEmail = async () => {

      const response = await fetch('http://102.37.113.211/api/logout', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization' :  Token
        }
      });



    };

    fetchUserEmail();
    localStorage.removeItem("token")
    history.push('/login')

  }, []);
  return(0
  )
}