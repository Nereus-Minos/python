# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem

class TencentpositionSpider(scrapy.Spider):
    name = 'tencentposition'
    allowed_domains = ['tencent.com']
    page = 0
    url = 'https://hr.tencent.com/position.php?lid=2156&start='
    start_urls = [url + str(page)]

    def parse(self, response):
        for each in response.xpath('//tr[@class="even"]|//tr[@class="odd"]'):
            item = MyspiderItem()
            # 职位名称
            try:
                name = each.xpath('./td[1]/a/text()').extract()[0]
            except:
                name = "  "
            # 职位链接
            try:
                position_link = each.xpath('./td[1]/a/@href').extract()[0]
            except:
                position_link = "  "
            # 职位类别
            try:
                position_type = each.xpath('./td[2]/text()').extract()[0]
            except:
                position_type = "  "
            # 招聘人数
            try:
                people_num = each.xpath('./td[3]/text()').extract()[0]
            except:
                people_num = "  "
            # 工作地点
            try:
                work_location = each.xpath('./td[4]/text()').extract()[0]
            except:
                work_location = "  "
            # 发布时间
            try:
                public_time = each.xpath('./td[5]/text()').extract()[0]
            except:
                public_time = "  "

            item['name'] = name
            item['position_link'] = position_link
            item['position_type'] = position_type
            item['people_num'] = people_num
            item['work_location'] = work_location
            item['public_time'] = public_time

            # 将获取得数据交给pipeline
            yield item

        # 发送新的url请求加入到带爬取的对列，并调用回调函数
        if self.page < 610:
            self.page += 10
        yield scrapy.Request(self.url + str(self.page), callback=self.parse)
