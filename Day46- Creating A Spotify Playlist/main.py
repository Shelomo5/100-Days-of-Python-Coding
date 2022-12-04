import requests
from bs4 import BeautifulSoup
# lightweight Python library for the Spotify Web API and access its music data.
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
import os

# Spotify ID and Secret
SPOTIPY_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
# Random uri just needed for parameter
REDIRECT_URI = "https://example.com"

# Authentication (verifies identity) with Spotify using OAuth to allow third-party applications
# spotify is an object to open spotify web API
# aut_manager is an object that allows us to use OAuth (authorization, limited access rights) to access Spotify account
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-modify-private",
    cache_path="token.txt"
    )
)
# Getting user id of authenticated user
user_id = spotify.current_user()["id"]
# print(spotify.current_user())
# print(user_id)


URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

# get hold of data from particular url
response = requests.get(URL + date)
# raw text
music_page = response.text

# instantiating soup class
soup = BeautifulSoup(music_page, "html.parser")

# find song titles using soup.select by specifying tag
music_list = soup.select("li #title-of-a-story")

# list comprehension to create a list of song titles isolating title text
song_titles = [music.getText().strip() for music in music_list]
# print(song_titles)

# splitting date as to get just the year
year = date.split("-")[0]
# print(year)

# 2022-10-08 year: {year}

# songs found on spotify appended to this list
song_URIs = []
# iterating through each top 100 song title
for title in song_titles:
    result = spotify.search(q=f"track: {title} ", limit=1, type='track', market="US")

    # Use try and except for songs that can't be found in Spotify API
    try:
        track = result["tracks"]["items"][0]["uri"]
        song_URIs.append(track)
    except IndexError:
        print(f" No {title} in spotify so skipped.")

# name of playlist
playlist_name = f"{date} Billboard 101"
# create playlist on spotify
playlist = spotify.user_playlist_create(user=user_id, name=playlist_name, public=False)
# adding song_URIs to the playlist
spotify.playlist_add_items(playlist_id=playlist["id"], items=song_URIs)

