#coding=utf-8

import urllib.request
from lxml import etree
import lxml
# from lxml.html.clean import Cleaner

url = "https://www.qiushibaike.com/hot/page/2/"

headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

request =urllib.request.Request(url, headers = headers)

html = urllib.request.urlopen(request).read()
#
# cleaner = Cleaner(style=True, scripts=True,page_structure=False, safe_attrs_only=False)
#
# cleaner.clean_html(html)

# 响应返回的是字符串，解析为HTML DOM模式
text = etree.HTML(html)

# 返回所有段子的节点位置，contains()模糊查询方法，第一个参数是要匹配的标签，第二个参数是标签名部分内容
node_list = text.xpath('//div[contains(@id, "qiushi_tag")]')

for node in node_list:
    # 取图片链接
    imgUrl = node.xpath('./div/a/img/@src')[0]
    # username = node.xpath('./div/a/@title')[0]    ## 取不出来
    username = node.xpath('.//h2')[0].text
    print(username)
    # 取内容
    # 先提取第一段
    content = node.xpath('.//div[@class="content"]/span')[0].text.strip()
    print(content)
    # 如果有好几段，则处理
    try:
        lst = node.xpath('.//div[@class="content"]/span/br')
        for ll in lst:
            print(ll.tail)
    except:
        pass

