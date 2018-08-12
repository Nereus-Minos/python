# -*- coding: utf-8 -*-
import os
import json
import scrapy
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.files import FilesPipeline


class Mp3Pipeline(FilesPipeline):
    '''
    自定义文件下载管道
    '''
    FILES_STORE = get_project_settings().get("FILES_STORE")

    def get_media_requests(self, item, info):
        '''
        根据文件的url逐一发送请求
        :param item:
        :param info:
        :return:
        '''
        for music_url in item['music_urls']:
            yield scrapy.Request(url=music_url, meta={'item':item})

    def item_completed(self, results, item, info):
        '''
        处理请求结果
        :param results:
        :param item:
        :param info:
        :return:
        '''
        print("*" * 100)
        print(results)
        print("*"*100)
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item contains no files")
        # for i in range(0, len(item['music_name'])):
        #     old_name = self.FILES_STORE + file_paths[i]
        #     new_name = self.FILES_STORE + 'Vol.' + item['vol_num'] + '_' + item['vol_title'] + '/' + item['music_name'][i] + '.mp3'
        #
        #     # 文件重命名
        #     os.rename(old_name, new_name)

        return item

    def file_path(self, request, response=None, info=None):
        '''
        自定义文件保存路径
        :param request:
        :param response:
        :param info:
        :return:
        '''
        # 将文件重新命名
        vol_title = request.meta['item']['vol_title']
        vol_num = request.meta['item']['vol_num']

        file_name = request.url.split('/')[-1]
        folder_name = 'Vol.' + vol_num + '_' + vol_title
        return '%s/%s' % (folder_name, file_name)

# # 将文本文件保存为json格式
# class LuoWangSpiderPipeline(object):
#     def __init__(self):
#         self.json_file = open(r'F:\luowang\luowang.json', 'wb')
#
#     def process_item(self, item, spider):
#         self.json_file.write(json.dumps(dict(item),ensure_ascii=False) + '\n')
#         return item
