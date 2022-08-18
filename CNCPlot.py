import os
import sys
import PySimpleGUI as sg
import pandas as pd
import Events
import CustomWindows
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Wedge

CNC_PLOT = {

}


def create_plot():
    global CNC_PLOT
    fig, ax = plt.subplots()
    fig.canvas.manager.window.setGeometry(50, 100, 640, 545)
    ax.set_aspect('equal')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    fig.patch.set_facecolor('xkcd:slate grey')
    ax.set_facecolor('xkcd:grey')

    print(CNC_PLOT)

    #i = 1
    #for event in CNC_PLOT:
    #    plt.plot((event[0], event[1]), linewidth=1, color=np.random.rand(3), label=f'Event {i}')
    #    i += 1
#
    #plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    #with mpl.rc_context(rc={'interactive': False}):
    #    fig.canvas.draw()
    #    plt.gcf().show()


def add_event(name, *args):
    global CNC_PLOT
    CNC_PLOT.append(name, *args)
