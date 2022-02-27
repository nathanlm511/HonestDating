from pprint import pprint
import instagram_scraper

class instaScraper():
    def __init__(self, username="", password="", scrapeUser=""):
        self.args = {"login_user": username, "login_pass": password, "cookiejar":"insta_cookies.txt"}
        self.scrapeUsername = scrapeUser
    
    def setAccountInfo(self, username, password):
        self.args = {"login_user": username, "login_pass": password}
    
    def setUserToScrape(self, scrapeUser):
        self.scrapeUsername = scrapeUser

    def getUserImages(self):
        insta_scraper = instagram_scraper.InstagramScraper(**self.args)
        insta_scraper.authenticate_with_login()
        shared_data = insta_scraper.get_shared_data_userinfo(username=self.scrapeUsername)
        
        arr = []
        cnt = 0
        for item in insta_scraper.query_media_gen(shared_data):
            arr.append(item)
            cnt += 1
            if cnt == 3:
                break

        return arr