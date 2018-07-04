class Animal(object):

	def __init__(self, name = "动物",color = "白色"):
		self.name = name
		self.color = color
	
	def __del__(self):
		print("-"*30)

	def __str__(self):
		msg = self.name + self.color
		return msg

	def eat(self):
		pass

	def bark(self):
		pass

	def run(self):
		pass


class Horse(Animal):

#def __init__(self, name, color = "白色"):
#	super().__init__(name, color)

	def bark(self):
		print("啊啊啊")

	def run(self):
		print("快")
	
class Donkey(Animal):
	
#def __init__(self, name, color = "白色"):
#	super().__init__(name, color)

	def bark(self):
		print("咩咩咩")

	def run(self):
		print("慢")


class HanxueBaoma(Horse):

	def __init__(self, name, color = "血红色"):
		super().__init__(name,color)

	def bark(self):
		print("哈哈哈")

	def run(self):
		print("快")


class Mule(Donkey, Horse):

#def __init__(self, name, color = "白色"):
#	super().__init__(name,color)

	def bark(self):
		print("哈哈哈")

	def __init__(self, name, color = "血红色"):
		super().__init__(name,color)
	def run(self):
		print("超级慢")

cituma = Mule("cituma","红色")
print(cituma)
