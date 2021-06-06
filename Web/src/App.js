import React from 'react';
import { Switch, Route,BrowserRouter,Redirect} from 'react-router-dom';
import Clients from './components/Clients/clients'
import Reports from './components/Reports/reports'
import SignIn from './components/login/login'
import './App.css';
import { Router } from 'react-router';

function setToken(userToken) {
  sessionStorage.setItem('token', JSON.stringify(userToken));
}

function getToken() {
  const tokenString = sessionStorage.getItem('token');
  const userToken = JSON.parse(tokenString);
  return userToken?.token
}


function App() {
  const token = getToken();
  if(!token) {
    return (<SignIn setToken={setToken}  />);
  }

  return (
    <div className="App">
      
      <BrowserRouter>
      <Switch>
        <Route exact path="/about">
        </Route>

        <Route exact path="/contact">
        </Route>
        <Route exact path="/reports">
          <Reports />
        </Route>
        <Route exact path="/clients" >
          <Clients/>
        </Route>
        <Route exact path="/">
        {SignIn ? <Redirect to="/clients" /> : <Clients />}
        </Route>
      </Switch>
      </BrowserRouter>
    
    </div>
  );
}

export default App;
