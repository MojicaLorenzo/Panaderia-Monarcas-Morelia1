import React, { useEffect, useState } from "react";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";


function LoginForm({customer, setCustomer, loggedInID, setLoggedInID}) {
    
    const [isLoading, setIsLoading] = useState(false);
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [errors, setErrors] = useState([]);
    
    const [user, setUser] = useState(null);
    const history = useHistory()

    
    function handleSubmit(e) {
        e.preventDefault();
        fetch("/login", {
            method: "POST",
            headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
        }).then((resp) => {
            if (resp.ok) {
            resp.json().then((customer) => setCustomer(customer));
            console.log ("Successfully logged in!")
            history.push("/homepage")
            alert(`welcome back ${username}`)
        } else {
            resp.json().then((err) => setErrors(err.errors));
            alert("Login failed try again")
            }
        });
    }
    return(
        <div className="login-form">
            <form onSubmit={handleSubmit}>
                Username:<input
                type="text"
                id="username"
                autoComplete="off"
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                />
                Password:<input
                type="password"
                id="password"
                placeholder="Password"
                autoComplete="current-password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                />
                <button type="submit">Login</button>
            </form>
        </div>
    )
}

export default LoginForm