import React from "react";
import CollectionView from "./CollectionView";
import ProfileCard from "./ProfileCard";
import { useAuth } from "../authFile/AuthContext.js";

const ProfileContainer = () => {
    
    const { userInfo } = useAuth();
    console.log(userInfo)
    return (
        <div className="ProfileContainer">
            <ProfileCard/>
            <CollectionView />
        </div>
      );
}
 
export default ProfileContainer;