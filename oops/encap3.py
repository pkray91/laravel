class demoClass:

	def __test1(self):
		print("I am test 1 function")

	def test2(self):
		print("I am test 2 function")
		a = 20
		b = 30
		c = a+b
		print(c)
		self.__test1()


obj = demoClass()
#obj.__test1()not possible becuse of private function
obj.test2()