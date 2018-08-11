# coding=utf-8

import threading
from queue import Queue
# 请求处理库
import requests
# 解析库
from lxml import etree
# 存储到json
import json1


class ThreadCraw(threading.Thread):
    """
    爬取页面
    """
    def __init__(self, thread_name, page_queue):
        # 调用父类的初始化函数
        super(ThreadCraw, self).__init__()
        # 线程名
        self.threadName = thread_name
        # 页码队列
        self.pageQueue = page_queue

    def run(self):
        while True:
            if self.pageQueue.empty():
                break
            else:
                page = self.pageQueue.get()
                print("threadName = " + self.threadName + ", page = " + str(page))

                url = "https://www.qiushibaike.com/hot/page/" + str(page) + "/"

                headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

                # 多次尝试失败后结束程序，防止死循环
                timeout = 4
                while timeout > 0:
                    timeout -= 1
                    try:
                        content = requests.get(url, headers=headers)
                        data_queue.put([page, content.text])
                        break
                    except Exception:
                        print("shit")
                if timeout < 0:
                    print("timeout" + url)


class ThreadParser(threading.Thread):
    """
    页面内容解析
    """
    def __init__(self, thread_name):
        super(ThreadParser, self).__init__()
        # 线程名
        self.threadName = thread_name

    def run(self):
        while not data_queue.empty():
            print("threadName = " + self.threadName + ":")
            try:
                """
                调用队列对象的get()方法的可选参数block默认为True
                如果队列为空且block为True，get()就会使地哦啊涌现成暂停，知道有项目可用
                如果队列为空且block为Fasle，队列将引发Empty异常
                """
                page, item = data_queue.get(False)

                if not item:
                    pass
                # 解析内容
                self.parse_data(item, page)
            except:
                pass

    def parse_data(self, item, page):

        # 响应返回的是字符串，解析为HTML DOM模式
        text = etree.HTML(item)

        # 返回所有段子的节点位置，contains()模糊查询方法，第一个参数是要匹配的标签，第二个参数是标签名部分内容
        node_list = text.xpath('//div[contains(@id, "qiushi_tag")]')

        for node in node_list:
            try:
                # 取图片链接
                img_url = node.xpath('./div/a/img/@src')[0]
                # username = node.xpath('./div/a/@title')[0]    ## 取不出来
                username = node.xpath('.//h2')[0].text
                # print(username)

                # 取内容
                # 先提取第一段
                content = node.xpath('.//div[@class="content"]/span')[0].text.strip()
                # print(content)
                # 如果有好几段，则处理
                try:
                    lst = node.xpath('.//div[@class="content"]/span/br')
                    for ll in lst:
                        # print(ll.tail)
                        content += ll.tail
                except:
                    pass

                # 写入到文件
                # 1.组建json文件
                result = {
                    'page': page,
                    'img_url': img_url,
                    'username': username,
                    'content': content,
                }
                content_queue.put(result)

            except:
                pass


class WriteFile(object):

    def __init__(self, flie_name):
        self.file_name = flie_name

    def write(self):
        file = open(self.file_name, 'a')
        while not content_queue.empty():
            result = content_queue.get()
            file.write(json.dumps(result, ensure_ascii=False) + "\n")

        file.close()


# 全局变量

# 采集结果（每页HTML源码）的数据队列，参数为空表示不限制
data_queue = Queue()

# 解析好的内容队列
content_queue = Queue()

# ############


def main():
    start_page = input("请输入要爬取的起始位置")
    end_page = input("请输入截止位置")
    flie_name = input("需要写入到哪个文件？(.json)")
    # 页码的队列，表示10个页面
    page_queue = Queue(10)
    # 放入1～10个数字，先进先出
    for i in range(int(start_page), int(end_page) + 1):
        page_queue.put(i)

# 采集线程
    crawl_threads = []
    # 三个采集线程的名字
    craw_list = ['采集线程1号', '采集线程2号', '采集线程3号']
    for thread_name in craw_list:
        # 写一个类用来表示线程
        thread = ThreadCraw(thread_name, page_queue)
        thread.start()
        crawl_threads.append(thread)

    # 等待所有线程完成
    for t in crawl_threads:
        t.join()

# 解析线程
    parser_threads = []
    # 三个解析线程的名字
    parser_list = ['解析线程1号', '解析线程2号', '解析线程3号']
    for thread_name in parser_list:
        # 写一个类用来表示线程
        thread = ThreadParser(thread_name)
        thread.start()
        parser_threads.append(thread)

    # 等待所有线程完成
    for t in parser_threads:
        t.join()

# 写入文件
    write_file = WriteFile(flie_name)
    write_file.write()


if __name__ == "__main__":
    main()
