import os

def get_path(filename):
    if hasattr(os.sys, "_MEIPASS"):
        return os.path.join(os.sys._MEIPASS, filename)
    else:
        return filename