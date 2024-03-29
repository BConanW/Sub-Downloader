import os
import re
import urllib.request
import requests
import imguralbum
import logger
from bs4 import BeautifulSoup
from urllib.request import urlopen

log = logger.StdoutLogger()


class ImageDownload:

    def __init__(self, image_url, save_location):
        if "imgur" in image_url:
            ImgurDownloader(image_url, save_location)
        elif "redd" in image_url:
            RedditDownloader(image_url, save_location)
        elif "gfycat" in image_url:
            GfycatDownloader(image_url, save_location)
        else:
            GenericDownloader(image_url, save_location)


class ImgurDownloader:

    def __init__(self, imgur_url, save_location):

        self.imgur_url = imgur_url
        self.save_location = save_location

        if "imgur" in self.imgur_url:
            # log.info("URL is Imgur")
            if any (x in self.imgur_url for x in [".png", ".jpg", ".jpeg", ".gif", ".gifv"]):
                # log.info("Attempting to download single image")
                try:
                    imagename = self.imgur_url.rpartition("/")[2]
                    imagesavelocation = self.save_location + "/" + imagename
                    if not os.path.exists(imagesavelocation):
                        urllib.request.urlretrieve(self.imgur_url, imagesavelocation)
                        log.info("Download Complete: %s" % self.imgur_url)
                    else:
                        log.info("Image already exists: %s" % self.imgur_url)
                except:
                    log.info("Unable to download from URL: %s" % self.imgur_url)

            elif any (x in self.imgur_url for x in ["/a/", "/gallery/", "/topic/"]):
                # log.info("Attempting to download album")
                try:
                    albumdownloader = imguralbum.ImgurAlbumDownloader(self.imgur_url)
                    if albumdownloader.num_images() == 1:
                        albumlocation =self.save_location
                    else:
                        albumfoldername = self.imgur_url.rpartition("/")[2]
                        albumlocation = os.path.join(self.save_location, albumfoldername)
                    # log.info("%s images in album" % albumdownloader.num_images())
                    albumdownloader.save_images(albumlocation)
                    log.info("Album Download Complete: %s" % self.imgur_url)

                except:
                    log.info("Failed to download album from URL: %s" % self.imgur_url)

            else:
                imgur_link = imgur_url.rpartition("//")[2]
                directlink = "http://" + "i." + imgur_link + ".jpg"

                try:
                    # log.info("Attempting to download %s using urllib" % self.image_url)
                    imagename = directlink.rpartition("/")[2]
                    # log.info("attempting to save with name: %s" % imagename)
                    imagesavelocation = self.save_location + "/" + imagename
                    # log.info("Attempting to download to %s" % imagesavelocation)
                    if not os.path.exists(imagesavelocation):
                        # log.info(imagesavelocation)
                        urllib.request.urlretrieve(directlink, imagesavelocation)
                        log.info("Download complete: %s" % directlink)
                    else:
                        log.info("Skipping. File already exists: %s" % directlink)
                except:
                    log.info("Unable to download: %s" % directlink)
                    pass



        else:
            log.error("URL is not Imgur: %s" % self.imgur_url)

class RedditDownloader:

    def __init__(self, reddit_url, save_location):
        self.reddit_url = reddit_url
        self.save_location = save_location

        if "redd" in self.reddit_url:
            # log.info("URL is Reddit")
            imagename = self.reddit_url.rpartition("/")[2]

            if "reddituploads" in reddit_url:
                # log.info("Image hosted on reddituploads, name requires formatting")
                imagename = imagename.rpartition("?")[0] + ".jpg"
                # log.info("Formatting Complete")
            else:
                pass

            imagesavelocation = self.save_location + "/" + imagename

            try:
                if os.path.isfile(imagesavelocation) is True:
                    log.info("Image already exists: %s" % self.reddit_url)
                else:
                    # log.info("Attempting to download: %s" % self.reddit_url)
                    self.response = requests.get(self.reddit_url)

                    # log.info('Image will be saved with name: %s' % imagesavelocation)
                    self.f = open(imagesavelocation, 'wb')
                    # log.info('local image name created')
                    self.f.write(self.response.content)
                    log.info("Download Complete: %s" % self.reddit_url)
                    self.f.close()
                    # log.info('connection closed')
            except:
                log.info('Unable to save: %s' % self.reddit_url)




        else:
            log.info("URL is not Reddit: %s" % self.reddit_url)


class GfycatDownloader:

    def __init__(self, image_url, save_location):

        self.image_url = image_url
        self.save_location = save_location

        html = urlopen(self.image_url)
        soup = BeautifulSoup(html, 'html.parser')
        
        for link in soup.find_all(type="video/webm"):
            # log.info("getting link")
            directlink = link.get("src")
            # log.info("Direct Link: %s" % directlink)

        try:
            # log.info("Attempting to download %s using urllib" % self.image_url)
            imagename = directlink.rpartition("/")[2]
            # log.info("attempting to save with name: %s" % imagename)
            imagesavelocation = self.save_location + "/" + imagename
            # log.info("Attempting to download to %s" % imagesavelocation)
            if not os.path.exists(imagesavelocation):
                # log.info(imagesavelocation)
                urllib.request.urlretrieve(directlink, imagesavelocation)
                log.info("Download complete: %s" % self.image_url)
            else:
                log.info("Skipping. File already exists: %s" % self.image_url)
        except:
            log.info("Unable to download: %s" % self.image_url)
            pass


class GenericDownloader:

    def __init__(self, image_url, save_location):

        self.image_url = image_url
        self.save_location = save_location

        # log.info("Attempting to Dowload: %s" % self.image_url)
        if any(x in self.image_url for x in [".png", ".jpg", ".jpeg", "gif", "gifv"]):
            try:
                # log.info("Attempting to download %s using urllib" % self.image_url)
                imagename = self.image_url.rpartition("/")[2]
                # log.info("attempting to save with name: %s" % imagename)
                imagesavelocation = self.save_location + "/" + imagename
                # log.info("Attempting to download to %s" % imagesavelocation)
                if not os.path.exists(imagesavelocation):
                    # log.info(imagesavelocation)
                    urllib.request.urlretrieve(self.image_url, imagesavelocation)
                    log.info("Download complete: %s" % self.image_url)
                else:
                    log.info("Skipping. File already exists: %s" % self.image_url)
            except:
                log.info("Unable to download: %s" % self.image_url)
                pass