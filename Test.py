import praw
import imguralbum
import urllib.request
import os
import logger
import requests

log = logger.StdoutLogger()

class main():
	
	def __init__(self):
		self.subr = "testSub" 
		self.sub = os.path.join("", self.subr)
		self.downloader = imguralbum.ImgurAlbumDownloader("")
        # log.info("This albums has %d images" % self.downloader.num_images())
        # Trial code below. Delete if script fails
		#foldernamesplit = self.url2.rpartition("/")
		#albumfoldername = foldernamesplit[2]
        # log.info('Naming folder: %s' % albumfoldername)
		#self.albumlocation = os.path.join(self.sub, albumfoldername)
		self.albumlocation = "Test"
		self.downloader.save_images(self.albumlocation)
        # end of trial code. Uncommment line below if this fails
        # self.downloader.save_images(self.sub)
		log.info("Album Download Complete")
		
main()