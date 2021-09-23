import tekore as tk
from .db import *
from .queries import insert_music_data, insert_fav_music


def get_list_of_fav_music(user_id,token):
    spotify = tk.Spotify(token, chunked_on=True)
    tracks = spotify.current_user_top_tracks(limit=50)
    tracks_ids = [track.id for track in tracks.items]
    user_track_rel = [(user_id, track_id) for track_id in tracks_ids]
    audios_features = spotify.tracks_audio_features(tracks_ids)
    records = [audio_features.__dict__ for audio_features in audios_features]
    song_info = [list(v for k, v in record.items()) for record in records]
    conn, cursor = open_connection_and_get_cursor()
    cursor.executemany(insert_music_data, song_info)
    cursor.executemany(insert_fav_music, user_track_rel)
    commit_transaction_and_close_connection(conn, cursor)
    return tracks
