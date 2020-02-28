a = int(input("Enter a number "))

for x in range(1,11):
	txt = '{} X {}='
	print(txt.format(a,x),x*a)

#print(txt.format(a))