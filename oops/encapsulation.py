class car:
 
 def __init__(self,color,speed):
  
  self.__speed = speed
  self.__color = color
  
  
 # def set_speed(self,value):
 #  self.__speed = value

 # def get_speed(self):
 #  return self.__speed

 # def set_color(self,value):
 #  self.__color = value

 # def get_color(self):
 #  return self.__color  

ford = car('red',200);
honda = car('green',300);
audi = car('blue',400);

ford.set_speed(500);
ford.set_color('purole');
ford.__speed=600;
print(ford.get_speed())
print(ford.get_color())