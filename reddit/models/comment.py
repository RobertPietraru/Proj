from praw.models.comment_forest import CommentForest
from praw.models.reddit.comment import Comment




class Comment:
    def __init__(self, comments):


        self.comments = []
        for comment in comments:
            self.comments.append(comment)


if __name__ == '__main__':
    pass