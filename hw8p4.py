#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 16:46:08 2023

@author: samuelculver
"""


import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import threading



class Scope(object):
    def __init__(self, ax, maxt=2, dt=0.02):
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = np.array([])
        self.ydata = np.array([])
        self.t0 = time.perf_counter()
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(-1, 101)
        self.ax.set_xlim(0, self.maxt)

    def update(self, data):
        t, y = data
        self.tdata = np.append(self.tdata, t)
        self.ydata = np.append(self.ydata, y)
        self.ydata = self.ydata[self.tdata > (t - self.maxt)]
        self.tdata = self.tdata[self.tdata > (t - self.maxt)]
        self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
        self.ax.figure.canvas.draw()
        self.line.set_data(self.tdata, self.ydata)
        return self.line,

    def emitter(self):
        global value
        while True:
            t = time.perf_counter() - self.t0
            v = value
            yield t, v
    
def global_var():
    global value
    while True:
        raw_value = input('Enter a number between 1 and 100: ')
        try:
            value = float(raw_value)
        except ValueError:
            print('Only numbers accepted')
    

thr = threading.Thread(target=global_var,args=())
thr.start()
value=0

if __name__ == '__main__':
    dt = 0.01
    fig, ax = plt.subplots()
    scope = Scope(ax, maxt=10, dt=dt)
  
    ani = animation.FuncAnimation(fig, scope.update, scope.emitter, interval=dt * 1000., blit=True, cache_frame_data=False)
    plt.ylabel('Global Variable')
    plt.xlabel('time(s)')
    plt.show()


#this serves to create a running plot displaying the user entered value, and utilizes
#threading and global variables to do so. We keep much of the stripchart the same 
#exept we simplifid the emmiter defenition to just contain the time and our global variable.
#We then define a function that creates the global variable and runs into an infnite 
#while loop that will indefinitely prompt for a number to be entered that is assigned
#to the global variable. There is a check that there is no error so an incompatable entry
#just does nothing. We then use threading to create a thread that runs through this function
#while the animated plot is executed the same as other stripcharts. We start the global 
#variable at 0 and when the user changes it the change is reflected on the plot. 
