#Luis Eduardo Vargas Victoria
f=int(input("Give me the temperature in Farenheit that you want to convert to Celsius: "))
c= 5*(f-32)/9
print("The temperature in Celsius is: ", int(c))
if c>=100: 
  print ("Water boils at this temperature.")
else:
   print ("Water doesn't boil at this temperature.")