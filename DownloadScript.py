# File containing a function to download the videos

import pytube

def Download(URL,Path):

	# Making a YouTube object from the URL provided to the function.
	vid=pytube.YouTube(URL)

	# Taking only the highest quality 'legacy' stream for the video.
	# TODO : Add DASH streams support
	Video=vid.streams.first()

	# Just the random UI.
	print("\nDownloading",Video.default_filename,"in",Video.resolution,"......")
	Video.download(Path)
	print("Download complete!")
