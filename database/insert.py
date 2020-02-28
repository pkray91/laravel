import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",passwd="",database="python_db");

mycur = con.cursor();

query="insert into employee(name,email) values(%s,%s)";

val= ('mohan','moss@gmail.com')

mycur.execute(query,val);

con.commit();
print("data inserted");