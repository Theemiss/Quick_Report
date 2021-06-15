import React from 'react';
import "./assets/css/nucleo-icons.css";
import { Switch, Route,BrowserRouter} from 'react-router-dom';
import Clients from './components/Clients/clients'
import ClientsId from './components/Clients/singleclient'
import ReportId from "./components/Reports/reportid"
import Reports from './components/Reports/reports'
import SignIn from './components/login/login'
import './App.css';
import useToken from './components/app/useToken'
import Logout from './components/login/logout'
import Index from './components/app/main'
function App() {
  const { token, setToken } = useToken();
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
        <Route exact path="/reports" component={Reports}/>

        <Route exact path="/allclients" component={Clients } />
        <Route exact path="/">
          <Index/>
        </Route>
        <Route name="user" exact path="client/:id" component={ClientsId}>
        </Route>
        <Route name="report" exact path="report/:id" component={ReportId}></Route>
   
        <Route exact path="/logout" component={Logout} >

        </Route>
        <Route exact path="/login" >
        <SignIn setToken={setToken}  />
        </Route>

      </Switch>
      </BrowserRouter>
    
    </div>
  );
}

export default App;
