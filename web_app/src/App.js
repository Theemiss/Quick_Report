import React from 'react';
import { Switch, Route,BrowserRouter} from 'react-router-dom';
import Clients from './components/Clients/clients'
import Reports from './components/Reports/reports'
import SignIn from './components/login/login'
import Container from './components/Clients/cientcontainer'
import './App.css';
import useToken from './components/app/useToken'


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

        <Route exact path="/clients" component={Clients } />
        <Route exact path="/">
        </Route>
        <Route name='Client' exact path="/client/:id" render={Container => Container(props)}>

        </Route>
      </Switch>
      </BrowserRouter>
    
    </div>
  );
}

export default App;
