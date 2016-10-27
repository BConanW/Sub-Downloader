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
    ben.download("week")
    ben.download("month")
    ben.download("year")
    ben.download("all")