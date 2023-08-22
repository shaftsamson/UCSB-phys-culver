#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 22:03:11 2023

@author: samuelculver
"""

import numpy as np
import matplotlib.pyplot as plt

N=input('Enter nuumber of points here: ')
N=int((int(N)))

x_vals=np.random.uniform(0,2,N)

y_vals=np.random.uniform(0,2,N)


count=0
for i in range(N):
    Rad=(x_vals[i]-1)**2+(y_vals[i]-1)**2
    if Rad <= 1:
        count=count+1        
pi=4*(count/N)

print('Pi estimated by Monte Carlo Method', pi)

#This program estimates the value of pi using the monte carlo estimation. It does so by generating
#a user specified number of randomly distributed points in the square 0-2 for x and y, and using the
#relation A=pi*r^2 for a circle and A=4*r^2 for a square to create a relation for pi. Because the ponts 
#are uniformly generated the area for the circle and square are directly related to the points enclosed
#within them, so the ratio time 4 is eqaul to an approximation for pi. The more datapoints we use the 
#more accurate the estimation will be. 