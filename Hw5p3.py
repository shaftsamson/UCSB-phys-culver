#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 09:00:58 2023

@author: samuelculver
"""


import numpy as np
import matplotlib.pyplot as plt

# Create a 2D array of zeros
image = np.zeros((512, 512))

# Sets the pixels for the legs of the triangles
image[50:70, 50:450] = 1
image[50:350, 430:450] = 1


#sets the pixels for the hypotenuse
for i in range(400):
    image[25+int(.75*i):50+int(.75*i),50+i]=1

#sets the overlap of the legs and hypotenuse back to white
image[25:50,50:84]=0
for i in range(26):
    image[50+int(.75*i):75+int(.75*i),50+i]=0
for i in range(26):
    image[331+int(.75*i):350+int(.75*i),425+i]=0

# Display the image
plt.imshow(image, cmap='Blues')


# Set the axis limits
plt.xlim(0, 512)
plt.ylim(0, 512)



# Show the plot
plt.show()

#to make the plot sharper, we could easily increase the pixel number

