# (EXPERIMENTAL, AND EXTREMELY STUPID)
# Adding support for playing videos post download.
# Uses very stupid methods for using VLC for this.

from subprocess import run
import os


def PLAY(Path):
    # Determining the OS first.
    if os.name == 'nt':  # Windows
        os.startfile(Path)
    elif os.name == 'posix':  # Linux
        run('vlc ' + Path, shell=True) # Totally unrelated, listen to Run - AWOLNATION.
