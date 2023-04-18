import PySimpleGUI as sg       
from project import *               

layout = [  [sg.Text("Change your ammo")],     
            [sg.Input()],
            [sg.Button('Ok')]]

window = sg.Window('Window Title', layout)     

while True:
    event, value = window.read()                   
    MemoryChanger(int(value[0]))     