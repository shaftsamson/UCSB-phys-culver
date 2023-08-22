#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 09:43:20 2023

@author: samuelculver
"""

import numpy as np
import matplotlib.pyplot as plt

N = int(input('Enter the number of data points: '))

if N >100:
    N=100
    print('Overflow data points. Number of data points was set to 100')

x_vals = np.random.uniform(0, 1000, N)
y_vals = np.random.uniform(0, 1000, N)

lin_coefficients = np.polyfit(x_vals, y_vals, 1)
N_3_coefficients = np.polyfit(x_vals, y_vals, N - 3)
N_1_coefficients = np.polyfit(x_vals, y_vals, N - 1)

x_vals_func = np.linspace(0, 1000, 1000)

lin_curve = np.polyval(lin_coefficients, x_vals_func)
N_3_curve = np.polyval(N_3_coefficients, x_vals_func)
N_1_curve = np.polyval(N_1_coefficients, x_vals_func)

plt.plot(x_vals, y_vals, 'rx', label='Data Points')
plt.plot(x_vals_func, lin_curve, label='Degree 1')
plt.plot(x_vals_func, N_3_curve, label='Degree N-3')
plt.plot(x_vals_func, N_1_curve, label='Degree N-1')

plot_title='Polynomial Curve Fits for ' + str(N) +' Data-points'

plt.xlabel('x')
plt.ylabel('y')
plt.title(plot_title)
plt.legend()

plt.xlim(-10, 1000)
plt.ylim(-10, 1000)

plt.show()

#This script serves to make three plynomial fits for a user specified number of random data points in 
#the range 0-1000 for x and y. It does so using numpys polyfit function and numpys polyvals to then 
#construct the actual polynomials. The Degrees for the three fits are 1, 3 less than the input data points
#and 1 less than the input data points. An interesting result is that as the data points increase, the fits 
#for the latter 2 functions begin to become nearly the same function. Legends and titles are made in the 
#ususal way. There is a limit of 100 data points to prevent overflow.




