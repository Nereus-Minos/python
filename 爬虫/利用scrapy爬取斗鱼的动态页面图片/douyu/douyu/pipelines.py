# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import scrapy


class DouyuPipeline(object):
    def process_item(self, item, spider):
        return item


class DouyuImagePipeline(ImagesPipeline):
    default_headers = {
        'accept': 'image/webp,image/*,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'cookie': 'bid=yQdC/AzTaCw',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            self.default_headers['referer'] = image_url
            yield scrapy.Request(image_url, headers=self.default_headers,
                                 meta={'item': item, 'index': item['image_urls'].index(image_url)})
            # 添加meta是为了下面重命名文件名使用

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']  # 通过上面的meta传递过来item
        index = request.meta['index']  # 通过上面的index传递过来列表中当前下载图片的下标

        # 图片文件名，item['names'][index]得到名称，request.url.split('/')[-1].split('.')[-1]得到图片后缀jpg,png
        image_guid = item['names'][index]+'.'+request.url.split('/')[-1].split('.')[-1]
        # 图片下载目录
        filename = u'full/{0}'.format(image_guid)
        return filename

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")

        item['image_paths'] = image_paths
        return item

