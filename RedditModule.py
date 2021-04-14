import praw


class Reddit:
    def __init__(self, clientID, clientSecret, username, password, userAgent):
        self.clientID = clientID
        self.clientSecret = clientSecret
        self.username = username
        self.password = password
        self.userAgent = userAgent

        self.reddit = praw.Reddit(client_id = self.clientID, client_secret = self.clientSecret, username = self.username, password = self.password, user_agent = self.userAgent)

    def searchSubreddit(self, subredditName, subredditCategory, submissionLimit):
        #define subreddit object
        subreddit = self.reddit.subreddit(subredditName)

        #figure out what subcategory of the subreddit to search, default will be 'hot'
        category = subreddit.hot(limit = int(submissionLimit))
        if subredditCategory == "hot":
            category = subreddit.hot(limit=int(submissionLimit))
        elif subredditCategory == "new":
            category = subreddit.new(limit = submissionLimit)
        elif subredditCategory == "controversial":
            category = subreddit.controversial(limit = submissionLimit)
        elif subredditCategory == "top":
            category = subreddit.top(limit = submissionLimit)

        for submission in category:
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