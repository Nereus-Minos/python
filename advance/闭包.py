
def test(number1):

	print("---1---")

	def test_in(number2):
		print("---2---")
		print(number1 + number2)

	print("---3---")
	return test_in

ret = test(100)
print("-"*30)
ret(1)
ret(100)
ret(200)
