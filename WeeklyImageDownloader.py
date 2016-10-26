__author__ = 'BCWright'

import RedditControl

sublist = ["pics"]
# with open('') as f:
#     sublist = f.read().splitlines()

slocation = 'c:\\saved\\'
# with open('savelocation.txt') as f:
#     slocation = f.read()

for item in sublist:
    ben = RedditControl.RedditC(item, slocation)
    ben.download("day")
    
for item in sublist:
    ben = RedditControl.RedditC(item, slocation)
    ben.download("week")

for item in sublist:
    ben = RedditControl.RedditC(item, slocation)
    ben.download("month")
    
for item in sublist:
    ben = RedditControl.RedditC(item, slocation)
    ben.download("year")

for item in sublist:
     ben = RedditControl.RedditC(item, slocation)
     ben.download("all")