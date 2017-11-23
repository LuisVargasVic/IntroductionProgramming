def findthrees(list):
    sum=0
    for x in range(0,len(list)):
        if(list[x]%3==0):
            sum+=list[x]
    return(sum)


a = int(input("Give me a number: "))
b = int(input("Give me a number: "))
c = int(input("Give me a number: "))
d = int(input("Give me a number: "))
e = int(input("Give me a number: "))
f = int(input("Give me a number: "))
g = int(input("Give me a number: "))
h = int(input("Give me a number: "))

list=[a,b,c,d,e,f,g,h]

print("The list is: ",list)

print("The sum of all the numbers divisible by 3 in your list is: ",findthrees(list))
