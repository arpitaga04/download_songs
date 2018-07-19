#!/usr/bin/python

import pafy
import threading

MAX_THREADS = 30
MIN_THREADS = 20
f = open('youtube_links.txt','r')

song_links = f.read()
song_links = song_links.split('\n')
song_links = song_links[:-1]

no_of_songs = len(song_links)
nthreads = 0
mod_val = MAX_THREADS
n = 0 #number of song download per thread
#calculate the number of threads to use for optimum run
if no_of_songs <= MAX_THREADS:
	nthreads = no_of_songs
	n = 1

else:
	for i in range(MIN_THREADS, MAX_THREADS+1):
		if(mod_val >= no_of_songs % i):
			mod_val = no_of_songs % i
			nthreads = i
	n = int(no_of_songs/nthreads)


def download(links = []):
	for link in links:
		video = pafy.new(link)
		bestaudio = video.getbestaudio()
		bestaudio.download('music/')

t = []
for i in range(nthreads):
	if i == nthreads-1 :
		links = song_links[i*n:]
	else:
		links = song_links[i*n:(i+1)*n]
		
	t.append(threading.Thread(target=download, args = (links,)))
	t[i].daemon = True
	t[i].start()
	
for _ in range(nthreads):
	t[_].join()

print "Number of threads used = " + str(nthreads)
print "Download completed"
