#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 16:42:07 2023

@author: samuelculver
"""

with open("myfile.txt", "w") as f:
    f.write(input("Write the first line of text here: "))
    f.write('\n')
    f.write(input("Write the second line of text here: "))
