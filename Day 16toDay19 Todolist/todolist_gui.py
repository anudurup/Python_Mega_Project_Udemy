import functions
import PySimpleGUI as sg
import time

# Apply pysimplegui themes from Google
sg.theme("DarkPurple")
clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
# For Size go to implementations and look at the param size and see the description.
# :param size: w=characters-wide, h=rows-high. If an int instead of a tuple is supplied, then height is auto-set to 1
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App', layout=[[clock],
                                           [label],
                                           [input_box, add_button],
                                           [list_box, edit_button, complete_button],
                                           [exit_button]]
                   , font=('Helvetica', 15))
# Layout expects a list. Items in first
# square bracket are all in the same line.
while True:
    event, values = window.read(timeout=200)
    # timeout is needed else it runs only for a event. This allows continuous running and time updated every 200ms.
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo']
        todos.append(new_todo + "\n")
        functions.write_todos(todos)
        window['todos'].update(values=todos)
    elif event == "Edit":
        try:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        except IndexError:
            sg.popup("Please select an item", font=('Helvetica', 10))
    elif event == 'Complete':
        try:
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        except IndexError:
            sg.popup("Please select an item", font=('Helvetica', 10))
    elif event == 'Exit':
        break
    elif event == 'todos':
        window['todo'].update(value=values['todos'][0])
    elif event == sg.WIN_CLOSED:
        break
window.close()
