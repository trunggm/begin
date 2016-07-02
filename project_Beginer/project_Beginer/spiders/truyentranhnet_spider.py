# -*- coding: utf-8 -*-
import scrapy
import unicodedata
from project_Beginer.items import TTNImageItem, ImageItem


class TTNImageSpider(scrapy.Spider):
    name = "ttnimage"
    allowed_domains = ['truyentranh.net']
    
    def __init__(self):
        f = open("C:/Users/thienloi/Documents/Project_Scrapy/project_Beginer/processFile/linktruyentranhChap.txt", 'r')
        data = f.read()
        f.close()
        listlink = data.split('\n')
        #self.start_urls = listlink[:1]
        self.start_urls = ['http://truyentranh.net/naruto/chap-002/',]
    
    def parse(self, response):
        arr = response.url.split('/')
        tentruyen = arr[3]
        tenchap = arr[4]
        arrSrc = []
        a = response.xpath('/html/body/section/div[3]/div[8]/div/div/img').extract()
        for i in range(len(a)):
            src = response.xpath('/html/body/section/div[3]/div[8]/div/div/img['+str(i+1)+']/@src').extract()[0]
            if type(src) == unicode:
                src = unicodedata.normalize('NFKD', src).encode('ascii','ignore')
            arrSrc.append(src.split('?')[0])
        
        item = ImageItem()
        for i in range(len(arrSrc)):
            #item['ten'] = tentruyen
            #item['chap'] = tenchap
            item["image_urls"] = arrSrc[i]
            item["page_title"] = "pic"+str(i)
            #item["image_paths"] = item['ten']+'/'+item['chap']+'/'+item['image_name']+'.jpg'
            yield item       



