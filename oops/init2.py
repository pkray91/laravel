
class TV:

 def __init__(self,model,volume):
  self.model= model
  self.volume= volume
  print(self.model,self.volume);
 
 def config(self):
   print('model and volume is', self.model,self.volume);
   
   
obj = TV('sm-3222',4);
obj1 = TV('Lg-5555',1);


obj.config()
obj1.config();
