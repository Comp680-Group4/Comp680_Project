import praw

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

        comments = submission.comments