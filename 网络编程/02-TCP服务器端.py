
from socket import *

#1.创建socket
s = socket(AF_INET, SOCK_STREAM)

#2.绑定本地信息
address = ('', 8080)
s.bind(address)

#3.tcp使用socket创建的套接字莫人的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的连接了
s.listen(5)

#4.接收客户端的连接
print("等待客户端连接")
clientSocket, clientAddr = s.accept()
print("客户端连接成功")

#5.接收发过来的数据
recvData = clientSocket.recv(1024)
print("接收的数据为:%s"%recvData.decode("utf-8"))

#6.发送数据
sendData = input("请输入回送数据：")
clientSocket.send(sendData.encode("utf-8"))

#关闭socket
clientSocket.close()
s.close()
