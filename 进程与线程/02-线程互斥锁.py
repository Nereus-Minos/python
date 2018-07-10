
from threading import Thread, Lock
import time

g_num = 0

def test1():
	global g_num 
	for i in range(1000000):
		mutex.acquire(True)
		g_num += 1
		mutex.release()
	
	print("---test1---g_num=%d"%g_num)

def test2():
	global g_num
	for i in range(1000000):
		mutex.acquire(True)
		g_num += 1
		mutex.release()
	
	print("----test2--g_num = %d"%g_num)

if __name__ == "__main__":
	mutex = Lock()

	p1 = Thread(target = test1)
	p1.start()

	p2 = Thread(target = test2)
	p2.start()

	print("---main---g_num=%d"%g_num)
