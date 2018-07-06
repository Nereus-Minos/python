#encoding=utf-8

import os

#批量重命名

##1.获取要重命名的文件夹的名字
#folder_name = input("请输入要重命名的文件夹：")

##2.获取文件夹中的文件
#file_names = os.listdir(folder_name)

##重命名
#add_name = input("请输入要添加的名字：")

#for file_name in file_names:
#	old_name = folder_name + '/' + file_name
#	new_name = folder_name + '/' + add_name + file_name
#	os.rename(old_name, new_name)

'''
批量删除文件名的前几个名
'''
folder_name = input("请输入要进行删除部分名的文件夹：")

file_names = os.listdir(folder_name)

del_name = input("请输入要删除的名字：")

for file_name in file_names:
	old_name = folder_name + '/' + file_name
	
	find_name = file_name.find(del_name)
	find_name_last = find_name+len(del_name)

	if find_name != -1:  
	#表示名字中有要删除的字		#利用切片
		new_name = folder_name + '/' + file_name[0:find_name] + file_name[find_name_last: ]
		print(file_name.strip(del_name))
	else:
		print("文件中不含此名")

	os.rename(old_name, new_name)
