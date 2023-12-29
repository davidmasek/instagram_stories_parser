# Instagram Stories Parser

Download all your instagram stories.

## Usage

1. See [official documentation](https://help.instagram.com/181231772500920/?cms_platform=www&helpref=platform_switcher) to "Access and download your information on Instagram". Choose the JSON version. Unzip the downloaded file.
2. Place the `parser.py` script inside the unzipped folder (it should contain folders `media` and `your_instagram_activity`).
3. Run the script with `python parser.py`. Any recent Python 3 version should work, no libraries needed.
4. All stories will be saved to a new folder called `stories_saved` in the same directory.

## Goals

I made this as a quick solution for myself and I am sharing this in case it helps someone and for future reference. The script is just a few lines and will likely break on any unexpected input or change in the data structure.
