from praw.models.reddit.submission import Submission


class Post:
    def __init__(self, submission: Submission):

        self.redditor = submission.author
        self.title = submission.title
        self.comments = submission.comments
        self.score = submission.score
        self.creationDate = submission.created_utc

    def output(self):
        print(self.redditor)
        print(self.title)
        print(self.comments)
        print(self.score)
        print(self.creationDate)
