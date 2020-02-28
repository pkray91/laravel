import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",passwd="",database="join");

mycur = con.cursor();

query="select * from std_acc inner join std_lib on std_acc.name=std_lib.name";

mycur.execute(query);
data = mycur.fetchall();

for x in data:
 print(x);