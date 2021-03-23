from tkinter import *
from tkinter import scrolledtext
import praw

root = Tk()
root.geometry('500x300')

def validate():
    try:
        int(limitEntry.get())
        checkLimit()
    except ValueError:
        limitEntry.delete(0, "end")
        limitEntry.insert(0,'Enter numeric value')

def checkLimit():
    if int(limitEntry.get())>59:
        limitEntry.delete(0, "end")
        limitEntry.insert(END,'Requests should be less than 60')

def onEntryClick(event):
    if limitEntry.get() == 'Requests should be less than 60':
        limitEntry.delete(0, "end")
        limitEntry.insert(END,'')

def onExit(event):

    if limitEntry.get() == "":
        limitEntry.insert(0, 'Requests should be less than 60')
    else:
        validate()


def search(args=None):
    subreddit=keywordEntry.get()
    limitation=limitEntry.get()


enterLabel = Label(root,text=" Enter the keyword: ")

keywordEntry = Entry(root, width=40)
limitLabel = Label(root,text=" Number of requests: ")

deftext = StringVar()
deftext.set("Requests should be less than 60")
limitEntry = Entry(root, textvariable=deftext, bd=1,width=40)
searchButton = Button(root, text= "Search", command= "search")

enterLabel.grid(row=0,column=0)
keywordEntry.grid(row=0,column=1)
limitLabel.grid(row=1, column=0)
limitEntry.grid(row=1,column=1)
searchButton.grid(row=4,column=0)


limitEntry.bind('<FocusIn>', onEntryClick)
limitEntry.bind('<FocusOut>', onExit)


root.mainloop()



