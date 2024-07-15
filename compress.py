import functions
import FreeSimpleGUI as sg

label1 = sg.Text("Select files type compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key = "files")

label2 = sg.Text("Select destination files")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key = "folder")

compress_button  = sg.Button("Compress")

window =sg.Window("Compresser", layout=[[label1,input1,choose_button1],
                                     [label2,input2,choose_button2],
                                        [compress_button]])


while True:


    event, values =window.read()
    print(event, values)
    filepath = values["files"].split(";")
    folder = values["folder"]
window.close()