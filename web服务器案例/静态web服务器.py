# coding=utf-8
import socket
from multiprocessing import Process
import re

HTML_ROOT_DIR = "./html"
#
# # 多进程完成多任务
# def func(client_socket):
# 	"""处理客户端的请求"""
# 	#获取客户端的数据
# 	request_data = client_socket.recv(1024)
# 	request_lines = request_data.splitlines()
#
# 	#解析请求报文
# 	#GET /请求的文件的路径 HTTP/1.1
# 	request_start_line = request_lines[0].decode("utf-8")
# 	#提取用户请求的文件名
# 	file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line).group(1)
# 	#print(file_name)
# 	if "/" == file_name:
# 		file_name = "/index.html"
#
# 	#打开文件，读取文件内容
# 	try:
# 		file = open(HTML_ROOT_DIR + file_name, "rb")
#
# 	except IOError:
# 		response_start_line = "HTTP/1.1 404 Not Found\r\n"
# 		response__headers = "Server: My server\r\n"
# 		response_body = "The file is not found!"
# 	else:
# 		file_data = file.read()
# 		file.close()
# 		#构造响应数据,HTTP协议
# 		response_start_line = "HTTP/1.1 200 OK\r\n"
# 		response__headers = "Server: My server\r\n"
# 		response_body = file_data.decode("utf-8")
# 	finally:
# 		response = response_start_line + response__headers + "\r\n" + response_body
# 		client_socket.send(bytes(response,"utf-8"))
# 		client_socket.close()
#
# def main():
# 	# tcp通信
# 	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 	#来解决socket不能重用地址的情况
# 	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 	server_socket.bind(("", 8080))
# 	server_socket.listen(128)
#
# 	while True:
# 		client_socket, client_address = server_socket.accept()
# 		handle_client_process = Process(target=func, args=(client_socket,))
# 		handle_client_process.start()
# 		client_socket.close()	#子进程已经复制了一份socket,所以将这个关闭
#
# if __name__ == "__main__":
# 	main()


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
		# print(file_name)
		if "/" == file_name:
			file_name = "/index.html"

		# 打开文件，读取文件内容
		try:
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


def main():
	httpServer = HTTPServer()
	httpServer.bind(8080)
	httpServer.start()


if __name__ == "__main__":
	main()