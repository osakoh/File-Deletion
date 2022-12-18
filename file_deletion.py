import os


def file_delete(filename):
    """deletes files from the filesystem"""
    if os.path.isfile(filename):
        os.remove(filename)
