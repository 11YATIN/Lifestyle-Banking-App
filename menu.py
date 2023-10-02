def menu():
    f = open("acct_no.txt", "r")
    g = open("acct_no.txt", "a")
    import random
    import datetime as d
    import mysql.connector
    a = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'sansanwal', database = 'BANK')
    b = a.cursor()

    a.autocommit = True
    flag = True
    while flag:
        print("==========================================================================================================")
        print("Please choose a valid option from below:")
        print('1.CREATE BANK ACCOUNT')
        print('2.TRANSACTION')
        print('3.CUSTOMER DETAILS')
        print('4.DELETE ACCOUNT')
        print('5.QUIT')
        n = int(input('Your choice: '))

        if n == 1:
            f = open("acct_no.txt", "r")
            o = []
            z = f.readline()
            spl = z.split()
            for i in spl:
                o.append(i)
            acc_no = random.choice(o)
            f.close()
            g = open("acct_no.txt", "w")
            for j in o:
                if acc_no == j:
                    continue
                else:
                    g.write(j + " ")
            g.close()

            acc_name = input('Enter the account name: ')
            ph_no = int(input('Enter the phone number: '))
            add = input('Enter the address: ')
            print()
            print("==========================================================================================================")
            print()
            print("1.Please check all the details again.")
            print("2.If details are correct press c. By pressing c you accept our terms and conditions ",end = "")
            print("and you will be held responsible for any wrong information.")
            print("3.Press q to make account again.")
            print()
            print("ACCOUNT NUMBER: ",acc_no)
            print("ACCOUNT NAME: ", acc_name)
            print("PHONE NUMBER: ", ph_no)
            print("ADDRESS:", add)
            print()
            z = input("your response: ")
            if z.capitalize() == "C":
                cr_amt = int(input('Enter your credit amount: '))
                b.execute("INSERT  INTO customer_details values ('" + str(acc_no) + "','" + acc_name + "','" + str(ph_no) + "','" + add + "','" + str(cr_amt) + "')")
                print()
                print('Account Created Successfully!!')
                a.commit()

            elif z.capitalize() == "Q":
                menu()

        elif n == 5:
            flag = False
            print('THANK YOU PLEASE VISIT AGAIN !!')
            print("==========================================================================================================")

        else:
            acct_no = int(input("Enter Your Account Number: "))
            acc_name = input('Enter the account name: ')
            b.execute('select * from customer_details where acct_no = "' + str(acct_no) + '" and acct_name = "' + str(acc_name) + '"')
            b.fetchall()
            count = b.rowcount
            a.commit()

            if count == 0:
                print()
                print("ERROR!!!")
                print('INVALID ACCOUNT NUMBER OR ACCOUNT NAME')

            else:
                if n == 2:
                    print()
                    print("Please choose an option from below: ")
                    print('1.WITHDRAW AMOUNT')
                    print('2.ADD AMOUNT')
                    x = int(input('Your choice: '))
                    print("==========================================================================================================")
                    if x == 1:
                        banner = True
                        while banner:
                            amt = int(input('Enter withdrawal amount: '))
                            b.execute('select * from customer_details where acct_no = "' + str(acct_no) + '"')
                            data = b.fetchall()
                            for row in data:
                                cr_amt = row[4]
                            if amt < cr_amt:
                                b.execute('update customer_details set cr_amt = cr_amt - "' + str(amt) + '"  where acct_no = "' + str(acct_no) + '"')
                                print()
                                print("Account Updated Successfully!!!")
                                banner = False
                            elif amt > cr_amt:
                                print("Insufficient Balance")

                    if x == 2:
                        amt = int(input('Enter amount to be added: '))
                        b.execute('update customer_details set  cr_amt = cr_amt +"' + str(amt) + '" where acct_no= "' + str(acct_no) + '" ')

                        print('Account Updated Successfully!!!!!')


                elif n == 3:
                    print()
                    print("==========================================================================================================")
                    b.execute('select * from customer_details where acct_no=' + str(acct_no))
                    if b.fetchone() is None:
                        print()
                        print('Invalid Account number')
                    else:
                        b.execute('select * from customer_details where acct_no = "' + str(acct_no) + '"')
                        data = b.fetchall()
                        for row in data:
                            print('ACCOUNT NUMBER:', acct_no)
                            print('ACCOUNT NAME:', row[1])
                            print('PHONE NUMBER:', row[2])
                            print('ADDRESS:', row[3])
                            print('BALANCE:', row[4])



                elif n == 4:
                    print()
                    print('DELETE YOUR ACCOUNT')
                    print("Are you sure you want to delete account!!")
                    acct_no = int(input('Enter your account number again: '))
                    b.execute('delete from customer_details where acct_no=' + str(acct_no))
                    print('ACCOUNT DELETED SUCCESSFULLY!!')

