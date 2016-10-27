import os
import urllib.request
import requests
import logger

log = logger.StdoutLogger()

class RedditDownloader:

    def __init__(self, reddit_url, save_location):
        self.reddit_url = reddit_url
        self.save_location = save_location

        if "redd" in self.reddit_url:
            log.info("URL is Reddit")
            imagesavelocation = self.save_location + "/" + self.reddit_url.rpartition("/")[2]

            if "reddituploads" in reddit_url:
                log.info("Image hosted on reddituploads, name requires formatting")
                imagesavelocation = imagesavelocation.rpartition("?")[0] + ".jpg"
                log.info("Formatting Complete")
            else:
                pass

            try:
                log.info("Attempting to download: %s" % self.reddit_url)
                self.response = requests.get(self.reddit_url)
                log.info('Image will be saved with name: %s' % imagesavelocation)
                self.f = open(imagesavelocation, 'wb')
                log.info('local image name created')
                self.f.write(self.response.content)
                log.info('Download Complete')
                self.f.close()
                # log.info('connection closed')
            except:
                log.info('Unable to save: %s' % self.reddit_url)




        else:
            log.info("URL is not Reddit: %s" % self.reddit_url)






# elif 'reddituploads' in self.url:
# log.info('URL is reddituploads: %s' % self.url)
# imagesavelocation = self.sub + "/" + self.url.rpartition("/")[2]
# # log.info('Attempting to save to: %s' % imagesavelocation)
# try:
#     self.response = requests.get(self.url)
#     # log.info('URL has been retrieved')
#     imagesavelocation = imagesavelocation.rpartition("?")[0] + '.jpg'
#     # log.info('Image will be saved with name: %s' % imagesavelocation)
#     fullfilename = os.path.join(self.slocation, imagesavelocation)
#     self.f = open(fullfilename, 'wb')
#     # log.info('local image name created')
#     self.f.write(self.response.content)
#     log.info('Download Complete')
#     self.f.close()
#     # log.info('connection closed')
# except:
#     log.info('Unable to save: %s' % self.url)
#
# elif 'redd' in self.url:
# # log.info('URL is i.redd.it: %s' % self.url)
# imagesavelocation = self.sub + "/" + self.url.rpartition("/")[2]
# fullfilename = os.path.join(self.slocation, imagesavelocation)
# # log.info('Attempting to save to: %s' % imagesavelocation)
# try:
#     self.response = requests.get(self.url)
#     # log.info('URL has been retrieved')
#     self.f = open(fullfilename, 'wb')
#     # log.info('local image name created')
#     self.f.write(self.response.content)
#     log.info('Download Complete')
#     self.f.close()
#     # log.info('connection closed')
# except:
#     # log.info('Unable to save: %s' % self.url)
#     pass
