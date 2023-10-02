import mysql.connector
import random

#Customer table
a = mysql.connector.connect(host='localhost', user='root', passwd='sansanwal')
if a.is_connected():
    print("CONNECTED SUCCESSFULLY")
b = a.cursor()
b.execute('create database BANK')
b.execute('use BANK')
b.execute('create table customer_details(acct_no int primary key,acct_name varchar(25) ,phone_no bigint(15),address varchar(45),cr_amt float)')

#user_table
b.execute('create table user_table(banker_id int(4) primary key,username varchar(25) ,password varchar(25) not null )')

#txt file
f = open("acct_no.txt", "w")
for i in range(10000,100000):
    f.write(str(i) + " ")
