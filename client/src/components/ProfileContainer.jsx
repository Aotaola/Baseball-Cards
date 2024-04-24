import React, { useState } from "react";
import CollectionContainer from "../components/CollectionContainer.jsx";
import ProfileCard from "./ProfileCard";
import { useAuth } from "../authFile/AuthContext.js";

const ProfileContainer = () => {
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
        console.log("logout");
    };

    console.log(settings)

    return (
        <div className="ProfileContainer">
            <ProfileCard/>
            <button className="settingsBtn" onClick={() => handleSettings()}>Account</button>
            <button className="settingsBtn" onClick={() => handleLogoutWindow()}>Logout</button>
            {logoutWindow === true ?(
                <window>
                    <div>
                        <h3>
                            are you sure you want to logout?
                        </h3>
                        <button className="logoutBtn" onClick={() => handleLogout()}>Yes, im sure</button>
                        <button className="dontLogoutBtn" onClick={()=> handleLogoutWindow()}>no, continue my session</button>
                    </div>
                </window>
            ):(<></>)}
            {settings === true ? (
                <div className="profile-settings">
                <label> edit account information </label>
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
            <div className="profile-org">
                <CollectionContainer/>
            </div>
        </div>
      );
}
 
export default ProfileContainer;