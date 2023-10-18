import functions
import PySimpleGUI as SG

label = SG.Text("Type in a to-do")
input_box = SG.InputText(tooltip="Enter todo", key='todo')
add_button = SG.Button("Add")
list_box = SG.Listbox(values=functions.get_todo(), key="todos",
                      enable_events=True, size=[45, 10])
edit_box = SG.Button("Edit")
complete_button = SG.Button("Complete")
exit_button=SG.Button("Exit")

window = SG.Window("My TO-DO App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_box, complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = values["todo"] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case 'Edit':
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"] + "\n"

            todos = functions.get_todo()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Complete":
            to_do_complete=values["todos"][0]
            todos=functions.get_todo()
            todos.remove(to_do_complete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todos"].update(values="")
        case "Exit":
            break
        case SG.WINDOW_CLOSED:
            break

window.close()
