import praw


class Reddit:
    def __init__(self, clientID, clientSecret, username, password, userAgent):
        self.clientID = clientID
        self.clientSecret = clientSecret
        self.username = username
        self.password = password
        self.userAgent = userAgent

        self.reddit = praw.Reddit(client_id = self.clientID, client_secret = self.clientSecret, username = self.username, password = self.password, user_agent = self.userAgent)


        ####TODO - add in fields for the user data that we're trying to track
        #self.usernameToTrack

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

    #This will take in all the user data, along with the subreddit you're tracking them in
    #   and it will output all posts that user has posted in that specific subreddit
    def searchUserDataInSubreddit(self):
        print("Not implemented yet")

    #This will take in all the user data, a number of "words", and then track how many times user has used those
    #   specific words in all posts they have made on reddit ever.
    #Out put will be a pie graph denoting precentages of how often they
    #   have used those words relative to the other words
    def searchTrackUserKeywordUsage(self):
        print("Not implemented yet")

    #This will take in all user data, a timeframe - (for simplicity, a number of days, which will be the X-axis on outputted histogram)
    #   Will count how many times user has posted on each of those days going back from current day to N (Number of days passed in)
    #   Will output a bar graph or histogram with each bar representing how many times the user has posted on that day
    def trackUserActivityOverTimeframe(self, numberDays):
        print("Not implemented yet")