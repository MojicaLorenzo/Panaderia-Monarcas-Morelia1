import React, { useEffect, useState} from "react";
import { Switch, Route, BrowserRouter, Link} from "react-router-dom";


function HomeItemDetails({name, type, price, image, id, description}) {

    const [inCart, setInCart] = useState(false)
    const [quantity, setQuantity] = useState(1)

    const handleQuantityChange = (e) => {
        const newQuantity = parseInt(e.target.value, 10);
        setQuantity(newQuantity);
    }

    const addToCart = async () => {
        try {
            await fetch("/cart/add", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ item_id: id }),
        });
        setInCart(true);
            console.log("added item successfully")
        } catch (error) {
            console.error("Error adding item to cart:", error);
        }
    };

    const removeFromCart = async () => {
        try {
            await fetch(`/cart/remove/${id}`, {
            method: "DELETE",
        });
        setInCart(false);
            console.log("item removed successfully")
        } catch (error) {
            console.error("Error removing item from cart:", error);
        }
    };

    

    return (
    <div className="home-item-card">
        <img src={image} alt={name} className="card-image" />
        <div className="card-info">
            <h3>{name}</h3>
            <p className="item-type">{type}</p>
            <p className="item-price">${price.toFixed(2)}</p>
            {/* <p className="item-description">{description}</p> */}
            <div className="card-buttons">
                <Link to={`/items/${id}`} className="info-button">
                    <i className="fa fa-info-circle" aria-hidden="true"></i>
                </Link>
                {inCart ? (
                    <button className="cart-button" onClick={removeFromCart}>
                    Remove from Cart
                    </button>
                ) : (
                    <button className="cart-button" onClick={addToCart}>
                    Add to Cart
                    </button>
                )}
            </div>
        </div>
    </div>
    );
}

export default HomeItemDetails