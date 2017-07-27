# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    # date = scrapy.Field()
    # caption = scrapy.Field()

# class ImageItem(scrapy.Item):
#     image_urls = scrapy.Field()
#     images = scrapy.Field()
