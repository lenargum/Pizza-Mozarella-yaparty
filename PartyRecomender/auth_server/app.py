import tekore as tk
from flask import Flask, request, redirect, session, Response
from utils.db import *
from utils.queries import *
from utils.music import get_list_of_fav_music
from dotenv import load_dotenv
from uuid import uuid4

load_dotenv()

# conf = tk.config_from_environment()

conf = [os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'), os.getenv('REDIRECT_URI')]
cred = tk.Credentials(*conf)
spotify = tk.Spotify()

auths = {}  # Ongoing authorisations: state -> UserAuth
users = {}  # User tokens: state -> token (use state as a user ID)
states2id = {}

in_link = '<a href="/login">login</a>'
out_link = '<a href="/logout">logout</a>'
login_msg = f'You can {in_link} or {out_link}'

app = Flask(__name__)
app.config['SECRET_KEY'] = "party"


@app.route('/', methods=['GET'])
def main():
    user = session.get('user', None)
    token = users.get(user, None)

    # Return early if no login or old session
    if user is None or token is None:
        session.pop('user', None)
        return f'User ID: None<br>{login_msg}'

    page = f'User ID: {user}<br>{login_msg}'
    if token.is_expiring:
        token = cred.refresh(token)
        users[user] = token

    try:
        with spotify.token_as(token):
            playback = spotify.playback_currently_playing()

        item = playback.item.name if playback else None
        page += f'<br>Now playing: {item}'
    except tk.HTTPError:
        page += '<br>Error in retrieving now playing!'

    return page


@app.route('/login', methods=['GET'])
def login():
    if 'user' in session:
        return redirect('/', 307)

    room_id = request.args.get("room_id")

    if not room_id:
        raise Exception("User ID and Party ID are not specified")

    scope = tk.scope.read
    auth = tk.UserAuth(cred, scope)
    auths[auth.state] = auth
    states2id[auth.state] = [room_id, str(uuid4().fields[-1])[:5]]

    return redirect(auth.url, 307)


@app.route('/callback', methods=['GET'])
def login_callback():
    code = request.args.get('code', None)
    state = request.args.get('state', None)
    auth = auths.pop(state, None)
    room_id, user_id = states2id[state]

    if auth is None:
        return 'Invalid state!', 400

    token = auth.request_token(code, state)
    conn, cursor = open_connection_and_get_cursor()
    # cursor.execute(insert_room % "rooms", (room_id,))
    cursor.execute(insert_user_id % "users", (user_id,))
    cursor.execute(insert_users_in_rooms % "users_in_rooms", (user_id, room_id))
    commit_transaction_and_close_connection(conn, cursor)
    session['user'] = state
    users[state] = token
    conn, cursor = open_connection_and_get_cursor()
    cursor.execute(add_spotify_token % "users", (user_id, str(token)))
    commit_transaction_and_close_connection(conn, cursor)
    get_list_of_fav_music(user_id, token)

    return Response("Success", status=200)


@app.route('/logout', methods=['GET'])
def logout():
    uid = session.pop('user', None)
    if uid is not None:
        users.pop(uid, None)
    return redirect('/', 307)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
