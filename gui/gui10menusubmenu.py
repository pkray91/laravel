from tkinter import *

def demo():
 print("I am demo");


root = Tk();
root.geometry("400x400");

menu1= Menu(root);
root.config(menu=menu1);

submenu = Menu(menu1);
menu1.add_cascade(label="File", menu=submenu);

submenu.add_cascade(label="New")
submenu.add_cascade(label="open")
submenu.add_cascade(label="Save")
submenu.add_cascade(label="Save as")
submenu.add_cascade(label="close")

submenu2 = Menu(menu1);

menu1.add_cascade(label="Exit", menu=submenu2);

root.mainloop()