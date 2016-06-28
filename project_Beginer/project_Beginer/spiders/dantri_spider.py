# -*- coding: utf-8 -*-
import scrapy

from project_Beginer.items import DantriItem


class DantriSpyder(scrapy.Spider):
    name = "dantri"
    allowed_domains = ["dantri.com.vn"]
    start_urls = ["http://dantri.com.vn/",]
    
    
    def parse(self, response):
        item = DantriItem()
        
        item["title"] = response.xpath('/html/head/title')
        item["link"] = response.url
        
        f = open("link.txt", "wt")
        linkArray = response.xpath('//a//@href').extract()
        for link in linkArray:
            f.write(link+"\n");
            
        f.close()

