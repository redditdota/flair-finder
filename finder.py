import praw
import sys
from tokens import *

code = input("2fa code? ")
pwd = MOD_PWD
if len(code) > 0:
    pwd = MOD_PWD + ":" + code

r = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent="finder-bot",
    username=MOD,
    password=pwd)

subreddit = r.subreddit("dota2")

query = sys.argv[1]

result = set()
for f in subreddit.flair(limit=None):
    flair = f['flair_css_class']
    if flair and query in flair:
        print(f)
        result.add(f['user'].name)

print(result)
