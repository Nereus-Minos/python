from socket import socket
import struct
import sys

if len(sys.argv) != 2:
	print("-"*30)
	print("tips:")
	print("采用这种方式运行程序: python xxxx.py 192.168.1.xxx")
	print("-"*30)
	exit()
else:
	ip = sys.argv[1]

#创建套接字
s = socket(AF_INET, SOCK_DGRAM)

#创建下载请求数据
cmd_buf = struct.pack("!H8sb5sb",1,"test.jpg",0,"octet",0)

#发送下载请求数据到指定的服务器
sendAddr = (ip, 69)
s.sendto(cmd_buf, sendAddr)

p_num = 0
recvFile = ''

while True:
	recvData, recvAddr = s.recvfrom(1024)

	recvDataLen = len(recvData)	#用来控制是否结束

	#recvData前4个字节是操作吗和块编号
	cmdTuple = struct.unpack("!HH", recvData[:4])
	#print(cmdTuple)

	cmd = cmdTuple[0]
	currentPackNum = cmdTuple[1]

	if cmd == 3:	#表示为数据包
		
		#如果是第一次接收数据，那么创建文件
		if currentPackNum == 1:
			recvFile = open("test.jpg",'a')

		#如果包的编号与上次相等
		if p_num+1 == currentPackNum:
			#写入数据
			recvFile.write(recvData[4:])
			p_num += 1
			print("(%d)次接收的数据"%p_num)

			ack_buf = struct.pack("!HH",4,p_num)

			s.sendto(ack_buf, recvAddr)	#一定要是recvAddr

		#如果接收到的数据小于516则认为传输完成
		if recvDataLen < 516:
			recvFile.close()
			print("已下载成功")
			break

	#当接收过来的操作吗为错误应答号时
	elif cmd == 5:
		print("error num : %d"%currentPackNum)
		break

s.close()
