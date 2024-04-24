import React, { useState, useEffect } from 'react';

const ProfileCard = () => {
    const [user, setUser] = useState({})
    const userId = 1
    const url = '54.161.219.191'

    useEffect(() => {
        fetch(`http://${url}/api/users/${userId}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(res => {
            if (!res.ok) {
                throw new Error('Network response was not ok');
            }
            return res.json();
        })
        .then(data => {
            console.log('Data received:', data);
            setUser(data);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
    }, []);
    console.log(user);

    const editUser = () => {
        
    }

    return (
        <div className='profile-card'>
            <p>{user.user_name}</p>
            <p>{user.email}</p>
            <p>{user.tokens}</p>
            <p>{user.bio}</p>
            
        </div>
      );
}
 
export default ProfileCard;