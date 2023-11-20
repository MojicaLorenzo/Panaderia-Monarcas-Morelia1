import React, { useEffect, useState } from "react";

function ItemDetails({name, type, description, price, quantity, image}){

    return (
        <div id="items-conatiner">
            <div id="items-info">
                <h3>{name}</h3>
                {/* <img src={image} alt={name}/> */}
                {/* <h5>{type}</h5> */}
            </div>
        </div>
    )
}

export default ItemDetails