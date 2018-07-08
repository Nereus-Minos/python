#工厂模式：定义一个创建对象的接口类，由子类来完成具体的任务


#定义一个基本的4S店类
class CarStore(object):
	#仅仅定义了有此方法，并未实现具体功能，具体功能需要在子类中完成
	def createCar(self,typeName):
		pass
	
	def order(self, typeName):
		#让工厂根据需求生产汽车
		self.car = self.createCar(typeName)
		self.car.move()
		self.car.stop()

#定义一个北京现代的4S店类
class XiandaiCarStore(CarStore):
	
	def createCar(self,typeName):
		self.carFactory = CarFactory()
		return self.carFactory.createCar(typeName)

#定义伊兰特车类
class YilanteCar(object):
	
	def move(self):
		print("---伊兰特移动---")
	def stop(self):
		print("---伊兰特停止---")

#定义一个索纳塔车类
class SuonataCar(object):
	
	def move(self):
		print("---索纳塔移动---")
	def stop(self):
		print("---索纳塔停止---")

#定义一个生产汽车的工厂，让他完成具体的任务
class CarFactory(object):
	
	def createCar(self, typeName):
		self.typeName = typeName
		if self.typeName == "伊兰特":
			self.car = YilanteCar()
		elif self.typeName == "索纳塔":
			self.car = SuonataCar()
		
		return self.car


#主函数
suonata = XiandaiCarStore()
suonata.order("索纳塔")
