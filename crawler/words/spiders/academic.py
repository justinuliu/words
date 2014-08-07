import scrapy
from scrapy.contrib.spiders.crawl import CrawlSpider
from words.items import Word


class AcademicSpider(CrawlSpider):
    name = 'AcademicSpider'
    start_urls = ['http://www.oxfordlearnersdictionaries.com/wordlist/english/academic/']
    pass
