from tkinter import *

def demo():
 print("I am demo");


root = Tk();
root.geometry("400x400");

menu1= Menu(root);
root.config(menu=menu1);

submenu = Menu(menu1);
menu1.add_cascade(label="File", menu=submenu);

submenu.add_command(label="New", command=demo)
submenu.add_command(label="open")
submenu.add_command(label="Save")
submenu.add_command(label="Save as")
submenu.add_command(label="close",command = quit)

submenu2 = Menu(menu1);
menu1.add_cascade(label="Search", menu=submenu2);

submenu3 = Menu(menu1);
menu1.add_cascade(label="View", menu=submenu3);

submenu4 = Menu(menu1);
menu1.add_cascade(label="Language", menu=submenu4);

submenu5 = Menu(menu1);
menu1.add_cascade(label="Tools", menu=submenu5);

submenu6 = Menu(menu1);
menu1.add_cascade(label="Exit", menu=submenu6);

root.mainloop()