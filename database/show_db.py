import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",passwd="");

mycur= con.cursor();

query= mycur.execute("show databases");

#result = mycur.fetchall()


for x in mycur:
 print(x)