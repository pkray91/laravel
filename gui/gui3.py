from tkinter import *

root = Tk();

content = Label(root, text="My first GUI page ia ready to display");
content1 = Label(root, text="My first GUI page ia ready to display",fg="red",bg="yellow");

content.pack();
content1.pack();
root.mainloop();
