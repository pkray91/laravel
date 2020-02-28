class student:
 
	address = "Delhi"#class var or static var
	def __init__(self):
	   self.name = "harshit"#instant var
	   self.email = "h@gmail.com"
	   self.mobile = 9898777898

obj1 = student()
obj2 = student()

print(obj1.name,student.address)
print(obj1.name,obj1.address)
print(obj2.name)

obj1.name="Mohan"

student.address="noida"
#obj1.address="noida"

print(obj1.name,student.address)
print(obj1.name,obj1.address)
print(obj2.name)