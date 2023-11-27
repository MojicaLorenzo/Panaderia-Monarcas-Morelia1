import React, { useState, useEffect } from 'react';

function Cart({}) {
    const [cartItems, setCartItems] = useState([]);
    const [isLoggedIn, setIsLoggedIn] = useState(false);

    const fetchCartItems = async () => {
        try {
            const response = await fetch('/cart');
            const data = await response.json();
            console.log('Fetched cart items:', data);
            setCartItems(Array.isArray(data) ? data : []);
        } catch (error) {
            console.error('Error fetching cart items:', error);
        }
    };
    // console.log(cartItems)

    const removeFromCart = async (id) => {
    try {
        // Assuming you have an item ID, make a DELETE request to remove the item from the cart
        await fetch(`/cart/remove/${id}`, {
            method: "DELETE",
        });

        // Update the local state to reflect the change
        setCartItems((prevCartItems) => prevCartItems.filter(item => item.id !== id));
        console.log("item removed successfully");
    } catch (error) {
        console.error("Error removing item from cart:", error);
    }
};

    useEffect(() => {
        // Check if the user is logged in
        const checkLoginStatus = async () => {
            try {
                const response = await fetch('/check_session');
                if (response.status === 200) {
                    // User is logged in
                    setIsLoggedIn(true);
                    // Fetch cart items for the logged-in user
                    fetchCartItems();
                } else {
                    // User is not logged in
                    setIsLoggedIn(false);
                }
            } catch (error) {
                console.error('Error checking session:', error);
            }
        };

        // Check login status when the component mounts
        checkLoginStatus();
    }, []);

    const total = cartItems.reduce((sum, item) => sum + item.price, 0);

    return (
        <div>
            {isLoggedIn ? (
                <div>
                    <h2>Your Cart</h2>
                    <ul>
                        {cartItems.map((item) => (
                            <li key={item.id}>
                                {item.name} - ${item.price.toFixed(2)}
                                <button onClick={() => removeFromCart(item.id)}>Remove</button>
                            </li>
                        ))}
                    </ul>
                    <p>Total: ${total.toFixed(2)}</p>
                </div>
            ) : (
                <p>Please log in to view your cart.</p>
            )}
        </div>
    );
}
    

export default Cart;






















//     const [cartItems, setCartItems] = useState([]);
//     const [addItemId, setAddItemId] = useState('');
//     const [removeItemId, setRemoveItemId] = useState('');

//     const fetchCartItems = async () => {
//         try {
//             const response = await fetch('/cart');
//             const data = await response.json();
//             setCartItems(data);
//         } catch (error) {
//             console.error('Error fetching cart items:', error);
//         }
//     };

//     const addToCart = async () => {
//         try {
//             await fetch('/cart/add', {
//             method: 'POST',
//             headers: {
//             'Content-Type': 'application/json',
//             },
//             body: JSON.stringify({ item_id: addItemId }),
//         });
//           // Optionally, you can fetch the updated cart items after adding
//             fetchCartItems();
//         } catch (error) {
//             console.error('Error adding item to cart:', error);
//         }
//     };

//     const removeFromCart = async () => {
//         try {
//             await fetch(`/cart/remove/${removeItemId}`, {
//             method: 'DELETE',
//         });
//           // Optionally, you can fetch the updated cart items after removing
//             fetchCartItems();
//         } catch (error) {
//             console.error('Error removing item from cart:', error);
//         }
//     };

//     useEffect(() => {
//         // Fetch initial cart items when the component mounts
//         fetchCartItems();
//     }, []);
    
//     return (
//         <div>
//             <h2>Your Cart</h2>
//             <ul>
//             {cartItems.map((item) => (
//                 <li key={item.id}>{item.name}</li>
//             ))}
//             </ul>
//         <div>
//             <input
//                 type="text"
//                 placeholder="Item ID to Add"
//                 value={addItemId}
//                 onChange={(e) => setAddItemId(e.target.value)}
//             />
//             <button onClick={addToCart}>Add to Cart</button>
//         </div>
//         <div>
//             <input
//                 type="text"
//                 placeholder="Item ID to Remove"
//                 value={removeItemId}
//                 onChange={(e) => setRemoveItemId(e.target.value)}
//             />
//             <button onClick={removeFromCart}>Remove from Cart</button>
//         </div>
//         </div>
//         );
//     };