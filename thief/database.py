import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Project")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Project"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Criminal (Criminal_Id INT PRIMARY KEY, Fname VARCHAR(255),Lname VARCHAR(255),Age INT(10),Crime_date VARCHAR(20),Thana VARCHAR(200),District VARCHAR(100),State VARCHAR(20),Crime_type VARCHAR(30),Image VARCHAR(200))")
mydb.close()
