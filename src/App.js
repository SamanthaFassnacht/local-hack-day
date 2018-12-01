import React, { Component } from 'react';
import Nav from './Nav';
import Router from './Router';
import './App.css';
import Home from "./Home";

class App extends Component {
  render() {
    return (
      <div className="App">
        <Nav></Nav>
        <Router></Router>
        <Home></Home>
      </div>
    );
  }
}

export default App;
