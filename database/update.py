import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",passwd="",database="python_db");

mycur = con.cursor();

query="update employee set name='sunil' where id=9";

mycur.execute(query);
con.commit();
print('updated');