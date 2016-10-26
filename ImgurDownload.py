import os
import urllib.request
import imguralbum
import logger

log = logger.StdoutLogger()

class ImgurException(Exception):
    def __init__(self, msg=False):
        self.msg = msg

class ImgurDownloader:

    def __init__(self, imgur_url, save_location):

        self.imgur_url = imgur_url
        self.save_location = save_location

        if "imgur" in self.imgur_url:
            log.info("URL is Imgur")
            if any (x in self.imgur_url for x in [".png", ".jpg", ".jpeg", ".gif", ".gifv"]):
                log.info("Attempting to download single image")
                try:
                    imagename = self.imgur_url.rpartition("/")[2]
                    imagesavelocation = self.save_location + "/" + imagename
                    if not os.path.exists(imagesavelocation):
                        urllib.request.urlretrieve(self.imgur_url, imagesavelocation)
                        log.info("Image '%s' successfully saved" % imagename)
                    else:
                        ImgurException("Image '%s' already exists" % imagename)
                except:
                    log.info("Unable to download from URL: %s" % self.imgur_url)

            else:
                log.info("Attempting to download album")
                try:
                    albumdownloader = imguralbum.ImgurAlbumDownloader(self.imgur_url)
                    albumfoldername = self.imgur_url.rpartition("/")[2]
                    albumlocation = os.path.join(self.save_location, albumfoldername)
                    albumdownloader.save_images(albumlocation)
                    log.info("Album '%s' download complete" % albumfoldername)

                except:
                    ImgurException("Failed to download album from URL: %s" % self.imgur_url)


        else:
            raise ImgurException("URL is not Imgur")




ImgurDownloader("http://imgur.com/a/uAFvn", 'c:\\saved\\')





        # if 'imgur' in self.imgur_url:
        #     log.info("URL is Imgur")
        #     if any(x in self.imgur_url for x in [".png", ".jpg", ".jpeg", "gif", "gifv"]):
        #         try:
        #             # log.info("Attempting to download %s using urllib" % self.url2)
        #             imagenamesplit = self.imgur_url.rpartition("/")
        #             imagename = imagenamesplit[2]
        #             # log.info("attempting to save with name: %s" % imagename)
        #             imagesavelocation = self.sub + "/" + imagename
        #             # log.info("Attempting to download to %s" % imagesavelocation)
        #             # log.info(os.path.abspath(imagesavelocation))
        #             fullfilename = os.path.join("", imagesavelocation)
        #             if not os.path.exists(fullfilename):
        #                 # log.info(fullfilename)
        #                 urllib.request.urlretrieve(self.imgur_url, fullfilename)
        #                 log.info("Image Download Complete")
        #             else:
        #                 log.info("Skipping. File already exists")
        #         except:
        #             log.info("Unable to download %s" % self.url2)
        #             pass
        #
        #     else:
        #         try:
        #             self.downloader = imguralbum.ImgurAlbumDownloader(self.url2)
        #             # log.info("This albums has %d images" % self.downloader.num_images())
        #             # Trial code below. Delete if script fails
        #             foldernamesplit = self.url2.rpartition("/")
        #             albumfoldername = foldernamesplit[2]
        #             # log.info('Naming folder: %s' % albumfoldername)
        #             self.albumlocation = os.path.join(self.sub, albumfoldername)
        #             self.downloader.save_images(self.albumlocation)
        #             # end of trial code. Uncommment line below if this fails
        #             # self.downloader.save_images(self.sub)
        #             log.info("Album Download Complete")
        #
        #         except imguralbum.ImgurAlbumException:
        #             log.info("Failed to download: %s" % self.url2)
        #
        #
        #
        #
        #
        # else:
        #     raise ImgurException("URL is not Imgur")
        #
        # if any(x in self.url2 for x in [".png", ".jpg", ".jpeg", "gif", "gifv"]):
        #     try:
        #         # log.info("Attempting to download %s using urllib" % self.url2)
        #         imagenamesplit = self.url2.rpartition("/")
        #         imagename = imagenamesplit[2]
        #         # log.info("attempting to save with name: %s" % imagename)
        #         imagesavelocation = self.sub + "/" + imagename
        #         # log.info("Attempting to download to %s" % imagesavelocation)
        #         # log.info(os.path.abspath(imagesavelocation))
        #         fullfilename = os.path.join("", imagesavelocation)
        #         if not os.path.exists(fullfilename):
        #             # log.info(fullfilename)
        #             urllib.request.urlretrieve(self.url2, fullfilename)
        #             log.info("Image Download Complete")
        #         else:
        #             log.info("Skipping. File already exists")
        #     except:
        #         log.info("Unable to download %s" % self.url2)
        #         pass
        #
        # else:
        #     try:
        #         self.downloader = imguralbum.ImgurAlbumDownloader(self.url2)
        #         # log.info("This albums has %d images" % self.downloader.num_images())
        #         # Trial code below. Delete if script fails
        #         foldernamesplit = self.url2.rpartition("/")
        #         albumfoldername = foldernamesplit[2]
        #         # log.info('Naming folder: %s' % albumfoldername)
        #         self.albumlocation = os.path.join(self.sub, albumfoldername)
        #         self.downloader.save_images(self.albumlocation)
        #         # end of trial code. Uncommment line below if this fails
        #         # self.downloader.save_images(self.sub)
        #         log.info("Album Download Complete")
        #
        #     except imguralbum.ImgurAlbumException:
        #         log.info("Failed to download: %s" % self.url2)