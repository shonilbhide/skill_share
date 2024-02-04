// Home.js
import React from 'react';
import './Home.css'; // Add a corresponding CSS file for styling

const Home = () => {
  return (
    <div className="home-container">
      {/* Dark Blue Banner */}
      <div className="banner">
        <h1>Skill Share</h1>
      </div>

      {/* Top Navigation */}
      <div className="top-nav">
        <ul>
          <li>
            <a href="#profile">Profile</a>
          </li>
          <li>
            <a href="#chat">Chat</a>
          </li>
          <li>
            <a href="#requests">Requests</a>
          </li>
        </ul>
      </div>

      {/* Main Content */}
      <div className="main-content">
        {/* Your main content goes here */}
        <p>Welcome to Skill Share! Explore and enhance your skills.</p>
      </div>
    </div>
  );
};

export default Home;
