for i in range(1,6):
	for j in range(1,6):
		if i==1 or j==1 or i==3 and j<=3:
			print('*',end='')
		else:
			print(' ',end='')

		
	print()