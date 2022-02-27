import './EnterInfo.css';
import { Component } from 'react'
import axios from 'axios';

const socials = ["", "", "instagram", "instagram", "twitter", "spotify"];
const texts = ["Enter your first name", 
              "Enter your last name", 
              "Enter your instagram username", 
              "Enter your instagram password", 
              "Enter your twitter handle", 
              "Enter your spotify username"];

class EnterInfo extends Component {

  constructor() {
    super();
    this.state = {
      index: 0,
      values: ["", "", "", "", "", ""]
    }
  }

  handleBack = () => {
    this.setState({index: this.state.index - 1});
  }
  
  handleNext = () => {
    this.setState({index: this.state.index + 1});
    console.log(this.state.values);
  }

  handleDone = () => {
    const inputs = {
      firstname: this.state.values[0],
      lastname: this.state.values[1],
      twitterHandle: this.state.values[2],
      instauser: this.state.values[3],
      instspass: this.state.values[4]
    }
    axios.post("http://localhost:5000/scrapeall", inputs)
      .then(res => {
        console.log(res.data);
      });
    // window.location = "/profile";
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
                <div className="info-text">{texts[this.state.index]}</div>
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
                    this.state.index != 5 ?
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
