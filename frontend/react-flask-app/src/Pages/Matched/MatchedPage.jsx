// MatchedPage.js
import React, { useEffect, useState } from 'react';
import { useHistory } from 'react-router-dom';
import './MatchedPage.css';
import axios from 'axios';

const MatchedPage = () => {
  const [matchedItems, setMatchedItems] = useState([]);
  const history = useHistory();

  const getRequestsForMe = async () => {
    const response = await axios.get(`http://127.0.0.1:5000/requests_for_user`, {
      headers: {
        "Authorization" : "Bearer " + localStorage.getItem("token")
      }
    });
    if(response && response.status >= 200){
      console.log("Submitted ", response.data);
      setMatchedItems(response.data);
    }
  };

  const handleApproveRequest = async(id) => {
    const response = await axios.post(`http://127.0.0.1:5000/request/accept/${id}`,{}, {
      headers: {
        "Authorization" : "Bearer " + localStorage.getItem("token")
      }
    });
    if(response && response.status >= 200){
      console.log("Submitted ", response.data);
      await getRequestsForMe();
    }
  }

  useEffect(() => {
    getRequestsForMe();
  }, []);

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
            <a href="/home">Home</a>
          </li>
        </ul>
      </div>

      <div className="main-content">
        <div className="item-list">
          {matchedItems &&  matchedItems.length > 0 ? matchedItems.map((item, index) => (
            <div key={index} className="item-tile">
              <div className="item-title" key={index}><b>
              {item.req_title}
              </b>
              <br />
              <p className="title">{item.req_description}</p>
              <br />
              <button onClick={() => handleApproveRequest(item.req_id)}>Accept Request</button>
              </div>
            </div>
          ))
        :
        <div>
          <p>Be Hyped to get your first teach request !!!</p>
          </div>
        }
        </div>
      </div>
    </div>
  );
};

export default MatchedPage;
