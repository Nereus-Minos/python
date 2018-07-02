#encodding=utf-8 

import random

#三件办公室8名老师随机分配，但要求每个办公室至少有俩名老师

offices = [ [],[],[] ]

teachers = [ "a","b","c","d","e","f","g","h" ]


#1,首先使每个办公室至少有两名
for office in offices:
	i = 0
	while i < 2 :
		temp=random.randint(0,len(teachers)-1)
		office.append(teachers[temp])
		teachers.pop(temp)
		i += 1
	
#2.将剩下的老师随机分配
for tempTeacher in teachers:
	temp=random.randint(0,2)
	offices[temp].append(tempTeacher)

print(offices)
