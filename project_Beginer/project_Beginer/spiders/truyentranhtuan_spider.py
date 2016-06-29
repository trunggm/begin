# -*- coding: utf-8 -*-

import scrapy
# thu vien decode
import unicodedata
from project_Beginer.supportlib import checkLink, checkFile

#from project_Beginer.items import TruyenFullItem


class TruyenFullSpider(scrapy.Spider):
    name = "truyentranhtuan"
    
    allowed_domains = ["truyentranhtuan.com"]
    
    start_urls = [
        "http://truyentranhtuan.com/",   
    ]
    
    
    def parse(self, response):
        linkArray = response.xpath('//a/@href').extract()
        url = response.url
        if checkFile("link.txt")==1:
            iofile = open("link.txt")
            data = iofile.read()
            arrayData = data.split()
            print "do dai: ", len(arrayData)
            iofile.close()
        else:
            arrayData = []
            print "do dai: ", len(arrayData)
        
        # mo file de ghi them
        appenFile = open("link.txt", "a")
        arrayNew = []
        for link in linkArray:
            # if link is unicode: convert to str            
            if type(link)==unicode:
                link = unicodedata.normalize('NFKD', link).encode('ascii','ignore')
            if checkLink(link)!=2:
                if(checkLink(link)==1):
                    link=url+link
                # kiem tra neu link nay chu co trong arrayData thi them no vao trong 
                if link not in arrayData:
                    if link.find("truyentranhtuan.com")!=-1:
                        arrayData.append(link)
                        arrayNew.append(link)
                        appenFile.write(link+"\n")
                    
        appenFile.close()
        for new in arrayNew:
            yield scrapy.Request(new, callback=self.parse)
        