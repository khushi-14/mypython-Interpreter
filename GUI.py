import tkinter as tk
from tkinter import filedialog

file = open('mypyfile.txt', 'w') 
file.truncate()
file.close()

file = open('user_globals.txt', 'w') 
file.truncate()
file.close()

root = tk.Tk()
root.geometry("950x600")
root.title("Python Interpreter")
root.iconbitmap("inter.ico")
canvas1 = tk.Canvas(root, width=1000, bg="black", height=1000)
canvas1.pack()

label1 = tk.Label(
    root, text="Welcome to mypython :)", fg="white", bg="black", font=("SansSerif", 24, "bold")
)
label1.place(x=280, y=50)

label2 = tk.Label(
    root, text="Enter Your Code", fg="white", bg="black", font=("SansSerif", 14)
)
label2.place(x=50, y=130)

label3 = tk.Label(
    root, text="User Variables", fg="white", bg="black", font=("SansSerif", 14)
)
label3.place(x=500, y=350)

label4 = tk.Label(
    root, text="Output", fg="white", bg="black", font=("SansSerif", 14)
)
label4.place(x=55, y=350)

l3 = tk.Label(root, text= ' ', bg="black", font=("SansSerif", 12), fg="white")
l3.pack()
l3.place(x=50, y=400)

canvas2 = tk.Canvas(root, width = 400, height = 300)
canvas2.pack()
my_text = tk.Text(root)
my_text.pack(pady=20)
canvas1.create_window(250, 240, width=400, height=100, window=my_text)

canvas3 = tk.Canvas(root, width = 400, height = 300)
canvas3.pack()
my_text1 = tk.Text(root)
my_text1.pack(pady=20)
canvas1.create_window(700, 240, width=400, height=100, window=my_text1)

canvas4 = tk.Canvas(root, width = 400, height = 300)
canvas4.pack()
my_text2 = tk.Text(root)
my_text2.pack(pady=20)
canvas1.create_window(700, 450, width=400, height=100, window=my_text2)

def out():
    code = my_text.get(1.0, tk.END)
    text_file = open('mypython_input.txt', 'w+')
    text_file.write(code)
    text_file.close()

    import myoutput
    myoutput.WriteMyOutput()

    file = open('mypython_output.txt', 'r') 
    message = file.read()
    file.close()
    
    l3.config(text = message)
    
    file = open('mypyfile.txt', 'a') 
    file.write("mypython In: " + code)
    file.write("mypython Out: " + message)
    file.close() 

def check():
    file = open('mypyfile.txt', 'r') 
    content = file.read()
    my_text1.insert(tk.END, content)
    file.close()

def clear():
    my_text1.delete(1.0, tk.END)
    file = open('mypyfile.txt', 'w') 
    file.truncate()
    file.close()

def save():
    file = filedialog.asksaveasfile(defaultextension=".*", mode='w', initialdir="C:\\Users\\drpre\\OneDrive\\Desktop\\teams", title="Save Text File", filetypes=(("Text Files", "*.txt"), ))
    stuff = my_text1.get(1.0, tk.END)
    file.write(stuff)
    file.close()
    my_text1.delete('1.0', tk.END)
    my_text1.update()

def get_user():
    file = open('user_globals.txt', 'r') 
    variables = file.read()
    my_text2.insert(tk.END, variables)
    file.close()

    
button1 = tk.Button(
    text="Generate Output", bg="#4EEE94", font=("SansSerif", 12), command = out
    )
canvas1.create_window(240, 320, width=140, height=30, window=button1)

button2 = tk.Button(
    text="Clear", bg="#4EEE94", font=("SansSerif", 12), command = clear
    )
canvas1.create_window(560, 160, width=80, height=30, window=button2)

button3 = tk.Button(
    text="Save", bg="#4EEE94", font=("SansSerif", 12), command = save
    )
canvas1.create_window(660, 160, width=80, height=30, window=button3)

button5 = tk.Button(
    text="Check", bg="#4EEE94", font=("SansSerif", 12), command = check
    )
canvas1.create_window(760, 160, width=80, height=30, window=button5)

button4 = tk.Button(
    text="Get User Variables", bg="#4EEE94", font=("SansSerif", 12), command = get_user
    )
canvas1.create_window(760, 360, width=180, height=30, window=button4)


root.mainloop()
