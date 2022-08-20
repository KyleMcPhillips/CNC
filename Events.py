import math
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd
import CNCPlot


class EventException(Exception):
    pass


def create_mill(x1, y1, x2, y2,):
    CNCPlot.add_event('Mill', x1, x2, y1, y2)


def create_arc(x1, y1, x2, y2, center_x, center_y, clock):

    angle1 = math.degrees(math.atan2(center_y-y1, center_x-x1))
    angle2 = math.degrees(math.atan2(center_y-y2, center_x-x2))
    if angle1 == angle2:
        angle2 = angle1 - 360

    # Confirm that entered points create valid circle
    radius = math.hypot(center_x-x1, center_y-y1)
    radius2 = math.hypot(center_x-x2, center_y-y2)
    if radius != radius2:
        raise EventException("Invalid Points")

    if clock == 'CW':
        wedge = Wedge((center_x, center_y), radius, angle2 + 180, angle1 + 180, color=np.random.rand(3), width=0.01,
                      fill=False, label=getName())
    elif clock == 'CCW':
        wedge = Wedge((center_x, center_y), radius, angle1 + 180, angle2 + 180, color=np.random.rand(3), width=0.01,
                      fill=False, label=getName())
    else:
        raise EventException("Invalid Input, please enter 'CC' or 'CCW'")

    CNCPlot.add_event('Arc', x1, y1, x2, y2, center_x, center_y, clock)


# def create_poly():
