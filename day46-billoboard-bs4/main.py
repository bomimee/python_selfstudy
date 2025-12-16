import requests
from bs4 import BeautifulSoup
import datetime as dt
import spotipy
from spotipy.oauth2 import SpotifyOAuth
CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = 'http://localhost:8888/callback'
scope = "playlist-modify-private"
sp_oauth = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    show_dialog=True,
    cache_path="token.txt"
    # client_id=os.environ['CLIENT_ID'],
    # client_secret=os.environ['CLIENT_SECRET'],
    # redirect_uri=os.environ['REDIRECT_URI'],
    scope=scope
)
user_id = sp_oauth.current_user()["id"]
sp = spotipy.Spotify(auth_manager=sp_oauth)
playlists = sp.user_playlists('spotify')
print(sp)
print(playlists)

year = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD \n")
URL = f'https://www.billboard.com/charts/hot-100/{year}/'
URL = 'https://www.billboard.com/charts/hot-100/'
now = dt.datetime.now()
formatted_date = now.strftime("%Y-%m-%d")

response = requests.get(URL)

html = BeautifulSoup(response.text, 'html.parser')
titles = html.select(selector='ul li ul li h3', class_="c-title")

title_list =[]
for title in titles:
    text = title.getText().strip()
    title_list.append(f"{text}\n")

# print(title_list)
with open(f"{formatted_date} billboard100.txt", 'w', encoding="utf-8") as file:
    for title in title_list:
        file.write(title)
