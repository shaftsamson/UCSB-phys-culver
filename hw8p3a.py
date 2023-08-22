#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 13:36:26 2023

@author: samuelculver
"""

import os

path='/bin/ls'
argument=['ls','-l']

os.execv(path, argument)

#when we run this we get an output of all files and directories in the current directory, 
#just like ls in the terminal! It also terminates the current run

