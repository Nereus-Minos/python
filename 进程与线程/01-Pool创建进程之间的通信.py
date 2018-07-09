from multiprocessing import Manager, Pool
import os,time,random

def write(q):
	for value in ['a', 'b','c','d']:
		print("put %s to queue"%(value))
		q.put(value)
		time.sleep(random.random())

def read(q):
	while True:
		if not q.empty():
			value = q.get(True)
			print("get %s from queue"%(value))
			time.sleep(random.random())
		else:
			break

if __name__ == "__main__":
	
	q = Manager().Queue()
	po = Pool()
	po.apply(write,(q,))
	po.apply(read,(q,))
	po.close()
	po.join()


