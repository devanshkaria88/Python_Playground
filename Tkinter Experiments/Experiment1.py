import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=800, bg="blue")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(frame, text="Open Files", padx=10, pady=5, fg='white', bg='blue')
openFile.pack()

runApp = tk.Button(frame, text="RunApps", padx=10, pady=5, fg='white', bg='blue')
runApp.pack()

root.mainloop()
