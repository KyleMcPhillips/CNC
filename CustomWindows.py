import PySimpleGUI as sg


title_font = ('Verdana', 40)
sub_font = ('Verdana', 10)
button_font = ('Verdana', 15)


def create_window(layout, window_name, borderless=False, justification='l'):
    if layout == 'starting_layout':
        layout = [
            [sg.Text('SELECT EVENT', font=title_font), sg.Push(),
             sg.Button('Restart', button_color=('red', 'black'), font=button_font)],  # Line 1
            [sg.Button('Add Mill', font=button_font), sg.Button('Add Arc', font=button_font),
             sg.Button('Add Polygon', font=button_font), sg.Button('Undo', font=button_font), sg.Push(),
             sg.Button('Cancel', font=button_font, button_color=('black', 'grey'))]  # Line 3
        ]
    elif layout == 'mill_layout':
        layout = [
            [sg.Text('New Mill')],  # Line 1
            [sg.Text('X1:'), sg.Input(key='-X1-', default_text='0.0', size=(10, 1), enable_events=True),
             sg.Text('Y1:'), sg.Input(key='-Y1-', default_text='0.0', size=(10, 1), enable_events=True)],  # Line 2
            [sg.Text('X2:'), sg.Input(key='-X2-', default_text='0.0', size=(10, 1), enable_events=True),
             sg.Text('Y2:'), sg.Input(key='-Y2-', default_text='0.0', size=(10, 1), enable_events=True)],  # Line 3
            [sg.Button('Ok'), sg.Button('Cancel')]  # Line 4
        ]
    elif layout == 'arc_layout':
        layout = [
            [sg.Text('New Arc')],  # Line 1
            [sg.Text('X1:'), sg.Input(key='-X1-', default_text='0.0', size=(10, 1), enable_events=True),
             sg.Text('Y1:'), sg.Input(key='-Y1-', default_text='0.0', size=(10, 1), enable_events=True)],  # Line 2
            [sg.Text('X2:'), sg.Input(key='-X2-', default_text='0.0', size=(10, 1), enable_events=True),
             sg.Text('Y2:'), sg.Input(key='-Y2-', default_text='0.0', size=(10, 1), enable_events=True)],  # Line 3
            [sg.Text('CenterX:'), sg.Input(key='-CENTER_X-', default_text='0.0', size=(10, 1), enable_events=True),
             sg.Text('CenterY:'), sg.Input(key='-CENTER_Y-', default_text='0.0', size=(10, 1), enable_events=True)],  # Line 4
            [sg.Text('CW/CCW:'),
             sg.Combo(['CW', 'CCW'], default_value='CW', readonly=True, key='-CLOCK-', size=(5, 1),
                      enable_events=True)],  # Line 5
            [sg.Text('Invalid Input', key='-INVALID-', text_color='red', visible=False), sg.Button('Ok'),
             sg.Button('Cancel')]  # Line 6
        ]
    elif layout == 'poly_layout':
        layout = [
            [sg.Text('New Polygon')],  # Line 1
            [sg.Text('FRM/PKT:'),
             sg.Combo(['FRM', 'PKT'], default_value='FRM', readonly=True, size=(5, 1), key='-CUT_TYPE-',
                      enable_events=True),
             sg.Text('Number of Sides:'),
             sg.Slider(range=(0, 20), key='-NUM_SIDES-', size=(15, 15), orientation='h', enable_events=True)]]
        for x in range(1, 31):
            layout.append([sg.Text(f'X{x}:', key=f'X{x}:', visible=False),
                           sg.Input(key=f'-X{x}-', size=(10, 1), enable_events=True, visible=False),
                           sg.Text(f'Y{x}:', key=f'Y{x}:', visible=False),
                           sg.Input(key=f'-Y{x}-', size=(10, 1), enable_events=True, visible=False)])
        layout.append([sg.Button('Ok'), sg.Button('Cancel')])
    return sg.Window(window_name, layout, no_titlebar=borderless, element_justification=justification)

# , sg.Text('Name:'), sg.InputText(key='-MILL_NAME-', size=(20, 1))
# , sg.Text('Name:'), sg.InputText(key='-ARC_NAME-', size=(20, 1))
