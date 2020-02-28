from tkinter import *

root = Tk();

root.geometry("600x600");

def left(event):
  print("you have clicked left button");
def right(event):
  print("you have clicked right button");
def middle(event):
  print("you have clicked middle button");
  
frame = Frame(root, width="400",height="500");

frame.bind("<Button-1>",left)
frame.bind("<Button-2>",middle)
frame.bind("<Button-3>",right)
frame.pack();
root.mainloop()