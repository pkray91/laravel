import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",passwd="",database="python_db");

mycur = con.cursor();

query="select * from employee order by name limit 1,2";

mycur.execute(query);
data = mycur.fetchall();

for x in data:
 print(x);