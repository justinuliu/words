# -*- coding: utf-8 -*-

# Scrapy settings for words project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'words'

SPIDER_MODULES = ['words.spiders']
NEWSPIDER_MODULE = 'words.spiders'
ITEM_PIPELINES = {
    'words.pipelines.WordsPipeline': 500,
    }
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'words (+http://www.yourdomain.com)'
