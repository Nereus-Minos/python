from multiprocessing import Process, Queue
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
	
	q = Queue()
	qw = Process(target = write, args = (q,))
	qr = Process(target = read, args = (q,))
	qw.start()
	qw.join()
	qr.start()
	


