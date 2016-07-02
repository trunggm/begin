# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import pymongo
import string

from scrapy.conf import settings
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import log

'''
class MyImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        return string.split(request.url, '/')[-3] + '/' + string.split(request.url, '/')[-1]
    
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_urls'])
    
    

    def item_completed(self, results, item, info):
        if results[0]:
            image_paths = item['image_name']+'.jpg'
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
'''
# ghi du lieu vao mongodb   

class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            log.msg("Question added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item
