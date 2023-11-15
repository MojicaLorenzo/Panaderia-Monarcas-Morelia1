import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import ItemDetails from "./ItemDetails";

function Items({itemsArr}){
    // console.log(itemsArr)

    const mappedItemsArr = itemsArr.map((item) => {
        return <ItemDetails
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
            <h1>items here</h1>
            {mappedItemsArr}
        </>
    )
}

export default Items