import React, {useState, useEffect}from "react";

function Search({ itemsArr, setSearchTerm}){


    
    return(
        <input id="searcher"
        type="text" 
        name="searchBar" 
        placeholder="Search..." 
        onChange={e=>setSearchTerm(e.target.value)}/>
    )
}

export default Search;