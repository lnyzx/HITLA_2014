import os
import re

dir_ = str(os.getcwd())
list_old = []
list_new = []


def compa():	
	with open(dir_+'\\new.txt','r') as f_old:
		lines_new=f_old.readlines()
		for line_new in lines_new:
			line_new = re.split(r'\s',line_new)
			list_new.append(line_new)

	with open(dir_+'\\old.txt','r') as f_old:
		lines_old=f_old.readlines()
		for line_old in lines_old:
			line_old = re.split(r'\s',line_old)
			list_old.append(line_old)

	for i in range(11):
		for j in range(11):
			if list_new[i][j] == list_old[i][j]:
				print str(i) + '. ' + str(j)
				f_t = float(list_new[i][j])
				list_new[i][j] = f_t


	with open(dir_ + '\\new.txt','r') as f:
		

if __name__ == "__main__":
	compa()
	a = raw_input()