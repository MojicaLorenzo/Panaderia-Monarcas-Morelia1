import React, { useEffect, useState } from "react";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";


function CustomerDetails({name, username, email, customersArr, setCustomersArr, customerObj}) {

    // console.log(customerObj)

    // const history = useHistory()
    // const [showForm, setShowForm] = useState(false)
    // const [formData, setFormData] = useState({
    //     email: customerObj.email,
    //     pasword: customerObj.pasword
    // })

    // function handleChange(e) {
    //     setFormData({
    //         ...formData,
    //         [e.target.name]: e.target.value
    //     })
    // }

    // function handleEdit(e) {
    //     e.preventDefault()

    //     // send PATCH request using this customer's id
    //     fetch(`customers/${customerObj.id}`, {
    //         method: "PATCH",
    //         headers: {
    //         "Content-Type": "application/json"
    //         },
    //         body: JSON.stringify(formData)
    //     })
    //         .then(resp => resp.json())
    //         .then(updatedCustomer => {
    //         // console.log(updatedCustomer)
    //         const updatedCustomers = customersArr.map(originalCustomer => {
    //         if (originalCustomer.id === updatedCustomer.id) {
    //             return updatedCustomer
    //         } else {
    //             return originalCustomer
    //         }
    //         })

    //         // update parent state
    //         setCustomersArr(updatedCustomers)

    //         // hide / reset form
    //         // e.target.reset() // moot
    //         setShowForm(!showForm)
    //     })
    // }


    return (

        <div id="customer-container">
            <div id="card-wrapper">
                <h1>{name}</h1>
                <h2>{username}</h2>
                <h3>{email}</h3>
            </div>
        </div>
    )
}

export default CustomerDetails