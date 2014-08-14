# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class WordsPipeline(object):
    '''Store words into sqlite'''
    def open_spider(self, spider):
        '''Open connection to sqlite'''
        print 'open spider'

    def close_spider(self, spider):
        '''Close connection to sqlite'''
        print 'close spider'

    def process_item(self, item, spider):
        '''Store them'''
        print 'Hello item %s' % type(item)
        return DropItem()
