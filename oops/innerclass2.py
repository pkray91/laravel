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
  
  def show(self):
   print(self.ram,self.cpu,self.brand)
  
  
s1 = demo('pappu','2')

lap1= demo.Laptop();
lap1.show();
s1.show();
#print(lap1.ram)
#print(lap1.cpu)
#print(lap1.brand)