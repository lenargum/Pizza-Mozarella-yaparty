insert_music_data = """insert into song_info(id, acousticness,analysis_url, danceability,duration_ms,energy,instrumentalness,
                    key,
                    liveness,
                    loudness,
                    mode,
                    speechiness,
                    tempo,
                    time_signature,
                    track_href,
                    type,
                    uri,
                    valence) values (%s, %s, %s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s, %s, %s, %s, %s)
                    on conflict do nothing"""

insert_fav_music = """insert into favorite_music(user_id, song_id) 
                      values (%s, %s) on conflict do nothing"""
insert_room = """insert into %s (room_id) values (%%s) on conflict do nothing"""
insert_user_id = "insert into %s (user_id) values (%%s) on conflict do nothing"
insert_users_in_rooms = "insert into %s (user_id, room_id) values (%%s, %%s) on conflict do nothing"
add_spotify_token = "insert into %s (user_id) values (%%s) on conflict (user_id) do update set spotify_token=%%s"