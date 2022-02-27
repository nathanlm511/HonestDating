import scrapeTwitter
import scrapeInsta
import scrapeSpotify
import pandas as pd
import cv2 as cv
import numpy as np
import imageDetector
import urllib
import os
import random
from pprint import pprint

class HonestUser():
    def __init__(self, userID=0, firstName="first", lastName="last", twitterUser="", twitterPass="", instaUser="", instaPass=""):
        self.userID = userID
        self.firstName = firstName
        self.lastName = lastName
        self.twitterUser = twitterUser
        self.twitterPass = twitterPass
        self.instaUser = instaUser
        self.instaPass = instaPass
        self.tScraper = scrapeTwitter.twitterScraper()
        self.iScraper = scrapeInsta.instaScraper()
        self.spotifyUsername = ""

    def setTwitterAccount(self, twitterUsername):
        self.tScraper.setAccountInfo(twitterUsername)

    def setInstaAccount(self, instaUser, instaPass, userToScrape=""):
        self.iScraper.setAccountInfo(instaUser, instaPass)
        self.iScraper.setUserToScrape(userToScrape)
        self.instaUser = instaUser
        self.instaPass = instaPass

    def getTwitterInfo(self):
        tweetData = self.tScraper.getUserTweetData()

        if len(tweetData) < 10:
            print("Not enough twitter data :(")
            return []

        bioData = {}
        bioData = tweetData.to_dict()
        randomTweetNums = []
        for i in range(0,len(bioData)):
            randomTweetNums.append(random.randint(0, len(bioData)))
        tweets = []
        for tweetNum in bioData:
            if tweetNum in randomTweetNums:
                tweets.append(bioData[tweetNum])
        return tweets

    def getInstaInfo(self, debug=False):
        iDetector = imageDetector.ImageDetector('MobileNetSSD_deploy.prototxt.txt', 'MobileNetSSD_deploy.caffemodel')
        interesting_objects = ["aeroplane", "bicycle", "bird", "boat",
            "bus", "car", "cat", "cow", "dog", "horse", "motorbike", 
            "person", "pottedplant", "sheep", "sofa", "train"]

        instaData = self.iScraper.getUserImages()
        print(instaData)
        instaPostInfo = []
        for postNum, instaPost in enumerate(instaData):
            if instaPost['is_video'] == True:
                if debug: print("[INFO] this post is a video")
                videoInfo = {}
                if len(instaPost['urls']):
                    videoInfo['url'] = instaPost['urls'][0]
                else:
                    videoInfo['url'] = instaPost['display_url']
                videoInfo['mediaType'] = 'video'
                vid_name = 'insta_video' + str(postNum) + '.mp4'
                urllib.request.urlretrieve(videoInfo['url'], vid_name) 
                cap = cv.VideoCapture(vid_name)
                first_img = cap.read()[1]
                interesting_vid = False
                detected_objs = iDetector.detectObjects(first_img)
                for obj in detected_objs:
                    if obj in interesting_objects:
                        interesting_vid = True
                if not interesting_vid:
                    if debug: print("[INFO] uninteresting photo")
                else:
                    instaPostInfo.append(videoInfo)
            elif instaPost['is_video'] == False:
                if debug: print("[INFO] this post is a photo")
                photoInfo = {}
                if len(instaPost['urls']):
                    photoInfo['url'] = instaPost['urls'][0]
                else:
                    photoInfo['url'] = instaPost['display_url']
                photoInfo['mediaType'] = 'photo'
                photo_name = 'insta_photo' + str(postNum) + '.jpg'
                req = urllib.request.urlopen(photoInfo['url'])
                arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
                image = cv.imdecode(arr, -1)
                detected_objs = iDetector.detectObjects(image)
                interesting_photo = False
                for obj in detected_objs:
                    if obj in interesting_objects:
                        interesting_photo = True
                if not interesting_photo:
                    if debug: print("[INFO] uninteresting photo")
                else:
                    instaPostInfo.append(photoInfo)

        return instaPostInfo

    def getSpotifyInfo(self):
        sAPI = scrapeSpotify.spotifyAPI()
        self.spotifyUsername = sAPI.getUsername()
        spotifyData = {}
        spotifyData['topSongs'], spotifyData['avgSongEnergy'] = sAPI.getTopSongs(numSongs=5)
        spotifyData['topArtists'], spotifyData['topGenres'] = sAPI.getTopArtistsAndGenres(numArtists=5)
        spotifyData['topSongAllTime'] = sAPI.getTopAllTimeSong()
        return spotifyData