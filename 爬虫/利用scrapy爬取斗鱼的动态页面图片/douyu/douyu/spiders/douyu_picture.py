# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import scrapy
from douyu.items import DouyuItem


class DouyuPictureSpider(scrapy.Spider):
    name = 'douyu_picture'
    allowed_domains = ['www.douyu.com']
    start_urls = ['https://www.douyu.com/g_yz']

    def __init__(self):
        self.browser =webdriver.Firefox()

    def parse(self, response):
        self.browser.get(response.url)

        # 因为是动态页面url不变，所以用yeild scrapy.Request不好使
        # 所以这里使用while循环点击下一页，终止条件就是没有下一页
        while True:
            # 使用WebDriverWait()等待数据加载：即确保对应内容加载完成后，再进行相应爬取任务。
            # 浏览器滚动条
            # self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # 实现平滑滚动?????
            i = 0
            while i < 15:
                code = "window.scrollTo(" + str(i * 1000) + "," + str((i + 1) * 1000) + ")"
                self.browser.execute_script(code)
                # sleep值需要修改
                time.sleep(0.8)  # 不然会load不完整
                i += 1

            list_imgs = self.browser.find_elements_by_xpath('//img[@class="JS_listthumb"]')

            if list_imgs:
                item = DouyuItem()
                imgs = []

                for img in list_imgs:
                    img = img.get_attribute('src')
                    imgs.append(img)

                item['image_urls'] = imgs
                yield item

            try:
                # 实现自动爬取下一页
                next = self.browser.find_element_by_xpath('//a[@class="shark-pager-next"]').click()
            except:
                break
