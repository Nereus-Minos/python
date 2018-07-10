
from threading import Thread, Lock
import time

class Task1(Thread):
	def run(self):
		while True:
			if lock1.acquire(True):
				print("---Task1---")
				time.sleep(0.5)
				lock2.release()

class Task2(Thread):
	def run(self):
		while True:
			if lock2.acquire():
				print("---Task2---")
				time.sleep(0.5)
				lock3.release()

class Task3(Thread):
	def run(self):
		while True:
			if lock3.acquire():
				print("---Task3---")
				time.sleep(0.5)
				lock1.release()

if __name__ == "__main__":
	lock1 = Lock()
	lock2 = Lock()
	lock3 = Lock()
	task1 = Task1()
	task2 = Task2()
	task3 = Task3()
	lock2.acquire()
	lock3.acquire()
	task1.start()
	task2.start()
	task3.start()

