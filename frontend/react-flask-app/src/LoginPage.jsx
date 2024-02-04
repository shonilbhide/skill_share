// LoginPage.jsx

import React, { useState } from 'react';

const LoginPage = () => {
    const [formData, setFormData] = useState({
    email: '',
    password: ''
    });

    const handleChange = (field, value) => {
        setFormData({ ...formData, [field]: value });
    };

    const handleSubmit = (e) => {
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

        console.log('Login data submitted:', formData);
    };

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
        </div>

    )
};

export default LoginPage;