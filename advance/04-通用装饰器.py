
def func(functionName):
	
	def inner(*args, **kwargs):
		return functionName(*args, **kwargs)

	return inner

@func
def test():
	print('---test---')

@func
def test2(a, b):
	return '---test2---' + a + '	' + b

ret = test()

print(ret)
print('-'*30)

ret = test2('aaa', 'bbb')

print(ret)
print('-'*30)	

