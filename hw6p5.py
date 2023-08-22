#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 20:03:11 2023

@author: samuelculver
"""

import matplotlib.pyplot as plt
import numpy as np

x_lower,x_upper=0,5*np.pi
y_lower,y_upper=-1,1

x=np.linspace(x_lower, x_upper,500)




tantheta = np.tan(x)
sintheta=np.sin(x)

plt.plot(x, sintheta, "-g", label="sine")


# Insert a NaN where the difference between successive points is negative.
# This removes the vertical line you get when you just use np.tan

tantheta[:-1][np.diff(tantheta) < 0] = np.nan

# Plot the result




plt.plot(x, tantheta, "-b", label="tan")

#makes a legend for the plot

plt.legend(loc="lower left")



#controls field of view
plt.axis([x_lower,x_upper,-1.5,1.5])
plt.ylabel('sine(theta), tan(theta)')
plt.xlabel('theta')
plt.title('sine and tan vs theta')
plt.show()

#This code creates a set of data using np.lispace with 500 points and makes 2 sets of y data 
#from this x list, using np.sin and np.tan. The tan function is undefined when it jumps from
#+ infinity to - infinity, which is also the only point that the next enry in the array is less than the prev.
#using this and np.diff, and np.nan, you can remove these vertical lines from the tan function. 
#finally a few plt functions are called to make axes, title and legend