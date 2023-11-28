import React, { useEffect, useState} from "react";
import { Switch, Route, BrowserRouter, Link} from "react-router-dom";


function HomeItemDetails({name, type, price, image, id, description}) {

    const [inCart, setInCart] = useState(false)

    const addToCart = async () => {
        try {
          // Assuming you have an item ID, make a POST request to add the item to the cart
            await fetch("/cart/add", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ item_id: id }),
        });
          // Update the local state to reflect the change
        setInCart(true);
            console.log("added item successfully")
        } catch (error) {
            console.error("Error adding item to cart:", error);
        }
    };

    const removeFromCart = async () => {
        try {
          // Assuming you have an item ID, make a DELETE request to remove the item from the cart
            await fetch(`/cart/remove/${id}`, {
            method: "DELETE",
        });
    
          // Update the local state to reflect the change
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













// {/* <div id="home-items-card">
//         <div id="home-items-info">
//             <img src={image} alt={name} />
//             <h3>{name}</h3>
//             <h5>${price.toFixed(2)}</h5>
//             <Link to={`/items/${id}`}><button id="more-info-button"><i className="fa fa-info-circle" aria-hidden="true"></i></button></Link>
//             <div id="cart-button">
//                 {inCart ? (
//                 <button className="cart-button" onClick={removeFromCart}>
//                     Remove from Cart
//                 </button>
//                 ) : (
//                 <button className="cart-button" onClick={addToCart}>
//                     Add to Cart
//                 </button>
//                 )}
//                 {/* <h5>{type}</h5> */}
//             </div>
//         </div>
//     </div>
            
//     )
// } */}





















// const addToCart = () => {
    //     setInCart(!inCart);
    // }











            // <div id="home-items-card">
            //     <div id="home-items-info">
            //         <img src={image} alt={name}/>
            //         <h3>{name}</h3>
            //         <h5>${price.toFixed(2)}</h5>
            //         <div id="cart-button">
            //         {inCart ? (
            //             <button className="cart-button" onClick={addToCart}>Remove from Cart</button>
            //         ) : (
            //             <button className="cart-button" onClick={addToCart}>Add to Cart</button>
            //         )} 
            //         {/* <h5>{type}</h5> */}
            //         </div>
            //     </div>
            // </div>