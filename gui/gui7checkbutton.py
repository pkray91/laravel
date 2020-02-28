from tkinter import *

root = Tk()
root.geometry("300x300");

label1 = Label (root , text="Name"); 
label1.grid(row=0, sticky="w");

label2 = Label (root , text="Email-id"); 
label2.grid(row=1);
 
entry1= Entry(root);
entry2= Entry(root);
entry1.grid(row=0,column=1);
entry2.grid(row=1,column=1);

check = Checkbutton(root, text="Remember me");
button = Button(root,text="click");
check.grid(row=3);
button.grid(row=4);
root.mainloop()