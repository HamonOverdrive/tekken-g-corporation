import shutil
import os


# MOVE CSV FILES TO OTHER DIRECTORY
source = r'/home/rlee/PycharmProjects/tekken-g-corporation/web_scraper_csv_handlers'
dest = r'/home/rlee/PycharmProjects/tekken-g-corporation/static/char_csvs2'

files = os.listdir(source)

for f in files:
    if f.endswith('.csv'):
        shutil.move(f, dest)