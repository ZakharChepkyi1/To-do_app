import functions
import PySimpleGUI as SG

label=SG.Text("Type in a to-do")
input_box=SG.InputText("Enter todo")
add_button=SG.Button("ADD")

window=SG.Window("My TO-DO App",layout=[[label],[input_box,add_button]])
window.read()
window.close()