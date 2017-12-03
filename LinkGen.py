# This program generates a list of URLs from the playlist

from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

def URLList(PlaylistURL):
	
	# These lines get the original playlist url passed as argument and try to make
	# a proper playlist-only URL.
	ListID = urlparse(PlaylistURL).query.split('&')
	ListID=ListID[1]

	# This line makes the actual link, of the form:
	# https://www.youtube.com/playlist?list=<listID>
	PlaylistURL_actual='https://www.youtube.com/playlist?'+ListID

	# These lines obtain the source of the page pointed to
	# by the URL above, and parse it in order to get the data
	# from the tags needed.
	# P.S I don't know anything about the "lxml" tag here.
	PageSrc=requests.get(PlaylistURL_actual).text
	soupObj=BeautifulSoup(PageSrc,'lxml')

	# These lines then go through the <a> tags in the page,
	# looking for valid video tags.
	LinkList=[] # LOL
	for Link in soupObj.find_all('a'):
		l=Link.get('href')
		if(l[0:6]=='/watch'):
			LinkList.append(l[7:].split('&')[0])
	# This line returns the final dictionary
	return LinkList

if __name__ == '__main__':
	# Boilerplate for TVF's Permanent Roommates Season 1.
	print(URLList('https://www.youtube.com/watch?v=6LedYr5tQUs&list=PLTB0eCoUXErZYQ0Ljy5smGvDL4Ng134rV'))