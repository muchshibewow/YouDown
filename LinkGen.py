# This program generates a list of URLs from the playlist

from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urlparse


def URLList(PlaylistURL):
    # These lines get the original playlist url passed as argument and try to make
    # a proper playlist-only URL.
    
    #PlaylistURL = https://youtube.com/playlist?list=PL-5egZTw99_7ml5khqKSHJ8Xp30Hz-dl9
    #ListID = PL-5egZTw99_7ml5khqKSHJ8Xp30Hz-dl9
    playlist_re = r"^(https?://)?(www\.)?(youtube\.com|youtu\.?be)/playlist\?list=(?P<id>[a-zA-Z0-9_-]+)"
    if re.match(playlist_re, PlaylistURL):
        PlaylistURL_actual = PlaylistURL
    else:
        ListID = urlparse(PlaylistURL).query.split('=')[1]
        PlaylistURL_actual = 'https://www.youtube.com/playlist?list=' + ListID

    # These lines obtain the source of the page pointed to
    # by the URL above, and parse it in order to get the data
    # from the tags needed.
    # P.S I don't know anything about the "lxml" tag here.
    PageSrc = requests.get(PlaylistURL_actual).text

    soupObj = BeautifulSoup(PageSrc, features="html.parser")

    # These lines then go through the <a> tags in the page,
    # looking for valid video tags.
    LinkList = []  # LOL
    for Link in soupObj.find_all('a'):
        l = Link.get('href')
        print(l)
    # This line returns the final array of URLs.
    return LinkList


if __name__ == '__main__':
    print("Useless alone, unless you modify the code. Enjoy!")
