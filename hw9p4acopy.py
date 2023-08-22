#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 13:04:10 2023

@author: samuelculver
"""
import numpy as np

def f(x):
    return np.exp(-(x**2))
   

boxes=1000000 
x_range=1000
x=np.linspace(0,x_range,boxes)
box_width=x_range/boxes

areas=np.zeros(boxes)
for i in range(boxes):
    areas[i]=box_width*(f(x[i]))
    
area=2*np.sum(areas)  #even function so we can multiply by 2. Saves time by halving the for loop iterations
print(area)

#By increasing the boxes and x range we will get more and more accureate answers. This code creates a set of x data 
#to 1000, as f(1000) and up is essentially zero. From there a specified number of rectangles are cunstructed with 
#a for loop each of which has a height of f(x) and equal width. The sum of the areas of these boxes is the integral 
#over the specified region. By going from 0-1000 and multiplying by 2 we utilize the even function to get the 
#same result that going from -1000 to 1000 would achieve.