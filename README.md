# Download Saavn Songs

The python 2.x scripts help you to get the list of songs in your Saavn playlist and further you can download them if you want to.
The songs are downloaded via python library called pafy. It takes in youtube links of the songs and downloads them in a audio webm format.

# How to use

* First make sure all the python libraries that are required are installed. You can run install_libraries.sh if you are not sure.
You need to provide proper permission to run this script.

* Once everthing is done, first run saavn_login.py
	This will take down all the songs of the playlist that you have specified and write it in song_names.txt

* Then the next script(ie, get_youtube_links.py) will fetch the youtube links of all the songs specified in song_names.txt and store it in youtube_links.txt

* Then the final script (final_downloads.py) will start downloading the songs. It will how up Download Complete once it is done.

---

* The advantage of dividing the task into three different scripts is that if you already have a list of songs from some other sources, you can put them in song_names.txt file and continue running the next script.

* Similarly, if you have youtube links, you can put them in youtube_links.txt and continue running the next script.

* The final_downloads.py script uses threading, which helps in downloading multiple songs at the same time. Downloading one song at a time is very slow and does not fully utilize user bandwidth. Using threading, this problem is solved.

---

These are python scripts made for learning purposes and it is not supposed to be misused. Any misuse is not my responsibilty.
