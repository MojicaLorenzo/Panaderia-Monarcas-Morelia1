import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import LoginForm from "./LoginForm";
import { useTheme } from './ThemeContext';


function Login( { loggedIn } ) {
    // console.log('here')

    const [customers, setCustomer] = useState([]);
    const { theme, toggleTheme } = useTheme();

    useEffect(() => {
        fetch('/customers')
            .then((resp) => resp.json())
            .then(setCustomer);
    }, []);


    return(
        <div className={theme === 'dark' ? 'dark' : 'light'}>
                <header className="main-title">
                        <img src="./images/testheader.png" alt="Panaderia Monarcas Morelia"/>
                </header> 
                <div id='login-container'>
                    <button className="dark-mode-button" onClick={toggleTheme}>Toggle Theme</button>
                    <span>
                        <Link customers={customers}  to="/loginform"><button className="login-butt" >Login</button></Link>
                        <Link to="/signup" ><button className="login-butt">Register New Account</button></Link>
                    </span>
                </div>
                <div class="overview-container">
                    <h1>Panaderia Monarcas Morelia</h1>
                    <p>Welcome to Panaderia Monarcas Morelia, explore our diverse selection of freshly baked goods, each crafted with care and authenticity. Whether you're a bread connoisseur or simply seeking a sweet treat, our online bakery has something for everyone. Create an account to unlock personalized features, manage your cart, and experience the convenience of online ordering. Join us on a journey where traditional baking meets modern technology, bringing the warmth of our bakery directly to your fingertips. Discover, indulge, and savor the flavors of Panaderia Monarcas Morelia.</p>
                    <p>Your bakery adventure starts here.</p>
                </div>
        </div>
    )
}

export default Login  
{/* {loggedIn ? 
                        <Link customers={customers}  to="/Account"><button className="login-butt" >Account</button></Link>:
                        <Link customers={customers}  to="/loginform"><button className="login-butt" >Login</button></Link>} */}

{/* <div style={{"background-color": "blue"}}> */}