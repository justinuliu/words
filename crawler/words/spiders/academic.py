import scrapy
from scrapy.item import Word


class AcademicSpider(scrapy.CrawlSpider):
    name = 'AcademicSpider'
    start_urls = ['http://www.oxfordlearnersdictionaries.com/wordlist/english/academic/sublist01/']
    pass
