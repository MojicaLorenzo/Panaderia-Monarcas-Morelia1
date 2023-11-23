import React, { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";
import HomeItemDetails from "./HomeItemDetails";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";



function HomePage({itemsArr}){
    // console.log()

    const mappedHomeItemsArr = itemsArr.map((item) => {
        return <HomeItemDetails
            key = {item.id}
            name = {item.name}
            type = {item.type}
            description = {item.description}
            price = {item.price}
            quantity = {item.quantity}
            image = {item.image}
        />
    })

    return(
        <>
        <header id="main-title">
            <img src="./images/testheader.png" alt="Panaderia Monarcas Morelia"/>
        </header>
            <div>
                <img id="logo-home" src="./images/logo.png" alt="Panaderia Monarcas Morelia"/>
            </div>
            <div className="nav-bar">
                {/* <NavLink to="/signup" className="login-button">  Signup  </NavLink>
                <NavLink to="/loginform" className="login-button">  Login  </NavLink> */}
                <NavLink to="/account" className="login-button"><i className="fa fa-user-circle-o" aria-hidden="true"></i></NavLink>
            </div>
            <div id="home-items-container">
                {mappedHomeItemsArr}
            </div>
        </>


    )
}

export default HomePage