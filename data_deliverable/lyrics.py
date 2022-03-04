# Credit to Jack Schultz for stencil code
# https://bigishdata.com/2016/09/27/getting-song-lyrics-from-geniuss-api-scraping/

import requests
from bs4 import BeautifulSoup
import re

base_url = "https://api.genius.com"
headers = {'Authorization': 'Bearer Cmy3VucAY4A_QoI6U8Zz5yO0ZCAlMc0Avk2DH2arPbXW4N-2wsUvv_309Cdi2MOW'}

song_title = "Na Na Na"
artist_name = "My Chemical Romance"

def lyrics_from_song_api_path(song_api_path):
	song_url = base_url + song_api_path
	response = requests.get(song_url, headers=headers)
	json = response.json()
	path = json["response"]["song"]["path"]
	
	#gotta go regular html scraping... come on Genius
	page_url = "https://genius.com" + path
	page = requests.get(page_url)
	html = BeautifulSoup(page.text, "html.parser")
	
	#remove script tags that they put in the middle of the lyrics
	[h.extract() for h in html('script')]
	
	for br in html.find_all("br"):
		br.replace_with("\n")
	#print(html.prettify())
	matches = re.findall(r'Lyrics__Container.*?"', str(html))
	m = matches[0]
	lyrics = html.find('div', class_=m[:-1]).get_text()
	return lyrics

if __name__ == "__main__":
	search_url = base_url + "/search"
	data = {'q': song_title}
	response = requests.get(search_url, params=data, headers=headers)
	json = response.json()
	if json["response"]["hits"] == []:
		print("Song DNE")
	song_info = None
	for hit in json["response"]["hits"]:
		if hit["result"]["primary_artist"]["name"] == artist_name:
			song_info = hit
			break
	if song_info:
		song_api_path = song_info["result"]["api_path"]
		print(lyrics_from_song_api_path(song_api_path).lstrip())
	elif json["response"]["hits"] != []:
		print("Could not find artist", artist_name, "for song", song_title)