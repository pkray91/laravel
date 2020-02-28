try:
 print(x)
except NameError:
 print('x is not declaered')
except:
 print('something went wrong')