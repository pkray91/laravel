def sum(a,*b):
	c = a
	for x in b:
		c = c+x
		#print(c)
	print(c)
sum(2,2,3,4,5)