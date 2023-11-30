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

                <div id='login-container'>
                    <header className="main-title">
                        <img src="./images/testheader.png" alt="Panaderia Monarcas Morelia"/>
                    </header> 
                    <button className="dark-mode-button" onClick={toggleTheme}>Toggle Theme</button>
                    <span>
                        <Link customers={customers}  to="/loginform"><button className="login-butt" >Login</button></Link>
                        <Link to="/signup" ><button className="login-butt">Register New Account</button></Link>
                    </span>
                </div>
        </div>
    )
}

export default Login  
{/* {loggedIn ? 
                        <Link customers={customers}  to="/Account"><button className="login-butt" >Account</button></Link>:
                        <Link customers={customers}  to="/loginform"><button className="login-butt" >Login</button></Link>} */}

{/* <div style={{"background-color": "blue"}}> */}