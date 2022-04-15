from sys import stdout
import tkinter as tk
# import subprocess

root = tk.Tk()
root.geometry("500x500")
root.title("Python Interpreter")
root.minsize(500, 500)
root.iconbitmap("inter.ico")

canvas1 = tk.Canvas(root, width=1000, bg="black", height=1000)
canvas1.pack()

label = tk.Label(
    root, text="Enter Your Code:", fg="white", bg="black", font=("SansSerif", 14)
)

# label.pack()
label.place(x=50, y=110)

label2 = tk.Label(
    root, text="PY Interpreter", fg="white", bg="black", font=("SansSerif", 24, "bold")
)
label2.place(x=150, y=50)

my_text = tk.Text(root)
my_text.pack(pady=20)
canvas1.create_window(250, 200, width=400, height=100, window=my_text)

def out():
    code = my_text.get(1.0, tk.END)
    text_file = open('mypython_input.txt', 'w+')
    text_file.write(code)

    # subprocess.call("interpreter_main.py")

    from io import StringIO
    import sys
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    eval(code)
    sys.stdout = old_stdout
    message = mystdout.getvalue()

    l3.config(text = message)

    with open('mypython_output.txt', 'w') as file:
            file.write(message)


button1 = tk.Button(
    text="Generate Output", bg="#4EEE94", font=("SansSerif", 12), command = out
    )
canvas1.create_window(240, 300, width=140, height=50, window=button1)

l3 = tk.Label(root, text= ' ', bg="black", font=("SansSerif", 12), fg="white")
l3.pack()
l3.place(x=50, y=350)

root.mainloop()