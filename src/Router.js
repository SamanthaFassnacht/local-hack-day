import React, { Component } from 'react';
import { BrowserRouter, Route } from 'react-router-dom';
import Home from './Home';
import AboutIdea from './AboutIdea';
import AboutUs from './AboutUs';

class MainContent extends Component {
    render() {
        return (       
            // <BrowserRouter>
            //     <Route exact path="/" Component={Home}/>
            //     <Route exact path="/aboutIdea" Component={AboutIdea}/>
            //     <Route exact path="/aboutUs" Component={AboutUs}/>
            // </BrowserRouter>
            <div></div>
        );
    }
}

export default MainContent;