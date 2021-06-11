import React, { useState } from "react";
import Avatar from "@material-ui/core/Avatar";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import Checkbox from "@material-ui/core/Checkbox";
import Box from "@material-ui/core/Box";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import Container from "@material-ui/core/Container";
import { Link } from "react-router-dom"
import PropTypes from 'prop-types';




function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {" "}
      {"Copyright © "}{" "}
      <Link color="inherit" to='/'>
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
    
    if ( token.Authonticate == undefined ){
      setError("Wrong Credential");
      console.log(token.Authonticate )

    }
    if (token.Authonticate === false)
       {
      setError("You are not admin");
      console.log(token.Authonticate )
    }
    else{
      setToken(token);
    }
    
  }
  return (
    <Container component="main" maxWidth="xs">
      <div className={classes.paper}>
        <Avatar className={classes.avatar}>
          <LockOutlinedIcon />
        </Avatar>{" "}
        <Typography component="h1" variant="h5">
          Sign in
        </Typography>{" "}
        <form className={classes.form} onSubmit={handleSubmit}>

          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="email"
            label="Email Address"
            name="email"
            autoComplete="email"
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

         {error && <div class="alert alert-warning" role="alert">
          {error}
          </div>} 
          <Button
            text="SignIn"
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
          >Sign In</Button>
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