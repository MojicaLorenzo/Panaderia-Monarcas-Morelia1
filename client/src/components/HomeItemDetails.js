import React, { useEffect, useState } from "react";


function HomeItemDetails({name, type, price, image}) {

    const [inCart, setInCart] = useState(false)


    const addToCart = () => {
        setInCart(!inCart);
    }

    return (

            <div id="home-items-card">
                <div id="home-items-info">
                    <img src={image} alt={name}/>
                    <h3>{name}</h3>
                    {/* <h5>price: ${price.toFixed(2)}</h5> */}
                    {inCart ? (
                        <button id="cart-button" onClick={addToCart}>Remove from Cart</button>
                    ) : (
                        <button onClick={addToCart}>Add to Cart</button>
                    )} 
                    {/* <h5>{type}</h5> */}
                </div>
            </div>
    )
}

export default HomeItemDetails