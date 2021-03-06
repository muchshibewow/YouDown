#!/usr/bin/env python3
# The main YouDown program

# TODO : add DASH streams support, and stitching with ffmpeg

# Importing from other files in the repository.
from LinkGen import URLList
from DownloadScript import Download
from PlayVid import PLAY

# Main UI
print("Welcome to YouDown!")
print("What would you like to download?")
ans = int(input('1. Video\n2. Playlist\n:'))

# Choices, choices..
if ans == 1:
    # Downloading a single video only.

    URL = input("Enter the URL of the video : ")
    Path = input("Where do you want to save this file? : ")
    Video = Download(URL, Path)

    # Video playback post-download.
    print("\nWould you like to play the video now? (y/n)")
    pl = input()
    if pl == 'y' or pl == 'Y':
        print("Playing")
        PLAY(Video)
    print("\n\nThank you for using YouDown!\n\n")


elif ans == 2:
    # Downloading an entire playlist

    URL = input("Enter the URL of the playlist : ")
    Path = input("Where do you want to save these videos? : ")
    URLs = URLList(URL)

    # Some random lolz.
    URLs.pop(2)
    URLs.pop(3)
    URLN = []
    for i in range(0, len(URLs), 2):
        URLN.append(URLs[i])
    URLs = URLN

    # The actual downloading process.
    for Link in URLs[1:]:  # Don't ask.
        Download(Link, Path)
    print("\nPlaylist download complete!\n")
    print("\n\nThank you for using YouDown!\n\n")

else: # You drunk, m8?
    print("There are only 2 options, mate. :3")
    exit()
