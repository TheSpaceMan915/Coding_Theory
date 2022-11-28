from PIL import Image
import numpy as np


#translating the image to gray colours and saving it
img = Image.open('../files/circles.bmp')
img = img.convert('L')
img.save('../files/slices/circles_gray.jpg')

#converting the image to the array of tuples
arr = np.asarray(img)

print(arr.shape[0])
print(arr.shape[1])

#changing each element of arr on 1. In order to multiply the array on 2 afterwards
fltr = np.array([[1 for i in range (arr.shape[1])] for j in range (arr.shape[0])])

#getting byte slices
for i in range(0,7):
    fltr *= 2
    Image.fromarray(fltr&arr).convert('L').save('../files/slices/slice' + str(i) + '.png')