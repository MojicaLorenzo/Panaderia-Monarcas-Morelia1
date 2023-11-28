import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

function DetailedItem() {
    const { id } = useParams();
    const [item, setItem] = useState(null);

    useEffect(() => {
    // Fetch item details based on the ID when the component mounts
    const fetchItemDetails = async () => {
        try {
        const response = await fetch(`/items/${id}`); // Replace with your API endpoint
        const data = await response.json();
        setItem(data);
    } catch (error) {
        console.error("Error fetching item details:", error);
    }
    };

    fetchItemDetails();
    }, [id]);

    if (!item) {
    return <div>Loading...</div>;
    }

return (
    <div className="detailed-item-container">
        <div className="detailed-item-info">
        <img src={item.image} alt={item.name} className="item-image" />
        <h2>{item.name}</h2>
        <p className="item-description">{item.description}</p>
        <p className="item-price">Price: ${item.price.toFixed(2)}</p>
        {/* Add other item details as needed */}
        </div>
        
    </div>
    
    );
}

export default DetailedItem;




        // <div>
        //     <h2>{item.name}</h2>
        //     <p>{item.description}</p>
        //     <p>Price: ${item.price.toFixed(2)}</p>
        // </div>