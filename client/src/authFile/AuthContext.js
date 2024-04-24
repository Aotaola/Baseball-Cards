import React, { createContext, useContext, useState, useEffect } from 'react';

export const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
    const [isUser, setIsUser] = useState(false);
    const [userInfo, setUserInfo] = useState(null);

    useEffect(() => {
        // Check if the user is already logged in when the app loads
        const loggedInUser = localStorage.getItem('isUser') === 'true';
        const storedUserInfo = localStorage.getItem('userInfo');
        setIsUser(loggedInUser);
        if (storedUserInfo) {
            setUserInfo(JSON.parse(storedUserInfo));
        }
    }, []);

    const login = (UserData) => {
        setIsUser(true);
        setUserInfo(UserData);
        // Securely storing user info
        localStorage.setItem('isUser', 'true');
        localStorage.setItem('userInfo', JSON.stringify(UserData));
    };

    const logout = () => {
        // Confirmation for logging out
        if (window.confirm('Are you sure you want to log out?')) {
            setIsUser(false);
            setUserInfo(null);
            localStorage.removeItem('isUser');
            localStorage.removeItem('userInfo');
        }
    };

    return (
        <AuthContext.Provider value={{ isUser, userInfo, login, logout }}>
            {children} 
        </AuthContext.Provider>
    );
};

