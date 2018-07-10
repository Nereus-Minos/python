#encoding=utf-8

from socket import *

udpsocket = socket(AF_INET, SOCK_DGRAM)

sendData = input("请输入需要发送的数据")

udpsocket.sendto(sendData.encode("utf-8"),("127.0.0.1",(8080)))
