from encodings import utf_8
import sys
import pymongo
import glob
import datetime
from PIL import Image
import numpy as np
from bson.json_util import dumps
import bson

def setup_connection(file_name):
    global connection
    global client
    global db
    global users

    connection = open(file_name).readline()
    client = pymongo.MongoClient(connection)
    db = client.db
    users = db.users

def example_user():
    create_user("Rushia", "Uruha", "https://pbs.twimg.com/profile_images/1485036871826952192/rfqIJ2W0_400x400.jpg", 2000)

    create_spotify_info("Rushia", "Uruha", "uruharushia", "Anime")
    create_user_twitter_info("Rushia", "Uruha", "uruharushia")
    create_user_instagram_info("Rushia", "Uruha", "uruharushia")

    add_tweet_to_user("Rushia", "Uruha", "i miss rushia", 4567, 43576)
    add_image_to_user("Rushia", "Uruha", "https://pbs.twimg.com/profile_images/1485036871826952192/rfqIJ2W0_400x400.jpg", 54356)
    add_video_to_user("Rushia", "Uruha", "https://www.youtube.com/watch?v=iDas_CFy1Rs", 23457)
    add_favorite_song("Rushia", "Uruha", "iya iya iya", 214354, 4258)
    add_top_recent_songs("Rushia", "Uruha", "iya iya iya", 10000000, 4567)
    add_top_artists("Rushia", "Uruha", "Ninomae Ina'nis", "https://www.youtube.com/channel/UCMwGHR0BTZuLsmjY_NT5Pwg")
    
    

def create_user(first_name, last_name, user_img_link, age):
    global users

    personDocument = {
        "name": 
        { 
            "first": first_name, 
            "last": last_name 
        },
        "age": age,
        "user_pfp" : user_img_link,
        "twitter": {},
        "insta": {},
        "spotify": {}
    }
    users.insert_one(personDocument)

def get_basic_user_info(first_name, last_name):
    global users

    return dumps(users.find_one({"name" : {"first" : first_name, "last" : last_name}}, {"_id" : 0, "name" : 1, "age" : 1, "user_pfp" : 1}))

def get_all_user_info(first_name, last_name):
    global users

    return dumps(users.find_one({"name" : {"first" : first_name, "last" : last_name}}))

def create_spotify_info(first_name, last_name, user, top_genre):
    global users

    users.find_one_and_update({"name" : {"first" : first_name, "last" : last_name}}, 
    { "$set" : 
        { "spotify": 
            {
                "user": user,
                "fav_song" : {},
                "top_recent_songs": [],
                "top_artists": [], 
                "top_genre": top_genre
            }
        }
    })

def add_favorite_song(first_name, last_name, name, album_url, energy):
    global users

    users.find_one_and_update({"name" : {"first" : first_name, "last" : last_name}}, 
    { "$set" : 
        { "spotify.fav_song": 
            { 
                "song": name,
                "album_url" : album_url,
                "energy": energy
            }
        }
    })

def add_top_recent_songs(first_name, last_name, song, album_url, energy_level):
    global users

    users.find_one_and_update({"name" : {"first" : first_name, "last" : last_name}}, 
    { "$push" : 
        { "spotify.top_recent_songs": 
            {
                "song": song,
                "album_url" : album_url,
                "energy_level" : energy_level
            }
        }
    })

def add_top_artists(first_name, last_name, artist, artist_link):
    global users

    users.find_one_and_update({"name" : {"first" : first_name, "last" : last_name}}, 
    { "$push" : 
        { "spotify.top_artists": 
            {
                "artist": artist,
                "num_listens" : artist_link
            }
        }
    })

def get_spotify_json(first_name, last_name):
    global users

    return dumps(users.find_one({"name" : {"first" : first_name, "last" : last_name}}, {"_id" : 0, "spotify" : 1}))
    
def create_user_twitter_info(first_name, last_name, twitter_handle):
    global users

    users.find_one_and_update({"name" : {"first" : first_name, "last" : last_name}}, 
    { "$set" : 
        { "twitter": 
            {
                "user": twitter_handle,
                "tweets" : []
            }
        }
    })


def add_tweet_to_user(first_name, last_name, tweet):
    global users

    users.find_one_and_update({"name" : {"first" : first_name, "last" : last_name}}, 
    {"$push" : 
        {
            "twitter.tweets" : 
            {
                "text" : tweet
            }
        }    
    })

def get_all_twitter_info(first_name, last_name):
    global users

    return dumps(users.find_one({"name" : {"first" : first_name, "last" : last_name}}, {"_id" : 0, "twitter" : 1}))

def get_all_tweets_from_user(first_name, last_name):   
    global users

    tweet_array = users.find_one({"name" : {"first" : first_name, "last" : last_name}}, {"_id" : 0, "twitter" : 1})
    return dumps(tweet_array['twitter']['tweets'])

def create_user_instagram_info(first_name, last_name, user): 
    global users

    users.find_one_and_update({"name" : {"first" : first_name, "last" : last_name}}, 
    { "$set" : 
        { "insta": 
            {
                "user": user,
                "images" : [],
                "videos" : []
            }
        }
    })

def add_image_to_user(first_name, last_name, image_link, likes):
    global users

    users.find_one_and_update({"name" : {"first" : first_name, "last" : last_name}}, 
    {"$push" : 
        {
            "insta.images" : 
            {
                "file" : image_link,
                "likes" : likes,
            }
        }
    })

def add_video_to_user(first_name, last_name, video_link, likes):
    global users

    users.find_one_and_update({"name" : {"first" : first_name, "last" : last_name}}, 
    {"$push" : 
        {
            "insta.videos" : 
            {
                "file" : video_link,
                "likes" : likes,
            }
        }    
    })

def get_insta_files_from_user(first_name, last_name, file_type):
    global users

    image_array = users.find_one({"name" : {"first" : first_name, "last" : last_name}}, {"_id" : 0, "insta" : 1})
    image_names = []

    for entry in image_array['insta'][file_type]:
        image_names.append(entry['file'])
    
    return dumps(image_names)

#setup_connection("connection.txt")
#example_user()
