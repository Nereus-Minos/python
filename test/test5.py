#encoding = utf-8

import random

#需求：现有三个办公室，8名老师，为8名老师随机分配办公室

#定义一个列表存储办公室
offices = [ [], [], [] ]

#定义一个列表存储老师
teachers = ["a", "b", "c", "d", "e", "f", "g", "h"]

#遍历所有的老师
for teacher in teachers:
	office = random.randint(0,2)
	offices[office].append(teacher)

print(offices)
