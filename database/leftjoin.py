import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",passwd="",database="join");

mycur = con.cursor();

query="select std_acc.name as name,std_lib.name as name from std_acc outer join std_lib on std_acc.name=std_lib.name";

mycur.execute(query);
data = mycur.fetchall();

for x in data:
 print(x);