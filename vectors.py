def dotproduct(x,y):
    ab=[]
    for i in range(0,len(x)):
        ab.append(x[i]*y[i])
    return sum(ab)

v1=[2,4,5,6]
v2=[1,2,3,4]

total=dotproduct(v1,v2)

print ("The dot product of this two vector is: ",total)
