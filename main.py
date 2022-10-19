import glob
import numpy as np
from PIL import Image
import os


def padding(img):
    # setting up new size of the file (need to be square)
    old_width, old_height = img.size
    diff = old_width - old_height

    if diff < 0:
        new_width = old_width + abs(diff)
        new_height = old_height
    else:
        new_height = old_height + abs(diff)
        new_width = old_width

    print(new_height, new_width)

    # setting up the padding size

    padding_left = int((new_width - old_width) / 2)
    padding_top = int((new_height - old_height) / 2)

    #
    result = Image.new(img.mode, (new_width, new_height), (0, 0, 0))
    #
    result.paste(img, (padding_left, padding_top))
    return result


# opening all images from folder
images = []

for f in glob.iglob("M:\DOKUMENTY\KUBA HALT\sesja\*"):
    images.append(Image.open(f))

i = 0
for img in images:
    i += 1
    padding(img).save(r"M:\DOKUMENTY\KUBA HALT\sesja\padding_%d.jpg" % i)
