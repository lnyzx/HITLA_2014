#-*- coding:UTF-8 -*-
import os

x=float(297.45)
list_a=range(30,101)
list_b = range(30,121)
k=0

def x_y():
	for i1 in range(30,66):
		i1=float(i1)/10000
		for i2 in list_b:
			i2=float(i2)/10000
			for i3 in list_b:
				i3=float(i3)/10000
				for i4 in list_b:
					i4=float(i4)/10000
					a=x-(156.7*i1)
					a_0 = x-(i1*59.7)
					c_1 = a_0+(i2*121.4)
					c = c_1+(i3*39.4)
					c1 = x+(i4*185.75)
					b = c_1-(i3*25.4)
					i_1 = (c-x)/153.9
					if abs(c-c1)<=0.01:
						global k
						k+=1
						print 'number:'+str(k)+'-------------------------------------------------'
						print 'a:'+str(a)
						print 'b:'+str(b)
						print 'c: '+str(c)
						print 'c_1: '+str(c_1)
						print 'a_0: '+str(a_0)
						print str('i1:')+str(i1)
						print str('i2:')+str(i2)
						print str('i3:')+str(i3)
						print str('i4:')+str(i4)
						print 'i_1: '+str(i_1)

									
a=float(296.51949)
def a_():
	for i1 in list_a:
		i1=float(i1)/10000
		for i2 in list_a:
			i2=float(i2)/10000
			for i3 in list_a:
				i3=float(i3)/10000
				for i4 in list_a:
					i4=float(i4)/10000
					b=a-(33.3*i1)
					c=b+(119.5*i2)
					d=c-(59.9*i3)
					a1=d-(80*i4)
					d_1 = d-(i3*30.87)
					if abs(a-a1)<=0.001 and i1 == 0.0053 and 297.12<d_1<=297.13:
						b_0 = b-(i1*10.9)
						b_1 = b_0-(i1*26.5)
						b_3 = c+(i3*45.86)
						i5 = (b_3-b_1)/137.68
						b_2 = b_1+(i5*102.72)
						global k
						k+=1
						print 'number:'+str(k)+'-------------------------------------------------'
						print 'a:a1'+str(a)+':'+str(a1)
						print 'b:'+str(b)
						print 'c:'+str(c)
						print 'd'+str(d)
						print 'd_1: '+str(d_1)
						print ' b_0: '+str(b_0)
						print 'b_1: '+str(b_1)
						print 'b_2: '+str(b_2)
						print str('i1:')+str(i1)
						print str('i2:')+str(i2)
						print str('i3:')+str(i3)
						print str('i4:')+str(i4)
						print 'i5: '+str(i5)

def youxia():
	i1 = 0.0049
	for i2 in list_a:
		i2=float(i2)/10000
		for i3 in list_a:
			i3=float(i3)/10000
			b=a-(26.4*i1)
			c=b-(147.3*i2)
			x1=c+(109.5*i3)
			if abs(x-x1)<=0.001:
				global k
				k+=1
				c_0 = c-(i3*91.7)
				c_1 = c+(i3*39.4)
				c_2 = c_1+(i3*24.97)
				c_3 = a+(29.63*i1)
				c_4 = c_3+(46.18*i1)
				i4 = (c_3-c_1)/120.01
				i5 = (c_4-c_2)/82.67
				print 'number:'+str(k)+'-------------------------------------------------'
				print 'b:'+str(b)
				print 'c:'+str(c)
				print 'c_0: '+str(c_0)
				print 'c_1: '+str(c_1)
				print 'c_2: '+str(c_2)
				print 'c_3: '+str(c_3)
				print 'c_4: '+str(c_4)
				print str('i2:')+str(i2)
				print str('i3:')+str(i3)
				print 'i4" '+str(i4)
				print 'i5'+str(i5)
				print str(x1)+':'+str(x)

z=float(x+0.05-(0.0036*92.7))
def zuoshang():
	for i1 in list_a:
		i1=float(i1)/10000
		for i2 in list_a:
			i2=float(i2)/10000
			for i3 in list_a:
				i3=float(i3)/10000
				for i4 in list_a:
					i4=float(i4)/10000
					b=z+(240*i1)
					c=b+(i2*72)
					d=c-(30.5*i3)
					e1=d-(i4*274.3)
					e2=z-(0.003*85.7)
					if e1==e2 and c<=298.3:
						global k
						k+=1
						d_0 = d-(i3*49.50)
						d_1 = d_0-(i3*43.9)
						d_2 = d_0-(i4*92.3)
						d_3 = d-(i4*195.6) 
						b_0 = b+(i2*41.14)
						b_1 = b-(i1*38.47)
						b_2 = b_1-(122.32*i1)
						b_3 = z-(0.003*48.4)
						print 'number:'+str(k)+'-------------------------------------------------'
						print 'b: '+str(b)
						print 'c: '+str(c)
						print 'd: '+str(d)
						print 'd_0: '+str(d_0)
						print 'd_1: '+str(d_1)
						print 'd_2: '+str(d_2)
						print 'd_3: '+str(d_3)
						print 'b_0: '+str(b_0)
						print 'b_1: '+str(b_1)
						print 'b_2: '+str(b_2)
						print 'b_3: '+str(b_3)
						print 'z: '+str(z)
						print str('i1: ')+str(i1)
						print str('i2: ')+str(i2)
						print str('i3: ')+str(i3)
						print str('i4: ')+str(i4)
						print 'E: '+str(e1)+':'+str(e2)

if __name__=="__main__":
	x_y()
	#a_()
	#youxia()
	#zuoshang()