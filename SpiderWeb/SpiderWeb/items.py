# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join

class SpiderwebItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CnblogsItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
    favorite = scrapy.Field()
    comment = scrapy.Field()
    watch = scrapy.Field()
    author = scrapy.Field()

class CnblogsItemLoader(ItemLoader):
    #自定义itemloader
    default_output_processor = TakeFirst()