class demo:
  
 def __init__(self,name,roll_no):
   self.name = name
   self.roll_no = roll_no
   self.lap = self.Laptop()
	
 def show(self):
  print(self.name,self.roll_no)
  
 class Laptop:
   
  def __init__(self):
   self.ram = 8
   self.cpu = 'i7'
   self.brand='lenovo'
  
  
s1 = demo('pappu','2')
lap1 = s1.lap
lap2 = s1.lap;
print(id(lap1));
print(id(lap2));
s1.show()
#print(s1.name,s1.roll_no);