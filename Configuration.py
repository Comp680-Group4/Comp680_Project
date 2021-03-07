from tkinter import *
from tkinter import scrolledtext
import praw

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

text_area = scrolledtext.ScrolledText(root,width = 90,height = 30,font = ("Times New Roman", 15), bg = "light cyan")
text_area.grid(column = 0, pady = 10, padx = 10)

reddit = praw.Reddit('reddit-configuration-bot1')
subreddit = reddit.subreddit("learnpython")


for submission in subreddit.hot(limit=5):
    text_area.insert(INSERT,"Title:  \n"+ submission.title+"\n")
    text_area.insert(INSERT,"\n"+"Text: \n"+ submission.selftext+"\n")
    text_area.insert(INSERT,"\n"+"Score: \n"+ str(submission.score)+"\n *********************\n")

## making it read only
text_area.configure(state="disabled")
root.mainloop()