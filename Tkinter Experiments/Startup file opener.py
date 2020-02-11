import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.geometry("500x500")
apps = ["C:\TURBOC3\Turbo C++\Turbo C++.exe"]


def addApp():
    runapps()
    # filename = filedialog.askopenfilename(initialdir='/', title='Select Files',
    #                                       filetypes=(('Exetuables', '*.exe'), ('All Files', '*.*')))
    # apps.append(filename)
    # print(filename)


def runapps():
    for app in apps:
        os.startfile(app)


base1 = tk.Frame(root, width=500, height=500, bg="#274632")
base1.place(relwidth=1.0, relheight=1.0)

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open Turbo C++", padx=10, pady=5, command=addApp)
openFile.place(relx=0.45, rely=0.45)

root.mainloop()
