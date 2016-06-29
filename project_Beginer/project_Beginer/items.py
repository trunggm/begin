# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectBeginerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class DantriItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    
    
class TruyenFullItem(scrapy.Item):
    name = scrapy.Field()
    chap = scrapy.Field()
    auth = scrapy.Field()
    content = scrapy.Field()
    