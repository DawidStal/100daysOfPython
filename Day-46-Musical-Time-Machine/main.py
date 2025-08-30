import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_ID = os.getenv("SPOTIFY_ID")
SPOTIFY_SECRET = os.getenv("SPOTIFY_SECRET")
SPOTIFY_USERNAME = os.getenv("SPOTIFY_USERNAME")

input_year = input("Which year do you want to travel to? Type the year in YYYY-MM-DD format: ")

scope = "user-library-read playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        redirect_uri="http://localhost:8000",
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="Day-46-Musical-Time-Machine/token.txt",
        username=SPOTIFY_USERNAME,
    )
)
user_id = sp.current_user()["id"]

response = requests.get(f"https://www.billboard.com/charts/hot-100/{input_year}/")
print(response.status_code)
soup = BeautifulSoup(response.text, "html.parser")

song_uris = []

def get_track_id(song_name, artist_name):
    query = f"track:{song_name} artist:{artist_name}"
    search_result = sp.search(query, type="track", market="US", limit=1)
    
    if search_result['tracks']['items']:
        return search_result['tracks']['items'][0]['id']
    return None

songs = soup.find_all("div", class_="o-chart-results-list-row-container")
for song in songs:
    title_tag = song.select_one("h3#title-of-a-story").get_text(strip=True)
    artist_tag = song.select_one("span.c-label.a-no-trucate").get_text(strip=True)
    print(f"{title_tag} by {artist_tag}")
    if(title_tag and artist_tag):
        track_id = get_track_id(title_tag, artist_tag)
        if track_id:
            song_uris.append(track_id)
        else:
            print(f"Song not found on Spotify.")

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{input_year} - Billboard 100",
    public=False,
    description=f"Billboard 100 songs from {input_year}"
)

if song_uris:
    sp.playlist_add_items(playlist["id"], song_uris)
    print(f"Playlist created! Check your Spotify account for '{input_year} - Billboard 100'")
else:
    print("No songs were found to add to the playlist")