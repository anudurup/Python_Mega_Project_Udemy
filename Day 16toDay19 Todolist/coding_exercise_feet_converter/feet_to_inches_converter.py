import PySimpleGUI as sg
from feet_to_meter import feet_to_meter
sg.theme('Black')

label1 = sg.Text("Enter feet:")
input1 = sg.Input(key="feet")
label2 = sg.Text("Enter inches:")
input2 = sg.Input(key="inches")
convert_button = sg.Button("Convert", key="convert")
exit_button = sg.Button("Exit", key="exit")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("Convertor", layout=[[label1, input1], [label2, input2], [convert_button, exit_button, output_label]])

while True:
    event, values = window.read()
    if event == "convert":
        if (values['feet'] == '') or (values['inches'] == ''):
            sg.popup("Enter two numbers")
        else:
            meters = feet_to_meter(values["feet"], values["inches"])
            window["output"].update(value=str(meters) + " m")
    elif event == "exit":
        break

window.close()