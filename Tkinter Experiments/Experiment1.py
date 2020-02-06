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

openFile = tk.Button(frame, text="Open Files", padx=10, pady=5, fg='white', bg='blue', command=addApp)
openFile.pack()

runApp = tk.Button(frame, text="RunApps", padx=10, pady=5, fg='white', bg='blue')
runApp.pack()

root.mainloop()
