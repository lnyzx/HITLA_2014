#coding:utf-8
import os

dir_this=str(os.getcwd())

list_a=[[0.0 for i in range(11)]for j in range(11)]

with open(dir_this+'\\old.txt','w') as f:
	for i in list_a:
		for j in i:
			f.write(str(float(j)))
			f.write(' ')
		f.write('\n')