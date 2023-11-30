import React, { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";
import HomeItemDetails from "./HomeItemDetails";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import Search from "./Search";
import { DarkModeContext } from "./App";
import { useTheme } from './ThemeContext';



function HomePage({itemsArr, searchTerm, setSearchTerm}){
    
    const [selectedType, setSelectedType] = useState("All");
    const { theme, toggleTheme } = useTheme();


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
    <div className={theme === 'dark' ? 'dark' : 'light'}>
        <header className="main-title"><img src="./images/testheader.png" alt="Panaderia Monarcas Morelia"/></header>
        <button className="dark-mode-button" onClick={toggleTheme}>Toggle Theme</button>
            <div className="nav-bar">
                <Search setSearchTerm={setSearchTerm} />
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
                <NavLink to="/account" className="login-button"><i className="fa fa-user-circle-o" aria-hidden="true"></i></NavLink>
                <NavLink to="/cart" id="cart-button" ><i className="fa fa-shopping-cart" aria-hidden="true"></i></NavLink>
            </div>
            <div id="home-items-container">
                {mappedHomeItemsArr}
            </div>
    </div>
    )
}

export default HomePage  

    // <div id={theme === 'light' ? 'light' : 'dark'}>
    // <div style={{"background-color": "black"}}>


// above nalink account
{/* <NavLink to="/signup" className="login-button">  Signup  </NavLink>
                <NavLink to="/loginform" className="login-button">  Login  </NavLink> */}