import React, { Component } from 'react';

class Home extends Component {
    constructor(props){
        super(props);
        this.state = {
            playing: true,
            earthXPos: [],
            earthYPos: [],
            marsXPos: [],
            marsYPos: [],
            currEarthPos: 0,
            currMarsPos: 0
        };
        this.orbit = this.orbit.bind(this);
        this.getEarthOrbitData = this.getEarthOrbitData.bind(this);
        this.getMarsOrbitData = this.getMarsOrbitData.bind(this);
    }

    componentDidMount() {
        getEarthOrbitData();
        getMarsOrbitData();

        var elem = document.getElementById('simulation');
        var params = { width: 800, height: 500, autoplay: true};
        var two = new window.Two(params).appendTo(elem);

        // two has convenience methods to create shapes.
        var sun = two.makeCircle(400, 250, 50);
        var earth = two.makeCircle(200, 250, 30);

        sun.fill = '#FF8000';
        sun.stroke = 'orangered';
        sun.linewidth = 2;

        earth.fill = '#194878';
        earth.opacity = 0.75;
        earth.noStroke();

        two.bind("update", this.orbit);
        
        two.update();
        two.play();
        this.state.playing = true;
    }

    startAnimation() {
        if(!this.state.playing) {
            console.log("Hi");
        }
    }

    stopAnimation() {
        if(this.state.playing) {
            console.log("Hi");
        }
    }

    orbit = () => {
        if(this.state.earthXPos.length - this.state.currEarthPos > 50) {
            
        } else {
            console.log("Need new call here!");
        }
        if(this.state.marsXPos.length - this.state.currMarsPos > 50) {

        }
    }

    getEarthOrbitData = () => {

    }

    getMarsOrbitData = () => {
        
    }

    render() {
        return (
            <div>
                <div id = "sidebar">
                    <h1>Simulation Controls</h1>
                    <h2>Orbit Controls</h2>
                    <button type="button" onClick="startAnimation">Start</button>
                    <button type="button" onClick="stopAnimation">Pause</button>
                    <h2>Flight Pattern</h2>
                    <h3>From:</h3>
                    <h3>Destination:</h3>
                    <h3>Flight Mode:</h3>
                    <h2>Flight Details</h2>
                </div>
                <div id="simulation-area">
                    <div id="simulation">
                    </div>
                </div>
            </div>
        );
    }
}

export default Home;