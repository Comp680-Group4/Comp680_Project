import praw

reddit = praw.Reddit(client_id = 'J8BdcKH3pAoZ5g',
                     client_secret = 'XSYxzeI8w-qQTFBJxraUHdzarAelOQ',
                     username = 'FallenGalaxies123',
                     password = 'Cronosphere123!',
                     user_agent= 'comp680project')
subreddit = reddit.subreddit('python')
hot_python = subreddit.hot(limit=5)

for submission in hot_python:
    print(submission)