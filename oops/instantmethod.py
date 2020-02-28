#instant method
#class method
#static method



class student:
 
 
  def __init__(self,m1,m2,m3):
   self.m1 = m1
   self.m2 = m2
   self.m3 = m3
   
  def get_m1(self):
  	return self.m1

  def set_m1(self,value):
  	return self.m1 = value 


  def avg(self):#instant method which is work for obj(this is two type accesor method and mutator method)
   return (self.m1 + self.m2 + self.m3)/3
    
s1 = student(20,30,40);
s2 = student(30,40,50);

print(s1.avg());
print(s2.avg());



print(s1.get_m1());
print(s1.set_m1());