# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import sqlite3


class WordsPipeline(object):
    db_name = 'words.db'
    '''Store words into sqlite'''
    def open_spider(self, spider):
        '''Initial database if needed'''
        print 'open spider'

    def close_spider(self, spider):
        '''Close connection to sqlite'''
        print 'close spider'

    def process_item(self, item, spider):
        '''Store them'''
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute('insert into words values(?)', (item['head_word']))
            for i in range(len(item['definitions'])):
                c.execute('insert into definitions values(?, ?, ?)',
                          (item['head_word'][0], i+1, item['definitions'][i]))
            conn.commit()

        return DropItem()
