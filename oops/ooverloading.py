
'''a= 5;
b= 10;

c= '20'
d='50'
print(a+b);

print(int.__add__(a,b));
print(str.__add__(c,d));'''

class student:
 
 def __init__(self,m1,m2):
  self.m1 = m1
  self.m2 = m2
  
 def __add__(self,other):
  m1 = self.m1 + other.m1;
  m2 = self.m2 + other.m2;
  s3 = student(m1,m2);
  return s3;
  
  
s1= student(33,55)
s2= student(44,34)

s3= s1+s2;#(student__add__(s1,s2))it wiil not add because our student dont have the add methode for students.

print(s3.m1);
print(s3.m2);

