import scrapy
from crawler.items import webCrawlerItem

class StackOverflowSpider(scrapy.Spider):
    name = 'xiaomi'
    start_urls = ['http://app.mi.com/category/1']

    def parse(self, response):
        for sel in response.xpath('//ul[@id="all-applist"]/li/h5'):
            item = webCrawlerItem()
            item['name'] = sel.xpath('a/text()').extract()
            item['url'] = response.urljoin(sel.xpath('a/@href')[0].extract())
            
            yield item