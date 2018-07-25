# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class MyspiderPipeline(object):

    def __init__(self):
        self.file = open("tencent.json", 'w+')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(content)
        # 必须返回一个对象，因为被丢弃的item将不会被之后的pipeline组件处理
        return item

    def close_spider(self, spider):
        self.file.close()
