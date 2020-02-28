#instant method which is  work with instant var
#class method which is work with class var
#static method ->which not work with class or instant var and 
#work for some difference purpose is callled static metod



class student:
     
  school = "DAV"
  def __init__(self,m1,m2,m3):
   self.m1 = m1
   self.m2 = m2
   self.m3 = m3
   
  def get_m1(self):
  	return self.m1

  @classmethod#decorator
  def get_school(cls):
  	return cls.school
  @staticmethod
  def info():
    print("I am static method and with other things like fectorial and all") 


  def avg(self):#instant method which is work for obj(this is two type accesor method and mutator method)
   return (self.m1 + self.m2 + self.m3)/3
    
s1 = student(20,30,40);
s2 = student(30,40,50);

print(s1.avg());
print(s2.avg());

print(s1.get_school())

s1.info()