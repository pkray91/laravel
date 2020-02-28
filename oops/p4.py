class demo:
     
 def feature1(self):
  print("I am featire 1")
	 
 def feature2(self):
  print("I am featire 2")
	  
	  
class semo(demo):

 def feature3(self):
  print("I am featire 3")
	 
 def feature4(self):
  print("I am featire 4")
	  
obj1 = demo();
obj1.feature1();
obj1.feature2();

obj2 = semo()

obj2.feature1();
obj2.feature2();
obj2.feature3();
obj2.feature4();