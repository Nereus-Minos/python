class Test(object):
	def __init__(slef):
		self.__num = 100

	@property
	def num(self):
		print("---getter---")
		return self.__num

	@num.setter
	def num(self, newNumm):
		print("---setter---")
		self.__num = newNum

t = Test()

t.num = 200   #相当于调用了t.setNum(200)

print(t.num)	#相当于调用了t.getNum()
