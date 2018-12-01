import React, { Component } from 'react';

class Nav extends Component {
    render() {
        return (
            <div className="nav">
                <ul className="nav-left">
                    <li>logo here</li>
                    <li>Project Title Here</li>
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
