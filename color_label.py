import tkinter
from tkinter import ttk

form = tkinter.Tk()
form.geometry("600x400")

lbl1 = ttk.Label( form, text ="label headere" )
lbl2 = ttk.Label(form ,text = "label1")

lbl1.config(background ="navy", foreground = "light blue")

lbl1.pack()
lbl2.pack()
form.mainloop()

