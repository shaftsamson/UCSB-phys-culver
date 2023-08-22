#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 09:08:58 2023

@author: samuelculver
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import j1
#j1 is the first order bessel function which is in the airy pattern.

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#  x, y coordinates. 
x = np.linspace(-15, 15, 100)
y = np.linspace(-15, 15, 100)

#plot_surface needs 3 2d arrays, so np.meshgrid works well
X, Y = np.meshgrid(x, y)

#here i make the airy function
r = np.sqrt(X**2 + Y**2)
Z = (2 * j1(r) / r)**2


#make z logscale to see more rings
Zlog=np.log10(Z)


# Plot the surface
ax.plot_surface(X, Y, Zlog,cmap='Reds')
ax.set_xlabel('x (arcseconds)')
ax.set_ylabel('y (arcseconds)')
ax.set_zlabel('intensity (log10(arcseconds))', labelpad=-2, fontsize=8)
fig
plt.show()

#This creates 2d arrays spanning from -15 to 15 for X and Y from linspce arrays and using np.meshgrid,
# then makes a 3d airy surfave using the bessel function from scipy and assigning it to Z. 
#We then plot log(Z) against X and Y to get a logscale of the airy functions ar 3d surfaces.