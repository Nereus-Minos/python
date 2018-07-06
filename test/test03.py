#encoding=utf-8

def lambdaFunc(a, b, func):
	
	ret = func(a, b)
	return ret

a = int(input("请输入一个数"))
b = int(input("请输入第二个数"))
#func = input("请输入一个匿名函数")  #python2可用

func = eval(func)	#相当于删除了""

test(a, b, func)
