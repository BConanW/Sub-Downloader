__author__ = 'BCWright'

import RedditControl
import logger

log = logger.StdoutLogger()

sublist = ["pics", "nvehnewghnwjolb", "aww"]
# with open('') as f:
#     sublist = f.read().splitlines()

slocation = '/Users/BCWright/Documents/Projects/SVN/Test'
# with open('savelocation.txt') as f:
#     slocation = f.read()

for item in sublist:
    ben = RedditControl.RedditC(item, slocation)
    if ben.sub_exists() is True:
        ben.download("day")
        ben.download("week")
        ben.download("month")
        ben.download("year")
        ben.download("all")
    else:
        log.info("Subreddit '%s' does not exist" % item)
        pass