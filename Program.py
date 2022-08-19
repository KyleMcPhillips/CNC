import os
import sys
import PySimpleGUI as sg
import Events
import CustomWindows
# import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import CNCPlot


sg.theme('DarkBlue')   # Add a touch of color

mill = 0


def main():
    starting_window = CustomWindows.create_window('starting_layout', 'CNC Project')
    while True:
        # =============================================================================================== Main Window ==
        # ----- Update Graph if new drawing added -----
        CNCPlot.create_plot()
        # ----- READ WINDOW -----
        event, values = starting_window.read()
        # ----- EVENT: Close window or hit Cancel button -----
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        # ----- EVENT: Hit Restart button -----
        elif event == 'Restart':
            os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
        # ====================================================================================================== Mill ==
        elif event == 'Add Mill':
            mill_window = CustomWindows.create_window('mill_layout', 'New Mill', False, 'c')
            mill_active = True
            while mill_active:
                event, values = mill_window.read()
                if event == sg.WIN_CLOSED or event == 'Cancel':
                    mill_window.close()
                    mill_active = False
                elif event == 'Ok':
                    Events.create_mill(float(values['-X1-']), float(values['-Y1-']), float(values['-X2-']),
                                       float(values['-Y2-']))
                    mill_window.close()
                    mill_active = False
        # ======================================================================================================= Arc ==
        elif event == 'Add Arc':
            arc_window = CustomWindows.create_window('arc_layout', 'New Arc', False, 'c')
            arc_active = True
            while arc_active:
                event, values = arc_window.read()
                if event == sg.WIN_CLOSED or event == 'Cancel':
                    arc_window.close()
                    arc_active = False
                elif event == '-X1-' and values['-X1-'] and values['-X1-'][-1] not in '-0123456789.':
                    arc_window['-X1-'].update(values['-X1-'][:-1])
                elif event == 'Ok':
                    try:
                        Events.create_arc(float(values['-X1-']), float(values['-Y1-']), float(values['-X2-']),
                                          float(values['-Y2-']), float(values['-CENTER_X-']),
                                          float(values['-CENTER_Y-']), values['-CLOCK-'])
                    except Events.EventException:
                        arc_window['-INVALID-'].update(visible=True)
                        continue
                    # ax.add_patch(arc)
                    arc_window.close()
                    arc_active = False
        # ====================================================================================================== Poly ==
        elif event == 'Add Polygon':
            poly_window = CustomWindows.create_window('poly_layout', 'New Polygon', False, 'c')
            poly_active = True
            while poly_active:
                event, values = poly_window.read()
                if event == sg.WIN_CLOSED or event == 'Cancel':
                    poly_window.close()
                    poly_active = False
                elif event == (event == '-NUM_SIDES-' or event == '-CUT_TYPE-') and int(values['-NUM_SIDES-']) == 0:
                    for x in range(1, 31):
                        print("test")
                        poly_window[f'X{x}:'].update(visible=False)
                        poly_window[f'-X{x}-'].update(visible=False)
                        poly_window[f'Y{x}:'].update(visible=False)
                        poly_window[f'-Y{x}-'].update(visible=False)
                elif (event == '-NUM_SIDES-' or event == '-CUT_TYPE-') \
                        and (values['-NUM_SIDES-'] and values['-CUT_TYPE-']):
                    if values['-CUT_TYPE-'] == 'FRM':
                        y = 2
                    else:
                        y = 1
                    for x in range(1, int(values['-NUM_SIDES-'])+y):
                        poly_window[f'X{x}:'].update(visible=True)
                        poly_window[f'-X{x}-'].update(visible=True)
                        poly_window[f'Y{x}:'].update(visible=True)
                        poly_window[f'-Y{x}-'].update(visible=True)
                    for x in range(int(values['-NUM_SIDES-']+y), 31):
                        poly_window[f'X{x}:'].update(visible=False)
                        poly_window[f'-X{x}-'].update(visible=False)
                        poly_window[f'Y{x}:'].update(visible=False)
                        poly_window[f'-Y{x}-'].update(visible=False)
                #elif event == 'Ok':
                #    mill = Events.create_mill(float(values['-X1-']), float(values['-Y1-']),
                #                              float(values['-X2-']),
                #                              float(values['-Y2-']))
                #    poly_window.close()
                #    poly_active = False
    starting_window.close()


if __name__ == "__main__":
    main()
