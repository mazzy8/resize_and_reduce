#!/usr/bin/python3
from PIL import Image
import os
from datetime import datetime


FOLDER_AND_FILES = os.walk('.')
FILES_COUNT = 0
RESIZE_COUNT = 0
DIF_SIZE = 0

print(f'Start: {datetime.now()}')
for root, dirs, files in FOLDER_AND_FILES:
    for file in files:
        FILES_COUNT += 1
        filepath = os.path.join(root, file)
        if file[-3:].lower() in ('peg', 'jpg', 'img'):
            try:
                size_file = os.path.getsize(filepath)
                with Image.open(filepath) as im:
                    print(f'{datetime.now()} ||| open: {filepath} ||| ', end=' ')
                    width, height = im.size
                    if width > 1920:  # height > 1080
                        height_percent = (1920 / width)  # width_percent = (1080 / height)
                        new_height = int(height * height_percent)  # new_width = int(width * width_percent)
                        im.thumbnail((1920, new_height), Image.LANCZOS)
                        im.save(filepath, quality=85, optimize=True)
                        size_file_after = os.path.getsize(filepath)
                        dif_size = int((size_file - size_file_after)/1024)
                        DIF_SIZE += dif_size
                        RESIZE_COUNT += 1
                        print(f'new size = {size_file_after} ||| difference: {dif_size}Kb')
                    else:
                        print(f'close, width <= 1920')
            except OSError:
                print('Error OS')
print(f'Stop: {datetime.now()}, all_files = {FILES_COUNT}, resize_files = {RESIZE_COUNT}, diff_size = {DIF_SIZE}Kb')
