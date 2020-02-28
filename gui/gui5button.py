from tkinter import *

root = Tk();
root.geometry("300x300");
topframe = Frame(root);
topframe.pack();

bottomframe = Frame(root);
bottomframe.pack();

button1 = Button(topframe, text="file", fg="red", bg="blue")
button1.pack(side=LEFT);

button2 = Button(topframe, text="edit", fg="green", bg="blue")
button2.pack(side=LEFT);

button3 = Button(topframe, text="delete", fg="yellow", bg="blue")
button3.pack(side=LEFT);

button4 = Button(topframe, text="view", fg="orange", bg="blue")
button4.pack(side=LEFT);

content = Label(root, text= "I am being added",bg="red");
content.pack(side=LEFT,fill=Y);

content2 = Label(root, text= "I am being added",bg="green");
content2.pack(side=BOTTOM , fill=X, padx=20,pady=20);

root.mainloop();
