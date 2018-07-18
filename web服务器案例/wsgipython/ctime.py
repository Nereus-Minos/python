# coding=utf-8

import time

def application(environ, start_response):
    status = "200 OK"
    headers_content = [("content-type", "text/plain")]
    start_response(status,headers_content)
    return time.ctime()