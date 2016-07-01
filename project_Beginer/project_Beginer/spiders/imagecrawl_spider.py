# -*- coding: utf-8 -*-
import scrapy

class ImageCrawlSpider(scrapy.Spider):
    name = "imagecrawl"
    
    allowed_domains = ["truyentranh.net"]
    
    start_url = [
        "http://truyentranh.net/marchan-the-embodiment-of-tales/chap-085",    
    ]
    
    def parse(self, response):
        node = responsive.xpath("/html/body/section/div[3]/div[8]/div/div/text()").extract()[0]
        print response.body
