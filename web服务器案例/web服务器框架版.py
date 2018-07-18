# coding=utf-8

import sys
import socket
from multiprocessing import Process
import re

'''使用类来封装程序'''

class HTTPServer(object):
	'''	服务器'''
	def __init__(self, application):
		# tcp通信
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# 来解决socket不能重用地址的情况
		self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.application = application

	def start(self):
		'''开启多进程'''
		self.server_socket.listen(128)
		while True:
			client_socket, client_address = self.server_socket.accept()
			handle_client_process = Process(target=self.func, args=(client_socket,))
			handle_client_process.start()
			client_socket.close()  # 子进程已经复制了一份socket,所以将这个关闭

	def func(self,client_socket):
		"""处理客户端的请求"""
		# 获取客户端的数据
		request_data = client_socket.recv(1024)
		request_lines = request_data.splitlines()

		# 解析请求报文
		# GET /请求的文件的路径 HTTP/1.1
		request_start_line = request_lines[0].decode("utf-8")
		# 提取用户请求的文件名
		file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line).group(1)
		method = re.match(r"\w+ +(/[^ ]*) ", request_start_line).group(1)
		#print(file_name)

		# HTTP请求的信息
		environ = {
			"PATH_INFO": file_name,
			"METHOD": method
		}
				#采用wsgi标准来接收响应的主体部分，用start_response函数来接收响应的头部分
				#appication的第一个参数是HTTP request的相关信息environ,第二个参数是函数start_response用来存储响应的头部
		response_body = str(self.application(environ, self.start_response))
		response = self.response__headers + "\r\n" + response_body

		client_socket.send(bytes(response, "utf-8"))
		client_socket.close()

	def bind(self,port):
		self.server_socket.bind(("", port))

	def start_response(self,status,headers_content):

		self.response__headers = "HTTP/1.1" + status + "\r\n"
		for header in headers_content:
			self.response__headers += "%s: %s\r\n" % header


def main():
	#采用运行时提供接口所在模块和函数名
	if len(sys.argv) <2:
		sys.exit("Please running in: python3 XXXX.py modlue_name:application_name")

	module_name, application_name = sys.argv[1].split(":")
	# 动态导入模块
	m = __import__(module_name)
	# 提取模块中的application
	application = getattr(m, application_name)
	httpServer = HTTPServer(m.application)
	httpServer.bind(8080)
	httpServer.start()


if __name__ == "__main__":

	main()