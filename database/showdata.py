import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",passwd="",database="python_db");

mycur = con.cursor();


mycur.execute("select * from employee");

data=mycur.fetchall();

for x in data:

 print(x);