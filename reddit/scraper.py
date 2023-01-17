from praw import Reddit
from praw.models.reddit.submission import Submission
from praw.models.comment_forest import CommentForest
from praw.models import MoreComments

from models.comment import Comment

from models.post import Post

reddit = Reddit(

    client_id="asdf",
    client_secret="asdf",
    user_agent="asdf",
)


def getComments(comments: CommentForest):
    output = []
    for comment in comments:
        if not isinstance(comment, MoreComments):
            output.append(Comment(comment))

    return output

if __name__ == "__main__":

    for submission in reddit.subreddit('memes').hot(limit=1):
        submission: Submission = submission

        post = Post(submission)
        post.output()

        submission.comment_sort = 'best'
        submission.comment_limit = 5
        submission.comments.replace_more(limit=0)

        comments = getComments(submission.comments)
    print('done')
