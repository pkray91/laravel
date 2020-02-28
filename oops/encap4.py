class demoClass:

	__empid = 200

	def setid(self,eid):
		self.__empid = eid
	
	def getid(self):
		print(self.__empid)



obj = demoClass()


#obj.setid(3)
obj.getid()