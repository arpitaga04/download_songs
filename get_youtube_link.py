#!/usr/bin/python

import requests
from bs4 import BeautifulSoup

f = open('song_names.txt','r')

song_names = f.read()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
f.close()
song_names = song_names.split('\n')
song_names = song_names[:-1]

song_urls = []
for song in song_names:

	song_url = song.replace(' ', '+')
	r = requests.get('https://www.google.com/search?q=' + song_url, headers=headers)
	soup = BeautifulSoup(r.content)
	a_tag = soup.find_all("a")
	for i in a_tag:
		hr = i.get("href")
		if hr:
			if "youtube.com" in hr:
				song_urls.append(hr)
				break
	print song
	
f = open('youtube_links.txt','w')

for i in song_urls:
	f.write(i)
	f.write('\n')
	
f.close()
