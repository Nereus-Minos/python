
from multiprocessing import Pool
import time
import os

def test():
	print("---进程池中的进程---pid=%d，ppid=%d"%(os.getpid(),os.getppid()))
	for i in range(3):
		print("---%d---"%i)
		time.sleep(1)
	return "hahaha"

def test2(args):
	print("---callback func---pid=%d"%os.getpid())
	print("---callback func---args=%s"%args)

pool = Pool(3)
pool.apply_async(func = test, callback = test2)

while True:
	time.sleep(1)
	print("This is main!")
