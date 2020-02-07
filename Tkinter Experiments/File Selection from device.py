import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []


def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir='/', title='Select Files',
                                          filetypes=(('Exetuables', '*.exe'), ('All Files', '*.*')))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg='grey')
        label.pack()
    runapps()


def runapps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=700, width=800, bg="blue")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

box1 = tk.Frame(frame, bg='red')
box1.place(relwidth=0.5, relheight=0.5)

box2 = tk.Frame(frame, bg='blue')
box2.place(relwidth=0.5, relheight=0.5, rely=0.5)

box3 = tk.Frame(frame, bg='green')
box3.place(relwidth=0.5, relheight=0.5, relx=0.5)

box4 = tk.Frame(frame, bg='yellow')
box4.place(relwidth=0.5, relheight=0.5, relx=0.5, rely=0.5)

openFile = tk.Button(root, text="Open Files", padx=10, pady=5, fg='white', bg='#2f2d2c', command=addApp)
openFile.pack()

root.mainloop()
