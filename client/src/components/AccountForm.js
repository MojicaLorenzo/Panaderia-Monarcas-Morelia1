import React, { useEffect, useState } from "react";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";

function AccountForm({ loggedInID, setLoggedIn, loggedIn}) {

    const history = useHistory()
    const [showPassword, setShowPassword] = useState(false);
    const [customerData, setCustomerData] = useState({});
    const [newData, setNewData] = useState({
        username: "",
        password: ""
    });

    useEffect(() => {
        setNewData({
            username: customerData.username,
            password: customerData.password
        });
    }, [customerData]);

    useEffect(() => {
        fetch("/check_session")
            .then((resp) => resp.json())
            .then(setCustomerData)
    }, [])

    console.log(customerData.id)
    
    // useEffect(() => {
    //     fetch(`customers/${loggedInID}`)
    //         .then((resp) => resp.json())
    //         .then(setCustomerData)
    // }, [loggedInID])

    const updateInfo = async (e) => {
        e.preventDefault()
        try {
            const changedFields = {};

            // Compare each field in newData with custData and add changed ones to changedFields
            for (const key in newData) {
                if (newData[key] !== customerData[key]) {
                    changedFields[key] = newData[key];
                }
            }
            console.log("here")
            const response = await fetch(`customers/${customerData.id}`, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(changedFields),
            });
            // console.log("here")

            if (response.ok) {
                // // ReFetch Updated Data
                fetch(`customers/${customerData.id}`)
                    .then((resp) => resp.json())
                    .then(setCustomerData);
                // Switch back to view mode after updating
                // setMakeChanges(true); 
                console.log("Account edit successful !")
                alert("Update successful!")
                history.push("/")
            } else {
                console.error('Failed to update customer information');
                alert('Failed to update customer');
            }
        } catch (error) {
            console.error('Error updating customer information', error);
        }
    };

    const handleChange = (e) => {
        const { name, value } = e.target
        setNewData({ ...newData, [name]: value })
    }

    // const logOut = (e) => {
    //     setLoggedIn(!loggedIn)
    //     history.push('/CustomerLogin')
    // }

    return ( 
            <div className="login-form">
                <h2 className="login" align = 'center'>Edit Account</h2>
                <form id="regform" name="form" onSubmit={updateInfo}>
                    <br />
                    Username:<input
                        className="reginput"
                        type="text"
                        name="username"
                        placeholder="New username"
                        value={newData.username}
                        onChange={handleChange} 
                        />
                    Password: <input
                        className="reginput"
                        type={showPassword ? "text" : "password"}
                        name="password"
                        placeholder="New password"
                        value={newData.password}
                        onChange={handleChange}
                    />
                    <button className="login" type='button' id="showPasswrd" onClick={() => setShowPassword(!showPassword)}>show password</button>
                    
                    <button className="login" id="register" type="submit" name="Register" value="submit" >Submit edit</button>
                </form>
            </div>
            
    )
}

export default AccountForm



{/* <div>
                <h2 className="login" align = 'center'>Edit Account</h2>
                <form id="regform" name="form" onSubmit={updateInfo}>
                    <br />
                    Username:<input
                        className="reginput"
                        type="text"
                        name="username"
                        placeholder={"username"}
                        value={formData.username}
                        onChange={handleChange} />
                    Password: <input
                        className="reginput"
                        type={"password"}
                        name="password"
                        placeholder="password"
                        value={formData.password}
                        onChange={handleChange}
                    /> */}
                    {/* <button className="buttons" type='button' onClick={() => setShowForm(!showForm)}>EDIT ACCOUNT</button> */}
                    {/* <input className="login" id="register" type="submit" name="Register" ></input>
                    <button className="login" type="button" onClick={() => setMakeChanges(!makeChanges)}>Return</button>
                </form>
            </div> */}