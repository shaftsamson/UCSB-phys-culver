#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 22:57:31 2023

@author: samuelculver
"""


import numpy as np
import matplotlib.pyplot as plt


def findpi(N):
    x_vals=np.random.uniform(0,2,N)
    y_vals=np.random.uniform(0,2,N)
    count=0
    for i in range(N):
        Rad=(x_vals[i]-1)**2+(y_vals[i]-1)**2
        if Rad <= 1:
            count=count+1        
    pi=4*(count/N)
    return pi

Ndatapoints=np.arange(10,10000,10)
errordatapoints=np.zeros(len(Ndatapoints))

i=0
for item in Ndatapoints:
    x=findpi(item)
    x=abs(np.pi-x)/np.pi
    errordatapoints[i]=x
    i=i+1
    
    
plt.plot(Ndatapoints,errordatapoints,'.')
plt.ylabel('Fractional Error')
plt.xlabel('Number of Points')
plt.title('Fractional Error From Monte Carlo Approximation vs Data-points')
plt.show()
    

#This proram serves to investigate the relation beyween datapoints and accuracy of the Monte carlo 
#estimation to find the value of pi and the number of data-points. It runs through 1000 iterations 
#of the estimation for values of N from 10 to 10000, and plots the fractional error vs N. We can see 
#that as the number of iterations increases the fractional error decreases, but is still relatively
#variable even at very high datapoints.
