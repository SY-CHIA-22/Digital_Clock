from cProfile import label
from curses import window
from thinter import TK, label

window = TK()
window.title("Digital Clcock")
window.geometry("600x300")

window.mainloop()
