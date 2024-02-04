// MatchedPage.js
import React from 'react';
import { useHistory } from 'react-router-dom';
import './MatchedPage.css';

const MatchedPage = () => {
  const matchedItems = ["User 1", "User 2", "User 3", "User 4", "User 5"];
  const history = useHistory();

  const handleLogOut = () => {
    history.push("/login");
    localStorage.removeItem("token");
  }

  return (
    <div className="matched-container">
      <div className="banner">
        <h1>Skill Share</h1>
        <button onClick={handleLogOut}>Logout</button>
      </div>

      {/* Top Navigation */}
      <div className="top-nav">
        <ul>
          <li>
            <a href="/profile">Profile</a>
          </li>
          <li>
            <a href="/home">Home</a>
          </li>
        </ul>
      </div>

      <div className="main-content">
        <div className="item-list">
          {matchedItems.map((item, index) => (
            <div key={index} className="item-tile">
              <div className="item-title" key={index}><b>
              {item}
              </b>
              <br />
              <p className="title">Description</p>
              <br />
              <button onClick={() => handleChatButtonClick(`#matchedItem${index + 1}`)}>Chat</button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

const handleChatButtonClick = (itemLink) => {
  // Handle chat button click, you can navigate to a chat page or perform other actions
  console.log(`Clicked Chat button for ${itemLink}`);
};

export default MatchedPage;
