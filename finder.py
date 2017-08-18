import praw
import sys
from tokens import *


r = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent="finder-bot",
    username=MOD,
    password=MOD_PWD)

subreddit = r.subreddit("dota2")

query = sys.argv[1]

result = set()
for f in subreddit.flair(limit=None):
    flair = f['flair_css_class']
    if flair and query in flair:
        print(f)
        result.add(f['user'].name)

print(result)
