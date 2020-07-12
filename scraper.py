# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('.')
from items import ReviewItems

class BlogScraper(scrapy.Spider):
    #Postlinks()
    name    =   "blogcrawl"
    start_urls  =   []
    f=open("links.txt","r+")
    for links in f:
        start_urls.append(links)
    
    def parse(self,response):
        item    =   ReviewItems()
        f1=open("reviews.txt","a+",encoding="utf-8")
        reviews =   response.css('div.post-content p::text').extract()
        for cont in reviews:
            item['review']  =   cont
            yield item
            f1.write(cont+"\n\n")


# class Postlinks(scrapy.Spider):
#     name    =   "linkextract"
#     start_urls  =   []
#     f=open("haha.txt","r+")
#     for link in f:
#         start_urls.append(link)
    
#     def parse(self,response):
#         f1=open("links.txt","a+")
#         links   =   response.css('.post-title a::attr(href)').extract()
#         for link in links:
#             yield{'postlink':link}
#             f1.write(link+"\n")
#         f1.close()
#     f.close()
#     start_urls=[]