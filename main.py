import glob
import numpy as np
from PIL import Image

# opening all images from folder
images = []
for f in glob.iglob("M:\DOKUMENTY\KUBA HALT\sesja\*"):
    images.append(Image.open(f))

for img in images:
    # img.show()
    # setting up new size of the file (need to be square)
    old_width, old_height = img.size
    diff = old_width-old_height

    # if (diff < 0 ):
    #     new_width = old_width + abs(diff)
    #     new_height = old_height
    # else:
    #     new_height = old_height + abs(diff)
    #     new_width = old_width
    #
    #
    # padding_right = int((new_width - old_width) /2)
    # padding_left = int((new_width - old_width) /2)
    # padding_top = int((new_height - old_height) /2)
    # padding_bottom = int((new_height - old_height) /2)
    #
    # #
    # result = Image.new(img.mode, (new_width, new_height), (0, 0, 0))
    # #
    # result.paste(img, (padding_left, padding_top))
    # result.show()