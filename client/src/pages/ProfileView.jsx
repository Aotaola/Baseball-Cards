import React from "react";
import ProfileContainer from "../components/ProfileContainer";
import { useAuth } from "../authFile/AuthContext";

const ProfileView = ({ user, handleLoginLogout }) => {

    const { userInfo } = useAuth();
    console.log(userInfo);

    return (
        <div className="profileView">
            <ProfileContainer user={user} handleLoginLogout={handleLoginLogout} />
        </div>
      );
}
 
export default ProfileView;