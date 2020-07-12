# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append(".")
class ReviewItems(scrapy.Item):
    review  =   scrapy.Field()
