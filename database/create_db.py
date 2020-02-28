import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",passwd="");

mycur= con.cursor();

query= mycur.execute("create database python_db");

print("created");