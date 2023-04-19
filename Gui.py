import PySimpleGUI as sg
from project import *

layout = [  [sg.Text("Change your ammo"),sg.Input(key='-AMMO-',default_text='30'),sg.Checkbox("Freeze the value",key="-FREEZE-",default=False)]]

window = sg.Window('MemoryChanger', layout)

while True:
    event, value = window.read(timeout=100)
    if value['-FREEZE-'] == True:
        MemoryChanger(value['-AMMO-'])
        
    if event == sg.WIN_CLOSED:
        break