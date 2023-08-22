#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:58:30 2023

@author: samuelculver
"""


import numpy as np

f=open(input("Enter file name here: "),"r")
print(np.mean(f.readlines()))
