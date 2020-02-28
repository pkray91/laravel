
num = int(input("Enter a number:-"))

for x in range(2,num):
	if(num%x==0):
		print('not prime')
		break
else:
	print('number is prime')