// SignUpPage.js

import React, { useState } from 'react';
import './SignUpPage.css'; // Import the CSS file

const SignUpPage = () => {

    const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    confirmPassword: '',
    phone: '',
    description: '',
    wantToOffer: '', // Updated to a single text area
    });

    const handleChange = (field, value) => {
        setFormData({ ...formData, [field]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        // Validation for mandatory fields
        if (
        !formData.name.trim() ||
        !formData.email.trim() ||
        !formData.password.trim() ||
        !formData.confirmPassword.trim() ||
        !formData.phone.trim() ||
        !formData.description.trim()
        ) {
            alert('One or more mandatory fields are incomplete');
            return;
        }

        // Email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(formData.email)) {
            alert('Invalid email address');
            return;
        }

        // Password matching validation
        if (formData.password !== formData.confirmPassword) {
            alert("Passwords don't match");
            return;
        }

        // Password validation
        const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,20}$/;
        if (!passwordRegex.test(formData.password)) {
            alert(
              'Password must be between 8 and 20 characters long and contain at least one uppercase letter, one lowercase letter, and one number.'
            );
            return;
        }

        console.log('Form data submitted:', formData);

    };

    return (
        <div>
          <h1>Sign Up</h1>
          <form onSubmit={handleSubmit}>
            <label>
              Name:
              <input
                type="text"
                value={formData.name}
                onChange={(e) => handleChange('name', e.target.value)}
                placeholder="John Doe"
              />
            </label>
            <br />

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

            <label>
              Confirm Password:
              <input
                type="password"
                value={formData.confirmPassword}
                onChange={(e) => handleChange('confirmPassword', e.target.value)}
              />
            </label>
            <br />

            <label>
              Phone:
              <input
                type="tel"
                value={formData.phone}
                onChange={(e) => handleChange('phone', e.target.value)}
                placeholder="xxxxxxxxxx"
              />
            </label>
            <br />

            <label>
              Description:
              <textarea
                value={formData.description}
                onChange={(e) => handleChange('description', e.target.value)}
                placeholder="About Me"
              />
            </label>
            <br />

            <label>
              Want to Offer (Optional):
              <textarea
                value={formData.wantToOffer}
                onChange={(e) => handleChange('wantToOffer', e.target.value)}
                placeholder="I am moderately proficient in swimming. I excel in Python programming."
              />
            </label>
            <br />

            <button type="submit">Submit</button>
          </form>
        </div>
    );
};

export default SignUpPage;
