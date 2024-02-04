import './App.css';
import SignUpPage from './Pages/Login/SignUpPage';
import LoginPage from './Pages/Login/LoginPage';
import HomePage from './Pages/Home/HomePage';
import ProfilePage from './Pages/Profile/ProfilePage';
import MatchedPage from './Pages/Matched/MatchedPage';
import React from 'react';
import { Route, BrowserRouter as Router, Switch } from "react-router-dom";
import ProtectedRoute from './Components/ProtectedRoute';

function App() {
    return (
        <Router>
            <Switch>
                <Route path="/" component={LoginPage} exact></Route>
                <Route path="/login" component={LoginPage}></Route>
                <Route path="/signup" component={SignUpPage}></Route>
                <ProtectedRoute path="/home" component={HomePage}></ProtectedRoute>
                <ProtectedRoute path="/profile" component={ProfilePage}></ProtectedRoute>
                <ProtectedRoute path="/matches" component={MatchedPage}></ProtectedRoute>
            </Switch>
        </Router>
    );
}

export default App;
