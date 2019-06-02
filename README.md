# imgur-randomizer
```
usage: imgur-randomizer.py [-h] [--extension {jpg,png,gif,mov,mp4}] [--name_length {5,6,7}] [--min_width MIN_WIDTH] [--min_height MIN_HEIGHT] [NUM_IMAGES]

Fetch random images from Imgur image hosting.

positional arguments:
  NUM_IMAGES            number of images to be fetched (default: 30)

optional arguments:
  -h, --help            show this help message and exit

  --extension {jpg,png,gif,mov,mp4}
                        fetch images by specified extension (default: random)

  --name_length {5,6,7}
                        file name length, 7-characters names are rare, so it’s better to use 6 or 7 (default: random)

  --min_width MIN_WIDTH
                        minimum width of fetched image in pixels (default: 100)

  --min_height MIN_HEIGHT
                        minimum height of fetched image in pixels (default: 100)
```
