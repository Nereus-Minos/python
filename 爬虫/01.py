# coding=utf-8
import urllib   #负责url编码处理
import urllib2
import random

url = "http://www.baidu.com/s"

keyword = raw_input("请输入需要查询的关键字：")

word = {"wd":keyword}
word = urllib.urlencode(word)   #转换成url编码格式（字符串）
newurl = url + "?" + word   #url首个分隔符是？

# headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
# request = urllib2.Request(newurl, headers = header)
ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; ) Apple....",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0)...",
    "Mozilla/5.0 (Macintosh; Intel Mac OS..."
]
user_agent = random.choice(ua_list)
request = urllib2.Request(newurl)
#通过Request.add_header()添加/修改一个特定的header
request.add_header("User-Agent", user_agent)
#得到相应的header值，第一个字母大写，其他的全部小写
request.get_header("User-agent")


print(response.read())