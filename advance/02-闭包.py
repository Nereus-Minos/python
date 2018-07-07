#
#def test(number1):
#
#	print("---1---")
#
#	def test_in(number2):
#		print("---2---")
#		print(number1 + number2)
#
#	print("---3---")
#	return test_in
#
#ret = test(100)
#print("-"*30)
#ret(1)
#ret(100)
#ret(200)
#
#
#获得不同的直线表达式
def lineExpression(a, b):
	
	def lineExpression_in(x):
		print(a*x+b)

	return lineExpression_in

line1 = lineExpression(1, 1)
line2 = lineExpression(2,1)

line1(2)
line2(3)


