from flask import Flask, render_template, request
import numpy as np
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import sqlite3

from config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET

cid = SPOTIPY_CLIENT_ID
secret = SPOTIPY_CLIENT_SECRET
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

con = sqlite3.connect('./resent.db')
cur = con.cursor()
cur.execute('SELECT "album.image", "artist.name", "song.name" FROM test t ORDER BY predict LIMIT 3')
df1 = pd.DataFrame(cur.fetchall(), columns=['image','artist', 'name'])
cur.execute('SELECT "album.image", "artist.name", "song.name" FROM test t ORDER BY predict DESC LIMIT 3')
df2 = pd.DataFrame(cur.fetchall(), columns=['image','artist', 'name'])


app = Flask(__name__)

@app.route('/')
def home():
    a = [df1['image'][0], df1['image'][1], df1['image'][2], df2['image'][0], df2['image'][1], df2['image'][2]]
    b = [df1['artist'][0], df1['artist'][1], df1['artist'][2], df2['artist'][0], df2['artist'][1], df2['artist'][2]]
    c = [df1['name'][0], df1['name'][1], df1['name'][2], df2['name'][0], df2['name'][1], df2['name'][2]]
    return render_template('start.html', sample1=a, sample2=b, sample3=c)

@app.route('/predict', methods=["GET","POST"])
def index():
    d1, d2, d3 = request.form['a'], request.form['b'], request.form['c']
    d1, d2, d3 = d1.split('/')[-1].split('?')[0], d2.split('/')[-1].split('?')[0], d3.split('/')[-1].split('?')[0]
    tr = spotify.recommendations(seed_tracks=[d1,d2,d3])
    album = tr['tracks'][0]['album']['name']
    artist = tr['tracks'][0]['album']['artists'][0]['name']
    track = tr['tracks'][0]['name']
    image = tr['tracks'][0]['album']['images'][1]['url']
    preview = tr['tracks'][0]['preview_url']
    link = tr['tracks'][0]['external_urls']['spotify']
    return render_template('after.html', album=album, artist=artist, track=track, image=image, preview=preview, link=link)

if __name__ == '__main__':
    app.run(debug=True)