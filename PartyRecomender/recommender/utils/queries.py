party_data = """
select fm.user_id, song_id from favorite_music fm inner join (
select user_id from users_in_rooms
inner join rooms r on r.room_id = users_in_rooms.room_id
where r.room_id= cast (%s as varchar(256))) u on u.user_id=fm.user_id
"""
