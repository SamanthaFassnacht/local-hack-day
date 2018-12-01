import React, { Component } from 'react';

class Nav extends Component {
    render() {
        return (
            <div className="nav">
                <ul className="nav-left">
                    <li><img className="logo" src="./logo.png" alt="logo, named elawn"/></li>
                    <li>Space Tour Simulator</li>
                </ul>
                <ul className="nav-right">
                    <li>About Idea</li>
                    <li>About Us</li>
                </ul>
            </div>
        );
    }
}

export default Nav;
