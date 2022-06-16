"""연습하는 부분입니다."""
"""
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = 'user-library-read'


def show_tracks(results):
    for item in results['items']:
        track = item['track']
        print("%32.32s %s" % (track['artists'][0]['name'], track['name']))


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
show_tracks(results)

while results['next']:
    results = sp.next(results)
    show_tracks(results)
---
import spotipy
from spotipy.oauth2 import SpotifyOAuth

song_list = {}
song_list['tracks'] = []

scope = 'user-read-recently-played'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
results = sp.current_user_recently_played(limit=50)
for i, item in enumerate(results['items']):
    print(item['played_at'], item['track']['name'])
---
    song_id = item['track']['id']
    features = sp.audio_features(song_id)

    album = item['track']['album']['name']
    album_id = item['track']['album']['id']
    artist = item['track']['artists'][0]['name']
    artist_id = item['track']['artists'][0]['id']
    song = item['track']['name']

    acousticness = features[0]["acousticness"]
    danceability = features[0]["danceability"]
    energy = features[0]["energy"]
    liveness = features[0]["liveness"]
    loudness = features[0]["loudness"]
    instrumentalness = features[0]["instrumentalness"]
    valence = features[0]["valence"]
    speechiness = features[0]["speechiness"]
    tempo = features[0]["tempo"]
    mode = features[0]["mode"]
    duration = features[0]["duration_ms"]
    popularity = item['track']['popularity']

    result = {"album" : {"album_id" : album_id,
                        "name" : album},
            "artist" : {"artist_id" : artist_id,
                        "name" :artist},
            "song" : {"song_id" : song_id,
                        "name" : song,
                        "acousticness" : acousticness,
                        "danceability" : danceability,
                        "energy" : energy,
                        "liveness" : liveness,
                        "loudness" : loudness,
                        "instrumentalness" : instrumentalness,
                        "speechiness" : speechiness,
                        "tempo" : tempo,
                        "valence" : valence,
                        "duration(ms)" : duration,
                        "mode" : mode,
                        "popularity" : popularity}}
    song_list['tracks'].append(result)
aa = len(song_list['tracks'])
print(song_list['tracks'][0])
import pandas as pd
import sqlite3
con = sqlite3.connect('./resent.db')
cur = con.cursor()
cur.execute('SELECT "album.image", "artist.name", "song.name" FROM test t ORDER BY predict LIMIT 3')
df1 = pd.DataFrame(cur.fetchall(), columns=['image','artist', 'name'])
cur.execute('SELECT "album.image", "artist.name", "song.name" FROM test t ORDER BY predict DESC LIMIT 3')
df2 = pd.DataFrame(cur.fetchall(), columns=['image','artist', 'name'])
a = [df1['image'][0], df1['image'][1], df1['image'][2]]
print(a[0])
import joblib
import numpy as np
import spotipy
from spotipy.oauth2 import SpotifyOAuth


scope = 'user-read-recently-played'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

rf_from_joblib = joblib.load('filename.pkl') 

song_list={}
song_list['tracks'] = []
results = sp.current_user_recently_played(limit=1)
a = results['items'][0]['track']['preview_url']
print(a)
"""
NYWKIM=$NYWKIM