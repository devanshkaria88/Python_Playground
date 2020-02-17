import tkinter as tk
import secrets

root = tk.Tk()
root.title("OTP GUI")
root.geometry('500x500')

frame = tk.Frame(root, background='red', height=500, width=500)
frame.place(x=220, y=220)

root.mainloop()
