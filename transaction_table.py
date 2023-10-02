import mysql.connector
a = mysql.connector.connect(host='localhost',user='root',passwd='sansanwal',database='BANK')
b = a.cursor()
b.execute('create table transactions(acct_no int(11),date date ,withdrawal_amt bigint(20),amount_added bigint(20) )')
