#encoding=utf-8

#需求：烤地瓜
#分析：
#一、属性：
#	1.cookedLevel:这是数字，0~3表示还是生的，超过3表示半生不熟，超过5表示已经烤好了，超过8表示已经烤成木炭了
#	2.cookedString：这是字符串，表示地瓜生熟的情况
#	3.condiments：调料列表
#二、方法：
#	1.cook()：把地瓜烤一段时间
#	2.addCondiments()：给地瓜添加配料
#.......

class sweetPotato:
	def __init__(self):
		"类属性"
		self.__cookedLevel = 0
		self.__cookedString = "生的"
		self.__condiments = []
	
	def __str__(self):
		#msg = str(self.__cookedLevel)+"	"+self.__cookedString+"	"+str(self.__condiments)
		msg = str(self.__cookedLevel)+"	"+self.__cookedString+"	"
		for temp in self.__condiments :
			msg += temp
			msg += "；"
		msg = msg.strip("；")
		return msg
		#print("%s	%s	%s"%(self.cookedLevel,self.cookedString,self.condiments))
		#return "potato"

	def cook(self,time):
		self.__cookedLevel += time
		if  self.__cookedLevel > 8 :
			self.__cookedString = "烤成木炭了"
		elif self.__cookedLevel > 5 :
			self.cookedString = "已经烤好了"
		elif self.__cookedLevel > 3 :
			self.__cookedString = "半生不熟"
		else :
			self.__cookedString = "生的"

	def addCondiments(self,condiment):
		self.__condiments.append(condiment)

#主函数
potato = sweetPotato()
print(potato)
print("-"*20)
potato.addCondiments("番茄酱")
potato.addCondiments("孜然")
print(potato)
print("-"*20)


potato.__cookedString = "arfdafafdas"   #这不是potato内部的私有属性，是新建立的一个公有属性
print(potato.__cookedString)
print("-"*20)
print(potato)
