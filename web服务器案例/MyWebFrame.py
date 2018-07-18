# coding=utf-8
import time

HTML_ROOT_DIR = "./html"

class Application(object):
    '''web框架,通用'''
    def __init__(self, url):
        self.url = url

    def __call__(self, environ, start_response):
        path = environ.get("PATH_INFO", "/")

        #静态页面
        if path.startswith("/static"):
            #要访问的静态文件
            file_name = path[7:]
            # 打开文件，读取文件内容
            try:
                if "/" == file_name:
                    file_name = "/index.html"
                file = open(HTML_ROOT_DIR + file_name, "rb")
            except IOError:
                response_start_line = "404 Not Found"
                # response__headers = "Server: My server\r\n"
                headers_content = []
                start_response(response_start_line, headers_content)
                return "not found"
            else:
                file_data = file.read()
                file.close()
        		# 构造响应数据,HTTP协议
                response_start_line = "200 OK"
                headers_content = []
                # response__headers = "Server: My server\r\n"
                response_body = file_data.decode("utf-8")
                start_response(response_start_line, headers_content)
                return response_body

        # 动态页面
        for url, hander in self.url:
            if path == url:
                return hander(environ, start_response)

        # 代表未找到路由信息，404错误
        status = "404 Not Found"
        headers = []
        start_response(status, headers)
        return "not found"

def show_ctime(environ, start_response):
    status = "200 OK"
    headers_content = [("content-type", "text/plain")]
    start_response(status,headers_content)
    return time.ctime()

def say_hello(environ, start_response):
    status = "200 OK"
    headers_content = [("content-type", "text/plain")]
    start_response(status,headers_content)
    return "say hello"

url = [("/ctime", show_ctime), ("/sayhello", say_hello)]
application = Application(url)