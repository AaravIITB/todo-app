import function
import FreeSimpleGUI as sg
import time

sg.theme("BlueMono")

label_time= sg.Text("",key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=function.get_todo(),key="todos",
                      enable_events=True, size=(45,10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[label_time],
                           [label],
                           [input_box,add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],
                   font=("Helvetica",20))


while True:
    event,values = window.read(timeout=200)#loop runs every 10 milliseconds
    window["clock"].update(value=time.strftime("%b %d,%Y %H:%M:%S"))

    match event:
        case "Add":
            todos = function.get_todo()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            function.write_todo(todos)
            window['todos'].update(values=todos)#updates the window in real time

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]#to get the string
                new_todo = values['todo'] + "\n"
                todos = function.get_todo()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                function.write_todo(todos)
                window['todos'].update(values=todos)#updates the window in real time
            except IndexError:
                sg.popup("Please select a task",font=("Helvetica",20))
        case "Complete":
            try:
                todo_to_complete=values['todos'][0]
                todos = function.get_todo()
                todos.remove(todo_to_complete)
                function.write_todo(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select a task",font=("Helvetica",20))

        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()