#coding:utf-8
import os
import re

dir_this=str(os.getcwd())

list_a=[]
with open(dir_this+'\\new_copy.txt','r') as f:
	lines = f.readlines()
	for each_line in lines:
		tem_list=[]
		temp_list=re.split(r'\s',each_line)
		for each_item in temp_list:
			tem_list.append(each_item)
		list_a.append(tem_list)

with open(dir_this+'\\new.txt','w') as f:
	for i in list_a:
		for j in i:
			try:
				j=float(j)-0.2
			except(ValueError):
				pass
			else:
				f.write(str(float(j)))
				f.write(' ')
		f.write('\n')