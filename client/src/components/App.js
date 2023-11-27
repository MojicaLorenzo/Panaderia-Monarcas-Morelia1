import React, { createContext, useEffect, useState, } from "react";
import { Switch, Route, BrowserRouter, Link} from "react-router-dom";
import HomePage from "./HomePage";
import Items from "./Items";
import SignUpForm from "./SignUpForm";
import LoginForm from "./LoginForm";
import Login from "./Login";
import AccountForm from "./AccountForm";
import Customers from "./Customers";
import CustomerDetails from "./CustomerDetails";
import Cart from "./Cart";
import Search from "./Search";
import { useLocation } from "react-router-dom/cjs/react-router-dom.min";

export const darkMode = createContext("light")

function App() {


    const [items, setItems] = useState([])
    // const [reviews, setReviews] = useState([])
    const [customers, setCustomers] = useState([])
    const [loggedIn, setLoggedIn] = useState(false)
    const [loggedInID, setLoggedInID] = useState()
    const [customer, setCustomer] = useState(null);
    const [searchTerm, setSearchTerm] = useState("")
    

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

    // useEffect(() => {
    //   fetch('/reviews')
    //       .then((resp) => resp.json())
    //       .then(setReviews);
    // }, [])
    

    useEffect(() => {
          fetch("/check_session").then((resp) => {
            if (resp.ok) {
              resp.json().then((customer) => setCustomer(customer));
            }
          });
        }, []);

        console.log(customer)

        // if (!customer) return <Login onLogin={setCustomer} loggedIn={loggedIn}/>

        const [theme, setTheme] = useState ("light")
        function toggleTheme(){
          setTheme(!theme)
        }

        const location = useLocation();
        const isAuthPage = location.pathname === "/login" || location.pathname === "/signup";

  return (
    <darkMode.Provider value={theme ? "light" : "dark"}>
      
      <div className="app" id={theme ? 'light' : 'dark'}>
            <Link to="/homepage" >
            <img id="logo"  src="https://upload.wikimedia.org/wikipedia/en/thumb/2/27/Monarcas_Morelia_2.svg/1200px-Monarcas_Morelia_2.svg.png" alt="Logo" />
            </Link>
            <button id="dark-mode-button" onClick={toggleTheme}>{theme ? 'dark' : 'light'} mode</button>
          <Switch onChange={toggleTheme}>

            

            <Route exact path="/homepage">
              <HomePage itemsArr={items} searchTerm={searchTerm} setSearchTerm={setSearchTerm}/>
            </Route>
            

            <Route exact path="/search">
              <Search itemsArr={items} setSearchTerm={setSearchTerm}/>
            </Route>

            <Route exact path='/signup'>
              <SignUpForm/>
            </Route>

            <Route exact path='/loginform'>
              <LoginForm loggedIn={loggedIn} setLoggedIn={setLoggedIn} setCustomer={setCustomer}  
                loggedInID={loggedInID} setLoggedInID={setLoggedInID} customer={customer}/>
            </Route>

            <Route exact path='/'>
              <Login loggedIn={loggedIn} onLogin={setCustomer} />
            </Route>

            <Route exact path='/account'>
              <AccountForm customersArr={customers} setCustomersArr={setCustomers} loggedIn={loggedIn} />
            </Route>
            
            <Route exact path='/customerdetails'>
              <CustomerDetails customersArr={customers} setCustomersArr={setCustomers} />
            </Route>

            <Route exact path='/customers'>
              <Customers customersArr={customers}/>
            </Route>

            <Route exact path="/items">
              <Items itemsArr={items}/>
            </Route>

            <Route exact path="/cart">
              <Cart/>
            </Route>

          </Switch>
          
      </div>
    </darkMode.Provider>
  )
}

export default App;
