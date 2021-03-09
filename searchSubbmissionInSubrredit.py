from tkinter import *
from tkinter import scrolledtext
import praw

root = Tk()

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