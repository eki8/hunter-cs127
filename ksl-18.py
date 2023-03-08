#Name: Egor Kislykh
#Email: egor.kislykh24@myhunter.cuny.edu
#Date: Mar 7, 2023
#This is program number 18

import numpy as np
import matplotlib.pyplot as plt

size = int(input("Input the size: "))
name = input("Inpur the name: ")

img = np.zeros((size, size, 3))
img[::2, :, ::2] = 1
img[1::2, :, 0:2] = 1

plt.imsave(name, img)

#plt.imshow(img)
#plt.show()
