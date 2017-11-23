def calculate_e(precision):
    x=1
    y=0
    a=0
    b=1
    while (y<=precision):
        y=y+1
        a=1/(y*b)
        x=x+a
        b=y*b
    x=str(x)
    res=x[:x.find(".")+precision+1]
    return res

print("This program calculates the mathematical constant 'e'")
dec=int(input("How many decimal places you want to be displayed?: "))
e=calculate_e(dec)
print(e)
