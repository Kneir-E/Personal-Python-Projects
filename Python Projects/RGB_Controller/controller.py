import wm_serial as ser
from wm_serial import CalibModule
from tkinter import Tk, Button
from tkinter.colorchooser import askcolor
from threading import Thread

selected, comlist = ser.detect_serial_auto(True)
SerialObj = CalibModule(com_port=selected, bool_print=True)

def choose_color():
    color = askcolor()[1]
    SerialObj.send_data(color)
    print(color)

def readMsg(arg):
    while True:
        if SerialObj.msg_list != []:
            print(SerialObj.msg_list.pop())


if __name__ == "__main__":
    # Create a thread instance
    thread = Thread(target=readMsg, args=(0,))
    thread.start()
    while True:
        color = input("choose color: ")
        SerialObj.send_data(color)
    # root = Tk()
    # Button(root, text='Choose Color', command=choose_color).pack()
    # root.mainloop()