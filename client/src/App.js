import card_logo from './images/card_logo.png';
import Home from './pages/Home.jsx';
import Profile from './pages/Profile.jsx';
import Footer from './components/Footer.jsx';
import {BrowserRouter as Router, Route, Routes, Link} from 'react-router-dom';

import './App.css';

function App() {
  return (
      <Router>
        <div className="App">
          <header className="App-header">
            <img src={card_logo} className="App-logo App-logo-spin" alt="logo" />
            <Link to="/profile" className="profile-link"> Profile </Link>
          </header>
          <Home/>
          <Routes>
            <Route path="/profile" component={Profile} />
          </Routes>
        </div>
          <Footer/>
      </Router>
  );
}

export default App;
