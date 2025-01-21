from tkinter import Tk, Button
from tkinter.colorchooser import askcolor

def choose_color():
    color = askcolor()[1]
    print(f"Selected color: {color}")

root = Tk()
Button(root, text='Choose Color', command=choose_color).pack()
root.mainloop()
