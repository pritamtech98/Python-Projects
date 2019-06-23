from cmsplfl import *
import os
import pickle

while(1):
    try:
        file_name = input("Enter the name of your file: ")
        f=open(os.path.join(os.getcwd(), file_name+'.txt'), 'rb+')
        Customer.custList=pickle.load(f)
        f.close()
        break
    except Exception:
        print("file not found!")
        continue


while(1):
    print("1. To add Customer")
    print("2. To delete Customer")
    print("3. To modify Customer")
    print("4. To search Customer")
    print("5. To display all Customer")
    print("6. Exit")
    try:
        choice=int(input("Enter your choice"))
    except ValueError:
        print("Enter choice in numbers only")
        continue
    if(choice==1):
        cust=Customer()
        while (1):
            password = input("Enter your password")
            space = password.split(" ")
            if (len(space) > 1):
                print("No space is allowed!Try again")
                continue

            elif (len(password) == 0):
                print("Length of password cannot be null!! Try again")
                continue

            else:
                cust.custPassword=password
                break

        while (1):
            id = input("Enter your Id")
            space = id.split(" ")
            if (len(space) > 1):
                print("Id cannot have spaces")
                continue
            else:
                cust.custid = id
                break
        while (1):
            name = input("Enter your Name")
            if (name.isnumeric()):
                print("Cannot have numbers into it")
                continue
            else:
                cust.custname = (name.lower()).capitalize()
                break
        while(1):
            try:
                cust.custage=int(input("Enter your age"))
                break
            except ValueError:
                print("Enter your age in numbers only")
                continue

        while (1):
            mob = input("Enter your mobile number")

            if ((str(mob)).isnumeric()):
                if (len(str(mob)) != 10):
                    print("Mobile number can have only 10 digits")
                    print("Try Again")
                    continue

                else:
                    cust.custmob = int(mob)
                    break
            else:
                print("Number cannot be else than numeric")
                continue

        cust.addCustomer()

    elif(choice==2):
        while(1):
            while (1):
                id = input("Enter the id to be deleted")
                space = id.split(" ")
                if (len(space) > 1):
                    print("Id cannot have spaces")
                    continue
                else:
                    val = Customer().deleteCustomer(id)
                    break
            if (val == 0):
                print("Id not found")
                ch = input("Want to continue! Y/N")
                if (ch.lower() == 'n'):
                    break
                else:
                    continue
            else:
                print("Account successfully deleted")
                break

    elif(choice==3):

        while(1):
            id = input("Enter the id to be modified")
            print("1. Enter 1 to modify id")
            print("2. Enter 2 to modify name")
            print("3. Enter 3 to modify age")
            print("4. Enter 4 to modify mobile number")
            print("5. Enter 5 to modify password")
            ch=input("Enter your choice")
            if(ch=='1'):
                while (1):
                    idnew = input("Enter your new id")
                    space = idnew.split(" ")
                    if (len(space) > 1):
                        print("Id cannot have spaces")
                        continue
                    else:
                        val = Customer().modifyCustomer(id, idnew, 1)
                        break

            elif(ch == '2'):
                while (1):
                    namenew = input("Enter your new name")
                    if (namenew.isnumeric()):
                        print("Cannot have numbers into it")
                        continue
                    else:
                        val = Customer().modifyCustomer(id, (namenew.lower()).capitalize(), 2)
                        break

            elif(ch == '3'):
                while (1):
                    try:
                        agenew = int(input("Enter your new age"))
                        break
                    except ValueError:
                        print("Enter your age in numbers only")
                        continue
                val = Customer().modifyCustomer(id, int(agenew), 3)

            elif (ch == '4'):
                while (1):
                    mobnew = input("Enter your new mobile number")

                    if ((str(mobnew)).isnumeric()):
                        if (len(str(mobnew)) != 10):
                            print("Mobile number can have only 10 digits")
                            print("Try Again")
                            continue

                        else:
                            val = Customer().modifyCustomer(id, int(mobnew), 4)
                            break
                    else:
                        print("Number cannot be else than numeric")
                        continue

            elif(ch=='5'):
                passnew = input("Enter your new password")
                val = Customer().modifyCustomer(id, passnew, 5)
            else:
                print("invalid choice")
                continue

            if (val == 0):
                print("Id not found")
                ch = input("Want to continue! Y/N")
                if (ch.lower() == 'n'):
                    break
                else:
                    continue
            else:
                print("Account successfully modified")
                break

    elif(choice==4):
        print("1. to search by id")
        print("2. to search by name")
        print("3. to search by mobile")
        ch=input("Enter your choice")
        if(ch=='1'):
            id = input("Enter the id to be searched")
            data=Customer().searchCustomer(id, 1)
        elif (ch == '2'):
            name = input("Enter the name to be searched")
            data = Customer().searchCustomer((name.lower()).capitalize(), 2)
        else:
            while (1):
                mob = input("Enter the mobile to be searched")

                if ((str(mob)).isnumeric()):
                    if (len(str(mob)) != 10):
                        print("Mobile number can have only 10 digits")
                        print("Try Again")
                        continue

                    else:
                        data = Customer().searchCustomer(int(mob), 3)
                        break
                else:
                    print("Number cannot be else than numeric")
                    continue


        if(len(data)==0):
            print("Value not found")
        else:
            print("Customer Id\tCustomerName\tCustomerAge\tCustomerMobile\tCustomerPassword")
            for el in data:
                print(el, end='\t\t')
            print()


    elif(choice==5):
        cust=Customer()
        data=cust.displayAll()
        for el in data:
            print('CustomerId: ', el.custid)
            print('CustomerName: ', el.custname)
            print('CustomerAge: ', el.custage)
            print('CustomerMobile: ', el.custmob)
            print('CustomerPassword: ', el.custPassword)
        print()


    elif(choice==6):
        print("Thanks for visit")
        try:
            f=open(file_name+'.txt', 'wb+')
            pickle.dump(Customer.custList, f)
        except Exception:
            pass
        finally:
            f.close()
        break

