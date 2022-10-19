import glob
from PIL import Image


path = "M:\DOKUMENTY\KUBA HALT\sesja_na_insta"


def padding(img, i, rgb):
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

    left = [1, 3, 7, 9]
    right = [4, 6, 10, 12]
    center = [2, 8]
    if (i in left):
        padding_left = int((new_width - old_width) / 4)
    elif (i in right):
        padding_left = int(((new_width - old_width) / 4) * 3)
    else:
        padding_left = int((new_width - old_width) / 2)

    padding_top = int((new_height - old_height) / 2)

    result = Image.new(img.mode, (new_width, new_height), rgb)
    result.paste(img, (padding_left, padding_top))
    return result


# opening all images from folder
images = []

for f in glob.iglob(path + "\*"):
    images.append(Image.open(f))

i = 0
for img in images:
    i += 1
    padding(img, i, (0, 0, 0)).save(path + "\JZ_black_%d.jpg" % i)
    padding(img, i, (255, 255, 255)).save(path + "\JZ_white_%d.jpg" % i)
