# -*- coding: utf-8 -*-
import os
import json
import scrapy
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.files import FilesPipeline
import requests


class Music163Pipeline(FilesPipeline):
    '''
    自定义文件下载管道
    '''
    FILES_STORE = get_project_settings().get("FILES_STORE")

    DEFAULT_REQUEST_HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }

    def handle_redirect(self, file_url):
        response = requests.head(file_url)
        if response.status_code == 302:
            file_url = response.headers["Location"]
        return file_url

    def get_media_requests(self, item, info):
        for music_url in item['music_urls']:
            # 解决重定向(302)问题
            redirect_url = self.handle_redirect(music_url)
            yield scrapy.Request(url=redirect_url, headers=self.DEFAULT_REQUEST_HEADERS,
                                 meta={'item': item, 'index': item['music_urls'].index(music_url)}
                                 , dont_filter=True)

    def item_completed(self, results, item, info):
        # print("*" * 100)
        # print(results)
        # print("*"*100)
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item contains no files")

        return item

    def file_path(self, request, response=None, info=None):
        # 将文件重新命名
        index = request.meta['index']
        music_name = request.meta['item']['music_name']
        music_author = request.meta['item']['music_author']
        rank_name = request.meta['item']['rank_name']

        # request.url.split('/')[-1].split('.')[-1]得到文件后缀
        file_name = rank_name[0] + "/" + str(index) + "--" + music_author[index] + "_" + music_name[index] + '.'+request.url.split('.')[-1]
        return file_name

# # 将文本文件保存为json格式
# class LuoWangSpiderPipeline(object):
#     def __init__(self):
#         self.json_file = open(r'F:\luowang\luowang.json', 'wb')
#
#     def process_item(self, item, spider):
#         self.json_file.write(json.dumps(dict(item),ensure_ascii=False) + '\n')
#         return item
