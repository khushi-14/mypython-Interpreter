import tkinter as tk
import sys
import os

root = tk.Tk()
root.geometry("500x500")
root.title("Python Interpreter")
root.minsize(500, 500)

canvas1 = tk.Canvas(root, width=1000, bg="black", height=1000)
canvas1.pack()

label2 = tk.Label(
    root, text="Welcome to myPython :)", fg="white", bg="black", font=("SansSerif", 24, "bold")
)
label2.place(x=150, y=50)

def openShell():
    os.system('start /B start cmd.exe @cmd /c python interpreter_main.py')

button1 = tk.Button(
    text="mypython Shell", bg="#4EEE94", font=("SansSerif", 12), command = openShell
)
canvas1.create_window(240, 150, width=140, height=50, window=button1)

button2 = tk.Button(
    text="mypython Interpreter", bg="#4EEE94", font=("SansSerif", 12), command = openShell
)
canvas1.create_window(240, 200, width=140, height=50, window=button2)

button3 = tk.Button(
    text="User Variables", bg="#4EEE94", font=("SansSerif", 12), command = openShell
)
canvas1.create_window(240, 250, width=140, height=50, window=button3)

root.mainloop()
