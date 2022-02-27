import './Landing.css';
import { Component } from 'react'

class Landing extends Component {

  handleStart = () => {
    window.location = "/login";
  }

  render() {
    return (
      <div className="window">
          <div className="landing-title">
            Sincerely Me.
          </div>
          <div className="landing-subtitle">
            The honest dating app
          </div>
          <div className="landing-button" onClick={this.handleStart}>
            Begin
          </div>
          <div className="landing-bottom-container">
            <div className="landing-text">Created with:</div>
            <div className="tech-container">
              <div className="tech instagram"></div>
              <div className="tech pytorch"></div>
              <div className="tech flask"></div>
              <div className="tech react"></div>
              <div className="tech spotify"></div>
              <div className="tech mongo"></div>
              <div className="tech twitter"></div>
            </div>
          </div>
      </div>
    );
  }
}

export default Landing;
