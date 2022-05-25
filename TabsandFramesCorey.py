# Corey Verkouteren
# 10/25/21 - 10/28/21
# Mr Ball's PM
# Learning Tabs and Frames in PySimpleGUI

# Corey's Game Library

import PySimpleGUI as sg
import random as rd

# tab1 functions


def progressbarchoices(total):
    rchoice = rd.choice(Choices)
    total += rchoice
    if total <= 0:
        total = 0
    return rchoice, total
# gets a random value and adds it to the current value of the progressbar


def gamereset():
    plyrtotal = 0
    cputotal = 0
    window["results"].update("")
    window["plyrp"].update(current_count=0)
    window["cpup"].update(current_count=0)
    window["racelength"].update("40", disabled=False)

    return plyrtotal, cputotal
# sets all updated values to their original state


# tab 2 resources

def duprem(string):
    nwstring = ""

    for l in string:
        if l not in nwstring:
            nwstring += l

    return nwstring
# deletes duplicates from a string, if a duplicate is present, only the first instance is kept


def buildCypherString(password, decrypters):
    cpypassword = password

    for l in decrypters:
        chkr = cpypassword.count(l)

        if chkr == 0:
            cpypassword += l

    return cpypassword
# creates a "copy" of the/a original password and adds all characters present in a/the base string that are not present
# in the original password string to the end of the copied string, creating a unique cypher


def EnDeCryptdictMaker(cypherstr, basestr, ende):
    Cryptdic = {}

    if ende == "De":
        for i in range(len(basestr)):
            Cryptdic[basestr[i]] = cypherstr[i]

    elif ende == "En":
        for i in range(len(basestr)):
            Cryptdic[cypherstr[i]] = basestr[i]

    return Cryptdic
# Creates a dictionary where the individual characters of the base string (basestr) and combination string (cypherstr)
# (created in the buildCypherString function) are the keys and values, the orders of these for decrypting and
# encrypting are important because it can cause decrypting errors if the orders are switched.


def endecoder(message, cypherdict):
    result = ""

    for l in message:
        chara = cypherdict.get(l, "nothing")

        if chara == "nothing":
            result += l

        else:
            result += chara

    return result
# uses the dictionary created with the EnDeCryptdictMaker function to decrypt or encrypt a message the user puts in.
# It does this by relating each character in the message to its key in the dictionary, grabbing the value of that key
# from the dictionary and adding it to the final encrypted or decrypted message (if it isn't there the character is just
# added)


# Dark Blue 14 2 DarkBrown3
sg.theme(new_theme="DarkBlue2")

tab1 = [[sg.Frame("Welcome to the races!", [
          [sg.Input("40", enable_events=True, s=4, disabled_readonly_background_color="white", k="racelength"),
           sg.Text("meter race")],
          [sg.Text("You", justification="left")],
          [sg.ProgressBar(orientation="horizontal", max_value=40, s=(40, 20), k="plyrp")],
          [sg.Text("CPU", justification="left")],
          [sg.ProgressBar(orientation="horizontal", max_value=40, s=(40, 20), k="cpup")],
          [sg.Button("Roll Movements", enable_events=True, k="rpick")],
          [sg.Multiline("Results", disabled=True, k="results")]],
                    title_location="n", element_justification="center")]]

tab2 = [[sg.Frame("Password-Based Decryptor/Encryptor", [
          [sg.Frame("Password", layout=[
              [sg.Input("", k="-pass")]],
                    vertical_alignment='center', element_justification="center", pad=10, title_location="n")],
          [sg.Frame("Message", layout=[
              [sg.Input("", enable_events=True, k="-message", tooltip="")]],
                    vertical_alignment='center', element_justification="center", title_location="n",
                    pad=5)],
          [sg.Frame("Encrypt or Decrypt", layout=[
               [sg.Button(button_text="Encrypt", k="-ebutton", enable_events=True)],
               [sg.Button(button_text="Decrypt", k="-dbutton", enable_events=True)]],
                    vertical_alignment='center', element_justification="center", pad=5)],
          [sg.Frame("Output", layout=[
               [sg.Input("Encrypted message here", readonly=True, k="-eout", tooltip="Encrypted message here",
                         disabled_readonly_background_color="#385464"),
                sg.Button("Clear", enable_events=True, k="-eclear")],
               [sg.Input("Decrypted message here", readonly=True, k="-dout", tooltip="Decrypted message here",
                         disabled_readonly_background_color="#385464"),
                sg.Button("Clear", enable_events=True, k="-dclear")]],
                    vertical_alignment='center', element_justification="center", title_location="n", pad=10)],
          [sg.Button(button_text="Reset All", enable_events=True, pad=10, k="-reset")]],
                    relief="ridge", title_location="n", pad=5,
                    element_justification="center")]]

tab3 = [[sg.Text('Guitar Lister', justification='center', size=(60, 1))],
          [sg.Frame("Please enter the make and model of the guitar:", [
            [sg.InputText("", size=(20, 1), key='-inputb', enable_events=True)],
            [sg.Text("What kind of guitar is it?")],
            [sg.Radio("Electric", enable_events=True, group_id='g1', key='-r1'),
                sg.Radio("Acoustic", enable_events=True, group_id='g1', key='-r2'),
                sg.Radio("Classical", enable_events=True, group_id='g1', key='-r3')]],
                    element_justification="center", title_location="n")],
          [sg.Frame("Please list the condition of the guitar:", [
              [sg.Checkbox("Has Strings", enable_events=True, key='-c1'),
                sg.Checkbox("Working/Functional", enable_events=True, key='-c2'),
                sg.Checkbox("Modified", enable_events=True, key='-c3'),
                sg.Checkbox("For Parts", enable_events=True, key='-c4')],
              [sg.Combo(values=['Mint', 'Near Mint', 'Minimal Wear', 'Mild Wear', 'Heavy Wear'], key='-con',
                        enable_events=True)],
              [sg.Column(layout=[[sg.Text("How much work does the guitar need?", key='-wrk')],
                                 [sg.Slider(range=(0, 10), resolution=0.5, orientation='h', relief='flat', key='-wrksl',
                                            enable_events=True)]], key='-wrclm')]],
                    element_justification="center", title_location="n")],
          [sg.Button(button_text='Reset all', key='-clr'), sg.Button(button_text='Submit/Save', key='-sbmt')],
          [sg.InputText("Not Submitted", readonly=True, key='-status', enable_events=True,
                        disabled_readonly_background_color="#385464")]]

layout = [[sg.TabGroup([[sg.Tab("Horse Race Simulator", tab1),
                         sg.Tab("De/En-Cryptor", tab2),
                         sg.Tab("Guitar Lister", tab3, element_justification="center")]])]]

window = sg.Window("Corey's GUI Program Library", layout, finalize=True, use_default_focus=True)

# tab1 resources

Choices = [2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 6, 6, 6, 6, 8, 8, 8, 10, 10, -2, -2, -6]
ChoicesResponse = {2: "horse has walked 2 meters", 4: "horse has ran 4 meters", 6: "horse has ran 6 meters",
                   8: "horse has dashed 8 meters", 10: "horse has sprinted 10 meters",
                   -2: "horse stumbled and lost 2 meters", -6: "horse got distracted and ran back 6 meters"}

window['plyrp'].update(0)
window['cpup'].update(0)

plyrtotal = 0
cputotal = 0
racemax = 40

# tab2 resources

Basestring = "zZ94aA1bBc0CeEg6GnNiIjJkK5mMoOqfFQd7DrR3sSlLtTpPuUv2VwW xX8yYhH"

showing = True

while showing:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

# tab1 operations

    if event == "rpick":
        try:
            racemax = int(window["racelength"].get())
            window["plyrp"].update(current_count=plyrtotal, max=racemax)
            window["cpup"].update(current_count=cputotal, max=racemax)
            window["racelength"].update(disabled=True)
            # finds the value input by the user for what the max score is and updates the progressbars to reflect that,
            # updates each click of the roll button is disabled after the first click

            window["results"].update("")
            # clears the results field as the first print of the scores will
            # include "results" at the start if not

            plyrbar = progressbarchoices(plyrtotal)
            cpubar = progressbarchoices(cputotal)
            plyrtotal = plyrbar[1]
            cputotal = cpubar[1]
            # uses the progressbarchoices function to get a random value to use as the roll for each

            window["results"].print("Player's " + ChoicesResponse[plyrbar[0]])
            window["results"].print("CPU's " + ChoicesResponse[cpubar[0]])

            window["plyrp"].update(plyrbar[1])
            window["cpup"].update(cpubar[1])

        except:
            window["racelength"].update(40)
            sg.popup("Race length invalid")
        # prevents crash if the race max input isn't an integer

    if plyrtotal >= racemax:
        sg.popup("You have won the Game! Resetting the board....")
        plyrtotal = gamereset()[0]
        cputotal = gamereset()[1]

    elif cputotal >= racemax:
        sg.popup("CPU has won the Game! Resetting the board....")
        plyrtotal = gamereset()[0]
        cputotal = gamereset()[1]

    elif cputotal and plyrtotal >= racemax:
        sg.popup("What a race! You and CPU tied! Resetting the board...")
        plyrtotal = gamereset()[0]
        cputotal = gamereset()[1]

# tab2 operations

    if event == "-message":
        currentmsg = window["-message"].get()
        window["-message"].set_tooltip(currentmsg)
    # updates the message tooltip to be accurate with what is in the field

    if event == "-ebutton":
        Password = window["-pass"].get()
        msg = window["-message"].get()

        finalpassword = duprem(Password)
        cypher = buildCypherString(finalpassword, Basestring)

        mode = "En"
        Encrypt = EnDeCryptdictMaker(cypher, Basestring, mode)
        window["-eout"].update(endecoder(msg, Encrypt))
        window["-eout"].set_tooltip(endecoder(msg, Encrypt))
    # If the "Encrypt" button is clicked, it gets the values from the "Password" and "Message" fields and runs the
    # encryption on the message, printing the result in the encryption input box and tooltip (under "Output")

    elif event == "-dbutton":
        Password = window["-pass"].get()
        msg = window["-message"].get()

        finalpassword = duprem(Password)
        cypher = buildCypherString(finalpassword, Basestring)

        mode = "De"
        Decrypt = EnDeCryptdictMaker(cypher, Basestring, mode)
        window["-dout"].update(endecoder(msg, Decrypt))
        window["-dout"].set_tooltip(endecoder(msg, Decrypt))
    # If the "Decrypt" button is clicked, it gets the values from the "Password" and "Message" fields and runs the
    # decryption on the message, printing the result in the decryption input box and tooltip (under "Output")

    if event == "-eclear":
        window["-eout"].update("Encrypted message here")

    elif event == "-dclear":
        window["-dout"].update("Decrypted message here")
    # Both if/elifs replace the Encryption or Decryption output fields with their starting text

    if event == "-reset":
        window["-pass"].update("")
        window["-message"].update("")
        window["-eout"].update("Encrypted message here")
        window["-dout"].update("Decrypted message here")
        window["-eout"].set_tooltip("Encrypted message here")
        window["-dout"].set_tooltip("Decrypted message here")
        window["-message"].set_tooltip("")
    # Sets all input elements (and tooltips) to their original values, probably an easier way to do this with a for loop

# tab3 operations

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
