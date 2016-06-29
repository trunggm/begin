# -*- coding: utf-8 -*-
import scrapy
from project_Beginer.items import ImageItem

arrayTest = ["http://1.bp.blogspot.com/-PhJOFkItuQ8/V2u77rs30bI/AAAAAAAAjPQ/8mrU8iym3bsrabSyh5W28HPFGiCao3nRgCHM/s0/01.jpg?imgmax=3000","http://1.bp.blogspot.com/-dT5XsZxKZwk/V2u77inrVCI/AAAAAAAAjPQ/iY72fT2FInIbpcdyHsctVtNggUa78w3LwCHM/s0/02.jpg?imgmax=3000","http://1.bp.blogspot.com/-K-tx476__K4/V2u77o_a7QI/AAAAAAAAjPQ/sAnilTw4prkNHlPze0dNo8xig77FdcMPQCHM/s0/03.jpg?imgmax=3000","http://1.bp.blogspot.com/-gRvtZUvLWfY/V2u78N9ga6I/AAAAAAAAjPQ/8BjZD8TRawEIRgwEeb0xI4dQVaV_wrnhACHM/s0/04.jpg?imgmax=3000","http://1.bp.blogspot.com/-jr6cddr98xw/V2u78TNkQjI/AAAAAAAAjPQ/VDLvmU_EgSItI_mvgVtsYm2h81nMlwG3ACHM/s0/05.jpg?imgmax=3000","http://1.bp.blogspot.com/-DAxRt01PMN0/V2u78blobSI/AAAAAAAAjPQ/UOV5KnCjH_MHk7Uz6SHf1kCrRYoGPw5uQCHM/s0/06.jpg?imgmax=3000","http://1.bp.blogspot.com/-Vo1QEE1g3Uc/V2u78-MOkAI/AAAAAAAAjPQ/iSYYfpPvsOI_05NKR6-ufaeoCsMqhsXbACHM/s0/07.jpg?imgmax=3000","http://1.bp.blogspot.com/-HYOCrWcxhCo/V2u79ZEyvyI/AAAAAAAAjPQ/yFGjJRpQUxEnQ7Z8Otg_WKZxlwCqMVdXwCHM/s0/08.jpg?imgmax=3000","http://1.bp.blogspot.com/-d-7NsX7pCJw/V2u790TGBPI/AAAAAAAAjPQ/BEOMnsMykb0kshhx6j2Mvf8eODrr9Ov-gCHM/s0/09.jpg?imgmax=3000","http://1.bp.blogspot.com/-VTziMo3nBSg/V2u7-PuUPZI/AAAAAAAAjPQ/t7x4W3nXWH0A1D8CaQlPmIOxrNfG8YZPQCHM/s0/10.jpg?imgmax=3000","http://1.bp.blogspot.com/-GEtEJ5FcRaI/V2u7-RBKhdI/AAAAAAAAjPQ/5oBejJ4Q-gwxPZzXtcDGPXEZF3SZvBzwQCHM/s0/11.jpg?imgmax=3000","http://1.bp.blogspot.com/-fNYP2WQ8xzs/V2u7-sCQDjI/AAAAAAAAjPQ/pfYB9B2ShqcZSmCqKUkRC9P0mNgfz2MZgCHM/s0/12.jpg?imgmax=3000","http://1.bp.blogspot.com/-k2-kGoY9sSY/V2u7-9rqOmI/AAAAAAAAjPQ/ueADmH1kgyoCToUc2u4ksPqSSXkOgnKcwCHM/s0/13.jpg?imgmax=3000","http://1.bp.blogspot.com/-roPyIHztcGA/V2u7_n2hbjI/AAAAAAAAjPQ/w6FUmiPhBGE2EKuWnKTDn581Ov_F2iHKACHM/s0/14.jpg?imgmax=3000","http://1.bp.blogspot.com/-Wns_fJtkOc8/V2u8AKM9OvI/AAAAAAAAjPQ/q0qCD9l3C0Iy_oaRQMocZ83wpDRY_Fx7wCHM/s0/15.jpg?imgmax=3000","http://1.bp.blogspot.com/-bE2Fu7nNxzQ/V2u8A31kflI/AAAAAAAAjPQ/xM7NoJeVNBUcYdBiwZkcBug18wtJyWnwQCHM/s0/16.jpg?imgmax=3000","http://1.bp.blogspot.com/-LXkQaWOe56o/V2u8BEm51mI/AAAAAAAAjPQ/NGPcNAafEWou-LlYt-CD4soFrj740wNwgCHM/s0/17.jpg?imgmax=3000","http://1.bp.blogspot.com/-4jGEjgJc_EA/V2u8BTwjshI/AAAAAAAAjPQ/gKgEpkdrSd8JiLStycrHTUgXtrMteC_5QCHM/s0/18.jpg?imgmax=3000","http://1.bp.blogspot.com/-EkkGCMO9VZE/V2u8BltDyaI/AAAAAAAAjPQ/xKtgMPrHy781ypvxFZbHmLye7UHwU90QACHM/s0/19.jpg?imgmax=3000","http://1.bp.blogspot.com/-yy-76crJe6M/V2u8B9BFTnI/AAAAAAAAjPQ/VFf8Yg1TKxYG9_HttzVmMOPG4wuXZxiVgCHM/s0/20.jpg?imgmax=3000","http://1.bp.blogspot.com/-cjErFGUoo4I/V2u8CsZKhvI/AAAAAAAAjP8/yu1nuom7UCIBu8iGFWe522vuaJjjJ5iDgCHM/s0/21.jpg?imgmax=3000","http://1.bp.blogspot.com/-j8gqiA0FbTE/V2u8DhXCQjI/AAAAAAAAjP8/myrW17v56WEZKHp1XeSEQEnoYmevI81_ACHM/s0/22.jpg?imgmax=3000","http://1.bp.blogspot.com/-VwKSS7UYgZM/V2u8DpD3_lI/AAAAAAAAjP8/xHDdaEl7PM0-qJ_ukzYtlHtsWbueFid1wCHM/s0/23.jpg?imgmax=3000","http://1.bp.blogspot.com/-tKTKtP9rnp0/V2u8D-05zCI/AAAAAAAAjP8/TydPGfSStyAkSjNXk_5Dm8HzvS4zbeyqQCHM/s0/24.jpg?imgmax=3000","http://1.bp.blogspot.com/-FEhem-GRj0E/V2u8EAL9gVI/AAAAAAAAjP8/cf6PPHo-ejoTRhHgz0zZyKDHaF8B3i9kQCHM/s0/25.jpg?imgmax=3000"]


# khai bao mot class la class con scrapy.spider

class ImageTestSpider(scrapy.Spider):
    name = "imagetest"
    
    allowed_domains = ["truyentranhtuan.com"]
    
    start_urls = [
        "http://truyentranhtuan.com/",   
    ]
    
    # dinh nghia mot ham parse
    def parse(self, response):
        item = ImageItem()
        item["image_urls"] = arrayTest[0]
        item["image_name"] = "pic one"
        yield item        
        
        
    
