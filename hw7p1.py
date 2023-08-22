#!/usr/bin/env python3
#
# stripchart.py
#
# 11May16  Many improvements by Ben LaRoque
# 10May16  Adapted from 
#             http://matplotlib.org/examples/animation/strip_chart_demo.html
#          by Everett Lipman
#
"""
Emulate an oscilloscope.  Requires the animation API introduced in
matplotlib 1.0 SVN.
"""
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


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
        self.ax.set_ylim(-1.1, 1.1)
        self.ax.set_xlim(0, self.maxt)

    def update(self, data):
        t,y = data
        self.tdata = np.append(self.tdata, t)
        self.ydata = np.append(self.ydata, y)
        self.ydata = self.ydata[self.tdata > (t-self.maxt)]
        self.tdata = self.tdata[self.tdata > (t-self.maxt)]
        self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
        self.ax.figure.canvas.draw()
        self.line.set_data(self.tdata, self.ydata)
        return self.line,

    def emitter(self, w=np.pi):
        while True:
            t = time.perf_counter() - self.t0
            y=np.sin(w*t)
            yield t,y

if __name__ == '__main__':
    dt = 0.01
    fig, ax = plt.subplots()
    scope = Scope(ax, maxt=10, dt=dt)
    ani = animation.FuncAnimation(fig, scope.update, scope.emitter(.1), interval=dt*1000., blit=True)
##    plt.title('Sin(wt) vs t')
  #  plt.ylabel('Sin(wt)')
  #  plt.xlabel('t (s)')
   ## plt.show()
    
#here the major modifications to get it to graph sin are in the emmiter definition. I have removed the previous
#code and replaced it with a sin function that is a funtion of t. Since t has been defined with the perferation 
#counter it is changing with time and therefore the sin funtion is as well, which leads to the graph changind at
#a rate chosen in the definition of t. 
