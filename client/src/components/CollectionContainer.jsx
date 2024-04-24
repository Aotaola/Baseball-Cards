import React, { useState, useEffect } from "react";
import { useAuth } from "../authFile/AuthContext";
import CollectionCard from "./CollectionCard";

const CollectionContainer = ({ isProfileView }) => {
    const [collections, setCollections] = useState([]);
    const { isUser, userInfo } = useAuth(); 
    
    useEffect(() => {
        const fetchCollections = async () => {
            let url = 'api/collections';
            if (isProfileView && isUser && userInfo){
                url += `/user/${userInfo.id}`;
            }
            try {
                const res = await fetchCollections(url);
                const data = await res.json();
                setCollections(data);
            } catch (error) {
                console.error('Failed to fetch collections: ' + error.message)
            }
        }
        fetchCollections();
    }, [isUser, userInfo, isProfileView]);

    return (
        <div className="CollectionContainer">
            <p>here is the container for the collections</p>
            {collections.map(collection => (
                <CollectionCard key={collection.id} collection={collection}/>
            ))}
        </div>
      );
}
 
export default CollectionContainer;