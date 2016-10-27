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
        self.sub = os.path.join(self.slocation, self.subr)
        if not os.path.exists(self.sub):
            log.info("Making new directory for sub %s" % self.subr)
            os.mkdir(self.sub)
        self.r = praw.Reddit(user_agent="bens_an_agent")
        # log.info(self.r)
        self.subreddit = self.r.get_subreddit(self.subr)

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
                log.info("Attempting to Dowload: %s" % self.url)
                if any(x in self.url for x in [".png", ".jpg", ".jpeg", "gif", "gifv"]):
                    try:
                        # log.info("Attempting to download %s using urllib" % self.url)
                        imagenamesplit = self.url.rpartition("/")
                        imagename = imagenamesplit[2]
                        # log.info("attempting to save with name: %s" % imagename)
                        imagesavelocation = self.sub + "/" + imagename
                        # log.info("Attempting to download to %s" % imagesavelocation)
                        # log.info(os.path.abspath(imagesavelocation))
                        fullfilename = os.path.join(self.slocation, imagesavelocation)
                        if not os.path.exists(fullfilename):
                            # log.info(fullfilename)
                            urllib.request.urlretrieve(self.url, fullfilename)
                            log.info("Download complete")
                        else:
                        	log.info("Skipping. File already exists")
                    except:
                        log.info("Unable to download %s" % self.url)
                        pass
                



