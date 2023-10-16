import functions
import PySimpleGUI as SG

label=SG.Text("Type in a to-do")
input_box=SG.InputText(tooltip="Enter todo",key='todo')
add_button=SG.Button("Add")

window=SG.Window("My TO-DO App",
                 layout=[[label],[input_box,add_button]],
                font=("Helvetica",20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todos = values["todo"]+'\n'
            todos.append(new_todos)
            functions.write_todos(todos)
        case SG.WINDOW_CLOSED:
            break

window.close()