import scrapy
from scrapy.contrib.spiders.crawl import CrawlSpider
from words.items import Word


class AcademicSpider(CrawlSpider):
    name = 'academic'
    allowed_domains = ['oxfordlearnersdictionaries.com']
    start_urls = ['http://www.oxfordlearnersdictionaries.com/wordlist/english/academic/sublist01/?page=1']

    def parse(self, response):
        for url in response.selector.xpath("//ul/li/a[contains(.//text(),'sublist')]/@href").extract():
            yield scrapy.Request(url, callback=self.parse)

        for url in response.selector.xpath('//div/span/a/@href').extract():
            yield scrapy.Request(url, callback=self.parse)
