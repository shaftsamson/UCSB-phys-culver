#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 16:30:28 2023

@author: samuelculver
"""

import numpy as np
import matplotlib.pyplot as plt
import time

def DFT(data):

    length=len(data)
    DFT_list=np.zeros(length, dtype = 'complex_')
    sum_list=np.zeros(length, dtype = 'complex_')
    for i in range(length):
        y=0
        for item in data:
            x=item*np.exp((-(1j*2*np.pi*i*y))/length)
            sum_list[y]=x
            y=y+1
        n_entry=np.sum(sum_list)
        DFT_list[i]=n_entry
    return DFT_list

#compare the run times

x=np.random.random(1024)

start = time.time()
transform_np=np.fft.fft(x)
end = time.time()
time1=end-start
print('Numpy time:')
print(time1)


print()

start = time.time()
transform_DFT=DFT(x)
end = time.time()
time2=end-start
print('Homegrown time:')
print(time2)

print()

ratio=time2/time1

print('Ratio of homegrown vs np times', ratio)

datapoint=12
numpydata=np.zeros(datapoint)
homegrowndata=np.zeros(datapoint)

#make the time data points

for i in range(datapoint):
    x=np.random.random(2**i)
    start = time.time()
    transform_np=np.fft.fft(x)
    end = time.time()
    time1=end-start
    numpydata[i]=time1
    
    
    start = time.time()
    transform_DFT=DFT(x)
    end = time.time()
    time2=end-start
    homegrowndata[i]=time2

length=np.zeros(datapoint)
for i in range(datapoint):
    length[i]=2**i
    
plt.loglog(length, numpydata,label= 'Numpy data')
plt.loglog(length, homegrowndata,label= 'Homegrown Data')


plt.legend()
# Set plot labels and title
plt.xlabel('Length of Sequence')
plt.ylabel('Time of Execution (s)')
plt.title('Time of Discrete Fourier Transform vs Sequence Length (loglog)')

# Display the plot
plt.show()
    
#slope of the logscale data
slope_homegrown, _ = np.polyfit(np.log10(length),np.log10(homegrowndata) , deg=1)
slope_numpy, _=np.polyfit(np.log10(length),np.log10(numpydata) , deg=1)
print()
print("Homegrown slope (logscale):", slope_homegrown)
print("Numpy slope (logscale):", slope_numpy)

#If a plot appears linear in loglog scale, then the data is following a power law,
# and slope of the line is the power. 

print('Execution time scaling is to the',slope_homegrown, 'power for the coded DFT, and',slope_numpy, 'for the numpy DFT')



#We start by creating our own fourier transform function. This is doen with nested for
#loops, as each fourier transform data point is affected by each point in the original 
#sequenece by the transform formula. Comparing this function to the np.fft.fft the exact 
#transformation is applied to the arrays so it appears it is functional. After 
#inspecting some run times an oddity becomes apparent which is that the function I created
#is reletively consistent but the numpy is greatly variable, and also much faster than the
#one I created. When I plot the times of execution for different sequence lengths in loglog we 
#get an essentially linear relationship for the coded DFT times, which means that computation 
#time increases by power rule with longer sequences, which makes sense with the way DFTs are defined 
#and the nested for loop I used to compute them. The numpy DFT on the other hands is almost unpredicable 
#in the speed with which it executes, and the slope of line of best fit and therefore power rule 
#are not accurate, as the data does not appear linear in logscale. 








