#-*- coding:UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
<<<<<<< HEAD
from PyQt4 import QtGui,QtCore,uic
 
dir_=str(os.getcwd())
qtCeeatorFile = dir_+"\unit_calc.ui" #enter file here
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCeeatorFile)

class MyApp(QtGui.QMainWindow,Ui_MainWindow):
=======
from PyQt4 import QtGui, QtCore, uic

dir_ = str(os.getcwd())
qtCeeatorFile = dir_+"\unit_calc.ui"  # enter file here
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCeeatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):

>>>>>>> e9de632769f4720d6cc057b8134899584158de02
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.jisuan_button.clicked.connect(self.calcunit)

	def calcunit(self):
<<<<<<< HEAD
		test_str=str(self.zuoshang.toPlainText())+str(self.youshang.toPlainText())+str(self.zuoxia.toPlainText())+str(self.youxia.toPlainText())+str(self.bianchang.toPlainText())
		H=float(self.bianchang.toPlainText())
		if H>0:
			h1=float(self.zuoshang.toPlainText())
			h2=float(self.youshang.toPlainText())
			h3=float(self.zuoxia.toPlainText())
			h4=float(self.youxia.toPlainText())
			l=h1,h2,h3,h4
			j=0
			bigger=[]
			lower=[]
			sum_=0
			for i in l:
				if i >=0:
					j+=1
					bigger.append(i)
				else :
					lower.append(i)
			if j==4:
				for i in bigger:
					sum_+=i
				result=((H**2)/4)*sum_
				self.result_box.setText('')
				self.result_box.append(u"填方："+str(result))
				self.result_box.append(u"填挖方："+str(result))
			elif j==3:
				if h1<0:
					v1=-((H**2)*-1*(h1**3))/(6*(-h1+h2)*(-h1+h3))
					v2=(((H**2)*(2*(h2+h3)+h4+h1))/6)-v1
					result=v1+v2
					self.result_box.setText('')
					self.result_box.append(u"填方："+str(v2))
					self.result_box.append(u"挖方："+str(v1))
					self.result_box.append(u"填挖方："+str(result))
				elif h2<0:
					v1=-(((H**2)*-1*(h2**3))/(6*(-h2+h1)*(-h2+h4)))
					v2=(((H**2)*(2*(h1+h4)+h3+h2))/6)-v1
					result=v2+v1
					self.result_box.setText('')
					self.result_box.append(u"填方："+str(v2))
					self.result_box.append(u"挖方："+str(v1))
					self.result_box.append(u"填挖方："+str(result))
				elif h3<0:
					v1=-(((H**2)*-1*(h3**3))/(6*(-h3+h1)*(-h3+h4)))
					v2=(((H**2)*(2*(h1+h4)+h2+h3))/6)-v1
					result=v2+v1
					self.result_box.setText('')
					self.result_box.append(u"填方："+str(v2))
					self.result_box.append(u"挖方："+str(v1))
					self.result_box.append(u"填挖方："+str(result))
				elif h4<0:
					v1=-(((H**2)*-1*(h4**3))/(6*(-h4+h2)*(-h4+h3)))
					v2=(((H**2)*(2*(h2+h3)+h4+h1))/6)-v1
					result=v2+v1
					self.result_box.setText('')
					self.result_box.append(u"填方："+str(v2))
					self.result_box.append(u"挖方："+str(v1))
					self.result_box.append(u"填挖方："+str(result))
			elif j==2:
				if h1*h4>=0:
					v1=(H**2)*(bigger[0]**3)/(6*(bigger[0]-lower[0])*(bigger[0]-lower[1]))
					v2=(H**2)*(bigger[1]**3)/(6*(bigger[1]-lower[0])*(bigger[1]-lower[1]))
					v=-(((H**2)/6)*(2*(-lower[0]-lower[1])-(bigger[0]+bigger[1]))+v1+v2)
					result=v+v1+v2
=======
		test_str = str(self.zuoshang.toPlainText()) + str(self.youshang.toPlainText()) + str(
			self.zuoxia.toPlainText()) + str(self.youxia.toPlainText())+str(self.bianchang.toPlainText())
		H = float(self.bianchang.toPlainText())
		if H > 0:
			h1 = float(self.zuoshang.toPlainText())
			h2 = float(self.youshang.toPlainText())
			h3 = float(self.zuoxia.toPlainText())
			h4 = float(self.youxia.toPlainText())
			l = h1, h2, h3, h4
			j = 0
			bigger = []
			lower = []
			sum_ = 0
			for i in l:
				if i >= 0:
					j += 1
					bigger.append(i)
				else:
					lower.append(i)
			if j == 4:
				for i in bigger:
					sum_ += i
				result = ((H ** 2) / 4) * sum_
				self.result_box.setText('')
				self.result_box.append(u"填方：" + str(result))
				self.result_box.append(u"填挖方：" + str(result))
			elif j == 3:
				if h1 < 0:
					v1 = -((H ** 2) * -1 * (h1 ** 3)) / \
						(6 * (-h1 + h2) * (-h1 + h3))
					v2 = (((H ** 2) * (2 * (h2 + h3) + h4 + h1)) / 6) - v1
					result = v1 + v2
					self.result_box.setText('')
					self.result_box.append(u"填方：" + str(v2))
					self.result_box.append(u"挖方：" + str(v1))
					self.result_box.append(u"填挖方：" + str(result))
				elif h2 < 0:
					v1 =- (((H ** 2) * -1 * (h2 ** 3)) / (6 * (-h2 + h1) * (-h2 + h4)))
					v2 = (((H ** 2) * (2 * (h1 + h4) + h3 + h2)) / 6) - v1
					result = v2 + v1
					self.result_box.setText('')
					self.result_box.append(u"填方：" + str(v2))
					self.result_box.append(u"挖方：" + str(v1))
					self.result_box.append(u"填挖方：" + str(result))
				elif h3 < 0:
					v1 =- (((H ** 2)*-1*(h3**3))/(6*(-h3+h1)*(-h3+h4)))
					v2 = (((H ** 2) * (2 * (h1 + h4) + h2 + h3)) / 6) - v1
					result = v2 + v1
					self.result_box.setText('')
					self.result_box.append(u"填方：" + str(v2))
					self.result_box.append(u"挖方：" + str(v1))
					self.result_box.append(u"填挖方：" + str(result))
				elif h4 < 0:
					v1 =- (((H ** 2) * -1 * (h4 ** 3)) / (6 * (-h4 + h2) * (-h4 + h3)))
					v2 = (((H ** 2) * (2 * (h2 + h3) + h4 + h1)) / 6) - v1
					result = v2 + v1
					self.result_box.setText('')
					self.result_box.append(u"填方：" + str(v2))
					self.result_box.append(u"挖方：" + str(v1))
					self.result_box.append(u"填挖方：" + str(result))
			elif j == 2:
				if h1*h4 >= 0:
					v1 = (H ** 2) * (bigger[0] ** 3) / (6 * (bigger[0] - lower[0]) * (bigger[0] - lower[1]))
					v2 = (H ** 2) * (bigger[1] ** 3) / (6 * (bigger[1] - lower[0]) * (bigger[1] - lower[1]))
					v = -(((H ** 2) / 6) * (2 * (-lower[0] - lower[1]) - (bigger[0] + bigger[1])) + v1 + v2)
					result = v+v1+v2
>>>>>>> e9de632769f4720d6cc057b8134899584158de02
					self.result_box.setText('')
					self.result_box.append(u"填方："+str(v1+v2))
					self.result_box.append(u"挖方："+str(v))
					self.result_box.append(u"填挖方："+str(result))
				else:
<<<<<<< HEAD
					v1=((H**2)*((bigger[0]+bigger[1])**2))/(4*(bigger[0]+bigger[1]-lower[0]-lower[1]))
					v2=-(((H**2)*((-lower[0]-lower[1])**2))/(4*(bigger[0]+bigger[1]-lower[0]-lower[1])))
					result=v1+v2
					self.result_box.setText('')
					self.result_box.append(u"填方："+str(v1))
					self.result_box.append(u"挖方："+str(v2))
					self.result_box.append(u"填挖方："+str(result))
			elif j==1:
				if h1>=0:
					v1=((H**2)*(h1**3))/(6*(h1-h2)*(h1-h3))
					v2=-((((H**2)*(2*(-h2-h3)-h4-h1)))/6+v1)
					result=v1+v2
					self.result_box.setText('')
					self.result_box.append(u"填方："+str(v1))
					self.result_box.append(u"挖方："+str(v2))
					self.result_box.append(u"填挖方："+str(result))
				elif h2>=0:
					v1=((H**2)*(h2**3))/(6*(h2-h1)*(h2-h4))
					v2=-(((H**2)*(2*(-h1-h4)-h3-h2))/6+v1)
					result=v1+v2
					self.result_box.setText('')
					self.result_box.append(u"填方："+str(v1))
					self.result_box.append(u"挖方："+str(v2))
					self.result_box.append(u"填挖方："+str(result))
				elif h3>=0:
					v1=((H**2)*(h3**3))/(6*(h3-h1)*(h3-h4))
					v2=-(((H**2)*(2*(-h1-h4)-h2-h3))/6+v1)
					result=v1+v2
					self.result_box.setText('')
					self.result_box.append(u"填方："+str(v1))
					self.result_box.append(u"挖方："+str(v2))
					self.result_box.append(u"填挖方："+str(result))
				elif h4>=0:
					v1=((H**2)*(h4**3))/(6*(h4-h2)*(h4-h3))
					v2=-(((H**2)*(2*(-h2-h3)-h4-h1))/6+v1)
					result=v1+v2
					self.result_box.setText('')
					self.result_box.append(u"填方："+str(v1))
					self.result_box.append(u"挖方："+str(v2))
					self.result_box.append(u"填挖方："+str(result))
			elif j==0:
				for i in lower:
					sum_+=i
				result=((H**2)/4)*sum_
=======
					v1 = ((H**2)*((bigger[0]+bigger[1])**2))/(4*(bigger[0]+bigger[1]-lower[0]-lower[1]))
					v2 =- \(((H**2)*((-lower[0]-lower[1])**2)) /(4*(bigger[0] + bigger[1] - lower[0] - lower[1])))
					result = v1 + v2
					self.result_box.setText('')
					self.result_box.append(u"填方：" + str(v1))
					self.result_box.append(u"挖方：" + str(v2))
					self.result_box.append(u"填挖方：" + str(result))
			elif j == 1:
				if h1 >= 0:
					v1 = ((H ** 2) * (h1 ** 3)) / (6 * (h1 - h2) * (h1 - h3))
					v2 =- ((((H ** 2) * (2 * (-h2 - h3) - h4-h1))) / 6 + v1)
					result = v1 + v2
					self.result_box.setText('')
					self.result_box.append(u"填方：" + str(v1))
					self.result_box.append(u"挖方：" + str(v2))
					self.result_box.append(u"填挖方：" + str(result))
				elif h2 >= 0:
					v1 = ((H ** 2) * (h2 ** 3)) / (6 * (h2 - h1) * (h2 - h4))
					v2 =- (((H ** 2) * (2 * (-h1 - h4) - h3 - h2)) / 6 + v1)
					result = v1 + v2
					self.result_box.setText('')
					self.result_box.append(u"填方：" + str(v1))
					self.result_box.append(u"挖方：" + str(v2))
					self.result_box.append(u"填挖方：" + str(result))
				elif h3 >= 0:
					v1 = ((H ** 2) * (h3 ** 3)) / (6 * (h3 - h1) * (h3 - h4))
					v2 = -(((H ** 2) * (2 * (-h1 - h4) - h2 - h3)) / 6 + v1)
					result = v1+v2
					self.result_box.setText('')
					self.result_box.append(u"填方：" + str(v1))
					self.result_box.append(u"挖方：" + str(v2))
					self.result_box.append(u"填挖方：" + str(result))
				elif h4 >= 0:
					v1 = ((H ** 2) * (h4 ** 3)) / (6 * (h4-h2)*(h4-h3))
					v2 = - (((H ** 2) * (2*(-h2-h3)-h4-h1))/6+v1)
					result = v1 + v2
					self.result_box.setText('')
					self.result_box.append(u"填方：" + str(v1))
					self.result_box.append(u"挖方：" + str(v2))
					self.result_box.append(u"填挖方：" + str(result))
			elif j == 0:
				for i in lower:
					sum_ += i
				result = ((H ** 2) / 4) * sum_
>>>>>>> e9de632769f4720d6cc057b8134899584158de02
				self.result_box.setText('')
				self.result_box.append(u"挖方："+str(result))
				self.result_box.append(u"填挖方："+str(result))
			else:
				self.result_box.setText("error")

		else:
			self.result_box.setText("error")


if __name__ == "__main__":
<<<<<<< HEAD
	app=QtGui.QApplication(sys.argv)
	window=MyApp()
=======
	app = QtGui.QApplication(sys.argv)
	window = MyApp()
>>>>>>> e9de632769f4720d6cc057b8134899584158de02
	window.show()
	sys.exit(app.exec_())
