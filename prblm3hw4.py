#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 09:08:12 2023

@author: samuelculver
"""

a=int(input('Enter n here: '))
fib1=1
fib2=1

for i in range(a):
    
    print(fib1)
    fib1, fib2=fib2, fib1+fib2
    if fib1 > 10**75:
        break
    
    

#input
#1
#1
#2
#3
#5
#8
#13
#21
#34
#55