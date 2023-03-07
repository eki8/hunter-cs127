#Name: Egor Kislykh
#Email: egor.kislykh24@myhunter.cuny.edu
#Date: Mar 6, 2023
#This is program number 17

import matplotlib.pyplot as plt
import numpy as np

def blue(slice, a, b, c, d):
    slice[a:b, c:d, 0:2] = 0
    slice[a:b, c:d, 2] = 255
    return slice

name = input("Enter file name: ")

img = np.zeros((30,30,3))
img[:, :, 1] = 255
img[:, :, 0] = 255

img = blue(img, 3, 26, 4, 7)
img = blue(img, 13, 16, 4, 26)
img = blue(img, 24, 27, 4, 26)
img = blue(img, 15, 27, 23, 26)

plt.imsave(name, img)

#plt.imshow(img)
#plt.show()
