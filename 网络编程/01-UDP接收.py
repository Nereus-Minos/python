#encoding=utf-8

from socket import *

#1.创建套接字
udpsocket = socket(AF_INET, SOCK_DGRAM)

#2.绑定本地信息，如果不绑定，则系统会随机分配
bindAddr = ('', 8080)	#ip一般不写，表示本机任何一个ip都可以
udpsocket.bind(bindAddr)

#3.等待接收
recvData = udpsocket.recvfrom(1024)	#1024表示本次接收的最大字节数

print(recvData)

print('-'*30)

#解码
content, sendInfo = recvData
#或者用content = recvData[0]
print(content.decode('utf-8'))
