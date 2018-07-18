# coding=utf-8

import sys
import socket
from multiprocessing import Process
import re

HTML_ROOT_DIR = "./html"
#其他.py文件的位置
WSGI_PYTHON = "./wsgipython"

'''只需要改写file_name那儿'''

'''使用类来封装程序'''


class HTTPServer(object):
	'''	服务器'''
	def __init__(self):
		# tcp通信
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# 来解决socket不能重用地址的情况
		self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

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
		#print(file_name)

		if file_name.endswith(".py"):
			try:
				#导入模块
				module_name = file_name[1:-3]
				#m就是模块名
				m = __import__(module_name)
				#print(m)
			except:
				self.response__headers = "HTTP/1.1 404 Not Found\r\n"
				response_body = "not found"
			else:
				# HTTP请求的信息
				environ = ""
				#采用wsgi标准来接收响应的主体部分，用start_response函数来接收响应的头部分
				#appication的第一个参数是HTTP request的相关信息environ,第二个参数是函数start_response用来存储响应的头部
				response_body = str(m.application(environ, self.start_response))
			response = self.response__headers + "\r\n" + response_body

		else:
			# 打开文件，读取文件内容
			try:
				if "/" == file_name:
					file_name = "/index.html"

				file = open(HTML_ROOT_DIR + file_name, "rb")
			except IOError:
				response_start_line = "HTTP/1.1 404 Not Found\r\n"
				response__headers = "Server: My server\r\n"
				response_body = "The file is not found!"
			else:
				file_data = file.read()
				file.close()
				# 构造响应数据,HTTP协议
				response_start_line = "HTTP/1.1 200 OK\r\n"
				response__headers = "Server: My server\r\n"
				response_body = file_data.decode("utf-8")
			finally:
				response = response_start_line + response__headers + "\r\n" + response_body

		client_socket.send(bytes(response, "utf-8"))
		client_socket.close()

	def bind(self,port):
		self.server_socket.bind(("", port))

	def start_response(self,status,headers_content):

		self.response__headers = "HTTP/1.1" + status + "\r\n"
		for header in headers_content:
			self.response__headers += "%s: %s\r\n" % header


def main():
	# 将其他.py文件的路径导入进来
	sys.path.insert(1,WSGI_PYTHON)
	httpServer = HTTPServer()
	httpServer.bind(8080)
	httpServer.start()


if __name__ == "__main__":
	main()