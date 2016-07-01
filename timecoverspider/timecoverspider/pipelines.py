# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import string

import scrapy

from scrapy.contrib.pipeline.images import ImagesPipeline

class CardImagePipeline(ImagesPipeline):  
    def file_path(self, request, response=None, info=None):
        return string.split(request.url, '/')[-3] + '/' + string.split(request.url, '/')[-1]