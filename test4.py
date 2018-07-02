#encoding=utf-8
#需求分析：取出列表中各元素（文件名）的后嘴

names = ["1.txt", "2.py", "3.c", "4.cpp", "5.java"]

for temp in names :
	#1/找到.所在的位置
	position = temp.rfind(".")
	
	#2.取出从position开始的字符窜
	print( temp[position:] )
