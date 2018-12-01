import React, { Component } from 'react';
import Sidebar from './Sidebar';
import Simulation from './Simulation';

class Home extends Component {
    render() {
        return (
            <div>
                <Sidebar/>
                <Simulation/>
            </div>
        );
    }
}

export default Home;