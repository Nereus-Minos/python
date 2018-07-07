
def w1(func):
	print('---1---')
	def inner():
		print('---w1---')
		func()
		return "w1 + " + func()

	return inner

def w2(func):
	print('---2---')
	def inner():
		print('---w2---')
		func()
		return "w2 + " +func()

	return inner

@w1
@w2
def f1():
	print('---f1---')
	return "hahaha"
ret = f1()
print(ret)
