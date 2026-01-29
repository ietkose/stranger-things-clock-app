import os

# path finder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_path(folder, filename):
    path_in_assets = os.path.join(BASE_DIR, 'assets', folder, filename)
    path_root = os.path.join(BASE_DIR, filename)
    if os.path.exists(path_in_assets):
        return path_in_assets
    elif os.path.exists(path_root):
        return path_root
    else:
        return None

# constants
FONT_PATH = get_path('fonts', 'Benguiat Bold.ttf')
ICON_PATH = get_path('images', 'icon.jpg') # for icon
BG_PATH = get_path('images', 'background.jpg') # for background

# colors
STRANGER_RED = "#ff1515"
BG_COLOR = "#1e0707"