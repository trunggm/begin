# -*- coding: utf-8 -*-

import scrapy
# thu vien decode
import unicodedata
import string
from project_Beginer.supportlib import checkLink, checkFile

from project_Beginer.items import TruyenTruyenFullItem


class TruyenFullSpider(scrapy.Spider):
    name = "truyenfullten"
    
    allowed_domains = ["truyenfull.vn"]
    #start_urls = ["http://truyenfull.vn/tro-dua-cua-adam/",]
    
    def __init__(self):
        f = open("C:/Users/thienloi/Documents/Project_Scrapy/project_Beginer/project_Beginer/spiders/linkTruyen.txt", "r")
        data = f.read()
        f.close()
        self.start_urls = data.split("\n")

    # tentruyen = scrapy.Field()
    # hinhanh = scrapy.Field()
    # tacgia = scrapy.Field()
    # theloai = scrapy.Field()
    # nguon = scrapy.Field()
    # trangthai = scrapy.Field()
    # sochuong = scrapy.Field()
    # mota = scrapy.Field()
    # danhgia = scrapy.Field()
    # soluong = scrapy.Field()    

    
    def parse(self, response):
        item = TruyenTruyenFullItem()
        item['tentruyen'] = response.xpath('//*[@id="truyen"]/div[1]/div[1]/div[4]/h3/text()').extract()[0]
        item['hinhanh'] = response.xpath('//*[@id="truyen"]/div[1]/div[1]/div[3]/div[1]/div/img/@src').extract()[0]
        item['tacgia'] = response.xpath('//*[@id="truyen"]/div[1]/div[1]/div[3]/div[2]/div[1]/a/text()').extract()[0]
        
        listTheloai = response.xpath('//*[@id="truyen"]/div[1]/div[1]/div[3]/div[2]/div[2]/a').extract()
        theloaiXpath = str('//*[@id="truyen"]/div[1]/div[1]/div[3]/div[2]/div[2]/a')
        arrayTheloai = []
        for i in range(len(listTheloai)):
            test = response.xpath(theloaiXpath+'['+str(i+1)+']/text()').extract()[0]
            arrayTheloai.append(test)
        item['theloai'] = arrayTheloai
        
        item['nguon'] = response.xpath('//*[@id="truyen"]/div[1]/div[1]/div[3]/div[2]/div[3]/span/text()').extract()[0]
        
        trangthai = response.xpath('//*[@id="truyen"]/div[1]/div[1]/div[3]/div[2]/div[4]/span')        
        if len(trangthai)>0:
            item['trangthai'] = response.xpath('//*[@id="truyen"]/div[1]/div[1]/div[3]/div[2]/div[4]/span/text()').extract()
        else:
             item['trangthai'] = "không rõ"
        
        item['mota'] = response.xpath('//*[@id="truyen"]/div[1]/div[1]/div[4]/div[2]/text()').extract()[0]
        
        item['danhgia'] = response.xpath('//*[@id="truyen"]/div[1]/div[1]/div[4]/div[1]/div[2]/em/strong[1]/span/text()').extract()[0]
        
        item['soluong'] = response.xpath('//*[@id="truyen"]/div[1]/div[1]/div[4]/div[1]/div[2]/em/span/text()').extract()[0]
        
        yield item