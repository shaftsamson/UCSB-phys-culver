#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 15:24:35 2023

@author: samuelculver
"""
import numpy as np

def f(x):
    return np.exp(-(x**2))


num_points = 1000000  # Specify the number of random points
x_min, x_max = -1000, 1000  # Specify the bounds for the x-coordinate
y_min, y_max = 0, 3  # Specify the bounds for the y-coordinate

# Generate random 2D points within the specified bounds
x_values = np.random.uniform(x_min, x_max, num_points)
y_values = np.random.uniform(y_min, y_max, num_points)
points = np.column_stack((x_values, y_values))

n=0
for i in range(num_points):
    if points[i][1] <= f(points[i][0]):
        n+=1
       
ratio=n/num_points
mcarea=(x_max-x_min)*(y_max-y_min)
area=ratio*mcarea #(again even function)
print(area)

#Here we make a collection of random points over the region -1000-1000 and 0-3 for x and y, as this is where the function 
#resides when it is non zero. We then check to see how many of the points reside under the curve, and estimate that 
#this ratio is the same ratio as that of the area under the curve and the while region. This gets our estimate for the integral.
#The more datapoitns we use the more accurate the estimation.