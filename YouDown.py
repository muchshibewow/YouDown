#!/usr/bin/python3.6
# The main YouDown program

# Importing from other files in the repository.
from LinkGen import URLList
from DownloadScript import Download

# Main UI
print("Welcome to YouDown!")
print("What would you like to download?")
ans = int(input('1. Video\n2. Playlist\n:'))
if ans == 1:
    # Downloading a single video only.
    URL = input("Enter the URL of the video : ")
    Path = input("Where do you want to save this file? : ")
    Download(URL, Path)
    print("\n\nThank you for using YouDown!\n\n")
elif ans == 2:
    # Downloading an entire playlist
    URL = input("Enter the URL of the playlist : ")
    Path = input("Where do you want to save these videos? : ")
    URLs = URLList(URL)
    URLs.pop(2)
    URLs.pop(3)
    URLN = []
    for i in range(0, len(URLs), 2):
        URLN.append(URLs[i])
    URLs = URLN
    for Link in URLs[1:]:  # Don't ask.
        Download(Link, Path)
    print("\nPlaylist download complete!\n")
    print("\n\nThank you for using YouDown!\n\n")
