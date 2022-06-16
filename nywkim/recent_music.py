"""해당 파일은 최근 들었던 음악 데이터를 가져오는 함수입니다."""
import joblib
import numpy as np
import spotipy
from spotipy.oauth2 import SpotifyOAuth


scope = 'user-read-recently-played'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

rf_from_joblib = joblib.load('filename.pkl') 

song_list={}
song_list['tracks'] = []
results = sp.current_user_recently_played(limit=50)
for i, item in enumerate(results['items']):
    song_id = item['track']['id']
    features = sp.audio_features(song_id)

    album = item['track']['album']['name']
    album_id = item['track']['album']['id']
    artist = item['track']['artists'][0]['name']
    artist_id = item['track']['artists'][0]['id']
    song = item['track']['name']
    image = item['track']['album']['images'][2]['url']

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
                        "name" : album,
                        "image" : image},
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

import json

file_path = "./test.json"

with open(file_path, 'w') as outfile:
    json.dump(song_list, outfile)

import pandas as pd
from pandas import json_normalize

with open(file_path, "r") as json_file:
    json_data = json.load(json_file)

df = json_normalize(json_data['tracks'])
dt = pd.DataFrame(df)
dt = dt.sample(frac=1)
new = dt.drop_duplicates(['song.song_id'], keep='first').reset_index(drop=True)
sp = new.drop(columns=['album.album_id', 'album.name', 'album.image', 'artist.artist_id', 'artist.name','song.song_id', 'song.name'], axis=1)
# print(song_list['tracks'][0])
new['predict'] = rf_from_joblib.predict_proba(sp)[:, -1]

import sqlite3

con = sqlite3.connect("./resent.db")
new.to_sql('test', con, if_exists='replace')