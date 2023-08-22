#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 11:47:38 2023

@author: samuelculver
"""


import numpy as np

import time
trials=1000000
totaltime=0


for i in np.arange(trials):
    
    starttime=time.perf_counter()
    pass
    endtime=time.perf_counter()
    elapsedtime=endtime-starttime
    totaltime+=elapsedtime
print('nothing time')
print(totaltime/trials)
print('')
#this code measures the time a comand take for any amount of trials and averges them. The output is 
#usually around 1*10^-7 for pass. This will work for any comand.

trials=1000000
totaltime=0


for i in np.arange(trials):
    
    starttime=time.perf_counter()
    1.1+2.5
    endtime=time.perf_counter()
    elapsedtime=endtime-starttime
    totaltime+=elapsedtime
print('Float additon time')
print(totaltime/trials)
print('')

trials=1000000
totaltime=0

trials=1000000
totaltime=0


for i in np.arange(trials):
    
    starttime=time.perf_counter()
    3.4*4.4
    endtime=time.perf_counter()
    elapsedtime=endtime-starttime
    totaltime+=elapsedtime
print('pfloat multiply time')
print(totaltime/trials)
print('')

for i in np.arange(trials):
    
    starttime=time.perf_counter()
    1.5/20.8
    endtime=time.perf_counter()
    elapsedtime=endtime-starttime
    totaltime+=elapsedtime
print('float division time')
print(totaltime/trials)
print('')


trials=1000000
totaltime=0


for i in np.arange(trials):
    
    starttime=time.perf_counter()
    20/5
    endtime=time.perf_counter()
    elapsedtime=endtime-starttime
    totaltime+=elapsedtime
print('intiger division time')
print(totaltime/trials)
print('')

trials=1000000
totaltime=0

l=50
lista=list(range(l))
for i in np.arange(trials):
    
    starttime=time.perf_counter()
    lista.append(1)
    endtime=time.perf_counter()
    elapsedtime=endtime-starttime
    totaltime+=elapsedtime
print('append time')
print(totaltime/trials)
print('')
#there seems to be no corellation of append time and list length


def function1():
    pass
    return


for i in np.arange(trials):
    
    starttime=time.perf_counter()
    function1()
    endtime=time.perf_counter()
    elapsedtime=endtime-starttime
    totaltime+=elapsedtime
print('call a function with nothing')
print(totaltime/trials)
print('')


def function2():
    2.22+3.54
    return


for i in np.arange(trials):
    
    starttime=time.perf_counter()
    function2()
    endtime=time.perf_counter()
    elapsedtime=endtime-starttime
    totaltime+=elapsedtime
print('call a function adding floats')
print(totaltime/trials)
print('')

#no input
#output
#nothing time
#8.744616448711895e-08

#Float additon time
#8.70548957191204e-08

#pfloat multiply time
#8.595700630939974e-08

#float division time
#1.7183892692264634e-07

#intiger division time
#8.574112764472374e-08

#append time
#1.233609081755276e-07

#call a function with nothing
#2.548334341681766e-07

#call a function adding floats
#3.8236855403010847e-07





