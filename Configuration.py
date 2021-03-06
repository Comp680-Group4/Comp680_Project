from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5)

def myClick():
    myLabel2 = Label(root, text="I clicked da button!")
    myLabel2.grid(row=1, column=0)

#Creating a Label Widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Josh Steward")
myButton = Button(root, text="Click me!", padx=50, pady=50, command=myClick, fg="blue", bg="purple")


myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myButton.grid(row=2, column=0)
e.grid(row=3, column=0)





root.mainloop()


