import honestuser
import pandas as pd

user = honestuser.HonestUser("taylor", "swift")
user.setTwitterAccount("taylorswift13")
user.setInstaAccount("samschoedel", "VTHACKS9!", userToScrape="taylorswift")

# tweetData = user.getTwitterInfo()
instaData = user.getInstaInfo()
# spotifyData = user.getSpotifyInfo()

# print(tweetData)
# print(instaData)
# print(spotifyData)