#coding=utf-8
import re
import urllib2


class Spider:
    def __init__(self):
        pass

    def loadPage(self,page):
        """
            下载页面
        """
        if 1 == page:
            url = "https://www.neihan8.com/article/index.html"
        else:
            url = "https://www.neihan8.com/article/index_" + str(page) + ".html"
        headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request)
        # 获得每页的HTML
        html = response.read()
        # 匹配段子标题和段子的链接，re.S表示匹配所有
        pattern = re.compile(r'<h3><a\shref="(.*?)"\sclass="title"\stitle="(.*?)">', re.S)
        # 获取每个段子的标题和段子的链接
        title_list = pattern.findall(html)
        self.dealPage(title_list)

    def dealPage(self,title_list):
        """
            处理每页的段子
        """
        for content_url,title in title_list:
            url = "https://www.neihan8.com" + content_url
            headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
            try:
                request = urllib2.Request(url, headers=headers)
                response = urllib2.urlopen(request)
            except:
                pass
            else:
                # 获得每页的HTML
                html = response.read()
                # print(html)
                # re.S表示匹配所有
                pattern = re.compile(r'\r\n<p>(.*?)</p>', re.S)
                #
                content_list = pattern.findall(html)
                print("\r\n")
                print(title)
                self.writePage("\r\n")
                self.writePage(title+"\n")
                for content in content_list:
                    content = content.replace("&ldquo;","\"").replace("&rdquo;","\"").replace("&nbsp;","  ")
                    print(content)
                    self.writePage(content+"\n")

    def writePage(self,item):
        """
            把每条段子逐个写道文件里面
        """
        with open("duanzi.txt", "a") as f:
            f.write(item)

    def startWork(self):
        """
            控制爬虫
        """
        startPage = raw_input("请输入要爬取的起始位置页数：")
        endPage = raw_input("请输入要爬取的结束位置页数：")
        for page in range(int(startPage), int(endPage)+1):
            self.loadPage(page)

def main():
    spider = Spider()
    spider.startWork()

if __name__ == "__main__":
    main()