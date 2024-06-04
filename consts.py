from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
MEDIA_PATH = os.path.join(BASE_DIR, 'media')
TEMP_FILES = os.path.join(BASE_DIR, 'temp')