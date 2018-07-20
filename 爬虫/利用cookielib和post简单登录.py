'''
这是直接用post登录的，而没有先有一个HTTP GET请求，再用POST登录，所以不适用一些网站
还有些网站是动态加密的
'''

import urllib
import urllib2
import cookielib

#1.构建一个CookielibJar对象实例来保存cookie
cookie = cookielib.CookieJar()

#2.使用HTTPCookieProcessor()来创建cookie处理器对象,参数为CoookieJar()对象
cookie_hander = urllib2.HTTPCookieProcessor(cookie)

#3.通过build_opener()来创建opener
opener = urllib2.build_opener(cookie_hander)

#4.addheaders接收一个列表，里面每个元素都是一个headers信息的元祖，opener将附带headers信息
opener.addheaders = [("User-Agent", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;")]
#添加报头也可以通过之前的方法添加

#5.需要登录的账户和密码
data = {"email":"xxxxx@163.com", "password":"xxxxxx"}

#6.通过urlencode()转吗
postdata = urllib.urlencode(data)

#7.构建Request请求对象，包含需要发送的用户名和密码
url = "http://www.renren.com/PLogin.do"
request = urllib2.Request(url, data = postdata)

#8.通过opener发送这个请求对象，并获取登录后的Cookie值
opener.open(request)

#9.opener包含用户的Cookie值，所以可以在此处直接访问登录后的网页
response = opener.open("http://www.renren.com/410043129/profile")
print(response.read())
