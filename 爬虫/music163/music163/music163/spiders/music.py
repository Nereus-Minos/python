# -*- coding: utf-8 -*-
import scrapy
from music163.items import Music163Item
import re


class MusicSpider(scrapy.Spider):
    name = 'music'
    allowed_domains = ['https://music.163.com/']
    start_urls = ['https://music.163.com/discover/toplist?id=19723756',
                  'https://music.163.com/discover/toplist?id=3779629',
                  'https://music.163.com/discover/toplist?id=2884035',
                  'https://music.163.com/discover/toplist?id=3778678']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # //*[@id="auto-id-3qJmU71M0f3UgJdC"]
        # print("8"*100)
        # print(response.url)
        # print(response)
        # print("8" * 100)

        '''
        通过对网址的判断来确定是哪一个排行榜
        '''
        rank_name = []
        if response.url.endswith("19723756"):
            rank_name.append("云音乐飙升榜")
        elif response.url.endswith("3779629"):
            rank_name.append("云音乐新歌榜")
        elif response.url.endswith("2884035"):
            rank_name.append("网易原创歌曲榜")
        elif response.url.endswith("3778678"):
            rank_name.append("云音乐热歌榜")

        # 查看返回回来的html
        with open(r'/home/zhao/桌面/音乐/总html.txt', 'wb+') as tf:
            tf.write(response.body)

        '''
        利用正则表达式获得歌手的名字
        '''
        js = response.xpath('//textarea[@id="song-list-pre-data"]')

        # 使用正则表达式提取其中的json
        pattern = re.compile('"artists":\[{.*?}]')

        jss = pattern.findall(js.extract()[0])

        pattern = re.compile('"name":".*?"')

        # 歌手名字
        music_author_list = []

        for name in jss:

            names = pattern.findall(name)
            nn = ''
            for n in names:
                nn += n
            nn = nn.replace('""name":"', "@").replace('"name":"', "").replace('"', "")
            music_author = nn
            music_author_list.append(music_author)


        '''
        利用xpath获得歌曲的id和名字
        '''
        list = response.xpath('//ul[@class="f-hide"]/li')

        item = Music163Item()

        music_id_list = []
        music_name_list = []
        music_url_list = []
        for music in list:
            music_id = music.xpath('./a/@href').extract()[0].split("=")[1]
            music_name = music.xpath('./a/text()').extract()[0]

            music_id_list.append(music_id)
            music_name_list.append(music_name)

        item['music_id'] = music_id_list
        item['music_author'] = music_author_list
        item['music_name'] = music_name_list
        item['rank_name'] = rank_name

        # # 由于该页面为js动态加载，通过抓包得到文件url，拼接url
        for j in item['music_id']:
            music_url = 'http://music.163.com/song/media/outer/url?id=' + j + '.mp3'
            music_url_list.append(music_url)
        item['music_urls'] = music_url_list

        response.meta['item'] = item

        yield item
