from cProfile import label
from curses import window
from tkinter import Label
from thinter import TK, label

window = TK()
window.title("Digital Clcock")
window.geometry("600x300")
window.configure(bg"steelblue)
label=Label(window, font=("Arial black", 78,"bold") bg="steelblue"
label.package(paddy=100)

def clock():
    time=datetime.now().strttime("%H:%M:%S")
label:Label(text=time)
label.after(500,clock)
clock()
window.mainloop()
