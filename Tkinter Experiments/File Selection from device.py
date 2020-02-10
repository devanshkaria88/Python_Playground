import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []


def addApp():
    filename = filedialog.askopenfilename(initialdir='/', title='Select Files',
                                          filetypes=(('Exetuables', '*.exe'), ('All Files', '*.*')))
    apps.append(filename)
    print(filename)
    runapps()


def runapps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=300, width=300, bg="#274632")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(frame, text="Open Files", padx=10, pady=5, command=addApp)
openFile.pack()

root.mainloop()
