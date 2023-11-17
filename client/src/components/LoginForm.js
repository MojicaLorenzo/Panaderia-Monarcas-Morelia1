import React, { useEffect, useState } from "react";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";


function LoginForm({loggedIn, setLoggedIn, onLogin}) {

    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [errors, setErrors] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [user, setUser] = useState(null);
    const history = useHistory()

    
    function handleSubmit(e) {
        e.preventDefault();
        // console.log(username)
        // console.log(password)
        // setIsLoading(true);
        fetch("/login", {
            method: "POST",
            headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
        }).then((resp) => {
            // setIsLoading(false);
            if (resp.ok) {
            resp.json().then((customer) => onLogin(customer));
            console.log ("Successfully logged in !")
            history.push("/")
            alert(`welcome back ${username}`)
        } else {
            resp.json().then((err) => setErrors(err.errors));
            }
        });
    }

    return(
        <form onSubmit={handleSubmit}>
            Username:<input
            type="text"
            id="username"
            autoComplete="off"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            />
            Password:<input
            type="password"
            id="password"
            autoComplete="current-password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            />
            <button type="submit">Login</button>
        </form>
        
    )
}

export default LoginForm


//  <div className="loginform">
//             <div className="centered-content">
//                 <h1 className="login">Login</h1>
//                 <br />
//                 <div id="regform">
//                     Username: <input
//                         className="reginput"
//                         type="text"
//                         placeholder="Username"
//                         value={username}
//                         onChange={(e) => setUsername(e.target.value)}
//                     />
//                     <br/>
//                     Password: <input
//                         className="reginput"
//                         type="password"
//                         placeholder="Password"
//                         value={password}
//                         onChange={(e) => setPassword(e.target.value)}
//                     />
//                     <br />
//                     <button id="register" onClick={handleSubmit}>Login</button>
//                     {validLogin && <p>{validLogin}</p>}
//                 </div>
//             </div>
//         </div>









// const handleLogin = async () => {
//     try{
//         const response = await fetch('/customers') // Fetch customer data
//         const customerData = await response.json()
//         const customer = customerData.find((customer) => customer.username === username);
//         console.log(response)
//         console.log(password)
        
//         if (customer && customer.password_hash === password) {
//             // Valid login
//             console.log('Login successful')
//             console.log(customer.id)
//             setLoggedIn(!loggedIn)
//             // setLoggedInID(customer.id)
//             history.push('/items')
//         } else {
//             // Invalid login
//             setValidLogin('Invalid username or password');
//         }
        
//     } catch (error) {
//         console.error('Error fetching customer data', error);
//     };
// };