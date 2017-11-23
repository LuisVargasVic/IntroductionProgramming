def findthrees(list):
    sum=0
    for x in range(0,len(list)):
        if(list[x]%3==0):
            sum+=list[x]
    return(sum)

list=[0,4,2,6,9,8,3,12]

print("The list is: ",list)

print("The sum of the numbers of the list divisible by three is: ",findthrees(list))
