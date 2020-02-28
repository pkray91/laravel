class A:
 model='abc';
 volume=2
 
 def abc(self):
  print("I am from class A")
 
 
class B(A):
 model1='xyz';
 volume=4
 def axz(self):
  print("I am from class B")
 
obj = B();
print(obj.model)
print(obj.volume)
obj.abc();