import React, { useState } from "react";

import TextField from "@material-ui/core/TextField";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import { Link } from "react-router-dom"
import PropTypes from 'prop-types';
import { Alert } from "reactstrap";
import './login.css'




const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: "100%",
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

async function loginUser(credentials) {
  return fetch('http://102.37.113.211/api/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(credentials)
  })
    .then(data => data.json())
}


export default function SignIn({ setToken }) {
  const classes = useStyles();
  const [Email, setUserName] = useState();
  const [Password, setPassword] = useState();
  const [error, setError] = useState();
  const handleSubmit = async e => {
    e.preventDefault();
    const token = await loginUser({
      Email,
      Password
    });

    if (token.Authonticate == undefined) {
      setError("Wrong Credential");
      console.log(token.Authonticate)

    }
    if (token.Authonticate === false) {
      setError("You are not admin");
      console.log(token.Authonticate)
    }
    else {
      setToken(token);
    }

  }
  return (
    < div className="limit" >
    <div className="login-container">
      <div className="bb-login">
        <form className="bb-form validate-form" onSubmit={handleSubmit}>
          <span className="bb-form-title p-b-26"> Welcome </span>
          <span className="bb-form-title p-b-48"> <i class="mdi mdi-symfony"></i>
          </span>
          <div className="wrap-input100 validate-input" data-validate="Valid email is: a@b.c">
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="email"
            label="Email Address"
            name="email"
            autoComplete="email"
            className='input100'

            onChange={e => setUserName(e.target.value)}
          />
          </div>
          <div className="wrap-input100 validate-input" data-validate="Enter password">
            <span className="btn-show-pass"> <i className="mdi mdi-eye show_password">
            </i>
            </span>  <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            className='input100'
            autoComplete="current-password"
            onChange={e => setPassword(e.target.value)}
          />  
            </div>
          {error && <Alert color="default"> {error}</Alert>}


          <div className="login-container-form-btn">
            <div className="bb-login-form-btn">
              <div className="bb-form-bgbtn"></div> <button className="bb-form-btn"> Login </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
  );
}
SignIn.propTypes = {
  setToken: PropTypes.func.isRequired
}

  