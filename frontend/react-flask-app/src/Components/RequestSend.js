import axios from 'axios';
import React from 'react';

function RequestSend({ requestData, callback }) {

    const handleSendRequest = async (item) => {
        console.log(requestData.req_id, item.email);
        try {
            const response = await axios.post(`http://127.0.0.1:5000/match_request/send/${requestData.req_id}/user/${item.email}`, {}, {
                headers: {
                    "Authorization": "Bearer " + localStorage.getItem("token")
                }
            });
            if (response && response.status === 200 && response.data) {
                console.log("Submitted ", response.data);
            }
        } catch (error) {
            console.error("Error submitting request:", error);
        } finally {
            callback();
        }
    }

    return (
        <div style={{ width: '400px', margin: 'auto', marginTop: '50px' }}>
            <h2 style={{ textAlign: 'center' }}>{requestData.title}</h2>
            {
                requestData.users && requestData.users.map((item, index) => (
                    <div key={index}>
                        <b> {item.name}</b>
                        <p>{item.email}</p>
                        <p className="req_id"><a href={`#id${index + 1}`}>ID {index + 1}</a></p>
                        <button onClick={() => handleSendRequest(item)}>Send Request</button>
                    </div>
                ))
            }
        </div>
    );
}

export default RequestSend;
