import praw
import pandas as pd
import datetime as dt
import sys


search_term='movies'
keyword='coming'

if (len(sys.argv)>1):
    search_term=(sys.argv[1])

if (len(sys.argv)>2):
    keyword=(sys.argv[2])

print ("Subreddit: ",search_term)
print ("Keyword: ",keyword)
print()

reddit = praw.Reddit('reddit-configuration-bot1')
subreddit = reddit.subreddit(search_term)


resp = subreddit.search(keyword,limit=5)

for submission in resp:
    print (" ID: ",submission.id)
    print ("  Title: ",submission.title)
    print ("  Score: ",submission.score)
    print ("  URL: ",submission.url)
    print ("  Text: ",submission.selftext[:120])