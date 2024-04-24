import React from "react";
import CollectionContainer from "../components/Collections";

const Home = () => {
    return(
        <div className="Home">
            <span className="home-title">Card Trade</span>
            <div>
                <h2 className="home-subtitle">Card Trade subtitle</h2>
            </div>
            <CollectionContainer/>
        </div>
    )
}

export default Home;