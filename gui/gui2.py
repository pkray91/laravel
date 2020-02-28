from tkinter import *

root = Tk();
#root.minsize(width=400,height=400);
#root.maxsize(width=400,height=400);
root.geometry("344x233");
label = Label(root, text="My first GUI page ia ready to display");

label.pack();

root.mainloop();