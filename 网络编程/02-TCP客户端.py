
from socket import *

#1.创建socket
clientSocket = socket(AF_INET, SOCK_STREAM)

#2.连接服务器
serverAddr = ("127.0.0.1", 8080)
clientSocket.connect(serverAddr)

#3.提示用户输入数据
sendData = input("请输入要发送的数据:")
clientSocket.send(sendData.encode("utf-8"))

#4.接收对方大送过来的数据
recvData = clientSocket.recv(1024)
print("接收到的数据为：%s"%recvData.decode("utf-8"))

clientSocket.close()
