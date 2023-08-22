# (EXPERIMENTAL, AND EXTREMELY STUPID)
# Adding support for playing videos post download.
# Uses very stupid methods for using VLC for this.

import os


def PLAY(Path: str) -> None:
    # Just one line to play the file.
    # Equivalent to double-clicking the file.
    os.startfile(Path)