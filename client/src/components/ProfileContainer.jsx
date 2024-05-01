import React, { useState } from "react";
import CollectionContainer from "../components/CollectionContainer.jsx";
import ProfileCard from "./ProfileCard";
import { useAuth } from "../authFile/AuthContext.js";

const ProfileContainer = ({ user, handleLoginLogout }) => {
    const [settings, setSettings] = useState(false);
    const [logoutWindow, setLogoutWindow] = useState(false);
    // const { userInfo } = useAuth();
    // console.log(userInfo)

    const handleSettings = () => {
        setSettings(!settings);
    }
    const handleLogoutWindow = () => {
        setLogoutWindow(!logoutWindow);
    };
    const handleLogout = () => {
        handleLoginLogout('');
    };

    if (!user) {
        return (
            <h1>Logged out</h1>
        )
    }

    return (
        <div className='profileContainer'>
            <ProfileCard user={user}/>
            <button className="settingsBtn" onClick={() => handleSettings()}>Account</button>
            <button className="settingsBtn" onClick={() => handleLogoutWindow()}>Logout</button>
            {logoutWindow === true ?(
                <window>
                    <div>
                        <label>
                            Are you sure you want to logout?
                        </label>
                        <button className="settingsBtn" onClick={() => handleLogout()}>Yes, I'm sure</button>
                        <button className="settingsBtn" onClick={()=> handleLogoutWindow()}>No, continue my session</button>
                    </div>
                </window>
            ):(<></>)}
            {settings === true ? (
                <div className="profile-settings">
                <label>Edit account</label>
                <table className="profile-edit-table">
                    <thead>
                        <tr>
                            <th>
                                name
                            </th>
                            <th>
                                email
                            </th>
                            <th>
                                bio
                            </th>
                            <th>
                                password
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <th>
                                <input placeholder="user.name"/>
                            </th>
                            <th>
                                <input placeholder="user.email"/>
                            </th>
                            <th>
                                <input placeholder="user.bio"/>
                            </th>
                            <th>
                                <input placeholder="user.password"/>
                            </th>
                        </tr>
                    </tbody>
                </table>
            </div>
            ):(<></>)}
            <CollectionContainer/>
        </div>
      );
}
 
export default ProfileContainer;