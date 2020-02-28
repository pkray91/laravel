import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",passwd="",database="python_db");

mycur = con.cursor();

query="select * from employee where name like %s";
val =('mohan',);
mycur.execute(query,val);

data = mycur.fetchall();

for x in data:
 print(x);