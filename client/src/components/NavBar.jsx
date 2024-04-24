import React from "react";
import { Link } from "react-router-dom";

const NavBar = () => {

    return (
        <div className="NavBar">
            <Link to="/" className="navLink-Logo">VFC!</Link>
            <div className="navLinks">
                <Link to="/collections" className="navLink">Collections</Link>
                <Link to="/signup" className="navLink">Sign in</Link>
                <Link to="/profile" className="navLink">Profile</Link>
            </div>
        </div>
      );
}
 
export default NavBar;