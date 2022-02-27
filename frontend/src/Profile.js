import './Profile.css';
import { Component } from 'react'

class Profile extends Component {

  constructor() {
    super();
    window.addEventListener("scroll", this.reveal);
    window.addEventListener("scroll", this.reveal_small);
    window.addEventListener("scroll", this.reveal_smaller);
    window.addEventListener("scroll", this.reveal_smallest);
    window.addEventListener("scroll", this.reveal_spotify);
    this.test_json = JSON.parse(window.localStorage.getItem("data"));
  }

  reveal() {
    var reveals = document.querySelectorAll(".reveal");
    for (var i = 0; i < reveals.length; i++) {
      var windowHeight = window.innerHeight;
      var elementTop = reveals[i].getBoundingClientRect().top;
      var elementVisible = -30;
      if (elementTop < windowHeight - elementVisible) {
        reveals[i].classList.add("active");
      } else {
        reveals[i].classList.remove("active");
      }
    }
  }
  
  reveal_small() {
    var reveals = document.querySelectorAll(".reveal-small");
    for (var i = 0; i < reveals.length; i++) {
      var windowHeight = window.innerHeight;
      var elementTop = reveals[i].getBoundingClientRect().top;
      var elementVisible = 200;
      if (elementTop < windowHeight - elementVisible) {
        reveals[i].classList.add("active-small");
      } else {
        reveals[i].classList.remove("active-small");
      }
    }
  }
  
  reveal_smaller() {
    var reveals = document.querySelectorAll(".reveal-smaller");
    for (var i = 0; i < reveals.length; i++) {
      var windowHeight = window.innerHeight;
      var elementTop = reveals[i].getBoundingClientRect().top;
      var elementVisible = 200;
      if (elementTop < windowHeight - elementVisible) {
        reveals[i].classList.add("active-smaller");
      } else {
        reveals[i].classList.remove("active-smaller");
      }
    }
  }
  
  reveal_smallest() {
    var reveals = document.querySelectorAll(".reveal-smallest");
    for (var i = 0; i < reveals.length; i++) {
      var windowHeight = window.innerHeight;
      var elementTop = reveals[i].getBoundingClientRect().top;
      var elementVisible = 200;
      if (elementTop < windowHeight - elementVisible) {
        reveals[i].classList.add("active-smallest");
      } else {
        reveals[i].classList.remove("active-smallest");
      }
    }
  }
  
  reveal_spotify() {
    var reveals = document.querySelectorAll(".reveal-spotify");
    for (var i = 0; i < reveals.length; i++) {
      var windowHeight = window.innerHeight;
      var elementTop = reveals[i].getBoundingClientRect().top;
      var elementVisible = 30;
      if (elementTop < windowHeight - elementVisible) {
        reveals[i].classList.add("active-spotify");
      } else {
        reveals[i].classList.remove("active-spotify");
      }
    }
  }

  render() {
    return (
      <div className="profile-window">
          <div className="profile-header"> 
            <img src={this.test_json.user_pfp.file} className="profile-image"></img>
            <div className="bio-container">
              <div className="bio-card">
                <div className="bio-name">{this.test_json.name.first + " " + this.test_json.name.last}</div>
                <div className="bio">{this.test_json.twitter.tweets[0].text}</div>
                <div className="tinder-button-container">
                  <div className="tinder-button green">
                    <div className="like-image"></div>
                  </div>
                  <div className="tinder-button-spacer"></div>
                  <div className="tinder-button red">
                    <div className="dislike-image"></div>
                    </div>
                </div>
              </div>
            </div>
          </div>
          <div className="page-spacer"></div>
          <div className="instagram-page"> 
            <div className="instagram-logo-container">
              <div className="instagram-logo"></div>
              <div className="instagram-description">Scraped from your instagram using instapy!</div>
            </div>
            <div className="instagram-card reveal">
              <div className="instagram-card-header">A trip through time</div>
              <div className="instagram-card-container">
                <div className="instagram-card-photo-container">
                  <img src={this.test_json.insta.images[0].file} className="instagram-card-photo"></img>
                  <div className="instagram-card-subtitle">First post ever!</div>
                </div>
                <div className="instagram-card-photo-container">
                  <div className="instagram-card-photo"></div>
                  <div className="instagram-card-subtitle">Most recent post</div>
                </div>
              </div>
            </div>
          </div>
          <div className="random-window">
            <div className="random-header-row">
              <div className="random-header">Take a peek</div>
              <div className="random-subheader">A sneakpeek at 3 random images from their feed.</div>
            </div>
            <div className="random-container">
              <div className="random-photo-container reveal-small">
                <div className="random-photo"></div>
                <div className="random-square"></div>
              </div>              
              <div className="random-photo-container jig reveal-smallest">
                <div className="random-photo"></div>
                <div className="random-square"></div>
              </div>              
              <div className="random-photo-container reveal-smaller">
                <div className="random-photo"></div>
                <div className="random-square"></div>
              </div>
            </div>
          </div>
          <div className="twitter-window">
            <div className="twitter-text-container">
              <div className="twitter-text-header">Twitter Grab Bag</div>
              <div className="twitter-text-subtitle">What kinds of things do you say?</div>
              <div className="tweet tweet-1">
                <div className="tweet-header-row">
                  <div className="tweet-name">Most liked</div>
                  <div className="tweet-verified"></div>
                  <div className="tweet-sub-name">@MostLiked • 7m</div>
                </div>
                <div className="tweet-text">
                  {this.test_json.twitter.tweets[0].text}
                </div>
              </div>
              <div className="tweet tweet-2">
                <div className="tweet-header-row">
                  <div className="tweet-name">Random Tweet</div>
                  <div className="tweet-verified"></div>
                  <div className="tweet-sub-name">@RandomTweet • 2d</div>
                </div>
                <div className="tweet-text">
                  {this.test_json.twitter.tweets[1].text}
                </div>
              </div>
              <div className="tweet tweet-3">
                <div className="tweet-header-row">
                  <div className="tweet-name">Random Tweet</div>
                  <div className="tweet-verified"></div>
                  <div className="tweet-sub-name">@RandomTweet • 3h</div>
                </div>
                <div className="tweet-text">
                  {this.test_json.twitter.tweets[2].text}
                </div>
              </div>
              <div className="tweet tweet-4">
                <div className="tweet-header-row">
                  <div className="tweet-name">Random Tweet</div>
                  <div className="tweet-verified"></div>
                  <div className="tweet-sub-name">@RandomTweet • 46m</div>
                </div>
                <div className="tweet-text">
                  {this.test_json.twitter.tweets[3].text}
                </div>
              </div>
              <div className="tweet tweet-5">
                <div className="tweet-header-row">
                  <div className="tweet-name">FirstTweet</div>
                  <div className="tweet-verified"></div>
                  <div className="tweet-sub-name">@FirstTweet • 131d</div>
                </div>
                <div className="tweet-text">
                  {this.test_json.twitter.tweets[4].text}
                </div>
              </div>
              <div className="twitter-text"></div>
            </div>
            <div className="twitter-num-container">
              <div className="twitter-data-container">
                <div className="twitter-number">85</div>
                <div className="twitter-number-cir"></div>
                <div className="twitter-number-desc">Twitter friends</div>
              </div>
              <div className="twitter-data-container jag">
                <div className="twitter-number">13</div>
                <div className="twitter-number-cir"></div>
                <div className="twitter-number-desc">Retweets</div>
              </div>
              <div className="twitter-data-container">
                <div className="twitter-number">90</div>
                <div className="twitter-number-cir"></div>
                <div className="twitter-number-desc">Likes on most-liked post</div>
              </div>
              <div className="twitter-data-container jag">
                <div className="twitter-number">5</div>
                <div className="twitter-number-cir"></div>
                <div className="twitter-number-desc">Total tweets</div>
              </div>
            </div>
          </div>
          <svg className="wave" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="#e0efe3" fill-opacity="1" d="M0,128L34.3,138.7C68.6,149,137,171,206,160C274.3,149,343,107,411,122.7C480,139,549,213,617,218.7C685.7,224,754,160,823,133.3C891.4,107,960,117,1029,144C1097.1,171,1166,213,1234,224C1302.9,235,1371,213,1406,202.7L1440,192L1440,320L1405.7,320C1371.4,320,1303,320,1234,320C1165.7,320,1097,320,1029,320C960,320,891,320,823,320C754.3,320,686,320,617,320C548.6,320,480,320,411,320C342.9,320,274,320,206,320C137.1,320,69,320,34,320L0,320Z"></path></svg>
          <div className="spotify-window">
            <div className="spotify-logo"></div>
            <div className="spotify-header">Musical Personality</div>
            <div className="spotify-container">
              <div className="spotify-column">
                <div className="spotify-section-header">Favorite Songs</div>
                <div className="spotify-section-container reveal-spotify">
                  <img src={this.test_json.spotify.top_recent_songs[0].album_url} className="spotify-section-image"></img>
                  <div className="spotify-section-text">{this.test_json.spotify.top_recent_songs[0].song}</div>
                </div>
                <div className="spotify-section-container reveal-spotify">
                  <img src={this.test_json.spotify.top_recent_songs[1].album_url} className="spotify-section-image"></img>
                  <div className="spotify-section-text">{this.test_json.spotify.top_recent_songs[1].song}</div>
                </div>
                <div className="spotify-section-container reveal-spotify">
                  <img src={this.test_json.spotify.top_recent_songs[2].album_url} className="spotify-section-image"></img>
                  <div className="spotify-section-text">{this.test_json.spotify.top_recent_songs[2].song}</div>
                </div>
                <div className="spotify-section-container reveal-spotify">
                  <img src={this.test_json.spotify.top_recent_songs[3].album_url} className="spotify-section-image"></img>
                  <div className="spotify-section-text">{this.test_json.spotify.top_recent_songs[3].song}</div>
                </div>
                <div className="spotify-section-container reveal-spotify">
                  <img src={this.test_json.spotify.top_recent_songs[4].album_url} className="spotify-section-image"></img>
                  <div className="spotify-section-text">{this.test_json.spotify.top_recent_songs[4].song}</div>
                </div>
              </div>
              <div className="spotify-column jig">
                <div className="spotify-section-header">Favorite Artists</div>
                <div className="spotify-section-container reveal-spotify">
                  <img src={this.test_json.spotify.top_artists[0].num_listens} className="spotify-section-image"></img>
                  <div className="spotify-section-text">{this.test_json.spotify.top_artists[0].artist}</div>
                </div>
                <div className="spotify-section-container reveal-spotify">
                  <img src={this.test_json.spotify.top_artists[1].num_listens} className="spotify-section-image"></img>
                  <div className="spotify-section-text">{this.test_json.spotify.top_artists[1].artist}</div>
                </div>
                <div className="spotify-section-container reveal-spotify">
                  <img src={this.test_json.spotify.top_artists[2].num_listens} className="spotify-section-image"></img>
                  <div className="spotify-section-text">{this.test_json.spotify.top_artists[2].artist}</div>
                </div>
                <div className="spotify-section-container reveal-spotify">
                  <img src={this.test_json.spotify.top_artists[3].num_listens} className="spotify-section-image"></img>
                  <div className="spotify-section-text">{this.test_json.spotify.top_artists[3].artist}</div>
                </div>
                <div className="spotify-section-container reveal-spotify">
                  <img src={this.test_json.spotify.top_artists[4].num_listens} className="spotify-section-image"></img>
                  <div className="spotify-section-text">{this.test_json.spotify.top_artists[4].artist}</div>
                </div>
              </div>
                {/*
              <div className="spotify-column-center">
                <div className="spotify-section-header left">Musical Energy</div>
                commented out because its ugly lol
                <div className="energy-bar">
                  <div className="energy-bar-empty" style={{height: 50 + "%"}}></div>
                  <div className="energy-bar-green" style={{height: 50 + "%"}}>
                    <div className="bar-percentage">50%</div>
                  </div>
                </div>
              </div>
                */}
            </div>
          </div>
      </div>
    );
  }
}

export default Profile;
