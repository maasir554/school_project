#importing the connector :-
#from distutils.util import execute
import mysql.connector as c
#defining the database :-
#Note: the name of database is Eshop. you have to create database Eshop to run this program.
database = c.connect(host = "localhost", user = 'root', password = "password", database = 'eshop')
#defining cursor(it will be used to excute SQL commands) :-
cursor = database.cursor(buffered=True)
print('You are connected to the server eshop successfully.')
cursor.execute('CREATE TABLE IF NOT EXISTS items(item_id INT(4) PRIMARY KEY NOT NULL,item_name VARCHAR(50),category VARCHAR(30),seller_id INT(4) NOT NULL,price INT(8) NOT NULL,date_added DATE,rating FLOAT(2,1))' )
cursor.execute('CREATE TABLE IF NOT EXISTS customers(customer_id INT(4) PRIMARY KEY NOT NULL,customer_name VARCHAR(30) NOT NULL,customer_age INT(3),gender ENUM("male","female","others"),email VARCHAR(30),mobile VARCHAR(12),city VARCHAR(20))')
cursor.execute('CREATE TABLE IF NOT EXISTS delboy(delboy_id INT(4) PRIMARY KEY NOT NULL,name VARCHAR(30) NOT NULL,city VARCHAR(20),mobile VARCHAR(12),salary INT(4),rating float(2,1))')
cursor.execute('CREATE TABLE IF NOT EXISTS sellers(seller_id INT(4) PRIMARY KEY NOT NULL,name VARCHAR(30) NOT NULL,city VARCHAR(20),mobile VARCHAR(12),email VARCHAR(30),rating float(2,1))')
cursor.execute('CREATE TABLE IF NOT EXISTS orders(order_id INT(4) PRIMARY KEY NOT NULL,item_id INT(4) NOT NULL,customer_id INT(4) NOT NULL,date_placed DATE,delboy_ID INT(4) NOT NULL)')
cursor.execute('CREATE TABLE IF NOT EXISTS complains(complain_id INT(4) PRIMARY KEY NOT NULL,order_id INT(4) NOT NULL,subject VARCHAR(20) NOT NULL)')

#MAKING THE MENU(USER INTERFACE) FOR FRONT END
def menu():
    print("--- menu opened ---")
    a = int(input("to add data please type : 1 \nto delete data please type : 2 \nto exit this menu, please type 3 \nResponse : "))
    if (a==1):
        b= int(input("type number : \n'1' to add customer data \n'2' to add seller data \n'3' to add item data \n'4' to add order data \n'5' to add delboy data \n'6' to add complain. \nResponse : "))
        if (b==1):
            add_customer()
        elif (b==2):
            add_seller()
        elif (b==3):
            add_item()
        elif (b==4):
            add_order()
        elif (b==5):
            add_delboy()
        elif (b==6):
            add_complain()
        else:
            print('please enter a valid response')
            
    elif (a==2):
        b= int(input("type number : \n'1' to delete customer data \n'2' to delete seller data \n'3' to delete item data \n'4' to delete order data \n'5' to delete delboy data \n'6' to delete complain \nResponse : "))
        if (b==1):
            delete_customer()
        elif (b==2):
            delete_seller()
        elif (b==3):
            delete_item()
        elif (b==4):
            delete_order()
        elif (b==5):
            delete_delboy()
        elif (b==6):
            delete_complain()
        else:
            print('please enter a valid response')
            menu()
    
    elif(a==3):
        print('Thank You! for using this program, Have a nice day! \n you can now exit or call functions manually. \nlist of the functions(prefix add_ OR delete_ before them) : \ncustomer\nseller\nitem\norder\ndelboy\ncomplain\n--- menu closed ---')
    else:
        print('please enter a valid response')
        menu()

#DEFINING FUNCTIONS FOR FEEDING DATA IN THE TABLES OF THE SERVER

def add_customer():
    print("add_customer() function started.")
    c_id = input('enter customer ID  : ')
    name = input('enter customer name : ')
    age = input("enter customer age : ")
    gender = input("enter gender of customer : ")
    email = input('enter customer email ID : ')
    mobile = input('enter customer mobile number : ')
    city = input('enter customer city : ')
    data = (c_id,name,age,gender,email,mobile,city)
    statement = "INSERT INTO customers VALUES(%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(statement,data)
    database.commit()
    print('data inserted to table customer successfully!')
    b = input("do you want ot add more data to THIS table? (y/n) : ")
    if (b=='y'):
        add_customer()
    elif (b=='n'):
        menu()
    else:
        print("please enter a valid response. (you exited the menu. to call back use menu())")

def add_seller():
    print("add_seller() function started.")
    s_id = input('enter seller ID  : ')
    name = input('enter seller name : ')
    city = input('enter seller city : ')
    mobile = input('enter seller mobile number : ')
    email = input('enter seller email ID : ')
    rating = input('enter the rating of seller : ')
    data = (s_id,name,city,mobile,email,rating)
    statement = "INSERT INTO sellers VALUES(%s,%s,%s,%s,%s,%s)"
    cursor.execute(statement,data)
    database.commit()
    print('data inserted to table sellers successfully!')
    b = input("do you want ot add more data to THIS table? (y/n) : ")
    if (b=='y'):
        add_seller()
    elif (b=='n'):
        menu()
    else:
        print("please enter a valid response. (you exited the menu. to call back use menu())")

def add_item():
    print("add_item() function started.")
    item_id = input('enter item ID  : ')
    name = input('enter item name : ')
    cat = input('enter category of item : ')
    sid = input('enter seller_id of item seller : ')
    price = input('enter price of item : ')
    date_added = input('enter date added : ')
    rating = input('enter rating of item : ')
    data = (item_id,name,cat,sid,price,date_added,rating)
    statement = "INSERT INTO items VALUES(%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(statement,data)
    database.commit()
    print('data inserted to table items successfully!')
    b = input("do you want ot add more data to THIS table? (y/n) : ")
    if (b=='y'):
        add_item()
    elif (b=='n'):
        menu()
    else:
        print("please enter a valid response. (you exited the menu. to call back use menu())")

def add_order():
    print("add_order() function started.")
    oid = input('enter order id : ')
    iid = input('enter item id : ')
    cid = input('enter customer id : ')
    dp = input('enter date placed : ')
    dbid = input('enter delivery boy id : ')
    data = (oid,iid,cid,dp,dbid)
    statement = 'insert into orders values(%s,%s,%s,%s,%s)'
    cursor.execute(statement,data)
    database.commit()
    print('data inserted to the table ORDERS successfully!')
    b = input("do you want ot add more data to THIS table? (y/n) : ")
    if (b=='y'):
        add_order()
    elif (b=='n'):
        menu()
    else:
        print("please enter a valid response. (you exited the menu. to call back use menu())")

def add_delboy():
    print("add_delboy() function started.")
    did = input('enter delboy ID  : ')
    name = input('enter delboy name : ')
    city = input('enter delboy city : ')
    mobile = input('enter delboy mobile number : ')
    salary = input('enter delboy salary : ')
    rating = input('enter the rating of delboy : ')
    data = (did,name,city,mobile,salary,rating)
    statement = "INSERT INTO delboy VALUES(%s,%s,%s,%s,%s,%s)"
    cursor.execute(statement,data)
    database.commit()
    print('data inserted to table delboy successfully!')
    b = input("do you want ot add more data to THIS table? (y/n) : ")
    if (b=='y'):
        add_delboy()
    elif (b=='n'):
        menu()
    else:
        print("please enter a valid response. (you exited the menu. to call back use menu())")

def add_complain():
    print("add_complain() function started.")
    cid = input("enter complain ID : ")
    oid = input("enter order id : ")
    sub = input("enter the subject of complain : ")
    data = (cid,oid,sub)
    statement = "INSERT INTO COMPLAINS VALUES(%s,%s,%s)"
    cursor.execute(statement,data)
    database.commit()
    print("data inserted to the table COMPLAINS successfully!")
    b = input("do you want ot add more data to THIS table? (y/n) : ")
    if (b=='y'):
        add_complain()
    elif (b=='n'):
        menu()
    else:
        print("please enter a valid response. (you exited the menu. toa call back use menu())")

#DEFINING FUNCTIONS TO DELETE DATA FROM TABLES OF DATABASE :-
def delete_customer():
    print("delete_customer() function started.")
    cid = input('enter customer_id : ')
    cursor.execute('DELETE FROM customers WHERE customer_id=%s',(cid,))
    database.commit()
    print('deleted the customer data of customer_id : ',cid,'from table customers successfully!')
    b = input("do you want ot delete more data to THIS table? (y/n) : ")
    if (b=='y'):
        delete_customer()
    elif (b=='n'):
        menu()
    else:
        print("please enter a valid response. (you exited the menu. to call back use menu())")

def delete_seller():
    print("delete_seller() function started.")
    sid = input('enter seller_id : ')
    cursor.execute('DELETE FROM sellers WHERE seller_id=%s',(sid,))
    database.commit()
    print('deleted the seller data of seller_id : ',sid,' from table sellers successfully!')
    b = input("do you want ot delete more data to THIS table? (y/n) : ")
    if (b=='y'):
        delete_seller()
    elif (b=='n'):
        menu()
    else:
        print("please enter a valid response. (you exited the menu. to call back, use menu())")

def delete_item():
    print("delete_item() function started.")
    iid = input('enter item_id : ')
    cursor.execute('DELETE FROM items WHERE item_id=%s',(iid,))
    database.commit()
    print('deleted the item data of item_id : ',iid,' from table items successfully!')
    b = input("do you want ot delete more data to THIS table? (y/n) : ")
    if (b=='y'):
        delete_item()
    elif (b=='n'):
        menu()
    else:
        print("please enter a valid response. (you exited the menu. to call back, use menu())")

def delete_order():
    print("delete_order() function started.")
    x = input('enter order_id : ')
    cursor.execute('DELETE FROM orders WHERE order_id=%s',(x,))
    database.commit()
    print('deleted the item data of order_id : ',x,' from table orders successfully!')
    b = input("do you want ot delete more data to THIS table? (y/n) : ")
    if (b=='y'):
        delete_order()
    elif (b=='n'):
        menu()
    else:
        print("please enter a valid response. (you exited the menu. to call back, use menu())")

def delete_delboy():
    print("delete_delboy() function started.")
    x = input('enter delboy_id : ')
    cursor.execute('DELETE FROM delboy WHERE delboy_id=%s',(x,))
    database.commit()
    print('deleted the data of delboy_id ',x,' from table delboy successfully!')
    b = input("do you want ot delete more data to THIS table? (y/n) : ")
    if (b=='y'):
        delete_delboy()
    elif (b=='n'):
        menu()
    else:
        print("please enter a valid response. (you exited the menu. to call back, use menu())")

def delete_complain():
    print("delete_complain() function started.")
    x = input('enter complain_id : ')
    cursor.execute('DELETE FROM complains WHERE complain_id=%s',(x,))
    database.commit()
    print('deleted the data of complain_id ',x,' from table complains successfully!')
    b = input("do you want ot delete more data to THIS table? (y/n) : ")
    if (b=='y'):
        delete_complain()
    elif (b=='n'):
        menu()
    else:
        print("please enter a valid response. (you exited the menu. to call back, use menu())")

#FINALLY, SERVING THE PROGRAM TO USER : -

print("* * * * * * * WELCOME TO THE DATABASE MANAGEMENT USER INTERFACE OF ESHOP * * * * * * *") 
print("(created by Mohammad Maasir @ date 13th Feb,2022, as a school project.)") 
menu()
"""
although this program have a menu, we can also call the functions defined here to 
add or delete data when this program is running in the IDLE shell, manually (when you are outside menu i.e. exit the menu.)









**************************************** END OF THE CODE ****************************************************
"""
