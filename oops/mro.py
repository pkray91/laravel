class A:
 
 def __init__(self):
  print("I am constructor A")
  
 def feature1(self):
  print("I am featire 1")
	 
 def feature2(self):
  print("I am featire 2")
	  
	  
class B(A):#mro(method resolution order)

 def __init__(self):
  super().__init__();
  print("I am constructor B")
  
 def feature3(self):
  print("I am featire 3")
	 
 def feature4(self):
  print("I am featire 4")
  
obj = B();


