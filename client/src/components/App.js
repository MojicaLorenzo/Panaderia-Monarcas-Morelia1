import React, { useEffect, useState } from "react";
import { Switch, Route, BrowserRouter } from "react-router-dom";
import HomePage from "./HomePage";
import Items from "./Items";
import SignUpForm from "./SignUpForm";
import LoginForm from "./LoginForm";
import Login from "./Login";

function App() {


    const [items, setItems] = useState([])
    const [reviews, setReviews] = useState([])
    const [customers, setCustomers] = useState([])
    // const [carts, setCarts] = useState([])
    const [loggedIn, setLoggedIn] = useState(false)


    const [customer, setCustomer] = useState(null);

    

    useEffect(() => {
      fetch('/items')
          .then((resp) => resp.json())
          .then(setItems);
    }, [])

    useEffect(() => {
          fetch('/customers')
              .then((resp) => resp.json())
              .then(setCustomers);
        }, [])

    useEffect(() => {
      fetch('/reviews')
          .then((resp) => resp.json())
          .then(setReviews);
    }, [])

    // console.log(customers)

    useEffect(() => {
          // auto-login
          fetch("/check_session").then((resp) => {
            if (resp.ok) {
              resp.json().then((customer) => setCustomer(customer));
            }
          });
        }, []);

        // if (!user) return <Login onLogin={setUser} loggedIn={loggedIn}/>;



  return (
        
          <Switch>
            <Route exact path="/">
              <HomePage/>
            </Route>
            <Route exact path='/signup'>
              <SignUpForm/>
            </Route>
            <Route exact path='/loginform'>
              <LoginForm loggedIn={loggedIn} onLogin={setCustomer} setLoggedIn={setLoggedIn}/>
            </Route>
            <Route exact path='/login'>
              <Login loggedIn={loggedIn} onLogin={setCustomer}/>
            </Route>
            <Route exact path="/items">
              <Items itemsArr={items}/>
            </Route>
          </Switch>
    
  )
}

export default App;
