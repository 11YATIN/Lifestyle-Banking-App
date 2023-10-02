import mysql.connector
a = mysql.connector.connect(host='localhost',user='root',passwd='sansanwal',database='BANK')
b = a.cursor()
b.execute('create table user_table(banker_id int(4) primary key,username varchar(25) ,password varchar(25) not null )')
