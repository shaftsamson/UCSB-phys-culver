#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 18:25:16 2023

@author: samuelculver
"""

import numpy as np
import matplotlib.pyplot as plt


x=512
y=384
values=np.zeros((y,x))

ax,bx,ay,by=-.8,-.6,0,.3
xvals=np.linspace(ax,bx,512)
yvals=np.linspace(ay,by,384)

for j in range(y):
   for i in range(x):
       z=0
       for n in range(250):
          z=z**2+xvals[i]+1j*yvals[j]
          if np.abs(z)>=2:
              values[j,i]=n
              break


plt.imshow(values, cmap='hot', extent=[ax , bx , ay, by])
plt.show()
        


#takes about 10-20 seconds from the tripple for loop but works very well