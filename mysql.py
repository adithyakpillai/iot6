#!/usr/bin/python3
# Install python pip if you dont have. 
# sudo apt install python3-pip
# once pip is installed, install python-mysql connector
# pip3 install pymysql
# Note: apt is the repository for linux(ubuntu) apps, pip/pip3 is the repository for python apps.
# pymysql is a python library to execute SQL commands.
#Create a database using mysql cli
#login to mysql --> mysql -u <username> -p
#give your password
#once logged in create a new database --> CREATE DATABASE ab1;
#after this step, you can use python to execute data read and write to table
import pymysql
conn =pymysql.connect(database="User",user="admin",password="password",host="localhost")
cur=conn.cursor()
#create database
#cur.execute("CREATE TABLE users(id int primary, name text, age int, gender text, address text);")
#to store user data
uid = 3
name = "yellari"
age = 22
city = "hyd"
state= "telengana"
data={'userID':uid,'username':name,'userage':age, 'usercity':city,'userstate':state}
print(data)
# Saving data to DB
cur.execute("INSERT INTO Userdata (username, userage, usercity, Userstate) VALUES (%(username)s,%(userage)s,%(usercity)s,%(userstate)s);",data)
conn.commit()
print("saved to db")

