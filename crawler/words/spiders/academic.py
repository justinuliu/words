import scrapy
from scrapy.contrib.spiders.crawl import CrawlSpider
from words.items import Word




class AcademicSpider(CrawlSpider):
    name = 'academic'
    allowed_domains = ['oxfordlearnersdictionaries.com']
    start_urls = ['http://www.oxfordlearnersdictionaries.com/wordlist/english/academic/sublist01/?page=1']

    def _parse_word(self, response):
        word = Word()
        word['head_word'] = response.selector.xpath('//h2/span[@class="z_core_h"]/text()').extract()
        if not word['head_word']:
            word['head_word'] = response.selector.xpath('//div[@class="webtop-g"]/h2/text()').extract()
        word['definitions'] = response.selector.xpath('//span[@class="d"]/text()').extract()
        yield word

    def parse(self, response):
        for url in response.selector.xpath("//ul/li/a[contains(.//text(),'sublist')]/@href").extract():
            yield scrapy.Request(url, callback=self.parse)

        for url in response.selector.xpath('//div/span/a/@href').extract():
            yield scrapy.Request(url, callback=self.parse)

        for url in response.selector.xpath('//div/ul/li/a[contains(@title, "definition")]/@href').extract():
            yield scrapy.Request(url, callback=self._parse_word)
