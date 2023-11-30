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

    // console.log(customerData.id)

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
                history.push("/homepage")
            } else {
                console.error('Failed to update customer information');
                alert('Failed to update customer');
            }
        } catch (error) {
            console.error('Error updating customer information', error);
        }
    };
    const handleDelete = async () => {
        try {
            const response = await fetch(`customers/${customerData.id}`,{
                method: "DELETE"
            });
    
            if (response.ok) {
            console.log("Customer deleted successfully!");
            alert("Account deleted successfully!");
            // setLoggedIn(false);
            history.push("/");
        } else {
            console.error("Failed to delete customer");
            alert("Failed to delete customer");
        }
        } catch (error) {
            console.error("Error deleting customer", error);
        }
    };

    const handleLogout = async () => {
        try {
            const response = await fetch("/logout", {
                method: "DELETE"
            });
            if (response.ok) {
            console.log("Logout successful!");
            // setLoggedIn(false);
            alert("Logout successful!")
            history.push("/");
        } else {
            console.error("Failed to logout");
            alert("Failed to logout");
        }
        } catch (error) {
            console.error("Error during logout", error);
        }
    };

    const handleChange = (e) => {
        const { name, value } = e.target
        setNewData({ ...newData, [name]: value })
    }

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
                    <button className="edit-button" type='button'  onClick={() => setShowPassword(!showPassword)}>show password</button>
                    
                    <button className="edit-button"  type="submit" name="Register" value="submit" >Submit edit</button>
                    <button className="edit-button" id="deleteAccount" type="button" onClick={handleDelete}>Delete Account</button>
                    <button className="edit-button" id="logout" type="button" onClick={handleLogout}>Logout</button>
                </form>
            </div>
            
    )
}



export default AccountForm
