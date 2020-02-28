from tkinter import *

def demo():
 print("Welcome to python world");

root = Tk()
root.geometry("300x300");

button = Button(root, text="click me call function", command=demo);
button.pack();
button2 = Button(root, text="Exit now", command=quit);
button2.pack();


mainloop()