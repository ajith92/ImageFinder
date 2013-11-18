# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose
from scrapy.utils.url import urljoin_rfc
from scrapy.item import Item, Field

def urljoin(url,loader_context):
    response = loader_context.get('response')
    return urljoin_rfc(response.url, url, response.encoding)

class ImgfinderItem(Item):
    # define the fields for your item here like:
    # name = Field()
    img_parenturl = Field()
    image_urls = Field(input_processor=MapCompose(urljoin),)
    images = Field()
    #img_parenturl_referer = Field()
    #img_parenturl_children = Field()
    #pass
