import React, { useEffect, useState } from 'react';
import './Profile.css'; // Import your CSS file
import { useHistory } from 'react-router-dom';
import axios from 'axios';

const ProfilePage = () => {
  const [profileData, setProfileData] = useState([]);

  const getProfileData = async () => {
    const response = await axios.get(`http://127.0.0.1:5000/user_profile`, {
      headers: {
        "Authorization" : "Bearer " + localStorage.getItem("token")
      }
    });
    if(response && response.status >= 200){
      console.log("Submitted ", response.data);
      setProfileData(response.data);
    }
  };

  useEffect(() => {
    getProfileData();
  }, []);

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
          <li>
            <a href="/profile">Profile</a>
          </li>
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
            <p>{profileData.description}</p>
            <div className="item-tile">
            <p>Skill-hours left: {profileData.skill_hours ? profileData.skill_hours : 5}</p>
            </div>
            
          </div>
        </div>


        <div className="item-list-container">
        <h3>My Skills:</h3>
        {profileData.want_to_teach &&  profileData.want_to_teach.length > 0 ? profileData.want_to_teach.map((item, index) => (
                <div key ={index} className="item-list">
                <div className="item-tile">
                <h6>{item.description}</h6>
                </div>
                </div>
              ))
            :
            <div>
              <p>Learn more and add skills !!!</p>
              </div>
            }
          </div>
        </div>
      </div>

  );
};

export default ProfilePage;
