import './EnterInfo.css';
import { Component } from 'react'

const socials = ["instagram", "twitter", "spotify"];

class EnterInfo extends Component {

  constructor() {
    super();
    this.state = {
      index: 0,
      values: ["", "", ""]
    }
  }

  handleBack = () => {
    this.setState({index: this.state.index - 1});
  }
  
  handleNext = () => {
    this.setState({index: this.state.index + 1});
  }

  handleDone = () => {
    window.location = "/profile";
  }
  
  handleChange = (event) => {
    let newValues = this.state.values;
    newValues[this.state.index] = event.target.value;
    this.setState({values: newValues});
  }


  render() {
    return (
      <div className="window">
          <div className="enter-info-container">
              <div className="info-input-container">
                <div className={"info-logo " + socials[this.state.index]}></div>
                <div className="info-text">Enter your {socials[this.state.index]} handle</div>
                <input className="info-input" value={this.state.values[this.state.index]} onChange={this.handleChange}></input>
              </div>
              <div className="enter-info-button-container">
                  {
                    this.state.index != 0 ? 
                    <div className="enter-info-button" onClick={this.handleBack}>Back</div>
                    :
                    <div className="enter-info-button-clear"></div>
                  }
                  {
                    this.state.index != 2 ?
                    <div className="enter-info-button" onClick={this.handleNext}>Next</div>
                    :
                    <div className="enter-info-button" onClick={this.handleDone}>Done</div>
                  }
              </div>
          </div>
      </div>
    );
  }
}

export default EnterInfo;
