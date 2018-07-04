class People(object):

	#类属性
	Num = 0

	def __init__(self):
		self.Num += 1

	#类方法
	@classmethod
	def getNum(cls):
		return cls.Num

class Dog(object):
	Num = 0

p = People()
print(People.Num)  #0
p2 = People()
print(People.Num)	#0
num = People.getNum()
print(num)	#0

d = Dog()
Dog.Num += 1
print(Dog.Num)	#1
d2 = Dog()
Dog.Num += 1
print(Dog.Num)	#2
d3 = Dog()
d3.Num += 1
print(Dog.Num)	#2
print(d3.Num)	#3 ,表明对象不能修改类属性
