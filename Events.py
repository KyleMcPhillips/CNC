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

    CNCPlot.add_event('Arc', x1, y1, x2, y2, center_x, center_y, clock)


def create_poly(poly_type, num_sides, coords):
    lines = []
    if poly_type == 'PKT':
        for x in range(0, len(coords)-1):
            lines.append([coords[x][0], coords[x][1], coords[x+1][0], coords[x+1][1]])
        lines.append([coords[len(coords)-1][0], coords[len(coords)-1][1], coords[0][0], coords[0][1]])
        print(lines)
    elif poly_type == 'FRM':
        for x in range(0, len(coords) - 1):
            lines.append([coords[x][0], coords[x][1], coords[x + 1][0], coords[x + 1][1]])
        print(lines)

    CNCPlot.add_event('Poly', lines, poly_type)
