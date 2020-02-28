import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",passwd="",database="python_db");

mycur = con.cursor();

query="delete from employee where id=4";

mycur.execute(query);
con.commit();
print('deleted');