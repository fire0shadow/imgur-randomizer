import requests
import os
import time
import datetime
import string
import random
import argparse

FILE_EXTENSIONS = ['jpg', 'png', 'gif', 'mov', 'mp4']
MIN_NAME_LENGTH = 5
MAX_NAME_LENGTH = 7
NAME_CHARACTERS_POOL = string.ascii_letters + string.digits

DIR_NAME = 'results/'
URL = 'https://i.imgur.com/'

parser = argparse.ArgumentParser(description='Fetch random images from Imgur image hosting.')
parser.add_argument('num_images', nargs='?', type=int, default=30, help='number of images to be fetched (default: %(default)s)')
parser.add_argument('--extension', choices=FILE_EXTENSIONS, default=-1, help='fetch images by specified extension (default: random)')
parser.add_argument('--name_length', type=int, choices=range(MIN_NAME_LENGTH, MAX_NAME_LENGTH+1), default=-1, help='file name length (default: random)')

arguments = parser.parse_args()

NUM_IMAGES = arguments.num_images
EXTENSION = arguments.extension
NAME_LENGTH = arguments.name_length

if not os.path.isdir(DIR_NAME):
	os.mkdir(DIR_NAME)

DIR_NAME = DIR_NAME + datetime.datetime.now().strftime("%d.%d.%y") + '/'
if not os.path.isdir(DIR_NAME):
	os.mkdir(DIR_NAME)

DIR_NAME = DIR_NAME + datetime.datetime.now().strftime("%H.%S") + ' [' + str(round(time.time())) + ']/'
os.mkdir(DIR_NAME)

def random_string(length):
    return ''.join(random.choice(NAME_CHARACTERS_POOL) for i in range(length))

def fetch_image(name, ext):
	image_name = name + '.' + ext

	image = requests.get(URL + image_name, allow_redirects=False)

	if image.status_code == 400:
		print(image_name + ' returned bad request, skipping...')
	elif image.status_code == 404 or image.status_code == 302:
		print(image_name + ' doesn\'t exists or removed, skipping...')
	elif image.status_code == 200:
		print(image_name + ' exists, fetching...')

		with open(DIR_NAME + image_name, 'wb') as f:
			f.write(image.content)

		return True

	return False

i = 0
while(i < NUM_IMAGES):
	image_name_length = random.randint(MIN_NAME_LENGTH, MAX_NAME_LENGTH) if NAME_LENGTH == -1 else NAME_LENGTH
	random_image_name = random_string(image_name_length)
	
	image_extension = random.choice(FILE_EXTENSIONS) if EXTENSION == -1 else EXTENSION
	if fetch_image(random_image_name, image_extension):
		i = i + 1