import React, { Component } from 'react';
import Nav from './Nav';
import MainContent from './MainContent';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Nav></Nav>
        <MainContent></MainContent>
      </div>
    );
  }
}

export default App;
