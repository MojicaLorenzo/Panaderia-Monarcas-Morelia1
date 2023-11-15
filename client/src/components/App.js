import React, { useEffect, useState } from "react";
import { Switch, Route, BrowserRouter } from "react-router-dom";
import HomePage from "./HomePage";
import Items from "./Items";
import SignUpForm from "./SignUpForm";

function App() {


    const [items, setItems] = useState([])
    const [reviews, setReviews] = useState([])
    const [customers, setCustomers] = useState([])
    // const [carts, setCarts] = useState([])

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




  return (
        <BrowserRouter>
          <Switch>
            <Route exact path="/">
              <HomePage/>
            </Route>
            <Route exact path='/signup'>
              <SignUpForm/>
            </Route>
            <Route exact path="/items">
              <Items itemsArr={items}/>
            </Route>
          </Switch>
        </BrowserRouter>
  )
}

export default App;
