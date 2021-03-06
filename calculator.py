from tkinter import *

root = Tk()

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def buttonAdd():
    myLabel1 = Label(root, text= e.get())
    myLabel1.grid(row=0, column=0)

button1 = Button(root, text="1", padx=40, pady=20, command=buttonAdd)

myButton = Button(root, text="Click me!", padx=50, pady=50, command=myClick, fg="blue", bg="purple")


myButton.grid(row=2, column=0)
e.grid(row=3, column=0)


root.mainloop()

