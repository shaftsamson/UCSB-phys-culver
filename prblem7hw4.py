#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 17:22:48 2023

@author: samuelculver
"""

import matplotlib.pyplot as plt

with open('wind.dat') as f:
    lines = f.readlines()


times = []
speeds = []
uncertainties = []
for line in lines:
    time, speed, uncertainty = line.split()
    times.append(float(time))
    speeds.append(float(speed))
    uncertainties.append(float(uncertainty))

# Plot data
plt.errorbar(times, speeds, yerr=uncertainties, fmt='o', capsize=3)
plt.xlabel('Time (hours)')
plt.ylabel('Average wind speed (knots)')
plt.title('Wind speed data')
plt.show()

