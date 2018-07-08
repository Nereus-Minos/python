import random

def randList(n):
	
	num = []
	while len(num) < 11:
		x = random.randint(1,11)
		if x not in num:
			num.append(x)
	print(num)

randList(10)
