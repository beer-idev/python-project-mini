from tkinter import Label, Tk, mainloop
# from tkinter.ttk import *

from time import strftime


app_window = Tk() 
app_window.title("Digital Clock") 
# app_window.geometry("420x150") 
# app_window.resizable(1,1)

def digital_clock():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, digital_clock)

lbl = Label(app_window, font = ('calibri', 68, 'bold'), background = '#171717', foreground = 'white')
lbl.grid(row=0, column=1)

lbl.pack(anchor = 'center')
digital_clock()

app_window.mainloop()