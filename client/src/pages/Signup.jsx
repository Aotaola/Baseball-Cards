import React from "react";
import LoginSignupContainer from "../components/LoginSignupContainer";

const Signup = ({ user, handleLoginLogout }) => {

    return (
        <div className="SignupView">
            <LoginSignupContainer user={user} handleLoginLogout={handleLoginLogout}/>
        </div>
      );
}
 
export default Signup;