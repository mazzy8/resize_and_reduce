#!/usr/bin/python3
from PIL import Image
import os
from datetime import datetime
import logging


logging.basicConfig(level=logging.INFO, filename=f"img_log_{datetime.now().date()}.log",
                    format="%(asctime)s %(levelname)s %(message)s")

FOLDER_AND_FILES = os.walk('.')
FILES_COUNT = 0
RESIZE_COUNT = 0
DIF_SIZE = 0

logging.info(f'#####################Start script#####################')
for root, dirs, files in FOLDER_AND_FILES:
    for file in files:
        filepath = os.path.join(root, file)
        if file[-3:].lower() in ('peg', 'jpg', 'img', 'png'):
            FILES_COUNT += 1
            try:
                size_file = os.path.getsize(filepath)
                with Image.open(filepath) as im:
                    width, height = im.size
                    if width > 1920 or height > 1080:
                        while width > 1920 or height > 1080:
                            if width > 1920:
                                height_percent = (1920 / width)
                                height = int(height * height_percent)
                                width = 1920
                            else:
                                width_percent = (1080 / height)
                                width = int(width * width_percent)
                                height = 1080
                        im.thumbnail((width, height), Image.LANCZOS)
                        im.save(filepath, quality=80, optimize=True)
                        size_file_after = os.path.getsize(filepath)
                        dif_size = int((size_file - size_file_after)/1024)
                        DIF_SIZE += dif_size
                        RESIZE_COUNT += 1
                        logging.info(f'Write file "{filepath}". Resize: {dif_size} Kb')
                    else:
                        continue
            except Exception as e:
                logging.error(f'Error: {e}')
logging.info(f'Stop script. All_image_files = {FILES_COUNT}, resize_files = {RESIZE_COUNT}, diff_size = {DIF_SIZE} Kb')
