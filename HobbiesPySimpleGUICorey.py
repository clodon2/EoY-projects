# Corey Verkouteren
# 9/21/21 - 9/24/21
# Mr Ball's class
# PySimpleGUI practice


import PySimpleGUI as sg

                                            # Guitar lister

newtheme = {'BACKGROUND': 'black', 'TEXT': 'white', 'INPUT': '#313131', 'SCROLL': '#313131',
                 'TEXT_INPUT': 'white', 'BUTTON': ('white', '#313131'), 'PROGRESS': '#313131', 'BORDER': 0,
                               'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}

sg.theme_add_new('blackgray', newtheme)

sg.theme('blackgray')
# creates a custom theme that is used for this window, mostly created so that setting colors in every element isn't
# necessary

layout = [[sg.Text('Guitar Lister', justification='center', size=(60, 1))],
          [sg.Text("Please enter the make and model of the guitar:", justification='center')],
          [sg.InputText("", size=(20, 1), key='-inputb', enable_events=True)],
          [sg.Text("What kind of guitar is it?")],
          [sg.Radio("Electric", enable_events=True, group_id='g1', key='-r1'),
           sg.Radio("Acoustic", enable_events=True, group_id='g1', key='-r2'),
           sg.Radio("Classical", enable_events=True, group_id='g1', key='-r3')],
          [sg.Text("Please list the condition of the guitar:")],
          [sg.Checkbox("Has Strings", enable_events=True, key='-c1'),
           sg.Checkbox("Working/Functional", enable_events=True, key='-c2'),
           sg.Checkbox("Modified", enable_events=True, key='-c3'),
           sg.Checkbox("For Parts", enable_events=True, key='-c4')],
          [sg.Combo(values=['Mint', 'Near Mint', 'Minimal Wear', 'Mild Wear', 'Heavy Wear'], key='-con',
                    background_color='#313131', enable_events=True)],
          [sg.Column(layout=[[sg.Text("How much work does the guitar need?", key='-wrk')],
                             [sg.Slider(range=(0, 10), resolution=0.5, orientation='h', relief='flat', key='-wrksl',
                                        enable_events=True)]], key='-wrclm')],
          [sg.Button(button_text='Reset all', key='-clr'), sg.Button(button_text='Submit/Save', key='-sbmt')],
          [sg.InputText("Not Submitted", readonly=True, background_color="black", key='-status',
                        disabled_readonly_background_color="black", enable_events=True)]]

window = sg.Window('Guitar Lister', layout, resizable=True, finalize=True, background_color='black',
                   use_default_focus=True, button_color='#313131')

while True:
    event, values = window.read()
# makes the window persistent

    if event == sg.WINDOW_CLOSED:
        break
# shuts down program on event of clicking the x on the top right

    elif event == '-clr':
        window['-inputb'].update("")
        window['-r1'].update(value=False)
        window['-r2'].update(value=False)
        window['-r3'].update(value=False)
        window['-c1'].update(value=False)
        window['-c2'].update(value=False)
        window['-c3'].update(value=False)
        window['-c4'].update(value=False)
        window['-con'].update("")
        window['-status'].update("Not Submitted")
        window['-wrksl'].update(value=0)
# Clears all inputs/choices picked out by the user, there is probably an easier way using a for loop but it kept giving
    # giving me key errors so I defaulted to this.

    elif event == '-sbmt':
        window['-status'].update("Submitted")
# Button (event) intended to submit the results to a database, which we are learning later, so for now it just updates
    # the status text

    elif event:
        window['-status'].update("Not Submitted")
# Changes the status to "Not Submiited" if any change is made in the entry, prevents confusion as it would still read
    # "submitted" as a new entry was being made

    if values['-con'] == 'Mint':
        window['-wrk'].hide_row()
        window['-wrksl'].hide_row()
# prevents the user from putting in values for how much work the guitar needs if its in 'Mint' condition since that
    # means the guitar is perfect, should also probably clear the inputs of that field in case the user fills out the
    # chart out of order

    else:
        window['-wrk'].unhide_row()
        window['-wrksl'].unhide_row()
        continue
# unhides the "work the guitar needs" elements so they can be selected if the user chooses anything other than 'Mint'
