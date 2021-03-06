import React, { useState } from "react";

import TextField from "@material-ui/core/TextField";
import PropTypes from "prop-types";
import { Alert } from "reactstrap";
import "./login.css";
/**
 * Login Component
 * @param {*} credentials 
 * @returns Saved Token
 */
async function loginUser(credentials) {
  /**
   * Login Function
   */
  return fetch("http://102.37.113.211/api/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(credentials),
  }).then((data) => data.json());
}

export default function SignIn({ setToken }) {
  const [Email, setUserName] = useState();
  const [Password, setPassword] = useState();
  const [error, setError] = useState();
  const handleSubmit = async (e) => {
    e.preventDefault();
    const token = await loginUser({
      Email,
      Password,
    });

    if (token.Authonticate === undefined) {
      setError("Wrong Credential");
    }
    if (token.Authonticate === false) {
      setError("You are not admin");
    } else {
      setToken(token);
    }
  };
  return (
    <div className="limit">
      <div className="login-container">
        <div className="bb-login">
          <form className="bb-form validate-form" onSubmit={handleSubmit}>
            <span className="bb-form-title p-b-26"> Welcome </span>
            <br />
            <div
              className="wrap-input100 validate-input"
              data-validate="Valid email is: a@b.c"
            >
              <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="email"
                label="Email Address"
                name="email"
                autoComplete="email"
                className="input100"
                onChange={(e) => setUserName(e.target.value)}
              />
            </div>
            <div
              className="wrap-input100 validate-input"
              data-validate="Enter password"
            >
              <span className="btn-show-pass">
                {" "}
                <i className="mdi mdi-eye show_password"></i>
              </span>{" "}
              <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                name="password"
                label="Password"
                type="password"
                id="password"
                className="input100"
                autoComplete="current-password"
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
            {error && <Alert color="default"> {error}</Alert>}

            <div className="login-container-form-btn">
              <div className="bb-login-form-btn">
                <div className="bb-form-bgbtn"></div>{" "}
                <button className="bb-form-btn"> Login </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
SignIn.propTypes = {
  setToken: PropTypes.func.isRequired,
};
