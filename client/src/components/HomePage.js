import React, { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";
import HomeItemDetails from "./HomeItemDetails";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import Search from "./Search";



function HomePage({itemsArr, searchTerm, setSearchTerm}){
    // console.log()
    const [selectedType, setSelectedType] = useState("All");

    const handleTypeChange = (type) => {
    setSelectedType(type);
};

const filteredArr = itemsArr.filter((searchItemObj) => {
    const matchesSearchTerm =
        searchItemObj.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        searchItemObj.price.toString().includes(searchTerm) ||
        searchItemObj.type.toLowerCase().includes(searchTerm.toLowerCase());

    const matchesSelectedType =
        selectedType === "All" || searchItemObj.type === selectedType;

    return matchesSearchTerm && matchesSelectedType;
});

    const mappedHomeItemsArr = filteredArr.map((item) => {
        return <HomeItemDetails
            key = {item.id}
            id = {item.id}
            name = {item.name}
            type = {item.type}
            description = {item.description}
            price = {item.price}
            quantity = {item.quantity}
            image = {item.image}
        />
    })

    const uniqueTypes = [...new Set(itemsArr.map((item) => item.type))];
  uniqueTypes.unshift("All"); // Add "All" option to show all types


    return(
        <>
        <header className="main-title">
            <img src="./images/testheader.png" alt="Panaderia Monarcas Morelia"/>
        </header>

            <div className="nav-bar">
                <NavLink to="/account" className="login-button"><i className="fa fa-user-circle-o" aria-hidden="true"></i></NavLink>
                <Search setSearchTerm={setSearchTerm} />
                <NavLink to="/cart" id="cart-button" ><i className="fa fa-shopping-cart" aria-hidden="true"></i></NavLink>
            <div>
                <span>Filter by Type:</span>
                <select
                value={selectedType}
                onChange={(e) => handleTypeChange(e.target.value)}
                >
                {uniqueTypes.map((type) => (
                    <option key={type} value={type}>
                        {type}
                    </option>
                ))}
                </select>
            </div>
            </div>

            <div id="home-items-container">
                {mappedHomeItemsArr}
            </div>

            {/* <footer>2023 Panaderia Monarcas Morelia. All Rights Reserved.</footer> */}
        </>


    )
}

export default HomePage 


// above nalink account
{/* <NavLink to="/signup" className="login-button">  Signup  </NavLink>
                <NavLink to="/loginform" className="login-button">  Login  </NavLink> */}