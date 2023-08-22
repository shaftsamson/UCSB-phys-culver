#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 12:36:32 2023

@author: samuelculver
"""

import numpy as np
import matplotlib.pyplot as plt

def flips():
    
    heads=0
    for i in range(100):
        x=np.random.randint(0,2)
        if x==0:
            heads+=1
    return heads



N=1000
data=np.zeros(1000)
for i in range(N):
    data[i]=flips()
    


 
plt.hist(data,bins= 30,density=True,label='Coin flip data')
plt.xlim(0,100)
#plt.title('Heads flipped from 100 coin flips and the predicted gaussian distribution')
plt.xlabel('Heads flipped')
plt.ylabel('Normalized count')

x=np.linspace(0,100,1000)
y=1/(np.sqrt(2*np.pi)*5)*(np.e)**((-(x-50)**2)/50)

plt.plot(x,y, label='Gaussian curve')
plt.legend()
plt.show()