import React, { useEffect, useState } from "react";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import { useTheme } from './ThemeContext';
import { Link } from "react-router-dom/cjs/react-router-dom.min";


function LoginForm({customer, setCustomer}) {
    
    const [isLoading, setIsLoading] = useState(false);
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [errors, setErrors] = useState([]);
    const { theme, toggleTheme } = useTheme();
    // const [customer, setCustomer ] = useState([])
    
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
        <div className={`login-container ${theme}`}>
        <button className="dark-mode-button" onClick={toggleTheme}>Toggle Theme</button>
        <div className="login-form">
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="username">Username:</label>
                    <input
                        type="text"
                        id="username"
                        autoComplete="off"
                        placeholder="Enter username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="password">Password:</label>
                    <input
                        type="password"
                        id="password"
                        placeholder="Enter password"
                        autoComplete="current-password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                </div>
                <button type="submit">Login</button>
            </form>
            <p className="need-account-text">
                Need an account? <Link to="/signup">Register here</Link>
            </p>
        </div>
    </div>
    )
}

export default LoginForm