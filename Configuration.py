from tkinter import *


root = Tk()

e = Entry(root, width=50, borderwidth=5)
e.insert(0, "Enter Your Name: ")

def myClick():
    myLabel1 = Label(root, text= e.get())
    myLabel1.grid(row=0, column=0)


#Creating a Label Widget
myLabel1 = Label(root, text="")
myButton = Button(root, text="Click me!", padx=50, pady=50, command=myClick, fg="blue", bg="purple")


myLabel1.grid(row=0, column=0)
myButton.grid(row=2, column=0)
e.grid(row=3, column=0)

root.mainloop()