import praw
from tkinter import *

root = Tk()
root.title('Reddit Behaviour Tracking')
root.geometry("400x400")






reddit = praw.Reddit(client_id = 'J8BdcKH3pAoZ5g',
                     client_secret = 'XSYxzeI8w-qQTFBJxraUHdzarAelOQ',
                     username = 'FallenGalaxies123',
                     password = 'Cronosphere123!',
                     user_agent= 'comp680project')


subreddit = reddit.subreddit('python')
hot_python = subreddit.hot(limit=5)

for submission in hot_python:
    if not submission.stickied:
        print('Title: {}, Ups: {}, Downs: {}, Have we visited: {}\n'.format(submission.title,
                                                                            submission.ups,
                                                                            submission.downs,
                                                                            submission.visited))

        submission.comments.replace_more(limit=0)

        for comment in submission.comments.list():
            print(20 * '-')
            print('Parent ID: ', comment.parent())
            print('Comment ID: ', comment.id)
            print(comment.body)


root.mainloop()


