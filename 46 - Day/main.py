import requests
from bs4 import BeautifulSoup

import spotipy
from spotipy.oauth2 import SpotifyOAuth


# user = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
user = "2000-08-12"

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{user}/")
data = response.text


soup = BeautifulSoup(data, 'html.parser')

titles = soup.find_all(name="h3", id="title-of-a-story", class_="u-line-height-125")

for (index, title) in enumerate(titles):
    print(index + 1, title.getText().strip())


#####################################################
#   SPOTIFY
#####################################################

CLIENT_SECRET = "0c5503ad2afb4e848581ea789f690854"

CLIENT_ID = "a5eaa30429544cc98d07f0dd60fb9543"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]















