# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TimecoverspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MagazineCover(scrapy.Item):
    title = scrapy.Field()
    pubDate = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    
class CardImage(scrapy.Item):
    page_title = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()