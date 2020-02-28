class student:
 
  school = "Michigan";
  def __init__(self,m1,m2,m3):
   self.m1 = m1#instance variable which is use with instance method
   self.m2 = m2
   self.m3 = m3
   
   
  def avg(self):#instant method
   return (self.m1 + self.m2 + self.m3)/3
  
  def get_m1(self):
   return self.m1 
  @classmethod
  def info(cls):#class method
   return cls.school
  @staticmethod
  def smethod():
   print("I am satatic method");
  
    
s1 = student(20,30,40);
s2 = student(30,40,50);

print(s1.avg());
print(s2.avg());
#print(s1.info())
print(student.info())
student.smethod()
#print(s1.get_m1);getter calling
#print(s1.m1):-getter.