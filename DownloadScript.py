# File containing a function to download the videos

import pytube
from root_check import Check


def Download(URL, Path):
    # Checking for write permission
    if not Check(Path):
        print("Write access denied.")
        print("Ensure you have write privileges for the specified path")
        exit()

    # Making the YouTube object.
    vid = pytube.YouTube(URL)

    # Taking only the highest quality 'legacy' stream for the video.
    # TODO : Add DASH streams support
    Video = vid.streams.first()

    # Just the random UI.
    print("\nDownloading", Video.default_filename, "in", Video.resolution + ".")
    Video.download(Path)
    print("Download complete!")
    return Path+os.sep+Video.default_filename
