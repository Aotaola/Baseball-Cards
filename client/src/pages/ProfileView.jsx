import React from "react";
import ProfileContainer from "../components/ProfileContainer";
import { useAuth } from "../authFile/AuthContext";

const ProfileView = () => {

    const { userInfo } = useAuth();
    console.log(userInfo);

    return (
        <div className="profileView">
            <ProfileContainer/>
        </div>
      );
}
 
export default ProfileView;