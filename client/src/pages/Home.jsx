import React from "react";
import tekken_card_logo from '../assets/tekken_card_logo.png';
import CollectionContainer from '../components/CollectionContainer';

const Home = () => {
    return (
        <div>
            <header className="App-header">
                <img src={tekken_card_logo} className="App-logo" alt="logo" />
            </header>
        </div>
      );
}
 
export default Home;