import React from 'react';
import './Profile.css'; // Import your CSS file
import { useHistory } from 'react-router-dom';

const ProfilePage = () => {
  // Dummy data for illustration
  const profileData = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    about: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    card1: {
      title: 'Python Basics',
      description: 'I can teach basics of python, which may include data structured and object oriented programming in python.',
    },
    card2: {
      title: 'Tennis',
      description: 'Being a professional Tennis player, I can teach Tennis from the basics to an advance level.',
    },
  };

  const handleLogOut = () => {
    history.push("/login");
    localStorage.removeItem("token");
  }

  const history = useHistory();

  return (
    <div className="home-container">

      <div className="banner">
        <h1>Skill Share</h1>
        <button onClick={handleLogOut}>Logout</button>
      </div>

      {/* Top Navigation */}
      <div className="top-nav">
        <ul>
          {/* <li>
            <a href="/profile">Profile</a>
          </li> */}
          <li>
            <a href="/matches">Requests</a>
          </li>
        </ul>
      </div>

      <div className="main-content">
        <div className="profile-section">
          <div className="profile-picture">
            <img src={require('../../Components/images.jpg')} alt="Profile" width="200" height="200" />
          </div>
          <div className="profile-details">
            <h2 className="title">{profileData.name}</h2>
            <p>{profileData.email}</p>
            <div className="item-tile">
            <p>Skill-hours left: 5</p>
            </div>
            
          </div>
        </div>


        <div className="item-list-container">
        <h3>My Skills:</h3>
          <div className="item-list">
            <div className="item-tile">
              <h5>{profileData.card1.title}</h5>
              <h6>{profileData.card1.description}</h6>
            </div>

            <div className="item-tile">
              <h5>{profileData.card2.title}</h5>
              <h6>{profileData.card2.description}</h6>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProfilePage;
