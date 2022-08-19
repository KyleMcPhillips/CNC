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
import math

CNC_PLOT = {

}
i = 1


def create_plot():
    plt.close('all')
    global CNC_PLOT
    if i == 1:
        return
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

    for key, event in CNC_PLOT.items():
        print(key)
        print(event[0])
        if event[0] == 'Mill':
            plt.plot((event[1][0], event[1][1]), (event[1][2], event[1][3]), linewidth=1, color=(0.1, event[2][0], 0.1),
                     label=key)
        elif event[0] == 'Arc':
            angle1 = math.degrees(math.atan2(event[1][5] - event[1][1], event[1][4] - event[1][0]))
            angle2 = math.degrees(math.atan2(event[1][5] - event[1][3], event[1][4] - event[1][2]))
            if angle1 == angle2:
                angle2 -= 360
            radius = math.hypot(event[1][4] - event[1][0], event[1][5] - event[1][1])
            radius2 = math.hypot(event[1][4] - event[1][2], event[1][5] - event[1][3])
            #if
            #ax.

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    with mpl.rc_context(rc={'interactive': False}):
        fig.canvas.draw()
        plt.gcf().show()


def add_event(event_type, *args):
    global CNC_PLOT
    global i
    CNC_PLOT.update({f'Event {i}': [event_type, args, np.random.rand(1)]})
    i += 1

