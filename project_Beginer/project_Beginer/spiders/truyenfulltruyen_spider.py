# -*- coding: utf-8 -*-
import scrapy

from project_Beginer.items import  TruyenItem
from project_Beginer.supportlib import getchaper

'''    
    # ten truyen
    ten = scrapy.Field()
    # poster truyen    
    hinh = scrapy.Field()
    # tac gia cua truyen
    tacgia = scrapy.Field()
    # list cac the loai
    theloai = scrapy.Field()
    # nguon truyen
    nguon = scrapy.Field()
    # trang thai: full, dang ra, khong ro
    trangthai = scrapy.Field()
    # mota truyen:
    mota = scrapy.Field()
    # danhgia
    danhgia = scrapy.Field()
    # so luot dang gia:
    soluot = scrapy.Field()
    # chap cua chuyen
    noidung = scrapy.Field()    
'''

class TruyenFullTruyenSpider(scrapy.Spider):
    name = 'truyenfulltruyen'
    
    allowed_domains = ['truyenfull.vn']
    
    def __init__(self):
        f = open('C:/Users/thienloi/Documents/Project_Scrapy/project_Beginer/project_Beginer/spiders/linktruyen.txt', 'r');
        data = f.read()
        f.close()
        listTruyen = data.split('\n')
        self.start_urls = listTruyen#['http://truyenfull.vn/yeu-han-vo-tan/']
        
    
    # ham extract du lieu:    
    def parse(self, response):
        item = TruyenItem()
        # ten truyen
        item['ten'] = response.xpath('//*[@id="nav"]/div[2]/div/ol/li[2]/h1/a/span/text()').extract()[0]
        # poster truyen
        item['hinh'] = response.xpath('//*[@id="truyen"]/div[1]/div[1]/div[3]/div[1]/div/img/@src').extract()      [0] 
        
        # tac gia
        item['tacgia'] = response.xpath('//*[@id="truyen"]/div[1]/div[1]/div[3]/div[2]/div[1]/a/text()').extract()
        
        
        # the loai
        listTheloai = response.xpath('//*[@id="truyen"]/div[1]/div[1]/div[3]/div[2]/div[2]/a').extract()
        theloaiXpath = str('//*[@id="truyen"]/div[1]/div[1]/div[3]/div[2]/div[2]/a')
        arrayTheloai = []
        if len(listTheloai)>0:
            for i in range(len(listTheloai)):
                test = response.xpath(theloaiXpath+'['+str(i+1)+']/text()').extract()[0]
                arrayTheloai.append(test)
        else:
            arrayTheloai.append("khác")
        item['theloai'] = arrayTheloai
        
        
        
        
        
        # nguon goc 
        nguongoc = response.xpath('//*[@id="truyen"]/div[1]/div[1]/div[3]/div[2]/div[3]/span')
        if len(nguongoc)>0:
            item['nguon'] = response.xpath('//*[@id="truyen"]/div[1]/div[1]/div[3]/div[2]/div[3]/span/text()').extract()[0]
        else:
            item['nguon'] = "vô danh"
            
        # trang thai
        trangthai = response.xpath('//*[@id="truyen"]/div[1]/div[1]/div[3]/div[2]/div[4]/span')        
        if len(trangthai)>0:
            item['trangthai'] = response.xpath('//*[@id="truyen"]/div[1]/div[1]/div[3]/div[2]/div[4]/span/text()').extract()
        else:
             item['trangthai'] = "không rõ"

        # dang gia
        item['danhgia'] =  response.xpath('//*[@id="truyen"]/div[1]/div[1]/div[4]/div[1]/div[2]/em/strong[1]/span/text()').extract()[0]

        # so luot danh gia 
        item['soluot'] =  response.xpath('//*[@id="truyen"]/div[1]/div[1]/div[4]/div[1]/div[2]/em/strong[2]/span/text()').extract()[0]

        # mo ta truyen 
        a =  response.xpath('//*[@id="truyen"]/div[1]/div[1]/div[4]/div[2]/*').extract()
        item['mota'] = ''.join(a)
        
        
        # tra ve item truyen da dc craw
        yield item
        