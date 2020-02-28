class demoClass:

	__a = 20

	def desp(self):
		print(self.__a)


obj = demoClass()
obj.__a = 30 #change not possible 
obj.desp()
#print(obj.a) not possible with private var
#========================================
# class demoClass:

# 	a = 20

# 	def desp(self):
# 		print(self.a)


# obj = demoClass()
# obj.a = 30
# obj.desp()
# #print(obj.a) not possible with private var