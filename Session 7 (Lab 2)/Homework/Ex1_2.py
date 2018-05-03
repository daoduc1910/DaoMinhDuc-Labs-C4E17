from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs"

#Open connection
conn = urlopen(url)

#read data
raw_data = conn.read()

#Decode
text = raw_data.decode("utf-8")

soup = BeautifulSoup(text, 'html.parser')

div = soup.find('div', id = "main")

li_list = div.find_all('li')

data_list = []

for li in li_list:
    a_name = li.h3.a
    a_artist = li.h4.a
    song = a_name.string
    artist = a_artist.string

    options = {
        "default_search": "ytsearch";
        "max_downloads" : 1;
        "format": 'bestaudio/audio'
    }
    dl = YoutubeDL(options)
    dl.download([song, '-', author])
