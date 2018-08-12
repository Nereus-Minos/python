# -*- coding: utf-8 -*-
import scrapy


class Mp3Spider(scrapy.Spider):
    name = 'Mp3'
    allowed_domains = ['music.163.com']
    start_urls = ['http://music.163.com/']

    def parse(self, response):
        pass
