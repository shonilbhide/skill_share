import React, { useState } from 'react';

function InputForm({ callback }) {
    const [formData, setFormData] = useState({ title: '', description: '' });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        callback(formData);
    };

    return (
        <div style={{ width: '400px', margin: 'auto', marginTop: '50px' }}>
            <h2 style={{ textAlign: 'center' }}>Input Form</h2>
            <form onSubmit={handleSubmit}>
                <div style={{ marginBottom: '20px' }}>
                    <label>Title:</label>
                    <input
                        type="text"
                        name="title"
                        value={formData.title}
                        onChange={handleChange}
                        style={{ width: '100%', padding: '8px', borderRadius: '4px', border: '1px solid #ccc' }}
                        required
                    />
                </div>
                <div style={{ marginBottom: '20px' }}>
                    <label>Description:</label>
                    <textarea
                        name="description"
                        value={formData.description}
                        onChange={handleChange}
                        style={{ width: '100%', padding: '8px', borderRadius: '4px', border: '1px solid #ccc' }}
                        rows="4"
                        required
                    ></textarea>
                </div>
                <button
                    type="submit"
                    style={{ backgroundColor: '#007bff', color: '#fff', padding: '10px 20px', borderRadius: '4px', border: 'none', cursor: 'pointer' }}
                >
                    Submit
                </button>
            </form>
        </div>
    );
}

export default InputForm;
