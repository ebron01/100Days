from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
date = input("Which year do you want to travel to? Type the date in this format YYYY:")
# URL = f"https://www.billboard.com/charts/hot-100/{date}"
URL = f"https://www.billboard.com/charts/year-end/{date}/hot-100-songs/"

ID = "6beffd1889524ffabdc69c16a36468b5"
PASSWD = "c0a8de6722474f0799b83d1189ee37b0"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names =[title.getText().strip() for title in song_names_spans]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=os.environ["SPOTIPY_REDIRECT_URI"],
        client_id=os.environ["SPOTIPY_CLIENT_ID"],
        client_secret=os.environ["SPOTIPY_CLIENT_SECRET"],
        show_dialog=True,
        cache_path="/home/beast/100Days/timeMachine/token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


#TODO: create a user playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
#TODO: add desired track to spotify playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print("Done")



