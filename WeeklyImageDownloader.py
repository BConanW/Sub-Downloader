__author__ = 'BCWright'

import RedditControl

# sublist = ["pics"]
with open('') as f:
    sublist = f.read().splitlines()

for item in sublist:
    ben = RedditControl.RedditC(item)
    ben.download("day")
    
for item in sublist:
    ben = RedditControl.RedditC(item)
    ben.download("week")

for item in sublist:
    ben = RedditControl.RedditC(item)
    ben.download("month")
    
for item in sublist:
    ben = RedditControl.RedditC(item)
    ben.download("year")

for item in sublist:
     ben = RedditControl.RedditC(item)
     ben.download("all")