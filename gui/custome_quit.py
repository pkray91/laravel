from tkinter import *
import tkinter.messagebox

def askquit():
  answer = tkinter.messagebox.askokcancel("are you sure","wana exit");

  if(answer):
    print("Exit")
    quit();

def demo():
 print("I am demo");
 root.geometry("400x400");
 
def work():
 print("Resize window");
 root.geometry("200x200");
def work1():
 print("Resize window");
 root.geometry("400x400");


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
submenu.add_command(label="Exit", command=askquit)

submenu2 = Menu(menu1);
menu1.add_cascade(label="Edit", menu=submenu2);
submenu2.add_command(label="Resize",command=work)
submenu2.add_command(label="Reset",command=work1)

submenu3 = Menu(menu1);
menu1.add_cascade(label="View", menu=submenu3);

submenu4 = Menu(menu1);
menu1.add_cascade(label="Language", menu=submenu4);

submenu5 = Menu(menu1);
menu1.add_cascade(label="Tools", menu=submenu5);

submenu6 = Menu(menu1);
menu1.add_cascade(label="Exit", menu=submenu6);




root.mainloop()