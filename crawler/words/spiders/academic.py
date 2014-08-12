import scrapy
from scrapy.contrib.spiders.crawl import CrawlSpider
from words.items import Word




class AcademicSpider(CrawlSpider):
    name = 'academic'
    allowed_domains = ['oxfordlearnersdictionaries.com']
    start_urls = ['http://www.oxfordlearnersdictionaries.com/wordlist/english/academic/sublist01/?page=1']
    empty_words = 0
    empty_defs = 0

    def _parse_word(self, response):
        word = Word()
        word['head_word'] = response.selector.xpath('//h2/span[@class="z_core_h"]/text()').extract()
        if not word['head_word']:
            word['head_word'] = response.selector.xpath('//div[@class="webtop-g"]/h2/text()').extract()
        word['definition'] = response.selector.xpath('//span[@class="d"]/text()').extract()
        if not word['head_word']:
            self.empty_words = self.empty_words + 1
        if not word['definition']:
            self.empty_defs = self.empty_defs + 1
        print 'empty words is %d' % self.empty_words
        print 'empty definition is %d' % self.empty_defs
        print 'word is %s, definition is %s' % (word['head_word'], word['definition'])

    def parse(self, response):
        for url in response.selector.xpath("//ul/li/a[contains(.//text(),'sublist')]/@href").extract():
            yield scrapy.Request(url, callback=self.parse)

        for url in response.selector.xpath('//div/span/a/@href').extract():
            yield scrapy.Request(url, callback=self.parse)

        for url in response.selector.xpath('//div/ul/li/a[contains(@title, "definition")]/@href').extract():
            yield scrapy.Request(url, callback=self._parse_word)
