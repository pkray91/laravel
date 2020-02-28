for i in range(1,6):
	for j in range(1,6):
		if (j==3 and i>=3) or (i==j and i<=3) or (i+j==6 and i<=3):
			print('*',end='')
		else:
			print(' ',end='')

		
	print()