
def fibonacci():
	a, b = 0, 1
	for i in range(5):
		print(b)
		a, b = b, a+b

#fibonacci()

#用生成器
def fibonacci2():
	a, b = 0, 1
	for i in range(5):
		print("---1---")
		yield(b)	#yiled()表示此函数成为一个生成器,会卡在这儿,用next(对象名)向下执行并且此时会返回一个值
		print("---2---")
		a, b = b, a+b
		print("---3---")

a = fibonacci2()	#不用next()函数则不会执行此函数

#for num in a:
#	print(num)

ret = next(a)
print(ret)

ret = a.__next__()	#这与next(a)等价
print(ret)

