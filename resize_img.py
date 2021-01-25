from src.img_resizer import resize_img
from argparse import ArgumentParser

parser = ArgumentParser(description="Symmetrically resizes images at supplied path and creates directory for result")
parser.add_argument("width", help="Desired width in pixels")
parser.add_argument("height", help = "Desired height in pixels")
parser.add_argument("img_path", help = "Path to image directory")

parse = parser.parse_args()

width = int(parse.width)
height = int(parse.height)
path = parse.img_path

if width == None:
    raise ValueError("Please input a valid width")

if height == None:
    raise ValueError("Please input a valid height")

resize_img(width, height, path)
