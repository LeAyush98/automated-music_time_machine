from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import strings

date = input("What date in past? YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")

html = response.text

tomato = BeautifulSoup(html, "html.parser")

song_list = tomato.find_all(name="h3", class_= "lrv-u-font-size-16", id = "title-of-a-story")

track = []

uri = []

for song in song_list:
    song = song.getText().strip()
    track.append(song)


spotspot = SpotifyOAuth(client_id= strings.Client_ID, client_secret= strings.Client_Secret, redirect_uri= "http://example.com", scope= "playlist-modify-private")

#print(spotspot.get_access_token())
#print(strings.access_token)

spot = spotipy.Spotify(auth=strings.access_token)

id = spot.current_user()["id"]

for index, song in enumerate(track):
    result = spot.search(q=track[index], type="track")["tracks"]["items"][0]["uri"]
    uri.append(result)

print(uri)