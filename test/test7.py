#encoding=utf-8

#定义一个空的字典存储名片
cards = {}


def displayMenu():
	"显示菜单"
	print("  名片管理系统	V8")
	print("1,添加名片")
	print("2.删除名片")
	print("3.修改名片")
	print("4.查询名片")
	print("5.遍历所有名片")
	print("6.退出系统")


def select():
	"选择"
	return input("请输入序号")


def createCard():
	"添加名片"
	name = input("请输入姓名")
	phone = input("请输入手机号")
	cards[name] = phone

def deleteCard(name):
	"删除名片"
	if ( len(cards) != 0 ) and ( name in cards.keys() ) :
		del cards[name]
	else :
		print("此名片已经不在")

def updateCard(name):
	"修改名片"
	if name in cards.keys():
		newPhone = input("请输入新的手机号")
		cards[name] = newPhone
	else :
		print("请输入正确的姓名")

def readCard(name):
	"查询名片"
	if name in cards.keys():
		print("%10s	%s"%(name, cards[name]))
	else :
		print("请输入正确的姓名")

def traverseCard():
	"遍历名片"
	for name,phone in cards:
		print("%10s	%s"%(name, phone))

	
#主函数
if __name__ == "__main__":
	displayMenu()
	while True:
		selection = int(select())   #必须转换成int
	
		if selection == 1 :
			createCard()
		elif selection == 2 :
			name = input("请输入要删除的姓名")
			deleteCard(name)
		elif selection == 3 :
			name = input("请输入要修改的姓名")
			updateCard(name)
		elif selection == 4 :
			name = input("请输入要查找的姓名")
		elif selection == 5 :
			traverseCard()
		else :
			break


