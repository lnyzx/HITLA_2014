
a=float(297.0752)
list_a=range(3,31)
x=float(298.8)

def a_():
	for i1 in list_a:
		i1=float(i1)/1000
		for i2 in list_a:
			i2=float(i2)/1000
			for i3 in list_a:
				i3=float(i3)/1000
				for i4 in list_a:
					i4=float(i4)/1000
					b=a-(33.3*i1)
					c=b+(119.5*i2)
					d=c-(90*i3)
					a1=d-(45*i4)
					if a==a1:
						print str(a)+':'+str(a1)
						print i1
						print i2
						print i3
						print i4

def youxia():
	for i1 in list_a:
		i1=float(i1)/1000
		for i2 in list_a:
			i2=float(i2)/1000
			for i3 in list_a:
				i3=float(i3)/1000
				b=a-(26.4*i1)
				c=b-(147.3*i2)
				x1=c+(109.5*i3)
				if abs(x1-x)<0.0009:
					print i1
					print i2
					print i3
					print str(x1)+':'+str(x)


if __name__=="__main__":
	youxia()
	#a_()