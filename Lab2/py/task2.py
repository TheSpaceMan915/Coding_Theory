from PIL import Image
import numpy as np


file_path = '../files/circles.bmp'
img = Image.open(file_path)

#getting array of pixels from the image
arr_pixels = np.array(img.getdata())

#going through the array and saving the first element, then the second and then the third
red = [(p[0], 0, 0) for p in arr_pixels]
green = [(0, p[1], 0) for p in arr_pixels]
blue = [(0, 0, p[2]) for p in arr_pixels]

img.putdata(red)
img.save('../files/red.png')
img.putdata(green)
img.save('../files/green.png')
img.putdata(blue)
img.save('../files/blue.png')