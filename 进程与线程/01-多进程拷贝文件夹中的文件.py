from multiprocessing import Pool,Manager
import os

def copyFileTask(name, oldFolderName, newFolderName, queue):
	fr = open(oldFolderName+"/"+name)
	fw = open(newFolderName+"/"+name,'w')

	content = fr.read()
	fw.write(content)

	fr.close()
	fw.close()

	queue.put(name)


def main():
	
	#0。获得文件夹名
	oldFolderName = input("请输入要拷贝文件夹的名字:")
	#1.创建一个文件夹
	newFolderName = oldFolderName+"-复件"
	os.mkdir(newFolderName)
	#2.获得文件夹下所有文件名
	filenames = os.listdir(oldFolderName)
	
	#3.使用多进程的方式拷贝
	pool = Pool(5)
	queue = Manager.Queue()
	for filename in filenames:
		pool.apply_async(copyFileTask, args=(filename, oldFolderName, newFolderName, queue))

	pool.close()
#	pool.join()

	num = 0
	allNum = len(filenames)
	while num < allNum:
		queue.get()
		num += 1
		copyRate = num/allNum
		print("\rcopy的进度是：%。2f%%"%(copyRate*100),end = "")


if __name__ == "__main__":
	main()
