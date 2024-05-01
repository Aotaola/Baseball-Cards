import React, { useState } from "react";
import yoshimitsu from "../assets/yoshimitsu.png"
import kaz from "../assets/kaz.png"
import jin_kaz from "../assets/jin_kaz.png"
import king from "../assets/king.png"




const LoginSignupContainer = ({ handleLoginLogout, user }) => {
     
    const [account, setAccount] = useState(false);
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    // const url = "http://54.243.7.16/"
    const url = 'http://127.0.0.1:5000/'
    
    // switch between login and signup
    const needsAccount = () => {
        setAccount(!account);
    }
    // creating a new user
    const userSignup = async(e) => {
        e.preventDefault();
        try {
            const res = await fetch(`${url}users/signup`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username: username,
                    password: password,
                    email: email
                })
            });
            const data = await res.json();
            if (res.ok) {
                // Handle successful login here (e.g., redirecting user or storing authentication token)
                console.log("User creation successful:", data);
                handleLoginLogout(data)
            } else {
                // Handle errors, e.g., display a message from the server
                console.log("User creation failed:", data.message);
            }
        } catch (error) {
            console.error("Failed to fetch:", error);
        }

    };

    // authenticating user 1) handle form change, 2) handle form submission
    const handleChange = (e) => {
        if (e.target.type === 'text') {
            setUsername(e.target.value);
        } else if (e.target.type === 'password') {
            setPassword(e.target.value);
        } else if (e.target.type === 'email') {
            setEmail(e.target.value);
        }
    };

    const userLogin = async(e) => {
        e.preventDefault();
        try {
            const res = await fetch(`${url}users/login`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username: username,
                    password: password
                })
            });
            const data = await res.json();
            if (res.ok) {
                // Handle successful login here (e.g., redirecting user or storing authentication token)
                console.log("Login successful:", data);
                handleLoginLogout(data);
            } else {
                // Handle errors, e.g., display a message from the server
                console.log("Login failed:", data.message);
            }
        } catch (error) {
            console.error("Failed to fetch:", error);
        }
    };

    if (user) {
        return (
            <h1>Logged in</h1>
        )
    }
    return (
        <div className="LoginSignupContainer">
            {!account ? (
            <>
                <div className="login-Container">
                    <label className="signup-label">Login</label>
                    <br/>
                    <input type="text" className="signup-input" onChange={handleChange} placeholder="User name"/>
                    <br/>
                    <input type="password" className="signup-input" onChange={handleChange} placeholder="Password"/>
                    <br/>
                    <button className="login-btn" onClick={userLogin}>Login</button>
                    <p>Dont have an account?</p>
                    <button className="login-btn" onClick={() => needsAccount()}>Sign Up</button>
                </div>
            </>
            ):(
            <>
                <div className="signup-container">
                    <label className="signup-label">Sign Up</label>
                    <br/>
                    <input type="username" onChange={handleChange} className="signup-input" placeholder="username"/>
                    <br/>
                    <input type="email" onChange={handleChange} className="signup-input" placeholder="email"/>
                    <br/>
                    <input type="password" onChange={handleChange} className="signup-input" placeholder="password"/>
                    <br/>
                    <div>
                        <label>
                            <input type="radio" name="avatar" value="avatar1" />
                            <img src={king} alt="Avatar 1" style={{width: '100px', height: '100px'}}/>
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
                    <button className="login-btn" onClick={userSignup}>Sign up</button>
                    <button className ="login-btn" onClick={() => needsAccount()}>Cancel</button>
                </div>
            </>
            )}
        </div>
      );
}
 
export default LoginSignupContainer;