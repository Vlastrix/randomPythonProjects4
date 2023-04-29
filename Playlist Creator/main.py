import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD.\n")

# Remove this later !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! FOR DEBUGGING
user_date = "2000-08-12"

URL = f"https://www.billboard.com/charts/hot-100/{user_date}"
SPOTIFY_ID = "YOUR SPOTIFY ID"
SPOTIFY_SECRET = "YOUR SPOTIFY SECRET"
SCOPE = "playlist-modify-private"

response = requests.get(URL)
website = response.text

soup = BeautifulSoup(website, "html.parser")
songs_webpage = soup.find_all(name='span', class_='chart-element__information__song text--truncate color--primary')

songs = []

for song in songs_webpage:
    song_name = song.getText()
    songs.append(song_name)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, client_id=SPOTIFY_ID, client_secret=SPOTIFY_SECRET,
                                               redirect_uri="http://127.0.0.1:5500/",
                                               show_dialog=True,
                                               cache_path='token.txt'))

user = sp.current_user()['id']

# song_uris = []
# year = user_date.split("-")[0]
# for song in songs:
#     result = sp.search(q=f"track:{song} year:{year}", type="track", limit=10)
#     try:
#         uri = result["tracks"]["items"][0]["uri"]
#         song_uris.append(uri)
#     except IndexError:
#         print(f"{song} doesn't exist in Spotify. Skipped.")
#
#
# playlist = sp.user_playlist_create(user=user, name=f"{user_date} Billboard 100", public=True)
#
# sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
