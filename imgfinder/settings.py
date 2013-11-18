# Scrapy settings for imgfinder project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'imgfinder'

SPIDER_MODULES = ['imgfinder.spiders']
NEWSPIDER_MODULE = 'imgfinder.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'imgfinder (+http://www.yourdomain.com)'

SPIDER_MIDDLEWARES = {
                        'scrapy.contrib.spidermiddleware.httperror.HttpErrorMiddleware': 50,
                        'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware': 500,
                        'scrapy.contrib.spidermiddleware.referer.RefererMiddleware': 700,
                        'scrapy.contrib.spidermiddleware.urllength.UrlLengthMiddleware': 800,
                        'scrapy.contrib.spidermiddleware.depth.DepthMiddleware': 900,
                     }

DOWNLOADER_MIDDLEWARES = {
                            'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware': 123,
                         }

ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}

IMAGES_STORE = 'imgfinder/images/'

# 90 days of delay for image expiration
IMAGES_EXPIRES = 90

IMAGES_MIN_HEIGHT = 4
IMAGES_MIN_WIDTH = 4
