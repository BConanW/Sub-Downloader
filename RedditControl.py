__author__ = 'BCWright'

import praw
import ImageDownload
import urllib.request
import os
import logger
import requests

log = logger.StdoutLogger()

class RedditC(object):

    def __init__(self, sub, slocation):
        self.subr = sub
        self.slocation = slocation

        log.info("sub is: %s" % self.subr)
        self.r = praw.Reddit(user_agent="bens_an_agent")
        # log.info(self.r)

    def login(self, username, password):
        self.r.login(username, password)

    # def top(self, amount):
    #     self.nmbr = amount
    #     self.submissions = self.subreddit.get_top(self.nmbr)
    #     for self.submission in self.submissions:
    #         log.info(self.submission)
    #         self.url = self.submission.url
    #         log.info(self.url)

    def download(self, topof):

        self.sub = os.path.join(self.slocation, self.subr)
        if not os.path.exists(self.sub):
            log.info("Making new directory for sub %s" % self.subr)
            os.mkdir(self.sub)

        self.topof = topof
        log.info("Downloading top of the %s" % self.topof)
        if self.topof is "day":
            self.toplist = self.subreddit.get_top_from_day()
        elif "week":
            self.toplist = self.subreddit.get_top_from_week()
        elif "month":
            self.toplist = self.subreddit.get_top_from_month()
        elif "year":
            self.toplist = self.subreddit.get_top_from_year()
        elif "all":
            self.toplist = self.subreddit.get_top_from_all()
        else:
            log.info("Please state time frame: day, week, month, year, all")

        for self.submission in self.toplist:
            self.url = self.submission.url

            if "imgur" in self.url:
                ImageDownload.ImgurDownloader(self.url, self.sub)

            elif "redd" in self.url:
                ImageDownload.RedditDownloader(self.url, self.sub)

            else:
                ImageDownload.GenericDownloader(self.url, self.sub)
                
    def sub_exists(self):
        try:
            self.subreddit = self.r.get_subreddit(self.subr, fetch=True)
            return True
        except:
            # log.info("Subreddit does not exist")
            return False

