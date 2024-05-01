import React, { useState, useEffect } from 'react';

const ProfileCard = ({ user }) => {
     
    const url = "http://54.243.7.16/"
    useEffect(() => {
        fetch(`${url}users/user/${user['id']}`, {
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
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
    }, []);

    const editUser = () => {
        
    }

    return (
        <div className='profile-card'>
            <p>{user.username}</p>
            
        </div>
      );
}
 
export default ProfileCard;