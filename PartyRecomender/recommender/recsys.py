from collections import Counter

import pandas as pd
import sqlalchemy
import numpy as np
import os
import tekore as tk
from lightfm import LightFM
from lightfm.data import Dataset
from lightfm.evaluation import auc_score
from dotenv import load_dotenv
from fastapi import FastAPI, Query
from utils import queries

load_dotenv()

app = FastAPI()


@app.get("/recommend")
def recommend(room_id: int, size: int):
    song_features = get_song_features()
    party_data = get_party_data(room_id)
    dataset = Dataset()
    dataset.fit(
        (x['user_id'] for x in party_data),
        (x['song_id'] for x in party_data)
    )
    dataset.fit_partial(items=(x['song_id'] for x in party_data),
                        item_features=(tuple(x.values()) for x in song_features))
    interactions, _ = dataset.build_interactions((x['user_id'], x['song_id']) for x in party_data)
    ids = [x['song_id'] for x in party_data]
    item_features = dataset.build_item_features(((x[0], [tuple(x[1].values())])
                                                 for x in zip(ids, song_features)))
    model = LightFM(loss='warp-kos', k=3)
    model.fit(interactions, item_features=item_features, epochs=20)

    # Compute and print the AUC score
    train_auc = auc_score(model, interactions, item_features=item_features, num_threads=4).mean()
    print('Collaborative filtering train AUC: %s' % train_auc)

    n_users, n_items = interactions.shape
    common_scores = np.zeros(n_items)
    simple_rank = Counter()
    data = pd.DataFrame.from_records(party_data)
    for user_id in range(n_users):
        scores = model.predict(user_id, np.arange(n_items))
        top_items = data['song_id'].iloc[np.argsort(-scores)].tolist()
        simple_rank += Counter(top_items)
        common_scores += scores
    sorted_scores = np.sort(-common_scores)
    top_items = {k: v for k, v in zip(data['song_id'].iloc[np.argsort(-common_scores)].tolist(), sorted_scores)}

    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    app_token = tk.request_client_token(client_id, client_secret)
    spotify = tk.Spotify(app_token, chunked_on=True)

    i = 0
    data = []
    for track_id, _ in list(top_items.items())[:size]:
        track = spotify.track(track_id)
        data.append({
            "track_name": track.name,
            "track_cover": track.album.images[-1],
            "duration_ms": track.duration_ms,
            "artists": [artist.name for artist in track.artists]
        })
    return data

def get_song_features():
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')
    conn = sqlalchemy.create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db_name}")
    song_data = pd.read_sql("select * from song_info", conn)
    song_data = song_data.select_dtypes(np.number)
    song_features = song_data.to_dict(orient="records")
    return song_features


def get_party_data(room):
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')
    conn = sqlalchemy.create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db_name}")
    party_data = pd.read_sql(queries.party_data % room, conn)
    party_data = party_data.to_dict(orient="records")
    return party_data


