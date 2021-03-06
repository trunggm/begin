# -*- coding: utf-8 -*-

import scrapy
# thu vien decode
import unicodedata
import string
from project_Beginer.supportlib import checkLink, checkFile, getchaper

from project_Beginer.items import ChapTruyenFullItem


class TruyenFullSpider(scrapy.Spider):
    name = "truyenfullchap"
    
    allowed_domains = ["truyenfull.vn"]
    #start_urls = ["http://truyenfull.vn/tro-dua-cua-adam/",]
    
    def __init__(self):
        f = open("C:/Users/thienloi/Documents/Project_Scrapy/project_Beginer/project_Beginer/spiders/linkchap.txt", "r")
        data = f.read()
        f.close()
        self.start_urls = data.split("\n")
        #self.start_urls = ['http://truyenfull.vn/nguoi-dan-ong-kien-cuong/chuong-3/']
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
        item = ChapTruyenFullItem()
        # lay ten chuyen
        item['tentruyen'] = response.xpath('//*[@id="wrap"]/div[2]/div/div/a[2]/text()').extract()[0]
        #lay noi dung cua chap
        noidung = response.xpath('//*[@id="wrap"]/div[2]/div/div/div[4]/text()').extract()
        item['noidung'] = ''.join(noidung)
        # lay ten cua chap
        item['tenchap'] = response.xpath('//*[@id="wrap"]/div[2]/div/div/h2/a/@title').extract()[0]
        
        url = response.url     
        #lay ten chuyen
        item['truyen'] = url.split('/')[3]
        # lay ten chap 
        item['chap']= url.split('/')[4]
        # chap so la 1 tuple
        #item['chapso'] = getchaper(item['tenchap'])
        
        
        yield item

