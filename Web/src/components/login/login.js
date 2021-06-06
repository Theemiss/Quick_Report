import React, { useState } from "react";
import Avatar from "@material-ui/core/Avatar";
import Button from "@material-ui/core/Button";
import CssBaseline from "@material-ui/core/CssBaseline";
import TextField from "@material-ui/core/TextField";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import Checkbox from "@material-ui/core/Checkbox";
import Box from "@material-ui/core/Box";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import Container from "@material-ui/core/Container";
import { Link, Redirect, useHistory } from "react-router-dom"
import PropTypes from 'prop-types';




function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {" "}
      {"Copyright © "}{" "}
      <Link color="inherit">
        Quick Report{" "}
      </Link>{" "}
      {new Date().getFullYear()} {"."}{" "}
    </Typography>
  );
}

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
  const history = useHistory();
  const classes = useStyles();
  const [Email, setUserName] = useState();
  const [Password, setPassword] = useState();
  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const token = await loginUser({ Email, Password });
      setToken(token);
    } catch (e) {
      alert(e.message);
    }
  };
  return (
    <Container component="main" maxWidth="xs">
      <div className={classes.paper}>
        <Avatar className={classes.avatar}>
          <LockOutlinedIcon />
        </Avatar>{" "}
        <Typography component="h1" variant="h5">
          Sign in
        </Typography>{" "}
        <form className={classes.form} noValidate onSubmit={handleSubmit}>

          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="email"
            label="Email Address"
            name="email"
            autoComplete="email"
            autoFocus
            onChange={e => setUserName(e.target.value)}
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            autoComplete="current-password"
            onChange={e => setPassword(e.target.value)}
          />

          <FormControlLabel
            control={<Checkbox value="remember" color="primary" />}
            label="Remember me"
          />
          <Link to="/clients">
            <Button
              text="SignIn"
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.submit}
            >Sign In</Button>
          </Link>
        </form>{" "}
      </div>{" "}
      <Box mt={8}>
        <Copyright />
      </Box>{" "}
    </Container>
  );
}
SignIn.propTypes = {
  setToken: PropTypes.func.isRequired
}