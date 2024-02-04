// // Home.js
// Home.js
import React, { useCallback, useEffect, useState } from 'react';
import { useHistory } from 'react-router-dom';
import './Home.css';
import axios from 'axios';
import Popup from '../../Components/Popup/Popup';

const Home = () => {
  const [items, setItems] = useState();
  const [isLoading, setIsLoading] = useState(false);
  const [showPopup, setShowPopup] = useState(false);
  const history = useHistory();

  const handleLogOut = () => {
    history.push("/login");
    localStorage.removeItem("token");
  }

  const getUserStudyJourney = useCallback(async () => {
    setIsLoading(true);
    try {
      const response = await axios.get("http://127.0.0.1:5000/users/requests", {
        headers : {
          "Authorization" : "Bearer " + localStorage.getItem("token")
        }
      });
      if(response && response.status >= 200){
        console.log(response.data);
        setItems(response.data);
      }
    } catch (error) {
      console.error("Error fetching data:", error);
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    getUserStudyJourney();
  }, []);

  const handleRequestSubmit = async (formData) => {
    try {
      const response = await axios.post("http://127.0.0.1:5000/requests", {
        "title": formData.title,
        "description": formData.description,
      }, {
        headers: {
          "Authorization" : "Bearer " + localStorage.getItem("token")
        }
      });
      if(response && response.status === 200 && response.data){
        console.log("Submitted ", response.data);
        getUserStudyJourney();
      }
    } catch (error) {
      console.error("Error submitting request:", error);
    } finally {
      setShowPopup(false);
    }
  }

  const handleRequestForm = () => {
    setShowPopup(true);
  }

  const handlePopupClose = () => {
    setShowPopup(false);
  }

  const handleRequestSend = async (item) => {
    const response = await axios.post("http://127.0.0.1:5000/requests", {
      // "title": formData.title,
      // "description": formData.description,
    }, {
      headers: {
        "Authorization" : "Bearer " + localStorage.getItem("token")
      }
    });
    if(response && response.status === 200 && response.data){
      console.log("Submitted ", response.data);
      getUserStudyJourney();
  }
}

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

      {/* Main Content */}
      <div className="main-content">
        <button onClick={handleRequestForm}> Add Request + </button>
        {/* List of Items in Rectangular Tiles */}
        <h1 className="title">Study Journey</h1>
        <div className="item-list">
          {isLoading && <div>Loading...</div>}
          {items ? items.map((item, index) => (
            <div className="item-tile" key={index}>
              <b> {item.title}</b>
              <p>{item.description}</p>
              <p className="req_id"><a href={`#id${index + 1}`}>ID {index + 1}</a></p>
              <button onClick={() => handleRequestSend(item)}>Request</button>
            </div>
          )) :
          <div>
            <span>Start your Journery with the First Request!!!</span>
          </div>
          }
        </div>
      </div>

      {/* Popup Component */}
      {showPopup && <Popup callback={handleRequestSubmit} onClose={handlePopupClose}/>}

    </div>
  );
};

export default Home;
