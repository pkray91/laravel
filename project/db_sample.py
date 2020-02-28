from pymysql import *
con = connect(db="demo11",user="root",password="",host="localhost")
cur = con.cursor()

def add():
	id = int(input("Enter Your Id  : "))
	name = input("Enter Your Name  : ")
	age = int(input("Enter Your age  : "))
	cur.execute("insert into register values(%d,'%s',%d)"%(id,name,age))
	con.commit()
	print("Record added")
def show():
	cur.execute("select * from register")
	data = cur.fetchall()
	print("====================================")
	print("ID\tName\tAge")
	print("====================================")
	for x in data:
		print(f"{x[0]}\t{x[1]}\t{x[2]}")
	print("====================================")

def main():
	print("Press 1 To add\tPress 2 to show")
	c = int(input("Enter Any number : "))
	if c==1:
		add()
	elif c==2:
		show()
	else:
		print("Wrong Input")
		main()
		
main()		
con.close()