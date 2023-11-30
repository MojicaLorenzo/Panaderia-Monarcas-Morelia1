import React, { useState, useEffect } from 'react';
import { useTheme } from './ThemeContext';

function Cart({}) {
    const [cartItems, setCartItems] = useState([]);
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const { theme, toggleTheme } = useTheme();


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
        <div className={theme === 'dark' ? 'dark' : 'light'}>
            <button className="dark-mode-button" onClick={toggleTheme}>Toggle Theme</button>
            <div className="cart-container">
                {isLoggedIn ? (
                <div>
                    <h2>Your Cart</h2>
                    <ul>
                    {cartItems.map((item) => (
                        <li key={item.id} className="cart-item">
                        <div className="item-info">
                            <img src={item.image} alt={item.name} className="item-image" />
                            <div className="item-details">
                            <p>{item.name}</p>
                            <p>${item.price.toFixed(2)}</p>
                        </div>
                        </div>
                        <div className="item-actions">
                            <button onClick={() => removeFromCart(item.id)}>Remove</button>
                        </div>
                        </li>
                    ))}
                    </ul>
                    <p className="total">Total: ${total.toFixed(2)}</p>
                    <button>Place order</button>
                </div>
                ) : (
                <h2 id='cart-empty'>Please log in to view your cart.</h2>
                )}
            </div>
        </div>
    );
}
    

export default Cart;