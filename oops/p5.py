class demo:
     
 def feature1(self):
  print("I am featire 1")
	 
 def feature2(self):
  print("I am featire 2")
	  
	  
class semo:

 def feature3(self):
  print("I am featire 3")
	 
 def feature4(self):
  print("I am featire 4")
  
class lemo(demo,semo):

 def feature5(self):
  print("I am featire 5")
	 
 def feature6(self):
  print("I am featire 6")
	  
obj1 = demo();
obj1.feature1();
obj1.feature2();

obj2 = lemo()

obj2.feature3();
obj2.feature4();
obj2.feature5();
obj2.feature6();