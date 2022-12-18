import os


def file_delete(filename):
    """deletes files from the filesystem"""
    os.remove(filename)
    # print(f"File {filename} deleted successfully")
