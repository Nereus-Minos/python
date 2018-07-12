from threading import Thread

import socket

#1.定义一个函数接收数据
class receiveData(Thread):
	def run(self):
		while True:
			content, sendInfo = s.recvfrom(1024)
			print("\r<<[%s]:%s"%(str(sendInfo), content.decode("utf-8")))
			if content.decode("utf-8") == "bye":
				break

#2.定义一个函数发送数据
class sendData(Thread):
	def run(self):
		destination_IP = "127.0.0.1"
		destination_PORT = 9091
		while  True:
			content = input(">>")
			s.sendto(content.encode("utf-8"), (destination_IP, destination_PORT))
			if content == "bye":
				break

#3.主函数
if __name__ == "__main__":
	
	#1.1.创建套接字UDP
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	#1.2.绑定本机信息
	bindAddr = ("", 9090)
	s.bind(bindAddr)
	
	#2.1.创建多进程
	receive = receiveData()
	send = sendData()
	#2.2.开启多线程
	receive.start()
	send.start()

#	s.close()
