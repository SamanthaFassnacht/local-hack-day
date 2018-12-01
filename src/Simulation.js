import React, { Component } from 'react';

class Simulation extends Component {
    componentWillMount() {
    }
    
    componentDidMount() {
        var elem = document.getElementById('simulation');
        var params = { width: 285, height: 200 };
        var two = new window.Two(params).appendTo(elem);

        // two has convenience methods to create shapes.
        var circle = two.makeCircle(72, 100, 50);
        var rect = two.makeRectangle(213, 100, 100, 100);

        // The object returned has many stylable properties:
        circle.fill = '#FF8000';
        circle.stroke = 'orangered'; // Accepts all valid css color
        circle.linewidth = 5;

        rect.fill = 'rgb(0, 200, 255)';
        rect.opacity = 0.75;
        rect.noStroke();

        // Don't forget to tell two to render everything
        // to the screen
        two.update();
    }

    render() {
        return(
            <div id="simulation-area">
                <div id="simulation">
                    
                </div>
            </div>
        );
    }
}

export default Simulation;