import React, { useEffect, useState } from "react";
import CustomerDetails from "./CustomerDetails";


function Customers({customersArr}) {
    // console.log(customersArr)
    const mappedCustomersArr = customersArr.map((customerObj) => 
    <CustomerDetails
    id = {customerObj.id}
    name = {customerObj.name}
    username = {customerObj.username}
    email = {customerObj.email}
    password = {customerObj.password}
    
    />
    )

    return (
        <>
        {mappedCustomersArr}
        </>
    )
}

export default Customers