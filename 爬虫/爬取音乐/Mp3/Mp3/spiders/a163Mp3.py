# -*- coding: utf-8 -*-
import scrapy
from Mp3.items import Mp3Item


class A163mp3Spider(scrapy.Spider):
    name = '163Mp3'
    allowed_domains = ['luoo.net']
    start_urls = ['http://www.luoo.net/tag/?p=1']

    def parse(self, response):
        # 音乐期刊的url
        vol_list = response.xpath("//div[@class='vol-list']/div/a/@href").extract()
        # 总的页数
        total_page = response.xpath("//div[@class='paginator']/a[12]/text()").extract()[0]

        for vol in vol_list:
            yield scrapy.Request(url=vol, callback=self.parse_1)

        # # 字符串拼接出所有分页的url
        # self.offset += 1
        # if self.offset < int(total_page):
        #     url = self.url + str(self.offset)
        #     yield scrapy.Request(url=url, callback=self.parse)
        #

    def parse_1(self, response):
        # 进入到期刊详情页

        item = Mp3Item()
        item['vol_num'] = response.xpath("//div[@class='container ct-sm']/h1/span[1]/text()").extract()[0]
        item['vol_title'] = response.xpath("//div[@class='container ct-sm']/h1/span[2]/text()").extract()[0]
        item['vol_time'] = response.xpath("//div[@class='clearfix vol-meta']/span[2]/text()").extract()[0]

        music_list = response.xpath("//*[@id='luooPlayerPlaylist']/ul/li")
        # vol系列字段为单一值，music系列字段为列表
        music_name_list = []
        music_author_list = []
        music_url_list = []
        for music in music_list:
            music_name = music.xpath('./div/a[1]/text()').extract()[0]
            music_author = music.xpath('./div/span[2]/text()').extract()[0]
            music_name_list.append(music_name)
            music_author_list.append(music_author)

        item['music_author'] = music_author_list
        item['music_name'] = music_name_list

        # 由于该页面为js动态加载，通过抓包得到文件url，利用期刊号加音乐编号，拼接url
        for j in item['music_name']:
            music_url = 'http://mp3-cdn2.luoo.net/low/luoo/radio' + item['vol_num'] + '/' + str(j[0:2]) + '.mp3'
            music_url_list.append(music_url)
        item['music_urls'] = music_url_list

        response.meta['item'] = item

        yield item
