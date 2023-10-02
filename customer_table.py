import mysql.connector
a = mysql.connector.connect(host='localhost', user='root', passwd='sansanwal', database='BANK')
if a.is_connected():
    print("CONNECTED SUCCESSFULLY")
b = a.cursor()
b.execute('create table customer_details(acct_no int primary key,acct_name varchar(25) ,phone_no bigint(15),address varchar(45),cr_amt float)')
