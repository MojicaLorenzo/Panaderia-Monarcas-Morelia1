import React, { useEffect, useState } from "react";


function SignUpForm(){

    const [showPassword, setShowPassword] = useState(false);
    const [newCustomer, setNewCustomer] = useState({
        name: "",
        username: "",
        email: "",
        password: "",
        
    })

    useEffect(() => {
        fetch('/customers')
            .then(resp => resp.json())
            .then(data => setNewCustomer(data))
    }, [])


    function handleChange(e) {
        const { name, value } = e.target
        setNewCustomer({ ...newCustomer, [name]: value })
    }

    const handleRegister = async (e) => {
        e.preventDefault()
        try {
            const response = await fetch('/customers', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(newCustomer),
            });

            if (response.ok) {
                console.log('User added successfully');
                e.target.name.value = ""
                e.target.username.value = ""
                e.target.email.value = ""
                e.target.password.value = ""
                // You can reset the form or perform other actions here
                setShowPassword(false);
                alert('User added successfully!')
            } else {
                console.error('Failed to add user');
                alert('Password must contain a special character and number!\n\n Email must be proper format Username must be unique!')
            }
        } catch (error) {
            console.error('Error:', error);
        }

    };


    return (
        <div>
            <div className="loginform" >
                <div className="centered-content">
                <h2 className="login">Register New Account!</h2>
                <br/>
                    <form id="regform" name='form' onSubmit={handleRegister}>
                            Name:<input
                            className="reginput"
                            type="text"
                            name="name"
                            placeholder='Name'
                            value={newCustomer.name}
                            onChange={handleChange}
                        />
                        <br/>
                        Username:<input
                            className="reginput"
                            type="text"
                            name="username"
                            placeholder='Username'
                            value={newCustomer.username}
                            onChange={handleChange} />
                        Password: <input
                            className="reginput"
                            type={showPassword ? "text" : "password"}
                            name="password"
                            placeholder='Password'
                            value={newCustomer.password}
                            onChange={handleChange}
                        />
                        <br/>
                        <button type='button' id="showPasswrd" onClick={() => setShowPassword(!showPassword)}>show password</button>
                        <br/>
                        Email: <input
                            className="reginput"
                            type="text"
                            name="email"
                            placeholder='Email'
                            value={newCustomer.email}
                            onChange={handleChange} />
                        <br/> 
                        <input id="register" type="submit" name="Register" ></input>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default SignUpForm