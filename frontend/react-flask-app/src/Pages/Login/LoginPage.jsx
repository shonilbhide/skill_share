// LoginPage.jsx

import React, { useState } from 'react';
import axios from "axios";
import { useHistory } from "react-router-dom";

const LoginPage = () => {
    const [formData, setFormData] = useState({
    email: '',
    password: ''
    });
    const history = useHistory();

    const handleChange = (field, value) => {
        setFormData({ ...formData, [field]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        // Email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(formData.email)) {
            alert('Invalid email address');
            return;
        }

        if(!formData.email.trim() || !formData.password.trim()){
            alert('One or more mandatory fields are incomplete');
            return;
        }
        let response = await axios
        .post("http://127.0.0.1:5000/users/login", {
            email: formData.email.trim(),
            password: formData.password.trim()
        });
        if (response && response.status === 200 && response.data){
            localStorage.setItem('token', response.data.access_token);
            history.push("/home");
        }
        console.log('Login data submitted:', formData);
    };

    const handleSingUp =() => {
        history.push("/signup");
    }

    return (
        <div>
          <div className="banner">
            <h1>Skill Share</h1>
          </div>
            <h1>Login</h1>
            <form onSubmit={handleSubmit}>
                <label>
                    Email:
                    <input
                        type="email"
                        value={formData.email}
                        onChange={(e) => handleChange('email', e.target.value)}
                        placeholder="johndoe@email.com"
                    />
                </label>
                <br />

                <label>
                    Password:
                    <input
                        type="password"
                        value={formData.password}
                        onChange={(e) => handleChange('password', e.target.value)}
                    />
                </label>
                <br />

                <button type="submit">Submit</button>
            </form>
            <button  onClick={handleSingUp}>Sign UP</button>
        </div>

    )
};

export default LoginPage;
