import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",passwd="",database="python_db");

mycur = con.cursor();

query="select * from employee where name like '%a%'";

mycur.execute(query);
data = mycur.fetchall();

for x in data:
 print(x);