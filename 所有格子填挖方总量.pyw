#-*- coding:UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import re
from PyQt4 import QtGui,QtCore,uic
#配置
dir_this=str(os.getcwd())
qtCeeatorFile = dir_this + "\\tufang.ui" #enter file here
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCeeatorFile)
list_old=[]
list_new=[]
H=30


class MyApp(QtGui.QMainWindow,Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.calc_button.clicked.connect(self.calc_tufang)#土方计算
		self.save_button.clicked.connect(self.save)#保存
		self.save_button_2.clicked.connect(self.save)
		self.save_button_3.clicked.connect(self.save)
		self.save_button_4.clicked.connect(self.save)
		self.save_button_5.clicked.connect(self.save)
		self.save_button_6.clicked.connect(self.save)
		self.save_button_7.clicked.connect(self.save)
		self.new_change_button.clicked.connect(self.changenew)#修改设计标高
		self.old_change_button.clicked.connect(self.changeold)#修改原标高
		self.new_next_button.clicked.connect(self.nextnew)#下一个设计坐标
		self.old_next_button.clicked.connect(self.nextold)#下一个原坐标
		self.read_button.clicked.connect(self.read_file)#读取文件

	def read_file(self):
		if self.table_old.model()==None:
			with open(dir_this+'\\old.txt','r') as f_old:
				lines_old=f_old.readlines()
				self.model=QtGui.QStandardItemModel(11,11)
				self.model.setHorizontalHeaderLabels(['0','1','2','3','4','5','6','7','8','9','10'])
				self.model.setVerticalHeaderLabels(['0','1','2','3','4','5','6','7','8','9','10'])
				row=0
				for line_old in lines_old:
					column=0
					temp_list=re.split(r'\s',line_old)
					list_old.append(temp_list)
					for each_item in temp_list:
						item = QtGui.QStandardItem(str(each_item))
						self.model.setItem(row,column,item)
						column+=1
					row+=1
				self.table_old.setModel(self.model)
			
			with open(dir_this+'\\new.txt','r') as f_new:
				lines_new=f_new.readlines()
				self.model=QtGui.QStandardItemModel(11,11)
				self.model.setHorizontalHeaderLabels(['0','1','2','3','4','5','6','7','8','9','10'])
				self.model.setVerticalHeaderLabels(['0','1','2','3','4','5','6','7','8','9','10'])
				row=0
				for line_new in lines_new:
					column=0
					temp_list=re.split(r'\s',line_new)
					list_new.append(temp_list)
					for each_item in temp_list:
						item = QtGui.QStandardItem(str(each_item))
						self.model.setItem(row,column,item)
						column+=1
					row+=1
				self.table_new.setModel(self.model)
		else:
			self.tufang_box.append(u'还读取个蛋')
	def calc_tufang(self):
		self.tufang_box.setText('')
		v_all=0
		v_wa=0
		v_tian=0
		for i in range(0,10):
			for j in range(0,10):
				h1=float(list_new[i][j])-float(list_old[i][j])
				h2=float(list_new[i][j+1])-float(list_old[i][j+1])
				h3=float(list_new[i+1][j])-float(list_old[i+1][j])
				h4=float(list_new[i+1][j+1])-float(list_old[i+1][j+1])
				l=h1,h2,h3,h4
				k=0
				bigger=[]
				lower=[]
				sum_=0
				for cam_i in l:
					if cam_i >=0:
						k+=1
						bigger.append(cam_i)
					else :
						lower.append(cam_i)
				if k==4:
					for bigger_h in bigger:
						sum_+=bigger_h
					result=((H**2)/4)*sum_
					if result>0:
						v_tian+=result
					else:
						v_wa+=result
				elif k==3:
					if h1<0:
						v1=-((H**2)*-1*(h1**3))/(6*(-h1+h2)*(-h1+h3))
						v2=(((H**2)*(2*(h2+h3)+h4+h1))/6)-v1
						result=v1+v2
						if result>0:
							v_tian+=result
						else:
							v_wa+=result
					elif h2<0:
						v1=-(((H**2)*-1*(h2**3))/(6*(-h2+h1)*(-h2+h4)))
						v2=(((H**2)*(2*(h1+h4)+h3+h2))/6)-v1
						result=v2+v1
						if result>0:
							v_tian+=result
						else:
							v_wa+=result
					elif h3<0:
						v1=-(((H**2)*-1*(h3**3))/(6*(-h3+h1)*(-h3+h4)))
						v2=(((H**2)*(2*(h1+h4)+h2+h3))/6)-v1
						result=v2+v1
						if result>0:
							v_tian+=result
						else:
							v_wa+=result
					elif h4<0:
						v1=-(((H**2)*-1*(h4**3))/(6*(-h4+h2)*(-h4+h3)))
						v2=(((H**2)*(2*(h2+h3)+h4+h1))/6)-v1
						result=v2+v1
						if result>0:
							v_tian+=result
						else:
							v_wa+=result
				elif k==2:
					if h1*h4>0:
						v1=(H**2)*(bigger[0]**3)/(6*(bigger[0]-lower[0])*(bigger[0]-lower[1]))
						v2=(H**2)*(bigger[1]**3)/(6*(bigger[1]-lower[0])*(bigger[1]-lower[1]))
						v=-(((H**2)/6)*(2*(-lower[0]-lower[1])-(bigger[0]+bigger[1]))+v1+v2)
						result=v+v1+v2
						if result>0:
							v_tian+=result
						else:
							v_wa+=result
					else:
						v1=((H**2)*((bigger[0]+bigger[1])**2))/(4*(bigger[0]+bigger[1]-lower[0]-lower[1]))
						v2=-(((H**2)*((-lower[0]-lower[1])**2))/(4*(bigger[0]+bigger[1]-lower[0]-lower[1])))
						result=v1+v2
						if result>0:
							v_tian+=result
						else:
							v_wa+=result
				elif k==1:
					if h1>0:
						v1=((H**2)*(h1**3))/(6*(h1-h2)*(h1-h3))
						v2=-((((H**2)*(2*(-h2-h3)-h4-h1)))/6+v1)
						result=v1+v2
						if result>0:
							v_tian+=result
						else:
							v_wa+=result
					elif h2>0:
						v1=((H**2)*(h2**3))/(6*(h2-h1)*(h2-h4))
						v2=-(((H**2)*(2*(-h1-h4)-h3-h2))/6+v1)
						result=v1+v2
						if result>0:
							v_tian+=result
						else:
							v_wa+=result
					elif h3>0:
						v1=((H**2)*(h3**3))/(6*(h3-h1)*(h3-h4))
						v2=-(((H**2)*(2*(-h1-h4)-h2-h3))/6+v1)
						result=v1+v2
						if result>0:
							v_tian+=result
						else:
							v_wa+=result
					elif h4>0:
						v1=((H**2)*(h4**3))/(6*(h4-h2)*(h4-h3))
						v2=-(((H**2)*(2*(-h2-h3)-h4-h1))/6+v1)
						result=v1+v2
						if result>0:
							v_tian+=result
						else:
							v_wa+=result
				elif k==0:
					for all_lower in lower:
						sum_+=all_lower
					result=((H**2)/4)*sum_
					if result>0:
						v_tian+=result
					else:
						v_wa+=result
		v_all=v_wa+v_tian
		self.tufang_box.append(u"填方："+str(v_tian))
		self.tufang_box.append(u"挖方："+str(v_wa))
		self.tufang_box.append(u"填挖方总量："+str(v_all))
	def save(self):
		if list_new:
			f1=open(dir_this+'\\old.txt','w')
			for i in range(11):
				for j in range(11):
					f1.write(str(list_old[i][j])+' ')
				f1.write('\n')
			f1.close()
			
			f2=open(dir_this+'\\new.txt','w')
			for i in range(11):
				for j in range(11):
					f2.write(str(list_new[i][j])+' ')
				f2.write('\n')
			f2.close()
		else:
			self.tufang_box.append(u'保存个鬼啊')
			#self.tufang_box.append(str(self.table_old.model()))
	def changenew(self):
		new_x=int(self.new_x_box.toPlainText())
		new_y=int(self.new_y_box.toPlainText())
		new_biaogao=float(self.new_biaogao_box.toPlainText())
		list_new[new_x][new_y]=str(new_biaogao)
		self.model=QtGui.QStandardItemModel(11,11)
		self.model.setHorizontalHeaderLabels(['0','1','2','3','4','5','6','7','8','9','10'])
		self.model.setVerticalHeaderLabels(['0','1','2','3','4','5','6','7','8','9','10'])
		row=0
		for line_new in list_new:
			column=0
			for each_item in line_new:
				item = QtGui.QStandardItem(str(each_item))
				self.model.setItem(row,column,item)
				column+=1
			row+=1
		self.table_new.setModel(self.model)
	def changeold(self):
		old_x=int(self.old_x_box.toPlainText())
		old_y=int(self.old_y_box.toPlainText())
		old_biaogao=float(self.old_biaogao_box.toPlainText())
		list_old[old_x][old_y]=str(old_biaogao)
		self.model=QtGui.QStandardItemModel(11,11)
		self.model.setHorizontalHeaderLabels(['0','1','2','3','4','5','6','7','8','9','10'])
		self.model.setVerticalHeaderLabels(['0','1','2','3','4','5','6','7','8','9','10'])
		row=0
		for line_old in list_old:
			column=0
			for each_item in line_old:
				item = QtGui.QStandardItem(str(each_item))
				self.model.setItem(row,column,item)
				column+=1
			row+=1
		self.table_old.setModel(self.model)
	def nextold(self):
		old_x=int(self.old_x_box.toPlainText())
		old_y=int(self.old_y_box.toPlainText())
		if old_y<10:
			old_y+=1
			self.old_y_box.setText(str(old_y))
		elif old_x<10:
			old_y=0
			self.old_y_box.setText(str(old_y))
			old_x+=1
			self.old_x_box.setText(str(old_x))
		elif old_x==10:
			old_y=0
			self.old_y_box.setText(str(old_y))
			old_x=0
			self.old_x_box.setText(str(old_x))
	def nextnew(self):
		new_x=int(self.new_x_box.toPlainText())
		new_y=int(self.new_y_box.toPlainText())
		if new_y<10:
			new_y+=1
			self.new_y_box.setText(str(new_y))
		elif new_x<10:
			new_y=0
			self.new_y_box.setText(str(new_y))
			new_x+=1
			self.new_x_box.setText(str(new_x))
		elif new_x==10:
			new_y=0
			self.new_y_box.setText(str(new_y))
			new_x=0
			self.new_x_box.setText(str(new_x))

if __name__ == "__main__":
	app=QtGui.QApplication(sys.argv)
	window=MyApp()
	window.show()
	sys.exit(app.exec_())
