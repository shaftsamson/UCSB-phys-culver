#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 12:44:39 2023

@author: samuelculver
"""

a=input('Enter an angle in degrees: ')
b=input('Enter the number of terms to sum in a series: ')

floata,floatb=float(a),float(b)
rad_angle=floata*0.0175

def sind(x):
    def factorial(m):
        result = 1
        for i in range(1, m+1):
            result *= i
        return result
            
    list_sums=[]
    for n in range(int(floatb)+1):
        term=(((-1)**n)/(factorial(2*n+1)))*(x**(2*n+1))
        list_sums.append(term)
    return(sum(list_sums))



print('sind of angle:', sind(rad_angle))

import math

print('sin using math:', math.sin(rad_angle))

print('difference between the two:', abs(sind(rad_angle)-math.sin(rad_angle)))

print('ratio of sind()/math.sin():', (sind(rad_angle))/(math.sin(rad_angle)))

#in 40, 10

#out
#sind of angle: 0.6442176872376911
#sin using math: 0.6442176872376911
#difference between the two: 0.0
#ratio of sind()/math.sin(): 1.0