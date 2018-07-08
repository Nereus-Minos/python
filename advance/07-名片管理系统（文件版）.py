#encoding=utf-8

#需求：编写学生管理系统


#1.显示菜单
def displayMenu():
	print("-"*30)
	print("学生管理系统		V1.0")
	print("1.添加学生信息")
	print("2.删除学生信息")
	print("3.修改学生信息")
	print("4.查询学生信息")
	print("5.遍历学生信息")
	print("6.保存学生信息")
	print("7.退出系统")
	print("-"*30)

#2.获取用户的选择
def selectMenu():
	return input("请输入功能（序号）：")

#3.根据用户的选择执行相应的操作

#3.1添加学生的信息
def createStudent(students):
	#定义一个字典存放学生信息{"id" : 'id', 'name':'name', 'age':'age'}
	student = {}
	name = input("请输入姓名")
	id = input("请输入id号")
	age = input("请输入年龄")
	student['name'] = name
	student['id'] = id
	student['age'] = age
	students.append(student)

#3.2删除学生信息
def deleteStudent(students):
	subscript = int(input("请输入要删除的学生的序号"))
	del students[subscript]

#3.3修改学生信息
def updateStudent(students):
	subscript = int(input("请输入要修改的学生的序号"))
	temp = students[subscript]
	newName = input("请输入新的姓名")
	newAge = input("请输入新的年龄")
	newId = input("请输入新的ID")
	students[subscript]['name'] = newName
	temp['age'] = newAge
	temp['id'] = newId

#3.4查询学生信息
def readStudent(students):
	subscript = int(input("请输入要修改的学生的序号"))
	temp = students[subscript]
	print("姓名"+" "*8+"年龄"+" "*8+"id")
	print("%s%10s%10s"%(temp['name'],temp['age'],temp['id']))
	

#3.5遍历学生信息
def traverseStudent(students):
	print("-"*30)
	print("姓名"+" "*6+"年龄"+" "*6+"id"+" "*6)
	for temp in students :
		print("%-10s%-10s%-10s"%(temp['name'],temp['age'],temp['id']))
	print("-"*30)


#3.6保存学生信息
def save_2_file(students):
	f = open("student_info.data", 'w')
	f.write(str(students))
	f.close()
	

#读取文件中的信息
def read_file_info():
	students = []
	try:
		f = open("student_info.data")
		students = eval(f.read())
		f.close()
	except Exception:
		pass
	return students

#主函数
#定义一个列表存放各学生字典
def main():

		students = read_file_info()

		displayMenu()
		while True:
			select = int(selectMenu())
			
			if 1 == select :
				createStudent(students)
			elif 2 == select :
				deleteStudent(students)
			elif 3 == select :
				updateStudent(students)
			elif 4 == select :
				readStudent(students)
			elif 5 == select :
				traverseStudent(students)
			elif 6 == select :
				save_2_file(students)
			elif 7 == select :
				break
			else:
				print("请输入正确的序号！")
				
		print("欢迎下次再来")



if __name__ == "__main__":
	
	main()

	

