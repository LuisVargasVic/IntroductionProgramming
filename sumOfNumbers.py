#Luis Eduardo Vargas Victoria A01630086
res = 0
num1 = int(input("Give me the lower bound: "))
num2 = int(input("Give me the upper bound: "))
while num1 > num2:
    print ("User input error, please give the numbers again.")
    num1 = int(input("Give me the lower bound: "))
    num2 = int(input("Give me the upper bound: "))
while num1 < num2 :
    res = res + num1
    num1  = num1 + 1
res = res + num1
print ("The sum from the lowe bound to" ,num2, "is",res)
