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
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute('create table if not exists words'
                      '(head_word varchar(30) primary key)')
            c.execute('create table if not exists definitions'
                      '(head_word varchar(30), definition varchar(300),'
                      ' num integer, foreign key(head_word)'
                      'references words(head_word));')
            conn.commit()

    def close_spider(self, spider):
        '''Close connection to sqlite'''
        print 'close spider'

    def process_item(self, item, spider):
        '''Store them'''
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            hw = item['head_word']
            c.execute('select * from words where head_word is ?', (hw))
            if c.fetchone() is None:
                c.execute('insert into words values(?)', (hw))
                for i in range(len(item['definitions'])):
                    c.execute('insert into definitions values(?, ?, ?)',
                              (item['head_word'][0],
                               i+1,
                               item['definitions'][i]))
                conn.commit()
        return DropItem()
