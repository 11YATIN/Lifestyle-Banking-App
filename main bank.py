import menu
import mysql.connector
a = mysql.connector.connect(host='localhost',user='root',passwd='sansanwal',database='BANK')
b = a.cursor()
#cur.execute('create table user_table(username varchar(25) primary key,passwrd varchar(25) not null )')
print("====================================WELCOME TO LIFESTYLE BANK=============================================")
print("                                   Your Security!! Our Priority")
import datetime as d
print(d.datetime.now())
print("Please choose a valid option from below!")
print("1.REGISTER")
print("2.LOGIN")
print()
n = int(input("Enter your response: "))
print()

if n== 1:
     print("NOTE: Banker id is the 4 digit number that you received when you got this job.")
     banker_id = int(input("banker id: "))
     name = input("Enter a Username: ")
     password = int(input("Enter a 4 DIGIT Password: "))
     print()
     q = "INSERT INTO user_table(banker_id,username,password) values('"+ str(banker_id) + "','"+ name + "', '" + str(password) + "')"
     b.execute(q)
     a.commit()
     print('User created succesfully')


if n == 2:
     banker_id = int(input("Enter banker_id: "))
     name = input("Enter your Username: ")
     password=int(input("Enter your 4 DIGIT Password: "))
     b.execute("select * from user_table where password='"+str (password)+"' and banker_id=  '" +str(banker_id)+ "' ")
     if b.fetchone() is None:
          print()
          print('Invalid username or password')
     else:
          print("Welcome back", name,"Nice to see you again")

menu.menu()

