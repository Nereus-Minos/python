
import os

import time

ret = os.fork()  #创建了一个新的进程，也就是从此行开始有两个进程一起在执行，即有两个ret, 主（父）进程中ret>0，子进程中ret=0

print(ret)

print("hahaha")

if ret == 0:
	while True:
		print("---1---")
		print("---12---")
		print("---123---")

		time.sleep(2)
	
else:
	while True:
		print("---2---")
		print("---22---")
		print("---223---")
		print("---2234---")
		time.sleep(2)




