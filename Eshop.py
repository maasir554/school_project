#importing the connector :-
import mysql.connector as c;
user = c.connect(host = "localhost", user = 'root', password = "password", database = 'eshop');
if user.is_connected():
    print("you are connected to the databse! \ntype add_customer() to add customer. \nadd_seller() to add seller. \nadd_item() to add an item. ")
    cursor= user.cursor()
#here some tables are created as per the ER diagram.
    cursor.execute('create table if not exists customers(C_ID int(4) NOT NULL PRIMARY KEY,C_NAME varchar(30) NOT NULL,C_PHONE varchar(10) NOT NULL,C_EMAIL varchar(50) NOT NULL,C_PINCODE int,LAST_LOGIN_DATE date,NUMBER_OF_ORDERS int(4))')
    cursor.execute('create table if not exists orders(ORDER_ID int(4) NOT NULL PRIMARY KEY,DATE_PLACED date,DATE_DILEVERED date,AMMOUNT int(3) NOT NULL,ITEM_ID varchar(30) NOT NULL,DELBOY varchar(15),CUSTOMER_ID int(4) NOT NULL,PAYMENT_MODE varchar(10) NOT NULL,O_REVIEWS varchar(100))' )
    cursor.execute('create table if not exists items(ITEM_ID int(4) NOT NULL PRIMARY KEY,ITEM_NAME VARCHAR(30),STOCK INT(3),ITEM_SELLER_ID INT(4),CATAGORY VARCHAR(30),PRICE int(6),DATE_ADDED date,DATE_REMOVED date,DESCRIPTION VARCHAR(100))')
    cursor.execute('create table if not exists sellers(SELLER_ID int(4) NOT NULL PRIMARY KEY,S_NAME varchar(30) NOT NULL,S_PWD int(8) NOT NULL,S_MOBILE varchar(10) NOT NULL,S_ADDRESS varchar(30) NOT NULL,S_EMAIL varchar(30) NOT NULL,S_PINCODE int(10) NOT NULL,S_AADHAR_NUMBER varchar(20) NOT NULL)')
    cursor.execute('create table if not exists delboy(D_ID int(4) NOT NULL PRIMARY KEY,D_AADHAR_NUMBER varchar(10),D_NAME varchar(30),D_MOBILE varchar(10),D_ADDRESS varchar(30),D_EMAIL varchar(30),D_PINCODE int(10),DATE_JOINED date,DATE_LEAVING date)')
    cursor.execute('create table if not exists reviews_and_ratings(REVIEW_ID int(4) NOT NULL PRIMARY KEY, SUBJECT varchar(10),R_ITEM_ID int(4),R_ORDER_ID int(4),R_DATE date,RATING int(1),REVIEW varchar(100))')
    cursor.execute('create table if not exists issues_and_complaints(COMP_ID INT(4) NOT NULL PRIMARY KEY,COMP_DATE DATE,COMP_SUBJECT VARCHAR(20),COMP_DESCRIPTION VARCHAR(100))')
    def add_customer():
        c_id = str(input("customer ID : "))
        c_n = str(input("name : "))
        c_ph = int(input("phone number : "))
        c_e = str(input("email : "))
        c_pin = int(input("pincode : "))
        c_lld = input("Last Login Date : ")
        c_noo = input("Number Of orders Made till Now : ")
        c_data = (c_id,c_n,c_ph,c_e,c_pin,c_lld,c_noo)
        c_statement  = "insert into customers values(%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(c_statement,c_data) 
        user.commit()
        print("Data entered successfully!")
    def add_seller():
        s_id = int(input("seller ID : "))
        s_n = str(input("name : "))
        s_pwd = int(input("PASSWORD : "))
        s_mob = str(input("contact number : "))
        s_adr = str(input("Address : "))
        s_e = input("Email : ")
        s_pin = str(input("Pincode : "))
        s_adh  = str(input("Aadhar card no. : "))
        s_data = (s_id,s_n,s_pwd,s_mob,s_adr,s_e,s_pin,s_adh)
        s_statement  = "insert into sellers values(%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(s_statement,s_data) 
        user.commit()
        print("Data entered successfully!")
    def add_item() :
        i_id = input("ITEM ID : ")
        i_n = input("NAME : ")
        i_stk = input("STOCK LEFT : ")
        i_sell = input("SELLER_ID : ")
        i_cat = input("CATAGORY : ")
        i_pri = input("PRICE : ")
        i_dad = input("DATE ADDED : ")
        i_drm = input("DATE REMOVED : ")
        i_des = input("DESCRIPTION : ")
        i_data = (i_id,i_n,i_stk,i_sell,i_cat,i_pri,i_dad,i_drm,i_des)
        i_statement  = "insert into items values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(i_statement,i_data) 
        user.commit()
        print("Data entered successfully!")
else:
    print("errror in connection.")

