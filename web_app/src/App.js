import React from "react";
import { Switch, Route, BrowserRouter } from "react-router-dom";
import Clients from "./components/Clients/clients";
import ClientsId from "./components/Clients/singleclient";
import ReportId from "./components/Reports/reportid";
import Reports from "./components/Reports/reports";
import SignIn from "./components/login/login";
import "./App.css";
import useToken from "./components/app/useToken";
import Logout from "./components/login/logout";
import About from "./components/about/about";
import Dashboard from "./components/Dashboard/Dashboard"
function App() {
  const { token, setToken } = useToken();
  if (!token) {
    return <SignIn setToken={setToken} />;
  }

  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <Route exact path="/about" component={About}></Route>

          <Route exact path="/contact"></Route>
          <Route exact path="/reports" component={Reports} />

          <Route exact path="/clients" component={Clients} />
          <Route exact path="/">
            <Dashboard />
          </Route>
          <Route
            name="user"
            exact
            path="/user/:id"
            component={ClientsId}
          ></Route>
          <Route
            name="report"
            exact
            path="/report/:id"
            component={ReportId}
          ></Route>

          <Route exact path="/logout" component={Logout}></Route>
          <Route exact path="/login">
            <SignIn setToken={setToken} />
          </Route>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
