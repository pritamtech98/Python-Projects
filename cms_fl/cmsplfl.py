
class Customer:

    custList=[]
    def __init__(self):
        self.custid=''
        self.custname=''
        self.custage=0
        self.custmob=0
        self.custPassword=''

    def addCustomer(self):
        Customer.custList.append(self)

    def displayAll(self):
        return Customer.custList


    def deleteCustomer(self, id):
        val=0
        for el in Customer.custList:
            if(el.custid==id):
                Customer.custList.remove(el)
                val=1
                return val
        return val

    def modifyCustomer(self, id, val, choice):

        val1=0
        obj=''
        for el in Customer.custList:
            if(el.custid==id):
                val1=1
                obj=el
                break

        if(choice==1 and val1==1):
            obj.custid=val
            return val1
        elif(choice==2 and val1==1):
            obj.custname=val
            return val1
        elif (choice == 3 and val1==1):
            obj.custage = val
            return val1
        elif (choice == 4 and val1==1):
            obj.custmob = val
            return val1
        elif(choice == 5 and val1==1):
            obj.custPassword = val
            return val1
        else:
            return val1

    def searchCustomer(self, val, choice):
        data=['', '', '', '', '']
        if(choice==1):
            for el in Customer.custList:
                if(el.custid==val):
                    data[:]=[]
                    data.append(el.custid)
                    data.append(el.custname)
                    data.append(el.custage)
                    data.append(el.custmob)
                    data.append(el.custPassword)
            return data
        elif (choice == 2):
            for el in Customer.custList:
                if(el.custname==val):
                    data[:]=[]
                    data.append(el.custid)
                    data.append(el.custname)
                    data.append(el.custage)
                    data.append(el.custmob)
                    data.append(el.custPassword)
            return data
        else:
            for el in Customer.custList:
                if(el.custmob==val):
                    data[:]=[]
                    data.append(el.custid)
                    data.append(el.custname)
                    data.append(el.custage)
                    data.append(el.custmob)
                    data.append(el.custPassword)
            return data





