import urllib2
import random

#网上搜免费代理IP
proxy_list = [
    {"http":"125.118.77.149:808"},
    {"http":"60.205.205.48:80"},
    {"http":"61.135.217.7:80"},
    {"http":"111.155.116.207:8123"}
]

# 随机选择一个代理
proxy = random.choice(proxy_list)
# 使用选择的代理构建代理处理器对象
httpproxy_hander = urllib2.ProxyHandler(proxy)
# 通过urllib2.build_opener()方法使用代理对象
openner = urllib2.build_opener(httpproxy_hander)

request = urllib2.Request("http://www.baidu.com")

# 1.如果这么写，只有一使用opener.open()方法发送请求才能使用代理，而urlopen()则不使用自定义代理
response = openner.open(request)
# # 2.如果这么写，就将opener应用到了全局，之后所有的不管是opener.open()还是urlopen()发送请求都使用自定义代理
# urllib2.install_opener(opener)
# response = urlopen(request)

print(response.read())