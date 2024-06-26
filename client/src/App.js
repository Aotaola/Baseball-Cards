import tekken_card_logo from './assets/tekken_card_logo.png';
import NavBar from './components/NavBar.jsx'
import Footer from './components/Footer.jsx';
import ProfileView from './pages/ProfileView.jsx';
import Signup from './pages/Signup.jsx';
import Home from './pages/Home.jsx';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AuthProvider } from './authFile/AuthContext.js'
import React, { useState } from "react";
import './App.css';
import CollectionView from './pages/CollectionView.jsx';

function App() {
  const [user, setUser] = useState();

  function handleLoginLogout(user) {
    setUser(user)
  }

  return (
    <AuthProvider>
      <BrowserRouter>
        <div className="App">
            <NavBar/>
            <header className='App-header'>
          <Routes>
            <Route path="/" element={<Home/>} />
            <Route path="/profile" element={<ProfileView user={user} handleLoginLogout={handleLoginLogout}/>}/>
            <Route path="/signup" element={<Signup user={user} handleLoginLogout={handleLoginLogout}/>}/>
            <Route path="/collections" element={<CollectionView/>}/>
          </Routes>
            </header>
          <Footer/>
        </div>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
