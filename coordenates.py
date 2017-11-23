import math
def distance(a,b,c,d):
	r1= c - a
	r2= d - b
	r1= r1*r1
	r2= r2*r2
	r3= r1+r2
	r= math.sqrt(r3)
	return r

x1= int(input("Give me x1: "))
y1= int(input("Give me y1: "))
x2= int(input("Give me x2: "))
y2= int(input("Give me y2: "))
c= distance(x1,y1,x2,y2)
print(c)
