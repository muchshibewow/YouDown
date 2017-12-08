# Simple script/utility to check for write permission

import os


def Check(Path):
    if os.name == 'nt':  # For Windows users
        try:
            os.makedirs(Path + '\\Lolz')
            os.rmdir(Path + '\\Lolz')
            return True
        except PermissionError as e:
            return False
    elif os.name == 'posix':  # For Linux users
        try:
            os.makedirs(Path + '/Lolz')
            os.rmdir(Path + '/Lolz')
            return True
        except PermissionError as e:
            return False
