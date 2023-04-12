#!/usr/bin/env python3
# The main YouDown program

# TODO : add DASH streams support, and stitching with ffmpeg

# Importing from other files in the repository.
from LinkGen import URLList
from DownloadScript import Download
from PlayVid import PLAY
from rich.console import Console
console = Console()

# Main UI
console.print("Welcome to [bright_red]You[/][bold]Down!")
console.print("What would you like to [bright_green][bold]download?")
ans = int(console.input('[bold][italic]1. Video\n2. Playlist\n:'))

# Choices, choices.. (we all know.)
if ans == 1:
    # Downloading a single video only.

    URL = console.input("[bright_yellow][bold]Enter the URL of the video : ")
    Path = input("Where do you want to save this file? : ")
    Video = Download(URL, Path)

    # Video playback post-download.
    pl = console.input("\n[bright_yellow][bold]Would you like to play the video now? (y/n) ")
    if pl == 'y' or pl == 'Y':
        print("Playing")
        PLAY(Video)
    console.print("\n\n[bright_green]Thank you for using [/][bright_red]You[/][bold]Down!\n\n")


elif ans == 2:
    # Downloading an entire playlist

    URL = console.input("[bright_yellow][bold]Enter the URL of the playlist : ")
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
    print("\n[bright_green]Playlist download complete!\n")
    print("\n\n[bright_green]Thank you for using [/][bright_red]You[/][bold]Down!\n\n")

else: # You drunk, m8?
    console.print("[bright_red]Error: There are only 2 options, mate. :3")
    exit() # Theres no need for exit, since it autmatically ends.
