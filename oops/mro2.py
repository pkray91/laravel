class A:
 
 def __init__(self):
  print("I am constructor A")
  
 def feature1(self):
  print("I am featire 1")
	 
 def feature2(self):
  print("I am featire 2")
	  
	  
class B:#mro(method resolution order)

 def __init__(self):
  super().__init__();
  print("I am constructor B")
  
 def feature3(self):
  print("I am featire 3")
	 
 def feature4(self):
  print("I am featire 4")

class C(A,B):#mro(method resolution order)

 def __init__(self):
  super().__init__();#left to and print A
  print("I am constructor C")
  
 def feature5(self):
  print("I am featire 5")
	 
 def feature6(self):
  print("I am featire 6")
 

 def test():
  super().feature1()
obj = C();

obj.feature3();


