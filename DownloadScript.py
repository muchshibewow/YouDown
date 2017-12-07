# File containing a function to download the videos

import pytube
from root_check import Check


def Download(URL, Path):
	if not Check(Path):
		print("Permission to write denied.")
		print("Please ensure you have write privileges to the directory specified.")
    # Making a YouTube object from the URL provided to the function.
    vid = pytube.YouTube(URL)

    # Taking only the highest quality 'legacy' stream for the video.
    # TODO : Add DASH streams support
    Video = vid.streams.first()

    # Just the random UI.
    print("\nDownloading", Video.default_filename, "in", Video.resolution, "......")
    Video.download(Path)
    print("Download complete!")
