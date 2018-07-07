
def func(functionName):
	
	def inner(*args, **kwargs):
		print("调用成功")
		functionName(*args, **kwargs)

	return inner

@func
def test(a, b):
	print("%d	%d"%(a, b))

test(10, 20)

@func
def test2(a, b, c):
	print("%d	%d	%d"%(a, b, c))

test2(20, 50, 80)
