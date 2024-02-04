import './App.css';
import axios from 'axios';
import SignUpPage from './SignUpPage';
import LoginPage from './LoginPage';
import HomePage from './HomePage';
import React , { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';

function App() {
    const [data, setData] = useState('');

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:5000/api/data');
                setData(response.data.message);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchData();
    }, []);

    return (
        <div className="App">
            <HomePage />
        </div>
    );
}

export default App;
