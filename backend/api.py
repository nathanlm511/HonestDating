from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import honestuser
import json
import backend
from flask import Flask, request, jsonify
import json
import cv2
import pymongo
from flask_cors import CORS, cross_origin
import numpy as np
from bson.json_util import dumps

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'

users = {}

@app.route('/', methods=['GET'])
def home():
    return "<h1>Something about being true to yourself</h1><p>What's up my homies fill out these fields and get your personalized page today!</p>"

@app.route('/createuser')
def createUser(userID, firstname, lastname, twitterHandle, instaUsername, instaPassword):
    usr = honestuser.HonestUser(userID, firstName=firstname, lastName=lastname, twitterUser=twitterHandle, instaUser=instaUsername, instaPass=instaPassword)
    users[userID] = usr
    backend.setup_connection('../connection.txt')
    return json.dumps(usr)

@app.route('/scrapeall', methods=['POST'])
@cross_origin()
def scrapeAll():
    firstname = request.json["firstname"]
    lastname = request.json["lastname"]
    twitterHandle = request.json["twitterhandle"]
    instaUsername = request.json["instauser"]
    instaPassword = request.json["instapass"]
    print(f"twithandle: {twitterHandle}")
    usr = honestuser.HonestUser(0, firstName=firstname, lastName=lastname, twitterUser=twitterHandle, instaUser=instaUsername, instaPass=instaPassword)
    backend.setup_connection('../connection.txt')
    backend.create_user(usr.firstName, usr.lastName, "", 25)
    
    # Twitter
    twitInfo = usr.getTwitterInfo()
    backend.create_user_twitter_info(usr.firstName, usr.lastName, usr.twitterUser)
    for tweet in twitInfo:
        backend.add_tweet_to_user(usr.firstName, usr.lastName, tweet)
    backend.get_all_twitter_info(usr.firstName, usr.lastName)

    # Instagram
    instaInfo = usr.getInstaInfo()
    print(f"instaInfo: {instaInfo}")
    backend.add_pfp_to_user(usr.firstName, usr.lastName, instaInfo[0]['url'])

    backend.create_user_instagram_info(usr.firstName, usr.lastName, usr.instaUser)
    if len(instaInfo) > 1:
        for image in instaInfo[1:]:
            print("adding image")
            backend.add_image_to_user(usr.firstName, usr.lastName, image['url'])
    

    # Spotify
    spotInfo = usr.getSpotifyInfo()
    backend.create_spotify_info(usr.firstName, usr.lastName, usr.spotifyUsername, spotInfo['topGenres'])
    for recentSong in spotInfo['topSongs']:
        backend.add_top_recent_songs(usr.firstName, usr.lastName, recentSong['songname'], recentSong['album_cover'], spotInfo['avgSongEnergy'])
    for topArtist in spotInfo['topArtists']:
        backend.add_top_artists(usr.firstName, usr.lastName, topArtist['artistname'], topArtist['imageurl'])
    topSongAllTime = spotInfo['topSongAllTime']
    backend.add_favorite_song(usr.firstName, usr.lastName, topSongAllTime['songname'], topSongAllTime['album_cover'])
    data = backend.get_all_user_info(usr.firstName, usr.lastName)
    # print(f"backend data: {data}")
    return data

@app.route('/scrapetwitter', methods=['POST'])
def scrapeTwit(userID):
    usr = users[userID]
    twitInfo = usr.getTwitterInfo()
    backend.create_user_twitter_info(usr.firstName, usr.lastName, usr.twitterUser)
    for tweet in twitInfo:
        backend.add_tweet_to_user(usr.firstName, usr.lastName, tweet)
    backend.get_all_twitter_info(usr.firstName, usr.lastName)

    return backend.get_all_twitter_info(usr.firstName, usr.lastName)

@app.route('/scrapeinsta', methods=['POST'])
def scrapeInsta(userID):
    usr = users[userID]
    usr.getInstaInfo()
    backend.create_user_instagram_info(usr.firstName, usr.lastName, usr.instaUser)

    return backend.get_insta_files_from_user(usr.firstName, usr.lastName, 'images')

@app.route('/scrapespotify', methods=['POST'])
def scrapeSpotify(userID):
    usr = users[userID]
    spotInfo = usr.getSpotifyInfo()
    backend.create_spotify_info(usr.firstName, usr.lastName, usr.spotifyUsername)
    for recentSong in spotInfo['topSongs']:
        backend.add_top_recent_songs(usr.firstName, usr.lastName, recentSong['songname'], recentSong['album_cover'], spotInfo['avgSongEnergy'])
    for topArtist in spotInfo['topArtists']:
        backend.add_top_artists(usr.firstName, usr.lastName, topArtist['artistname'], topArtist['imageurl'])
    topSongAllTime = spotInfo['topSongAllTime']
    backend.add_favorite_song(usr.firstName, usr.lastName, topSongAllTime['songname'], topSongAllTime['imageurl'])

    return backend.get_spotify_json(usr.firstName, usr.lastName)

    
app.run()
