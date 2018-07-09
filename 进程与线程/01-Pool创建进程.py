
from multiprocessing import Pool

import time
import os
import random

def worker(msg):
	t_start = time.time()
	print("%s开始执行，进程号为%d"%(msg, os.getpid()))
	#random.random()产生0~1之间的浮点数
	time.sleep(random.random()*2)
	#time.sleep(1)
	t_stop = time.time()
	print(msg,"执行完毕，耗时%0.2f"%(t_stop - t_start))

po = Pool(3)   #定义一个进程池，最大进程数为3
for i in range(0,10):
	po.apply_async(worker, (i,))   #参数通过元组传递

print("---start---")
po.close()   #关闭进程池，关闭后不再接受新的请求
po.join()    #等待所有进程执行结束，必须放在close语句后面
print("---end---")
