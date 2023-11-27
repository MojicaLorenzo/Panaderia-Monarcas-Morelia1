import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import LoginForm from "./LoginForm";


function Login( { loggedIn } ) {
    // console.log('here')

    const [customers, setCustomer] = useState([]);

    useEffect(() => {
        fetch('/customers')
            .then((resp) => resp.json())
            .then(setCustomer);
    }, []);


    return(
        <div id='login-container'>
            {/* <img src="./images/testheader.png"></img> */}
            <header className="main-title">
                <img src="./images/testheader.png" alt="Panaderia Monarcas Morelia"/>
            </header>
            <span>
                {/* {loggedIn ? 
                <Link customers={customers}  to="/Account"><button className="login-butt" >Account</button></Link>:
                <Link customers={customers}  to="/loginform"><button className="login-butt" >Login</button></Link>} */}
                <Link customers={customers}  to="/loginform"><button className="login-butt" >Login</button></Link>
                <Link to="/signup" ><button className="login-butt">Register New Account</button></Link>
            </span>
        </div>
    )
}

export default Login