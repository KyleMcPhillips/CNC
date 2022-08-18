import math
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd
import CNCPlot

eventNum = 0


class EventException(Exception):
    pass


def getName():
    global eventNum
    eventNum += 1
    return f"Event{eventNum}"


def create_mill(x1, y1, x2, y2,):
    CNCPlot.add_event(x1, x2, y1, y2)


def create_arc(x1, y1, x2, y2, center_x, center_y, clock):

    # Get starting points
    # x1 = int(input("X1: "))
    # y1 = int(input("Y1: "))
    # x2 = int(input("X2: "))
    # y2 = int(input("Y2: "))
    # center_x = int(input("Center of Circle X: "))
    # center_y = int(input("Center of Circle Y: "))

    angle1 = math.degrees(math.atan2(center_y-y1, center_x-x1))
    angle2 = math.degrees(math.atan2(center_y-y2, center_x-x2))
    print(f"Angle of center of circle to 1st coordinate: {angle1}")
    print(f"Angle of center of circle to 2nd coordinate: {angle2}")
    if angle1 == angle2:
        angle2 = angle1 - 360
    # Confirm that entered points create valid circle
    radius = math.hypot(center_x-x1, center_y-y1)
    radius2 = math.hypot(center_x-x2, center_y-y2)
    if radius != radius2:
        raise EventException("Invalid Points")
    print(f"Radius: {radius}")

    # Get direction of cut, and determine path
    # clock = input("Clockwise/Counterclockwise? (CC/CCW): ")
    if clock == 'CW':
        wedge = Wedge((center_x, center_y), radius, angle2 + 180, angle1 + 180, color=np.random.rand(3), width=0.01,
                      fill=False, label=getName())
    elif clock == 'CCW':
        wedge = Wedge((center_x, center_y), radius, angle1 + 180, angle2 + 180, color=np.random.rand(3), width=0.01,
                      fill=False, label=getName())
    else:
        raise EventException("Invalid Input, please enter 'CC' or 'CCW'")

    CNCPlot.add_event(wedge)


# def create_poly():
