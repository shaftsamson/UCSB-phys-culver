#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 17:09:17 2023

@author: samuelculver
"""

import os
import time

n=0
i=0
while n==0:
    i+=1
    print(i)
    
    if i%10==0:
        print('-Fork imminet- prepare your constitution')
        retval = os.fork()
        child = (retval == 0)
        if child:
            print('The child will now be sacraficed. The good of many outweighs the good of all, and donating its pure flesh to our heavenly creators will execute the ls command')
            
            path='/bin/ls'
            argument=['ls','-l']
            os.execv(path, argument)
    time.sleep(.5)
        

        
#This code serves to repeatedly use the ls -l command in the terminal. We do so by creating an unbounded 
#while loop which repeatedly counts and prints asceding intigers startimg with one every .5 second. Every ten we enter a 
#sfork, and the child immediately performs the os.execv to list the files and derectories of the current 
#directory. The execv cmomand also terminates the child, so we are just left with the parent which cotinues the loop.
#This will repeat until the user stops it.