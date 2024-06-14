import pyautogui
from tkinter import *

def take_ss():
    add_data = path.get()
    pa = add_data + "\\Mowgli.png"
    print(pa)
    screenshot_taker = pyautogui.screenshot()
    screenshot_taker.save(pa)

# We are building an application
win = Tk()
win.title("Mowgli SS taker")
win.geometry("800x400")
win.config(bg="blue")
win.resizable(False, False)

path = Entry(win, font=('Times New Roman', 50, "bold"))
path.place(x=20, height=70, width=660, y=50)

# Connect the button to the take_ss function
button = Button(win, text="Done", font=('Times New Roman', 50, "bold"), command=take_ss)
button.place(x=250, y=140, height=100, width=200)

win.mainloop()
