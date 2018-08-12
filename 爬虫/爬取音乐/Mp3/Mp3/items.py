# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Mp3Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    vol_num = scrapy.Field()
    vol_title = scrapy.Field()
    vol_time = scrapy.Field()
    music_name = scrapy.Field()
    music_author = scrapy.Field()

    # 文件url保存
    music_urls = scrapy.Field()
    # 件的结果保存
    music_files = scrapy.Field()
