import praw
from datetime import datetime

search_term='movies'
keyword='official'

print ("Subreddit: ",search_term)
print ("Keyword: ",keyword)

reddit = praw.Reddit('reddit-configuration-bot1')
subreddit = reddit.subreddit(search_term)

subreddit = subreddit.search(keyword,limit=5)

for submission in subreddit:
    print (" ID: ",submission.id)
    print ("  Title: ",submission.title)
    print ("  Score: ",submission.score)
    print ("  URL: ",submission.url)
    print ("time:" , datetime.fromtimestamp(submission.created_utc))
