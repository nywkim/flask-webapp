"""해당 파일은 랜덤포레스트 이진분류의 모델 생성 부분입니다."""
import json
import pandas as pd
import numpy as np
from sklearn import ensemble
from sklearn.model_selection import train_test_split
import pickle
import joblib

file_path = "./sample.json"

with open(file_path, "r") as json_file:
    json_data = json.load(json_file)

from pandas import json_normalize

df = json_normalize(json_data['tracks'])
dt = pd.DataFrame(df)
dt = dt.sample(frac=1)
new = dt.drop_duplicates(['song.song_id'], keep='first').reset_index(drop=True)
sp = new.drop(columns=['album.album_id', 'album.name', 'artist.artist_id', 'artist.name','song.song_id', 'song.name'], axis=1)

target = 'song.mood'
train, val = train_test_split(sp, test_size=0.2, random_state=2021)
features = sp.drop(columns=[target]).columns
X_train = train[features]
y_train = train[target]
X_val = val[features]
y_val = val[target]

rf = ensemble.RandomForestClassifier()
rf.fit(X_train, y_train)
saved_model = pickle.dumps(rf)
joblib.dump(rf, 'filename.pkl') 
