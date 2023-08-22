#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 20:47:07 2023

@author: samuelculver
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson



def detections(array_size):
    
    lower_bound = 0
    upper_bound = 10000
    
    random_array = np.random.randint(lower_bound, upper_bound, size=array_size)
    
    i=0
    for item in random_array:
        if item < 45:
            i+=1
            
    return i


data=np.zeros(1000)

for i in range(1000):
    data[i]=detections(1000)
    
bin_width = 1  # Specify the desired bin width
bin_edges = np.arange(min(data), max(data) + bin_width, bin_width)  # Calculate the bin edges

x=np.arange(0,50,1)
mean=1000*(45/10000)
STDEV=mean**(1/2)

y = 1000*poisson.pmf(x, mu=mean)  #the 1000 to scale the diatribution to the histogram 

plt.plot(x,y)




plt.hist(data, bins=bin_edges, edgecolor='black')  # Setting the number of bins and edgecolor for the histogram
plt.xlim(0, 15)  # Set the x-axis range
custom_ticks = np.arange(0, 15, 1)  # Define the desired tick locations
plt.xticks(custom_ticks) 
plt.xlabel('Detections')  # Label for the x-axis
plt.ylabel('Occurences')  # Label for the y-axis
plt.title('Photon detection after 1000 simulations')  # Title of the histogram
plt.show()  # Display the histogram

#With this code I created a simulation for the detection of photons and plotted the results as a histogram.
#I then compared this to a poisson distribution from the scypi library and we see decent correlation. 



