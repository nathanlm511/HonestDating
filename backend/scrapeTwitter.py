import twint
import pandas as pd
import time

class twitterScraper():   
    def __init__(self, username=""):
        self.twit = twint.Config()
        self.twit.Username = username
        print(f"twithandlehusertwscraper: {username}")
    
    def setAccountInfo(self, username):
        self.twit.Username = username

    def getUserTweetData(self, csvName="tweets.csv", searchLim=1):
        # Clear csv first
        # with open(csvName, "w+") as f:
            # f.close()
        self.twit.Search = str(self.twit.Username)
        self.twit.Limit = searchLim
        self.twit.Output = csvName
        self.twit.Hide_output = True
        self.twit.Store_csv = True
        twint.run.Search(self.twit)
        tweetData = pd.read_csv(csvName, header=None)
        return tweetData.iloc[:17,10]