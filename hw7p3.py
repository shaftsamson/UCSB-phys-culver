#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 17:09:55 2023

@author: samuelculver
"""

import numpy as np
import matplotlib.pyplot as plt

#sunlight data
sunlight_data=np.loadtxt('/Users/samuelculver/Downloads/sunlight.txt')

#LED data
LED_data=np.loadtxt('/Users/samuelculver/Downloads/LEDlight.txt')

timesun=sunlight_data[:,0]
timeLED=LED_data[:,0]

ft_sunlight=np.fft.fft(sunlight_data[:,1])
ft_LED=np.fft.fft(LED_data[:,1])

norm_sun=np.abs(ft_sunlight[1:])
norm_LED=np.abs(ft_LED[1:])

ps_sun=(norm_sun**2)
ps_LED=norm_LED**2


xvals_LED=np.fft.fftfreq(len(ps_LED),.001087)

f1,ax1=plt.subplots()
ax1.plot(xvals_LED,ps_LED)
ax1.set_xlim(0,200)
ax1.set_title('LED Power Spectrum')
ax1.set_xlabel('Frequency (Hz)')
ax1.set_ylabel('Relative Intensity')
f1.show()


xvals_sun = np.fft.fftfreq(len(ps_sun),.001087)

f2, ax2 = plt.subplots()
ax2.plot(xvals_sun,ps_sun)
ax2.set_xlim(0,400)
ax2.set_title('Sunlight Power Spectrum')
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Relative Intensity')
f2.show()


#In this code I use numpy to compute the DFT of the two datafiles after loading them with loadtxt.
#Only the right hand column of the data is relevant to this, so I slice it. (The left column is just 
#repeated time increments. I also slice out the first entry as there are issues with the plot 
#if there is a zero frequency component. Then the DFT squared is plotted against the frequencies, which
# is calculated with np.fft.fftfreq. We see classic power series spikes in the result. This makes 
#sense for the LED as it is powered by AC current probably at a frequency of 60 Hz, but the frequency 
#is doubled by the data as it has no way of distinguishing which way the current is travelling, only 
#if the light is on or off. So the spike on the LED graph makes sense to be at 120 Hz. The sunlight spikes 
#are more novel, as I have no idea why sunlight intensity would be varying as sinusoidally. We see
#2 spikes, one at 60 Hz and one at 70 Hz, with the 60Hz peak about twice as large. For refrence these
#Peaks are much smaller than the LED peak, implying the Relative intensity with these oscillations is 
#much smaller than the LED, which makes sense. My thought for why they exist at all is that they are due to '
#the instrumentation not actual sunlight oscillations. Potentially the machine being powered by 609 Hz
#AC makes slight variaitions in the data that can be picked up by a power spectrum. 



