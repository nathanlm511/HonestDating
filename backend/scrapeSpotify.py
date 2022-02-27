# Shows the top artists for a user
import spotipy
from spotipy.oauth2 import SpotifyPKCE

class spotifyAPI():
    def __init__(self, client_id = '0c1a35c79618447692fcff61d67e2999', 
                       client_secret = 'af8e5e8deddd4d80b930f7cd91fdf0de',
                       redirect_uri = 'http://127.0.0.1:9090/callback'):
        self.SPOTIPY_CLIENT_ID = client_id
        self.SPOTIPY_CLIENT_SECRET = client_secret
        self.SPOTIPY_REDIRECT_URI = redirect_uri
        self.scopes = 'user-top-read user-read-recently-played user-library-read'
        self.ranges = ['short_term', 'long_term']
        self.auth_manager = SpotifyPKCE(client_id=client_id, redirect_uri=redirect_uri, scope=self.scopes)
        self.sp = spotipy.Spotify(auth_manager=self.auth_manager)

    def getSongInfoFromId(self, track_id):
        data = self.sp.track(track_id)
        relevantData = {}
        relevantData['songname'] = data['name']
        relevantData['album'] = data['album']['name']
        relevantData['artist'] = data['album']['artists'][0]['name']
        relevantData['album_cover'] = data['album']['images'][0]['url']
        return relevantData

    def getTopSongs(self, numSongs=1):
        shortTermTopTracks = self.sp.current_user_top_tracks(limit=numSongs, offset=0, time_range="short_term")
        track_ids = []
        for song in shortTermTopTracks['items']:
            track_ids.append(song['id'])
        topSongsInfo= []
        total_energy = 0
        for track_id in track_ids:
            topSongsInfo.append(self.getSongInfoFromId(track_id))
            track_uri = self.sp.track(track_id)['uri']
            total_energy += self.sp.audio_features(track_uri)[0]['energy']
        avgSongEnergy = total_energy / len(track_ids)
        return topSongsInfo, avgSongEnergy
    
    def getTopAllTimeSong(self):
        long_term_top_track = self.sp.current_user_top_tracks(limit=1, offset=0, time_range="long_term")
        top_track = long_term_top_track['items'][0]
        longTermTopSongInfo = self.getSongInfoFromId(top_track['id'])
        return longTermTopSongInfo

    def getArtistInfoFromId(self, artist_id):
        data = self.sp.artist(artist_id)
        relevantData = {}
        relevantData['artistname'] = data['name']
        relevantData['imageurl'] = data['images'][0]['url']
        return relevantData

    def getTopArtistsAndGenres(self, numArtists=1):
        top_artists = self.sp.current_user_top_artists(limit=numArtists)
        artist_ids = []
        for artist in top_artists['items']:
            artist_ids.append(artist['id'])
        top_artists_info = []
        top_genres = []
        for artist_id in artist_ids:
            top_artists_info.append(self.getArtistInfoFromId(artist_id))
            genres = self.sp.artist(artist_id)['genres']
            if len(genres):
                if genres[0] not in top_genres:
                    top_genres.append(genres[0])
        return top_artists_info, top_genres
    
    def getUsername(self):
        return self.sp.current_user()['id']