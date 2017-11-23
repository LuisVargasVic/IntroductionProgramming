def power(x,y):
	c=0
	for c in range(y):
		c= c+1
		a= pow(x,c)
	return a
x = int(input("Give me the number: "))
y = int(input("Give me the power: "))
r = power(x,y)
print(r)
