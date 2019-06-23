import pymysql
import re
con = pymysql.connect("localhost", "root", " ", "customerdb")
mycursor = con.cursor()

class Customer:
    @staticmethod
    def connection():

        try:
            mycursor.execute("create table customer(custId varchar(30) not null primary key, custName varchar(30), custAge int, custMob bigint, custPassword varchar(40) not null, custPhoto varchar(60));")
        except Exception:
            pass

    adminPassword = "r"
    adminId = "a"

    @staticmethod
    def customer_Verify(password, id, ch):
        if (ch == 1):
            if (password == Customer.adminPassword and id == Customer.adminId):
                return 1
            else:
                return 0
        else:
            mycursor.execute("select * from customer where custId='%s' and custPassword='%s';"%(id, password))
            val = mycursor.fetchall()
            if(len(val)==0):
                return False
            else:
                return val[0]


    def __init__(self):
        self.custId=''
        self.custName=''
        self.custAge=0
        self.custMob=0
        self.custPassword=''
        self.custPhoto=''
    def add_Customer(self):
        p=re.compile("\s")
        m=p.search(self.custId)
        m2=p.search(self.custPassword)
        p2=re.compile("\d{10, 11}")
        m3=p2.match(str(self.custMob))
        mycursor.execute("select custId from customer where custId='%s';"%(self.custId))
        res=mycursor.fetchall()
        if(len(res)>0 ):
            return False
        if(m!=None):
            return 2
        elif(m2!=None):
            return 3
        mycursor.execute("insert into customer values('%s', '%s', %d, %d, '%s', '%s');"%(self.custId, self.custName, self.custAge, self.custMob, self.custPassword, self.custPhoto))
        con.commit()
        return True


    def displayAll(self):
        list=[]
        mycursor.execute("desc customer;")
        data=mycursor.fetchall()
        list.append(data)
        mycursor.execute("select * from customer;")
        data=mycursor.fetchall()
        list.append(data)
        return list

    def delete_Customer(self, id):

        mycursor.execute("delete from customer where custId='%s';" % (id))
        val = mycursor.rowcount
        return val

    def update_Customer(self, id, val, choice):
        if(choice==1):
            mycursor.execute("update customer set custId='%s' where custId='%s';"%(val, id))
            val=mycursor.rowcount
            return val
        elif(choice==2):
            mycursor.execute("update customer set custName='%s' where custId='%s';" % (val, id))
            val = mycursor.rowcount
            return val
        elif (choice == 3):
            mycursor.execute("update customer set custAge=%d where custId='%s';" % (val, id))
            val = mycursor.rowcount
            return val
        elif (choice == 4):
            mycursor.execute("update customer set custMob=%d where custId='%s';" % (val, id))
            val = mycursor.rowcount
            return val
        else:
            mycursor.execute("update customer set custPassword='%s' where custId='%s';" % (val, id))
            val = mycursor.rowcount
            return val

    def search_Customer(self, val, choice):
        if(choice == 1):
            mycursor.execute("select * from customer where custId='%s';"%(val))
            data=mycursor.fetchall()
            return data
        elif (choice == 2):
            mycursor.execute("select * from customer where custName='%s';" %(val))
            data = mycursor.fetchall()
            return data
        else:
            mycursor.execute("select * from customer where custMob=%d;" %(val))
            data = mycursor.fetchall()
            return data





