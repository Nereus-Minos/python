# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Music163Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    music_id = scrapy.Field()
    music_name = scrapy.Field()
    music_author = scrapy.Field()

    # 文件url保存
    music_urls = scrapy.Field()

    # 排行榜的名字
    rank_name = scrapy.Field()
