import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",passwd="",database="python_db");

mycur = con.cursor();

query="create table employee(id int(11) auto_increment unique,name varchar(30),email varchar(30) primary key)";


mycur.execute(query);