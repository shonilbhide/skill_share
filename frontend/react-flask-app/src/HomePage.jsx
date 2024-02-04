// Home.js
import React from 'react';
import './Home.css'; // Add a corresponding CSS file for styling

const Home = () => {
  const items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"];

  return (
    <div className="home-container">

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
        {/* List of Items in Rectangular Tiles */}
            <h1 className="title">Requests</h1>
        <div className="item-list">
          {items.map((item, index) => (
            <div className="item-tile" key={index}><b>
              {item}</b>
              <p>Description</p>
              <br />
              <p className="req_id"><a href={`#id${index + 1}`}>ID</a></p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Home;
