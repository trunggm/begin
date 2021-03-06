# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# tao moi class item chua moi truyen la 1 object:
#   - ten truyen

class TruyenItem(scrapy.Item):
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

# TTN = truyentranhnet
class TTNImageItem(scrapy.Item):
    # source cua image dung de crawl    
    image_urls = scrapy.Field()
    # ten cuar image
    image_name = scrapy.Field()
    # ten truyen
    truyen = scrapy.Field()
    # chap cua image
    chap = scrapy.Field()















class ProjectBeginerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class DantriItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    
    
class TruyenFullItem(scrapy.Item):
    name = scrapy.Field()
    chap = scrapy.Field()
    auth = scrapy.Field()
    content = scrapy.Field()
    
    
    
class ImageItem(scrapy.Item):
    #ten = scrapy.Field()
    #chap = scrapy.Field()
    page_title = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    #image_urls = scrapy.Field()
    #image_name = scrapy.Field()
    #image_paths = scrapy.Field()
    #images = scrapy.Field()
                                            
class StackItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    
    
    
class TruyenTruyenFullItem(scrapy.Item):
    tentruyen = scrapy.Field()
    hinhanh = scrapy.Field()
    tacgia = scrapy.Field()
    theloai = scrapy.Field()
    nguon = scrapy.Field()
    trangthai = scrapy.Field()
    mota = scrapy.Field()
    danhgia = scrapy.Field()
    soluong = scrapy.Field()
    
class ChapTruyenFullItem(scrapy.Item):
    tentruyen = scrapy.Field()
    tenchap = scrapy.Field()
    truyen = scrapy.Field()
    chap = scrapy.Field()
    chapso = scrapy.Field()    
    noidung = scrapy.Field()
    
    
    
    
    
    
    
    
    
    
    