n=int(input("Число: "))

x=0
y=1
while n>0:
	z=n%10
	x=x+z
	y=y*z
	n=n//10


print ("Сумма: ",x)