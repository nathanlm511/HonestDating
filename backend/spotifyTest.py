import spotipy
from spotipy.oauth2 import SpotifyPKCE
from pprint import pprint

scopes = 'user-top-read user-read-recently-played user-library-read'
scope = 'user-top-read'
client_id = '0c1a35c79618447692fcff61d67e2999'
client_secret = 'af8e5e8deddd4d80b930f7cd91fdf0de'
# redirect_uri = 'https://localhost:8888/callback'
redirect_uri = 'http://127.0.0.1:9090/callback'
# auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scopes)
auth_manager = SpotifyPKCE(client_id=client_id, redirect_uri=redirect_uri, scope=scopes)
sp = spotipy.Spotify(auth_manager=auth_manager)
# sp = spotipy.Spotify(auth_manager=SpotifyPKCE(client_id=client_id, redirect_uri=redirect_uri, scope=scope, username=spotifyUsername))
# print(sp.current_user())
# print(sp.user(spotifyUsername))
uri = sp.track(sp.current_user_top_tracks()['items'][0]['id'])['uri']
features = sp.audio_features(uri)[0]
pprint(features)

# def getArtistInfoFromId(artist_id):
#     data = sp.artist(artist_id)
#     relevantData = {}
#     relevantData['artistname'] = data['name']
#     relevantData['image_url'] = data['images'][0]['url']
#     return relevantData
    
# top_artists = sp.current_user_top_artists(limit=5)
# print(top_artists)
# artist_ids = []
# for artist in top_artists['items']:
#     artist_ids.append(artist['id'])
# top_artists_info = []
# for artist_id in artist_ids:
#     top_artists_info.append(getArtistInfoFromId(artist_id))
# print(top_artists_info)

# long_term_top_track = sp.current_user_top_tracks(limit=1, offset=0, time_range="long_term")
# top_track = long_term_top_track['items'][0]
# data = sp.track(top_track['id'])
# relevantData = {}
# relevantData['songname'] = data['name']
# relevantData['album'] = data['album']['name']
# relevantData['artist'] = data['album']['artists'][0]['name']
# relevantData['spotify_url'] = data['external_urls']['spotify']
# relevantData['album_cover'] = data['album']['images'][0]['url']
# print(relevantData)
# ranges = ['short_term', 'medium_term', 'long_term']

# for sp_range in ranges:
#     print("range:", sp_range)
#     results = sp.current_user_top_tracks(time_range=sp_range, limit=50)
#     for i, item in enumerate(results['items']):
#         print(i, item['name'], '//', item['artists'][0]['name'])
#     print()
