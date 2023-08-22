#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 13:33:47 2023

@author: samuelculver
"""

import numpy as np
import matplotlib.pyplot as plt

# Create a 2D array of zeros

res=512


#makes two arrays for the plot, change the bounds to change the area of interest
ax=-1
bx=1

ay=-1
by=1

x = np.linspace(ax, bx, res)
y = np.linspace(ay, by, res)


#this makes it a 2d array, adding the terms together. This is a specefied region of the complex plane
c= x[:,np.newaxis]+1j*y[np.newaxis,:]

z = np.zeros_like(c)
pixel=np.zeros((res,res))

iterations=250

#this sets each diverging point in c the the number of iterations it took to be >=2 in the pixels array. This gets a cool coolor gradient
for i in range(iterations):
    trufal=np.abs(z)>2
    pixel[trufal]=i
    z=z**2+c



plt.imshow(pixel, cmap='cool', extent=[ax , bx , ay, by])
plt.show()