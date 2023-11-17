import React, { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";

function HomePage(){
    // console.log()

    return(
        <>
        <h1>Welcome</h1>
            <div className="nav-bar">
                <NavLink to="/login" id="login-button">  Login  </NavLink>
                <NavLink to="/signup" id="login-button">  signup  </NavLink>

            </div>
        </>


    )
}

export default HomePage