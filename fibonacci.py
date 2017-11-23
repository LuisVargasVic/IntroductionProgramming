import sys
def fibonacci(n):
    if(n==0 or n==1):
        return n
    return (fibonacci(n-1)+fibonacci(n-2))

op="y"
while (op == "y"):
    n=input("Give me an integer number: ")
    if(n.isdigit() == False):
        print ("Only integers.")
    else:
        n = int(n)
        fi = fibonacci(n)
        if n < 0:
            print ("Negative numbers are not accepted.")
        else:
            if (n == 0):
                print ("The fibonacci of 0 is 0.")
            else:
                if (n == 1):
                    print ("The fibonacci of 1 is 1.")
                else:
                    print ("The fibonacci of",n,"is",fi,".")
    op=input("Want to try again? (y/n)")
if (op == "n"):
    print ("Have a nice day.")
sys.exit
