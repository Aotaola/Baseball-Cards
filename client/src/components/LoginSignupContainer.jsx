import React, { useState } from "react";
import yoshimitsu from "../assets/yoshimitsu.png"
import kaz from "../assets/kaz.png"
import jin_kaz from "../assets/jin_kaz.png"
import king from "../assets/king.png"




const LoginSignupContainer = () => {
     
    const [account, setAccount] = useState(false);
    const [formData, setFormData] = useState({user_name: '', password: ''});
    const [newUser, setNewUser] = useState([]);
    const url = "http://54.161.219.191/"
    
    // switch between login and signup
    const needsAccount = () => {
        setAccount(!account);
    }
    console.log(account);
    // creating a new user
    const userSignup = async() => {};

    console.log(newUser);
    // authenticating user 1) handle form change, 2) handle form submission
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(name, value);
    };

    const userLogin = async(e) => {
        e.preventDefault();
        try {
            const res = await fetch(`${url}/api/users/login`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username: formData.user_name,
                    password: formData.password
                })
            });
            const data = await res.json();
            console.log(data); // Output the response from the server
            if (res.ok) {
                // Handle successful login here (e.g., redirecting user or storing authentication token)
                console.log("Login successful:", data);
            } else {
                // Handle errors, e.g., display a message from the server
                console.log("Login failed:", data.message);
            }
        } catch (error) {
            console.error("Failed to fetch:", error);
        }
    };
    console.log(formData);


    return (
        <div className="LoginSignupContainer">
            {!account ? (
            <>
                <div className="login-Container">
                    <label className="signup-label">Jump back into the fight!</label>
                    <br/>
                    <input type="text" className="signup-input" placeholder="User name"/>
                    <input type="password" className="signup-input" placeholder="Password"/>
                    <br/>
                    <button className="login-btn" onClick={() => userLogin}>Login</button>
                </div>
                <p>Don't have an account? </p>
                <button className="login-btn" onClick={() => needsAccount()}>Signup!</button>
            </>
            ):(
            <>
            <button className = "login-btn" onClick={() => needsAccount()}>back to login</button>
                <div className="signup-container">
                    <label className="signup-label">Signup</label>
                    <br/>
                    <input type="text" className="signup-input" placeholder="name"/>
                    <br/>
                    <input type="text" className="signup-input" placeholder="email"/>
                    <br/>
                    {/* <input type="text" className="signup-input" placeholder="bio"/> */}
                    <input type="password" className="signup-input" placeholder="password"/>
                    <br/>
                    <div>
                        <label>
                            <input type="radio" name="avatar" value="avatar1" />
                            <img src={king} alt="Avatar 1" style={{width: '100px', height: '150px'}}/>
                        </label>
                        <label>
                            <input type="radio" name="avatar" value="avatar2" />
                            <img src={jin_kaz} alt="Avatar 2" style={{width: '100px', height: '100px'}}/>
                        </label>
                        <label>
                            <input type="radio" name="avatar" value="avatar3" />
                            <img src={kaz} alt="Avatar 3" style={{width: '100px', height: '100px'}}/>
                        </label>
                        <label>
                            <input type="radio" name="avatar" value="avatar4" />
                            <img src={yoshimitsu} alt="Avatar 4" style={{width: '100px', height: '100px'}}/>
                        </label>
                    </div>
                    <button className="login-btn">Signup</button>
                </div>
            </>
            )}
        </div>
      );
}
 
export default LoginSignupContainer;