doc=open("93cars.dat.txt","r")
gmac=0
gmah=0
mrp=0
cars=0
f=1
for line in doc:
    if f%2==1:
        gmac=gmac+float(line[52:54])
        gmah=gmah+float(line[55:57])
        mrp=mrp+float(line[42:46])
        cars=cars+1
    f=f+1
x=round(gmac/cars,6)
y=round(gmah/cars,6)
z=round(mrp/cars,6)

print("Average gas mileage in city (City MPG): ", x)
print("Average gas mileage on highway (Highway MPG): ",y)
print("Average midrange price of the vehicles: ",z)
