from scrapy.spider import BaseSpider
from scrapy.contrib.loader import XPathItemLoader
from scrapy.selector import HtmlXPathSelector
from scrapy.utils.url import urljoin_rfc
from scrapy.http import Request
from imgfinder.items import ImgfinderItem

class BmysmallwebpageSpider(BaseSpider):
    name = "bmysmallwebpage"
    allowed_domains = ["mysmallwebpage.com"]
    start_urls = (
        'http://www.mysmallwebpage.com/',
        )

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        l = XPathItemLoader(item=ImgfinderItem(), response=response)

        current_url = response.url
        referer_url = response.request.headers.get('referer', None)
        
        l.add_value('img_parenturl', current_url)
        l.add_xpath('img_url', '//img/@src')
        
        yield l.load_item()

	urls = hxs.select('//a/@href').extract()
        for relurl in urls:
            url = urljoin_rfc(response.url, relurl, response.encoding)
            if "process/RedirectN?url=" in url:
                pass
            else : 
                yield Request(url, callback=self.parse, headers={'referer': url})
	#pass
