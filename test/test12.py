#encoding=utf-8

class ShortInputException(Exception):
	"自定义的异常类"
	def __init__(self, length, atleast):
		super().__init__("长度不够")
		self.length = length
		self.atleast = atleast

def main():
		try:
			s = input("请输入：")
			if len(s) < 3 :
				#raise引发一个定义的异常类
				raise ShortInputException(len(s), 3)

		except ShortInputException as result:
			print("输入的长度为%d小于要求的最小长度%d"%(result.length, result.atleast))
			print(result)
		else:
			print("没有异常发生")


main()
