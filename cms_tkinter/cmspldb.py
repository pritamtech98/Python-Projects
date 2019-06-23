from cmsblldb import *
from tkinter import *
import tkinter.ttk
from tkinter.messagebox import *
import re
import tkinter.filedialog
from PIL import Image, ImageTk
Customer.connection()

class loginForm(Frame):


    def __init__(self, master, widthx, heighty):
        self.master=master
        super().__init__(master)
        master.title("Login")
        master.minsize(widthx, heighty)
        self.pack()
        self.config(bg='lightgrey')
        self.createWidget()
        self.counter=0


    def createWidget(self):
        self.lbl_headingframe = Frame(self, bg='lightgrey')
        self.lbl_headingframe.pack()
        self.containerframe=tkinter.ttk.Frame(self)
        self.containerframe.pack(pady=10)
        self.lbl_heading = Label(self.lbl_headingframe, text="Customer Login", font=('Times New Roman', '16' , 'bold', 'italic'), bg='lightgrey', fg='grey')
        self.lbl_heading.pack(pady=10)
        self.lbl_userId=Label(self.containerframe, text="UserID", width=8, padx=3, pady=2)
        self.lbl_Password=Label(self.containerframe, text="Password", width=8, padx=3, pady=2)
        self.var_UserId=StringVar()
        self.entry_userId=tkinter.ttk.Entry(self.containerframe, width=30, textvariable=self.var_UserId)
        self.var_Password=StringVar()
        self.entry_Password=tkinter.ttk.Entry(self.containerframe, width=30, show="*", textvariable=self.var_Password)
        self.var_check_signup=IntVar()
        self.check_signup=tkinter.ttk.Checkbutton(self.containerframe, text="Sigup? New Customer", variable=self.var_check_signup, onvalue=1, offvalue=0)
        self.btn_Submit=tkinter.ttk.Button(self.containerframe, text="Submit", padding=(4))
        self.btn_Submit.bind("<Button-1>", self.action_submit)

        self.lbl_userId.grid(row=0, column=0)
        self.lbl_Password.grid(row=1, column=0)
        self.entry_userId.grid(row=0, column=1, padx=8, pady=15)
        self.entry_Password.grid(row=1, column=1, padx=8)
        self.check_signup.grid(columnspan=2, pady=15)


        self.varRbtn=IntVar()
        self.rbtn_admin=tkinter.ttk.Radiobutton(self.containerframe, text="admin", padding=(2), variable=self.varRbtn, value=1)
        self.rbtn_user=tkinter.ttk.Radiobutton(self.containerframe, text="regular user", padding=(2), variable=self.varRbtn, value=0)
        self.varRbtn.set(1)
        self.rbtn_admin.grid(row=3, column=0, padx=15, pady=8)
        self.rbtn_user.grid(row=3, column=1, sticky=E, padx=15)

        self.btn_Submit.grid(columnspan=2, pady=20, sticky=S)


    def action_submit(self, event):
        if(self.var_check_signup.get() == 0):
            if(self.varRbtn.get() == 1):
                var_verify = Customer.customer_Verify(self.var_Password.get(), self.var_UserId.get(), 1)
                if(var_verify == 1):
                    adminLogin=userLogin(Toplevel())
                else:
                    showinfo("Error Login", "Incorrect admin id or password")
            else:
                var_verify = Customer.customer_Verify(self.var_Password.get(), self.var_UserId.get(), 0)
                if(var_verify==False):
                    showinfo("Error Login", "Incorrect User id or password")
                else:
                    userform = customerLogin(Toplevel(), var_verify)
        else:
            if(self.counter==1):
                pass
            else:
                self.destroy()
                Signup(self.master)
                loginForm.counter=1

class Signup(Frame):
    master=""
    def action_Submit(self):
        val=askquestion("Query", "Do you really want to submit this details")
        if(val=="yes"):
            cust = Customer()
            cust.custName = self.varName.get()
            try:
                cust.custAge = self.varAge.get()
                cust.custMob = self.varMob.get()
            except ValueError:
                print("Only Numbers")
            except Exception:
                print("Error in values")
            cust.custId = self.varId.get()
            cust.custPassword = self.varPassword.get()
            try:
                cust.custPhoto=self.filepath[0]
            except Exception:
                cust.custPhoto=''
            val=cust.add_Customer()
            if(val==False):
                showinfo("Error", "UserId already taken")
            elif(val==2):
                showinfo("Error", "UserId cannot have spaces")
            elif (val == 3):
                showinfo("Error", "Password cannot have spaces")
            elif (val == 4):
                showinfo("Error", "mobile can be only decimal of 10 or 11 digits")
            else:
                self.destroy()
                loginForm(Signup.master, 200, 100)
        else:
            pass

    def __init__(self, master):
        Signup.master=master
        super().__init__(master)
        master.title("SignUp")
        self.pack()
        self.config(bg='lightgrey')
        self.createWidget()

    def showNormal(self):
        if(self.varCheck.get()==1):
            self.entry_Password["show"]=""
        else:
            self.entry_Password["show"]="*"

    def action_back(self):
        self.destroy()
        loginForm(Signup.master, 200, 100)

    def upload_photo(self):
        self.filepath=tkinter.filedialog.askopenfilenames()
        self.img=Image.open(self.filepath[0])
        self.newimg=self.img.resize((70, 78), Image.ANTIALIAS)
        self.myimg=ImageTk.PhotoImage(self.newimg)
        self.lbl_img.config(image=self.myimg)
        self.lbl_img.pack()

    def createWidget(self):
        self.newimg = ""
        self.img = ""
        self.myimg = ""
        self.filepath=''
        self.heading_frame=Frame(self, bg='lightgrey')
        self.heading_frame.pack()
        self.heading=Label(self.heading_frame, text="Sign Up", font=('Times New Roman', '16', 'bold', 'italic'), fg='grey', bg='lightgrey')
        self.heading.pack(pady=5)
        self.containerframe=Frame(self)
        self.containerframe.pack(pady=5, padx=5)
        self.lbl_name=tkinter.ttk.Label(self.containerframe, text="Name", padding=4, anchor=E)
        self.lbl_name.grid(row=0, column=0, pady=6)
        self.lbl_Age = tkinter.ttk.Label(self.containerframe, text="Age", padding=4, anchor=E)
        self.lbl_Age.grid(row=1, column=0, pady=2)
        self.lbl_UserId = tkinter.ttk.Label(self.containerframe, text="UserID", padding=4, anchor=E)
        self.lbl_UserId.grid(row=2, column=0, pady=2)
        self.lbl_Mob = tkinter.ttk.Label(self.containerframe, text="Mobile Number:", padding=4, anchor=E)
        self.lbl_Mob.grid(row=3, column=0, pady=2)
        self.lbl_Password=tkinter.ttk.Label(self.containerframe, text="Password", padding=4, anchor=E).grid(row=4, column=0, pady=2)

        self.varName = StringVar()
        self.entry_name=tkinter.ttk.Entry(self.containerframe, width=30, textvariable=self.varName).grid(row=0, column=1, padx=6)
        self.varAge = IntVar()
        self.entry_age=tkinter.ttk.Entry(self.containerframe, width=30, textvariable=self.varAge).grid(row=1, column=1, padx=5)
        self.varId = StringVar()
        self.entry_UserId=tkinter.ttk.Entry(self.containerframe, width=30, textvariable=self.varId).grid(row=2, column=1, padx=5)
        self.varMob = IntVar()
        self.entry_Mob=tkinter.ttk.Entry(self.containerframe, width=30, textvariable=self.varMob).grid(row=3, column=1, padx=5)
        self.varPassword=StringVar()
        self.entry_Password=tkinter.ttk.Entry(self.containerframe, width=30, show="*", textvariable=self.varPassword)
        self.entry_Password.grid(row=4, column=1, padx=5)

        self.varCheck=IntVar()
        self.check_showPassword=tkinter.ttk.Checkbutton(self.containerframe, text="Show Password", variable=self.varCheck, command=self.showNormal)
        self.check_showPassword.grid(columnspan=2, pady=8)
        self.btn_Submit=tkinter.ttk.Button(self.containerframe, text="Submit", padding=(3,3), command=self.action_Submit)
        self.btn_back=tkinter.ttk.Button(self.containerframe, text="<< Back ", padding=(3, 3), command=self.action_back)
        self.btn_back.grid(row=6, column=0, pady=15)
        self.btn_Submit.grid(row=6, column=1, pady=15, sticky=E, padx=10)

        self.imgframe = tkinter.ttk.LabelFrame(self.containerframe, text="upload photo", height=128, width=110)
        self.imgframe.grid(row=1, column=2, rowspan=3, padx=10)
        self.btn_uploadpic = tkinter.ttk.Button(self.containerframe, text="Upload photo", command=self.upload_photo)
        self.btn_uploadpic.grid(row=4, column=2)
        self.lbl_img = Label(self.imgframe, text="hey")

class customerLogin(Frame):

    master=None
    def __init__(self, master, val):
        super().__init__(master)
        customerLogin.master=master
        master.title("Customer login")
        self.pack()
        self.createWidget(val)

    def action_search(self, event):
        cust=Customer()
        if(self.frame_searchCustomer.var_rbtn.get()==0):
            val=cust.search_Customer(self.frame_searchCustomer.ent_searchId.get(), 1)
            if(len(val)!=0):
                self.frame_searchCustomer.txt.delete('1.0', END)
                self.frame_searchCustomer.txt.insert(END, "CustomerId:\t"+val[0][0]+"\t\tCustomerName:\t"+val[0][1]+"\t\tCustomerAge:\t"+str(val[0][2])+"\t\tCustomerMobile:\t"+str(val[0][3]))
            else:
                self.frame_searchCustomer.txt.delete('1.0', END)
                self.frame_searchCustomer.txt.insert(END, "Search unsuccessfull")

        elif (self.frame_searchCustomer.var_rbtn.get() == 1):
            val = cust.search_Customer(self.frame_searchCustomer.ent_searchname.get(), 2)
            if (len(val)!=0):
                self.frame_searchCustomer.txt.delete('1.0', END)
                self.frame_searchCustomer.txt.insert(END,"CustomerId:\t" + val[0][0] + "\t\tCustomerName:\t" + val[0][1] + "\t\tCustomerAge:\t" + str(val[0][2]) + "\t\tCustomerMobile:\t" + str(val[0][3]))
            else:
                self.frame_searchCustomer.txt.delete('1.0', END)
                self.frame_searchCustomer.txt.insert(END, "Search unsuccessfull")

        else:
            val = cust.search_Customer(self.frame_searchCustomer.var_searchmob.get(), 3)
            if (len(val)!=0):
                self.frame_searchCustomer.txt.delete('1.0', END)
                self.frame_searchCustomer.txt.insert(END,"CustomerId:\t" + val[0][0] + "\t\tCustomerName:\t" + val[0][1] + "\t\tCustomerAge:\t" + str(val[0][2]) + "\t\tCustomerMobile:\t" + str(val[0][3]))
            else:
                self.frame_searchCustomer.txt.delete('1.0', END)
                self.frame_searchCustomer.txt.insert(END, "Search unsuccessfull")

    def createFrame(self):
        if (self.frame_searchCustomer.var_rbtn.get() == 0):

            self.frame_searchCustomer.frame.destroy()
            self.frame_searchCustomer.frame = Frame(self.frame_searchCustomer)
            self.frame_searchCustomer.frame.pack()
            self.frame_searchCustomer.lbl_searchId = tkinter.ttk.Label(self.frame_searchCustomer.frame,
                                                                       text="Enter your Id")
            self.frame_searchCustomer.lbl_searchId.grid(row=0, column=0, pady=20, padx=5)
            self.frame_searchCustomer.ent_searchId = tkinter.ttk.Entry(self.frame_searchCustomer.frame, width=30)
            self.frame_searchCustomer.ent_searchId.grid(row=0, column=1, pady=10, padx=8)
            self.frame_searchCustomer.btnSubmit = tkinter.ttk.Button(self.frame_searchCustomer.frame, text="Search",
                                                                     padding=(8, 4))
            self.frame_searchCustomer.btnSubmit.grid(columnspan=2, pady=20)
            self.frame_searchCustomer.btnSubmit.bind("<Button-1>", self.action_search)
            self.frame_searchCustomer.txt = Text(self.frame_searchCustomer.frame, width=45, height=5, wrap=WORD)
            self.frame_searchCustomer.txt.grid(columnspan=2, pady=35)

        elif (self.frame_searchCustomer.var_rbtn.get() == 1):

            self.frame_searchCustomer.frame.destroy()
            self.frame_searchCustomer.frame = Frame(self.frame_searchCustomer)
            self.frame_searchCustomer.frame.pack()
            self.frame_searchCustomer.lbl_searchname = tkinter.ttk.Label(self.frame_searchCustomer.frame,
                                                                         text="Enter your Name")
            self.frame_searchCustomer.lbl_searchname.grid(row=0, column=0, pady=20, padx=5)
            self.frame_searchCustomer.ent_searchname = tkinter.ttk.Entry(self.frame_searchCustomer.frame, width=30)
            self.frame_searchCustomer.ent_searchname.grid(row=0, column=1, pady=10, padx=8)
            self.frame_searchCustomer.btnSubmit = tkinter.ttk.Button(self.frame_searchCustomer.frame, text="Search",
                                                                     padding=(8, 4))
            self.frame_searchCustomer.btnSubmit.grid(columnspan=2, pady=20)
            self.frame_searchCustomer.btnSubmit.bind("<Button-1>", self.action_search)
            self.frame_searchCustomer.txt = Text(self.frame_searchCustomer.frame, width=45, height=5, wrap=WORD)
            self.frame_searchCustomer.txt.grid(columnspan=2, pady=35)

        else:

            self.frame_searchCustomer.frame.destroy()
            self.frame_searchCustomer.frame = Frame(self.frame_searchCustomer)
            self.frame_searchCustomer.frame.pack()
            self.frame_searchCustomer.lbl_searchmob = tkinter.ttk.Label(self.frame_searchCustomer.frame,
                                                                        text="Enter your mobile")
            self.frame_searchCustomer.lbl_searchmob.grid(row=0, column=0, pady=20, padx=5)
            self.frame_searchCustomer.var_searchmob = IntVar()
            self.frame_searchCustomer.ent_searchmob = tkinter.ttk.Entry(self.frame_searchCustomer.frame, width=30,
                                                                        textvariable=self.frame_searchCustomer.var_searchmob)
            self.frame_searchCustomer.ent_searchmob.grid(row=0, column=1, pady=10, padx=8)
            self.frame_searchCustomer.btnSubmit = tkinter.ttk.Button(self.frame_searchCustomer.frame, text="Search",
                                                                     padding=(8, 4))
            self.frame_searchCustomer.btnSubmit.grid(columnspan=2, pady=20)
            self.frame_searchCustomer.btnSubmit.bind("<Button-1>", self.action_search)
            self.frame_searchCustomer.txt = Text(self.frame_searchCustomer.frame, width=45, height=5, wrap=WORD)
            self.frame_searchCustomer.txt.grid(columnspan=2, pady=35)

    def modify_customer(self):

        if(self.frame_modify.var_rbtn.get()==0):
            Customer().update_Customer(self.custid, self.frame_modify.var_entid.get(), 1)
            showinfo("Success", "your id changed successfully")
        elif(self.frame_modify.var_rbtn.get()==1):
            Customer().update_Customer(self.custid, self.frame_modify.var_newname.get(), 2)
            showinfo("Success", "your name changed successfully\nLogin again to see the changes")
        elif (self.frame_modify.var_rbtn.get() == 2):
            Customer().update_Customer(self.custid, self.frame_modify.var_entage.get(), 3)
            showinfo("Success", "your age changed successfully\nLogin again to see the changes")
        elif (self.frame_modify.var_rbtn.get() == 3):
            Customer().update_Customer(self.custid, self.frame_modify.var_entpassword.get(), 5)
            showinfo("Success", "your password changed successfully\nLogin again to see the changes")
        else:
            Customer().update_Customer(self.custid, self.frame_modify.var_entmob.get(), 4)
            showinfo("Success", "your mobile changed successfully\nLogin again to see the changes")

    def action_logout(self):
        val=askquestion("info", "Do you really want to logout?")
        if(val == "yes"):
            customerLogin.master.destroy()
        else:
            pass

    def frame_modify_switchFrames(self):
        if(self.frame_modify.var_rbtn.get()==1):
            self.frame_modify.info_container.destroy()
            self.frame_modify.info_container=Frame(self.frame_modify.containerframe, bg="white")
            self.frame_modify.info_container.pack(side=RIGHT, fill="both", padx=10)
            self.frame_modify.lbl_newname=Label(self.frame_modify.info_container, text="Enter your new name", padx=3, pady=2)
            self.frame_modify.lbl_newname.grid(row=0, column=0, pady=20, padx=6)
            self.frame_modify.var_newname=StringVar()
            self.frame_modify.ent_newname=tkinter.ttk.Entry(self.frame_modify.info_container, width=30, textvariable=self.frame_modify.var_newname)
            self.frame_modify.ent_newname.grid(row=0, column=1, padx=10)
            self.frame_modify.btn_submitname = tkinter.ttk.Button(self.frame_modify.info_container, text="Submit", padding=(3, 3), command=self.modify_customer)
            self.frame_modify.btn_submitname.grid(columnspan=2, pady=20)

        elif (self.frame_modify.var_rbtn.get() == 0):
            self.frame_modify.info_container.destroy()
            self.frame_modify.info_container = Frame(self.frame_modify.containerframe, bg="white")
            self.frame_modify.info_container.pack(side=RIGHT, fill="both", padx=10)
            self.frame_modify.lbl_newuid = Label(self.frame_modify.info_container, text="Enter your new Id", padx=3,
                                                 pady=2)
            self.frame_modify.lbl_newuid.grid(row=0, column=0, pady=20, padx=6)
            self.frame_modify.var_entid = StringVar()
            self.frame_modify.newentid = tkinter.ttk.Entry(self.frame_modify.info_container, width=30,
                                                           textvariable=self.frame_modify.var_entid)
            self.frame_modify.newentid.grid(row=0, column=1, padx=10)
            self.frame_modify.btn_submitid = tkinter.ttk.Button(self.frame_modify.info_container, text="Submit",
                                                                padding=(3, 3), command=self.modify_customer)
            self.frame_modify.btn_submitid.grid(columnspan=2, pady=20)

        elif (self.frame_modify.var_rbtn.get() == 2):
            self.frame_modify.info_container.destroy()
            self.frame_modify.info_container = Frame(self.frame_modify.containerframe, bg="white")
            self.frame_modify.info_container.pack(side=RIGHT, fill="both", padx=10)
            self.frame_modify.lbl_newage = Label(self.frame_modify.info_container, text="Enter your new age", padx=3,
                                                 pady=2)
            self.frame_modify.lbl_newage.grid(row=0, column=0, pady=20, padx=6)
            self.frame_modify.var_entage = IntVar()
            self.frame_modify.newentage = tkinter.ttk.Entry(self.frame_modify.info_container, width=30,
                                                           textvariable=self.frame_modify.var_entage)
            self.frame_modify.newentage.grid(row=0, column=1, padx=10)
            self.frame_modify.btn_submitage = tkinter.ttk.Button(self.frame_modify.info_container, text="Submit",
                                                                padding=(3, 3), command=self.modify_customer)
            self.frame_modify.btn_submitage.grid(columnspan=2, pady=20)


        elif (self.frame_modify.var_rbtn.get() == 3):
            self.frame_modify.info_container.destroy()
            self.frame_modify.info_container = Frame(self.frame_modify.containerframe, bg="white")
            self.frame_modify.info_container.pack(side=RIGHT, fill="both", padx=10)
            self.frame_modify.lbl_newpassword = Label(self.frame_modify.info_container, text="Enter your new password", padx=3,
                                                 pady=2)
            self.frame_modify.lbl_newpassword.grid(row=0, column=0, pady=20, padx=6)
            self.frame_modify.var_entpassword = StringVar()
            self.frame_modify.newentpassword = tkinter.ttk.Entry(self.frame_modify.info_container, width=30,
                                                           textvariable=self.frame_modify.var_entpassword)
            self.frame_modify.newentpassword.grid(row=0, column=1, padx=10)
            self.frame_modify.btn_submitpassword = tkinter.ttk.Button(self.frame_modify.info_container, text="Submit",
                                                                padding=(3, 3), command=self.modify_customer)
            self.frame_modify.btn_submitpassword.grid(columnspan=2, pady=20)

        else:
            self.frame_modify.info_container.destroy()
            self.frame_modify.info_container = Frame(self.frame_modify.containerframe, bg="white")
            self.frame_modify.info_container.pack(side=RIGHT, fill="both", padx=10)
            self.frame_modify.lbl_newmob = Label(self.frame_modify.info_container, text="Enter your new mobile", padx=3,
                                                 pady=2)
            self.frame_modify.lbl_newmob.grid(row=0, column=0, pady=20, padx=6)
            self.frame_modify.var_entmob = IntVar()
            self.frame_modify.newentmob = tkinter.ttk.Entry(self.frame_modify.info_container, width=30,
                                                           textvariable=self.frame_modify.var_entmob)
            self.frame_modify.newentmob.grid(row=0, column=1, padx=10)
            self.frame_modify.btn_submitmob = tkinter.ttk.Button(self.frame_modify.info_container, text="Submit",
                                                                padding=(3, 3), command=self.modify_customer)
            self.frame_modify.btn_submitmob.grid(columnspan=2, pady=20)



    def btn_displayAll_click(self):
        self.frame_displayAll.txt.delete('1.0', END)
        fetched_val=Customer().displayAll()
        for el in fetched_val[0]:
            self.frame_displayAll.txt.insert(END, el[0]+'\t  ')
        self.frame_displayAll.txt.insert(END, '\n')
        c=1
        #print(fetched_val[1])
        for el in fetched_val[1]:
            for val in el:
                self.frame_displayAll.txt.insert(END, str(val)+'\t  ')
            self.frame_displayAll.txt.insert(END, '\n')

    def createWidget(self, val):
        self.custid=val[0]
        self.notebook=tkinter.ttk.Notebook(self)
        self.notebook.pack(pady=2)

        self.frame_homepage=tkinter.ttk.Frame(self.notebook)
        self.frame_modify=tkinter.ttk.Frame(self.notebook)
        self.frame_searchCustomer=tkinter.ttk.Frame(self.notebook)
        self.frame_displayAll=tkinter.ttk.Frame(self.notebook)

        self.notebook.add(self.frame_homepage, text="Home")
        self.notebook.add(self.frame_modify, text="Modify details")
        self.notebook.add(self.frame_searchCustomer, text="search")
        self.notebook.add(self.frame_displayAll, text="display all")
        self.notebook.select(0)

        #self.frame_modify

        self.frame_modify.headingframe=tkinter.ttk.Frame(self.frame_modify)
        self.frame_modify.headingframe.pack(pady=5)

        self.frame_modify.headingframe.heading = Label(self.frame_modify.headingframe, text="Welcome "+(str(val[1])).lower().capitalize(), font=("Times New Roman", "20", "bold", "italic"), bg="lightgrey", fg="grey")
        self.frame_modify.headingframe.heading.pack(padx=10, pady=30)

        self.frame_modify.containerframe=tkinter.ttk.Frame(self.frame_modify)
        self.frame_modify.containerframe.pack(pady=20)
        self.frame_modify.rbtn_container=tkinter.ttk.Frame(self.frame_modify.containerframe)
        self.frame_modify.rbtn_container.pack(side=LEFT, padx=6)
        self.frame_modify.var_rbtn=IntVar()
        self.frame_modify.rbtn_uid=tkinter.ttk.Radiobutton(self.frame_modify.rbtn_container, text="Change userId", variable=self.frame_modify.var_rbtn, value=0, command=self.frame_modify_switchFrames)
        self.frame_modify.rbtn_name=tkinter.ttk.Radiobutton(self.frame_modify.rbtn_container, text="Change Name", variable=self.frame_modify.var_rbtn, value=1, command=self.frame_modify_switchFrames)
        self.frame_modify.rbtn_age=tkinter.ttk.Radiobutton(self.frame_modify.rbtn_container, text="Change Age", variable=self.frame_modify.var_rbtn, value=2, command=self.frame_modify_switchFrames)
        self.frame_modify.rbtn_password=tkinter.ttk.Radiobutton(self.frame_modify.rbtn_container, text="Change Password", variable=self.frame_modify.var_rbtn, value=3, command=self.frame_modify_switchFrames)
        self.frame_modify.rbtn_mob=tkinter.ttk.Radiobutton(self.frame_modify.rbtn_container, text="Change Mobile", variable=self.frame_modify.var_rbtn, value=4, command=self.frame_modify_switchFrames)
        self.frame_modify.var_rbtn.set(0)
        self.frame_modify.rbtn_uid.grid(row=0, column=0, pady=8, sticky=W, padx=6)
        self.frame_modify.rbtn_name.grid(row=1, column=0, pady=8, sticky=W, padx=6)
        self.frame_modify.rbtn_age.grid(row=2, column=0, pady=8, sticky=W, padx=6)
        self.frame_modify.rbtn_password.grid(row=3, column=0, pady=8, sticky=W, padx=6)
        self.frame_modify.rbtn_mob.grid(row=4, column=0, pady=8, sticky=W, padx=6)

        self.frame_modify.info_container=Frame(self.frame_modify.containerframe, background="white")
        self.frame_modify.info_container.pack(side=RIGHT, padx=10, fill="both")

        self.frame_modify.lbl_newuid=Label(self.frame_modify.info_container, text="Enter your new Id", padx=3, pady=2)
        self.frame_modify.lbl_newuid.grid(row=0, column=0, pady=20, padx=6)
        self.frame_modify.var_entid=StringVar()
        self.frame_modify.newentid=tkinter.ttk.Entry(self.frame_modify.info_container, width=30, textvariable=self.frame_modify.var_entid)
        self.frame_modify.newentid.grid(row=0, column=1, padx=10)
        self.frame_modify.btn_submitid=tkinter.ttk.Button(self.frame_modify.info_container, text="Submit", padding=(3, 3), command=self.modify_customer)
        self.frame_modify.btn_submitid.grid(columnspan=2, pady=20)


        # self.frame_searchCustomer

        self.frame_searchCustomer.headingframe=Frame(self.frame_searchCustomer)
        self.frame_searchCustomer.headingframe.pack(pady=3)
        self.frame_modify.headingframe.heading = Label(self.frame_searchCustomer.headingframe, text="Welcome "+(str(val[1])).lower().capitalize(),
                                                       font=("Times New Roman", "20", "bold", "italic"), bg="lightgrey",
                                                       fg="grey")
        self.frame_modify.headingframe.heading.pack(padx=10, pady=20)

        self.frame_searchCustomer.frame_rbtn = Frame(self.frame_searchCustomer)
        self.frame_searchCustomer.frame_rbtn.pack(pady=8)
        self.frame_searchCustomer.var_rbtn = IntVar()
        self.frame_searchCustomer.rbtn_Id = tkinter.ttk.Radiobutton(self.frame_searchCustomer.frame_rbtn,
                                                                    text="Search by ID",
                                                                    variable=self.frame_searchCustomer.var_rbtn,
                                                                    value=0, command=self.createFrame)
        self.frame_searchCustomer.rbtn_name = tkinter.ttk.Radiobutton(self.frame_searchCustomer.frame_rbtn,
                                                                      text="Search by Name",
                                                                      variable=self.frame_searchCustomer.var_rbtn,
                                                                      value=1, command=self.createFrame)
        self.frame_searchCustomer.rbtn_mob = tkinter.ttk.Radiobutton(self.frame_searchCustomer.frame_rbtn,
                                                                     text="Search by mobile number",
                                                                     variable=self.frame_searchCustomer.var_rbtn,
                                                                     value=2, command=self.createFrame)
        self.frame_searchCustomer.rbtn_Id.grid(row=0, column=0, padx=5, pady=10)
        self.frame_searchCustomer.rbtn_name.grid(row=0, column=1, padx=5)
        self.frame_searchCustomer.rbtn_mob.grid(row=0, column=2, padx=5)
        self.frame_searchCustomer.var_rbtn.set(0)

        self.frame_searchCustomer.frame = Frame(self.frame_searchCustomer)
        self.frame_searchCustomer.frame.pack()
        self.frame_searchCustomer.lbl_searchId = tkinter.ttk.Label(self.frame_searchCustomer.frame,
                                                                   text="Enter your Id")
        self.frame_searchCustomer.lbl_searchId.grid(row=0, column=0, pady=20, padx=5)
        self.frame_searchCustomer.ent_searchId = tkinter.ttk.Entry(self.frame_searchCustomer.frame, width=30)
        self.frame_searchCustomer.ent_searchId.grid(row=0, column=1, pady=10, padx=8)
        self.frame_searchCustomer.btnSubmit = tkinter.ttk.Button(self.frame_searchCustomer.frame, text="Search",
                                                                 padding=(8, 4))
        self.frame_searchCustomer.btnSubmit.grid(columnspan=2, pady=20)
        self.frame_searchCustomer.btnSubmit.bind("<Button-1>", self.action_search)
        self.frame_searchCustomer.txt = Text(self.frame_searchCustomer.frame, width=45, height=5, wrap=WORD)
        self.frame_searchCustomer.txt.grid(columnspan=2, pady=35)


        # frame_home

        self.frame_homepage.headingframe=Frame(self.frame_homepage)
        self.frame_homepage.headingframe.pack(pady=15)
        self.frame_homepage.heading=Label(self.frame_homepage.headingframe, text="Welcome "+(str(val[1])).lower().capitalize(), font=('Times New Roman', '24', 'bold', 'italic'), bg='lightgrey', fg='grey')
        self.frame_homepage.heading.pack(pady=10)

        self.frame_homepage.containerframe=Frame(self.frame_homepage)
        self.frame_homepage.containerframe.pack(pady=15)

        self.frame_homepage.lbl_uid=Label(self.frame_homepage.containerframe, text="User Id : ")
        self.frame_homepage.lbl_uname=Label(self.frame_homepage.containerframe, text="User Name : ")
        self.frame_homepage.lbl_uage=Label(self.frame_homepage.containerframe, text="User Age : ")
        self.frame_homepage.lbl_upassword=Label(self.frame_homepage.containerframe, text="User Password : ")
        self.frame_homepage.lbl_umobile=Label(self.frame_homepage.containerframe, text="User Mobile : ")
        self.frame_homepage.lbl_uid.grid(row=0, column=0, pady=12, sticky=W)
        self.frame_homepage.lbl_uname.grid(row=1, column=0, pady=12, sticky=W)
        self.frame_homepage.lbl_uage.grid(row=2, column=0, pady=12, sticky=W)
        self.frame_homepage.lbl_upassword.grid(row=3, column=0, pady=12, sticky=W)
        self.frame_homepage.lbl_umobile.grid(row=4, column=0, pady=12, sticky=W)

        self.frame_homepage.ent_uid = Label(self.frame_homepage.containerframe, text=str(val[0]), fg='grey')
        self.frame_homepage.ent_uname = Label(self.frame_homepage.containerframe, text=(str(val[1])).lower().capitalize(), fg='grey')
        self.frame_homepage.ent_uage = Label(self.frame_homepage.containerframe, text=str(val[2]), fg='grey')
        self.frame_homepage.ent_upassword = Label(self.frame_homepage.containerframe, text=str(val[4]), fg='grey')
        self.frame_homepage.ent_umobile = Label(self.frame_homepage.containerframe, text=str(val[3]), fg='grey')
        self.frame_homepage.ent_uid.grid(row=0, column=1, pady=2, padx=20, sticky=W)
        self.frame_homepage.ent_uname.grid(row=1, column=1, pady=2, padx=20, sticky=W)
        self.frame_homepage.ent_uage.grid(row=2, column=1, pady=2, padx=20, sticky=W)
        self.frame_homepage.ent_upassword.grid(row=3, column=1, pady=2, padx=20, sticky=W)
        self.frame_homepage.ent_umobile.grid(row=4, column=1, pady=2, padx=20, sticky=W)

        self.frame_homepage.imgframe=tkinter.ttk.LabelFrame(self.frame_homepage.containerframe, text="Image", height=128, width=120)
        self.frame_homepage.imgframe.grid(row=0, column=2, rowspan=3, sticky=E, padx=25)
        self.frame_homepage.lbl_img = Label(self.frame_homepage.imgframe, text="hey")
        self.frame_homepage.btn_logout=tkinter.ttk.Button(self.frame_homepage.containerframe, text="Log out", command=self.action_logout, padding=(4, 4))
        self.frame_homepage.btn_logout.grid(columnspan=2, pady=15)
        try:
            self.frame_homepage.img=Image.open(val[5])
            self.frame_homepage.newimg=self.frame_homepage.img.resize((70, 78), Image.ANTIALIAS)
            self.frame_homepage.myimg=ImageTk.PhotoImage(self.frame_homepage.newimg)
            self.frame_homepage.lbl_img.config(image=self.frame_homepage.myimg)
            self.frame_homepage.lbl_img.pack()
        except Exception:
            pass


        #frame_displayall

        self.frame_displayAll.headingframe = tkinter.ttk.Frame(self.frame_displayAll)
        self.frame_displayAll.headingframe.pack(pady=5)

        self.frame_displayAll.headingframe.heading = Label(self.frame_displayAll.headingframe,
                                                       text="Welcome " + (str(val[1])).lower().capitalize(),
                                                       font=("Times New Roman", "20", "bold", "italic"), bg="lightgrey",
                                                       fg="grey")
        self.frame_displayAll.headingframe.heading.pack(padx=10, pady=30)

        self.frame_displayAll.containerframe=Frame(self.frame_displayAll)
        self.frame_displayAll.containerframe.pack(pady=10)
        self.frame_displayAll.btn_displayAll=tkinter.ttk.Button(self.frame_displayAll.containerframe, text="Display all customers", padding=(4, 4), command=self.btn_displayAll_click)
        self.frame_displayAll.btn_displayAll.pack(pady=20)
        self.frame_displayAll.textcontainer=Frame(self.frame_displayAll.containerframe)
        self.frame_displayAll.textcontainer.pack(side="left", pady=20)
        self.frame_displayAll.vscroll=tkinter.ttk.Scrollbar(self.frame_displayAll.containerframe)
        self.frame_displayAll.vscroll.pack(side=RIGHT, fill=Y)
        self.frame_displayAll.hscroll=tkinter.ttk.Scrollbar(self.frame_displayAll.textcontainer, orient="horizontal")

        self.frame_displayAll.txt=Text(self.frame_displayAll.textcontainer, width=50, height=13, wrap="none")
        self.frame_displayAll.txt.config(xscrollcommand=self.frame_displayAll.hscroll.set)
        self.frame_displayAll.txt.config(yscrollcommand=self.frame_displayAll.vscroll.set)
        self.frame_displayAll.txt.pack()
        self.frame_displayAll.hscroll.pack(side="bottom", fill=X)
        self.frame_displayAll.vscroll.config(command=self.frame_displayAll.txt.yview)
        self.frame_displayAll.hscroll.config(command=self.frame_displayAll.txt.xview)

class userLogin(Frame):

    def __init__(self, master):
        super().__init__(master)
        master.title("Home")
        self.pack()
        self.config(bg='lightgrey')
        self.createWidget()

    def deleteCustomer(self):
        val=askquestion("info", "Do you really want to delete this id?")
        cust=Customer()
        if(val=="yes"):
            res=cust.delete_Customer(self.frame_deleteCustomer.var_deleteId.get())
            if(res==True):
                showinfo("Success", "Customer deleted successfullly")
            else:
                showinfo("Error", "Cannot find customer")
        else:
            pass

    def update_textPressed(self, event):
        if (len(self.frame_updateCustomer.p.findall(event.char))):
            self.frame_updateCustomer.rbtn_mid.config(state="active")
            self.frame_updateCustomer.rbtn_mname.config(state="active")
            self.frame_updateCustomer.rbtn_mage.config(state="active")
            self.frame_updateCustomer.rbtn_mpassword.config(state="active")
        else:
            if (len(self.frame_updateCustomer.var_upid.get()) != 0):
                self.frame_updateCustomer.rbtn_mid.config(state="active")
                self.frame_updateCustomer.rbtn_mname.config(state="active")
                self.frame_updateCustomer.rbtn_mage.config(state="active")
                self.frame_updateCustomer.rbtn_mpassword.config(state="active")
            else:
                self.frame_updateCustomer.rbtn_mid.config(state="disabled")
                self.frame_updateCustomer.rbtn_mname.config(state="disabled")
                self.frame_updateCustomer.rbtn_mage.config(state="disabled")
                self.frame_updateCustomer.rbtn_mpassword.config(state="disabled")

    def btn_displayAll_click(self):
        self.frame_displayAll.txt.delete('1.0', END)
        fetched_val=Customer().displayAll()
        for el in fetched_val[0]:
            self.frame_displayAll.txt.insert(END, el[0]+'\t  ')
        self.frame_displayAll.txt.insert(END, '\n')
        for el in fetched_val[1]:
            for val in el:
                self.frame_displayAll.txt.insert(END, str(val)+'\t  ')
            self.frame_displayAll.txt.insert(END, '\n')


    def action_search(self, event):
        cust=Customer()
        if(self.frame_searchCustomer.var_rbtn.get()==0):
            val=cust.search_Customer(self.frame_searchCustomer.ent_searchId.get(), 1)
            if(len(val)!=0):
                self.frame_searchCustomer.txt.delete('1.0', END)
                self.frame_searchCustomer.txt.insert(END, "CustomerId:\t"+val[0][0]+"\t\tCustomerName:\t"+val[0][1]+"\t\tCustomerAge:\t"+str(val[0][2])+"\t\tCustomerMobile:\t"+str(val[0][3]))
            else:
                self.frame_searchCustomer.txt.delete('1.0', END)
                self.frame_searchCustomer.txt.insert(END, "Search unsuccessfull")

        elif (self.frame_searchCustomer.var_rbtn.get() == 1):
            val = cust.search_Customer(self.frame_searchCustomer.ent_searchname.get(), 2)
            if (len(val)!=0):
                self.frame_searchCustomer.txt.delete('1.0', END)
                self.frame_searchCustomer.txt.insert(END,"CustomerId:\t" + val[0][0] + "\t\tCustomerName:\t" + val[0][1] + "\t\tCustomerAge:\t" + str(val[0][2]) + "\t\tCustomerMobile:\t" + str(val[0][3]))
            else:
                self.frame_searchCustomer.txt.delete('1.0', END)
                self.frame_searchCustomer.txt.insert(END, "Search unsuccessfull")

        else:
            val = cust.search_Customer(self.frame_searchCustomer.var_searchmob.get(), 3)
            if (len(val)!=0):
                self.frame_searchCustomer.txt.delete('1.0', END)
                self.frame_searchCustomer.txt.insert(END,"CustomerId:\t" + val[0][0] + "\t\tCustomerName:\t" + val[0][1] + "\t\tCustomerAge:\t" + str(val[0][2]) + "\t\tCustomerMobile:\t" + str(val[0][3]))
            else:
                self.frame_searchCustomer.txt.delete('1.0', END)
                self.frame_searchCustomer.txt.insert(END, "Search unsuccessfull")

    def createFrame(self):
        if(self.frame_searchCustomer.var_rbtn.get()==0):

            self.frame_searchCustomer.frame.destroy()
            self.frame_searchCustomer.frame=Frame(self.frame_searchCustomer)
            self.frame_searchCustomer.frame.pack()
            self.frame_searchCustomer.lbl_searchId = tkinter.ttk.Label(self.frame_searchCustomer.frame, text="Enter your Id")
            self.frame_searchCustomer.lbl_searchId.grid(row=0, column=0, pady=20, padx=5)
            self.frame_searchCustomer.ent_searchId = tkinter.ttk.Entry(self.frame_searchCustomer.frame, width=30)
            self.frame_searchCustomer.ent_searchId.grid(row=0, column=1, pady=10, padx=8)
            self.frame_searchCustomer.btnSubmit = tkinter.ttk.Button(self.frame_searchCustomer.frame, text="Search", padding=(8, 4))
            self.frame_searchCustomer.btnSubmit.grid(columnspan=2, pady=20)
            self.frame_searchCustomer.btnSubmit.bind("<Button-1>", self.action_search)
            self.frame_searchCustomer.txt = Text(self.frame_searchCustomer.frame, width=45, height=5, wrap=WORD)
            self.frame_searchCustomer.txt.grid(columnspan=2, pady=35)

        elif(self.frame_searchCustomer.var_rbtn.get()==1):

            self.frame_searchCustomer.frame.destroy()
            self.frame_searchCustomer.frame = Frame(self.frame_searchCustomer)
            self.frame_searchCustomer.frame.pack()
            self.frame_searchCustomer.lbl_searchname = tkinter.ttk.Label(self.frame_searchCustomer.frame, text="Enter your Name")
            self.frame_searchCustomer.lbl_searchname.grid(row=0, column=0, pady=20, padx=5)
            self.frame_searchCustomer.ent_searchname = tkinter.ttk.Entry(self.frame_searchCustomer.frame, width=30)
            self.frame_searchCustomer.ent_searchname.grid(row=0, column=1, pady=10, padx=8)
            self.frame_searchCustomer.btnSubmit = tkinter.ttk.Button(self.frame_searchCustomer.frame, text="Search", padding=(8, 4))
            self.frame_searchCustomer.btnSubmit.grid(columnspan=2, pady=20)
            self.frame_searchCustomer.btnSubmit.bind("<Button-1>", self.action_search)
            self.frame_searchCustomer.txt = Text(self.frame_searchCustomer.frame, width=45, height=5, wrap=WORD)
            self.frame_searchCustomer.txt.grid(columnspan=2, pady=35)

        else:

            self.frame_searchCustomer.frame.destroy()
            self.frame_searchCustomer.frame = Frame(self.frame_searchCustomer)
            self.frame_searchCustomer.frame.pack()
            self.frame_searchCustomer.lbl_searchmob = tkinter.ttk.Label(self.frame_searchCustomer.frame, text="Enter your mobile")
            self.frame_searchCustomer.lbl_searchmob.grid(row=0, column=0, pady=20, padx=5)
            self.frame_searchCustomer.var_searchmob=IntVar()
            self.frame_searchCustomer.ent_searchmob = tkinter.ttk.Entry(self.frame_searchCustomer.frame, width=30, textvariable=self.frame_searchCustomer.var_searchmob)
            self.frame_searchCustomer.ent_searchmob.grid(row=0, column=1, pady=10, padx=8)
            self.frame_searchCustomer.btnSubmit = tkinter.ttk.Button(self.frame_searchCustomer.frame, text="Search", padding=(8, 4))
            self.frame_searchCustomer.btnSubmit.grid(columnspan=2, pady=20)
            self.frame_searchCustomer.btnSubmit.bind("<Button-1>", self.action_search)
            self.frame_searchCustomer.txt = Text(self.frame_searchCustomer.frame, width=45, height=5, wrap=WORD)
            self.frame_searchCustomer.txt.grid(columnspan=2, pady=35)

    def update_frame(self):
        if(self.frame_updateCustomer.var_rbtn.get()==1):

            self.frame_updateCustomer.frame2.destroy()
            self.frame_updateCustomer.frame2=Frame(self.frame_updateCustomer)
            self.frame_updateCustomer.frame2.grid(columnspan=2, pady=10)
            self.frame_updateCustomer.lbl_updatedid=tkinter.ttk.Label(self.frame_updateCustomer.frame2, text="Enter your new Id")
            self.frame_updateCustomer.lbl_updatedid.grid(row=0, column=0, pady=10, padx=5)
            self.frame_updateCustomer.var_updatedid = StringVar()
            self.frame_updateCustomer.ent_updatedid=tkinter.ttk.Entry(self.frame_updateCustomer.frame2, width=35, textvariable=self.frame_updateCustomer.var_updatedid)
            self.frame_updateCustomer.ent_updatedid.grid(row=0, column=1, padx=8, pady=10)
            self.frame_updateCustomer.btn_upsubmit=tkinter.ttk.Button(self.frame_updateCustomer.frame2, text="Submit", padding=(5, 4), command=self.btn_upsubmit_click)
            self.frame_updateCustomer.btn_upsubmit.grid(columnspan=2, pady=30)

        elif (self.frame_updateCustomer.var_rbtn.get() == 2):

            self.frame_updateCustomer.frame2.destroy()
            self.frame_updateCustomer.frame2 = Frame(self.frame_updateCustomer)
            self.frame_updateCustomer.frame2.grid(columnspan=2, pady=10)
            self.frame_updateCustomer.lbl_updatedname = tkinter.ttk.Label(self.frame_updateCustomer.frame2, text="Enter your new Name")
            self.frame_updateCustomer.lbl_updatedname.grid(row=0, column=0, pady=10, padx=5)
            self.frame_updateCustomer.var_updatedname = StringVar()
            self.frame_updateCustomer.ent_updatedname = tkinter.ttk.Entry(self.frame_updateCustomer.frame2, width=35, textvariable=self.frame_updateCustomer.var_updatedname)
            self.frame_updateCustomer.ent_updatedname.grid(row=0, column=1, padx=8, pady=10)
            self.frame_updateCustomer.btn_upsubmit = tkinter.ttk.Button(self.frame_updateCustomer.frame2, text="Submit", padding=(5, 4), command=self.btn_upsubmit_click)
            self.frame_updateCustomer.btn_upsubmit.grid(columnspan=2, pady=30)

        elif (self.frame_updateCustomer.var_rbtn.get() == 3):

            self.frame_updateCustomer.frame2.destroy()
            self.frame_updateCustomer.frame2 = Frame(self.frame_updateCustomer)
            self.frame_updateCustomer.frame2.grid(columnspan=2, pady=10)
            self.frame_updateCustomer.lbl_updatedage = tkinter.ttk.Label(self.frame_updateCustomer.frame2, text="Enter your new Age")
            self.frame_updateCustomer.lbl_updatedage.grid(row=0, column=0, pady=10, padx=5)
            self.frame_updateCustomer.var_updatedage = IntVar()
            self.frame_updateCustomer.ent_updatedage = tkinter.ttk.Entry(self.frame_updateCustomer.frame2, width=35, textvariable=self.frame_updateCustomer.var_updatedage)
            self.frame_updateCustomer.ent_updatedage.grid(row=0, column=1, padx=8, pady=10)
            self.frame_updateCustomer.btn_upsubmit = tkinter.ttk.Button(self.frame_updateCustomer.frame2, text="Submit", padding=(5, 4), command=self.btn_upsubmit_click)
            self.frame_updateCustomer.btn_upsubmit.grid(columnspan=2, pady=30)

        else:

            self.frame_updateCustomer.frame2.destroy()
            self.frame_updateCustomer.frame2 = Frame(self.frame_updateCustomer)
            self.frame_updateCustomer.frame2.grid(columnspan=2, pady=10)
            self.frame_updateCustomer.lbl_updatedpassword = tkinter.ttk.Label(self.frame_updateCustomer.frame2, text="Enter your new Password")
            self.frame_updateCustomer.lbl_updatedpassword.grid(row=0, column=0, pady=10, padx=5)
            self.frame_updateCustomer.var_updatedpassword=StringVar()
            self.frame_updateCustomer.ent_updatedpassword = tkinter.ttk.Entry(self.frame_updateCustomer.frame2, width=35, textvariable=self.frame_updateCustomer.var_updatedpassword)
            self.frame_updateCustomer.ent_updatedpassword.grid(row=0, column=1, padx=8, pady=10)
            self.frame_updateCustomer.btn_upsubmit = tkinter.ttk.Button(self.frame_updateCustomer.frame2, text="Submit", padding=(5, 4), command=self.btn_upsubmit_click)
            self.frame_updateCustomer.btn_upsubmit.grid(columnspan=2, pady=30)

    def upload_photo(self):
        self.filepath=tkinter.filedialog.askopenfilenames()
        self.frame_addCustomer.img=Image.open(self.filepath[0])
        self.frame_addCustomer.newimg=self.frame_addCustomer.img.resize((70, 78), Image.ANTIALIAS)
        self.frame_addCustomer.myimg=ImageTk.PhotoImage(self.frame_addCustomer.newimg)
        self.frame_addCustomer.lbl_img.config(image=self.frame_addCustomer.myimg)
        self.frame_addCustomer.lbl_img.pack()

    def frame_displayAll_rbtn_save_click(self):
        self.frame_displayAll.displayframe.destroy()
        self.frame_displayAll.displayframe=LabelFrame(self.frame_displayAll, text="Enter the name of file")
        self.frame_displayAll.displayframe.pack(pady=5)
        self.frame_displayAll.displayframe.text=tkinter.ttk.Entry(self.frame_displayAll.displayframe, width=20)
        self.frame_displayAll.displayframe.btn=tkinter.ttk.Button(self.frame_displayAll.displayframe, text="Submit")
        self.frame_displayAll.displayframe.text.pack(pady=5)
        self.frame_displayAll.displayframe.btn.pack(pady=2)
        fileloc=tkinter.filedialog.askdirectory()
        print(fileloc)

    def btn_upsubmit_click(self):

        cust=Customer()
        if(self.frame_updateCustomer.var_rbtn.get()==1):

            res=cust.update_Customer(self.frame_updateCustomer.var_upid.get(), self.frame_updateCustomer.var_updatedid.get(), 1)
            if(res==False):
                showinfo("error", "Cannot find your entered Id")
            else:
                showinfo("success", "Id updated successfully")

        elif (self.frame_updateCustomer.var_rbtn.get() == 2):

            res = cust.update_Customer(self.frame_updateCustomer.var_upid.get(),self.frame_updateCustomer.var_updatedname.get(), 2)
            if (res == False):
                showinfo("error", "Cannot find your entered Id")
            else:
                showinfo("success", "Name updated successfully")

        elif (self.frame_updateCustomer.var_rbtn.get() == 3):

            res = cust.update_Customer(self.frame_updateCustomer.var_upid.get(),self.frame_updateCustomer.var_updatedage.get(), 3)
            if (res == False):
                showinfo("error", "Cannot find your entered Id")
            else:
                showinfo("success", "Age updated successfully")

        else:

            res = cust.update_Customer(self.frame_updateCustomer.var_upid.get(),
                                       self.frame_updateCustomer.var_updatedpassword.get(), 5)
            if (res == False):
                showinfo("error", "Cannot find your entered Id")
            else:
                showinfo("success", "Password updated successfully")

    def createWidget(self):

        self.notebook=tkinter.ttk.Notebook(self)
        self.notebook.pack(pady=3, padx=5)
        self.frame_addCustomer=Frame(self.notebook, width=250, height=200)
        self.frame_deleteCustomer=Frame(self.notebook, width=250, height=200)
        self.frame_updateCustomer=Frame(self.notebook, width=250, height=200)
        self.frame_searchCustomer=Frame(self.notebook, width=250, height=200)
        self.frame_displayAll=Frame(self.notebook, width=250, height=200)
        self.notebook.add(self.frame_addCustomer, text="Add Customer")
        self.notebook.add(self.frame_deleteCustomer, text="Delete Customer")
        self.notebook.add(self.frame_updateCustomer, text="Update Customer")
        self.notebook.add(self.frame_searchCustomer, text="Search Customer")
        self.notebook.add(self.frame_displayAll, text="Display All Customers")
        self.notebook.select(0)

        #add customer
        self.frame_addCustomer.newimg=""
        self.frame_addCustomer.img=""
        self.frame_addCustomer.myimg=""
        self.filepath=''
        self.frame_addCustomer.userId=tkinter.ttk.Label(self.frame_addCustomer, text="UserID", padding=5).grid(row=0, column=0, pady=8)
        self.frame_addCustomer.name=tkinter.ttk.Label(self.frame_addCustomer, text="Name", padding=5).grid(row=1, column=0, pady=8)
        self.frame_addCustomer.age=tkinter.ttk.Label(self.frame_addCustomer, text="Age", padding=5).grid(row=2, column=0, pady=8)
        self.frame_addCustomer.password=tkinter.ttk.Label(self.frame_addCustomer, text="Password", padding=5).grid(row=3, column=0, pady=8)
        self.frame_addCustomer.mob=tkinter.ttk.Label(self.frame_addCustomer, text="Mobile", padding=5).grid(row=4, column=0, pady=8)

        self.frame_addCustomer.var_userId=StringVar()
        self.frame_addCustomer.ent_userId=tkinter.ttk.Entry(self.frame_addCustomer, width=40, textvariable=self.frame_addCustomer.var_userId).grid(row=0, column=1, pady=8, padx=10)
        self.frame_addCustomer.var_name = StringVar()
        self.frame_addCustomer.ent_name=tkinter.ttk.Entry(self.frame_addCustomer, width=40, textvariable=self.frame_addCustomer.var_name).grid(row=1, column=1, pady=8, padx=10)
        self.frame_addCustomer.var_age = IntVar()
        self.frame_addCustomer.ent_age=tkinter.ttk.Entry(self.frame_addCustomer, width=40, textvariable=self.frame_addCustomer.var_age).grid(row=2, column=1, pady=8, padx=10)
        self.frame_addCustomer.var_password = StringVar()
        self.frame_addCustomer.ent_password=tkinter.ttk.Entry(self.frame_addCustomer, width=40, show="*", textvariable=self.frame_addCustomer.var_password)
        self.frame_addCustomer.chek_password=IntVar()
        self.frame_addCustomer.ent_password.grid(row=3, column=1, pady=8, padx=10)
        self.frame_addCustomer.var_mob = IntVar()
        self.frame_addCustomer.ent_mob=tkinter.ttk.Entry(self.frame_addCustomer, width=40, textvariable=self.frame_addCustomer.var_mob).grid(row=4, column=1, pady=8, padx=10)
        self.frame_addCustomer.chk_password=tkinter.ttk.Checkbutton(self.frame_addCustomer, text="Show Password", padding=6, command=self.show_password, variable=self.frame_addCustomer.chek_password, onvalue=1, offvalue=0)
        self.frame_addCustomer.chk_password.grid(columnspan=2)
        self.frame_addCustomer.imgframe=tkinter.ttk.LabelFrame(self.frame_addCustomer, text="upload photo", height=128, width=110)
        self.frame_addCustomer.imgframe.grid(row=1, column=2, rowspan=3, padx=10)
        self.frame_addCustomer.btn_uploadpic=tkinter.ttk.Button(self.frame_addCustomer, text="Upload photo", command=self.upload_photo)
        self.frame_addCustomer.btn_uploadpic.grid(row=4, column=2)
        self.btnSubmit=tkinter.ttk.Button(self.frame_addCustomer, text="Submit", padding=(3, 3), command=self.action_submit)
        self.btnSubmit.grid(columnspan=2, pady=40)

        self.frame_addCustomer.heading_frame=Frame(self.frame_addCustomer, bg='lightgrey')
        self.frame_addCustomer.heading_frame.grid(columnspan=2)
        self.frame_addCustomer.lbl_heading = Label(self.frame_addCustomer.heading_frame, text="Add Customer",font=('Times New Roman', '18', 'bold', 'italic'), bg='lightgrey', fg='grey')
        self.frame_addCustomer.lbl_heading.grid(columnspan=2, pady=15, padx=120)
        self.frame_addCustomer.lbl_img = Label(self.frame_addCustomer.imgframe, text="hey")
        # add customer ends here

        #search customer

        self.frame_searchCustomer.frame_rbtn=Frame(self.frame_searchCustomer)
        self.frame_searchCustomer.frame_rbtn.pack(pady=8)
        self.frame_searchCustomer.var_rbtn=IntVar()
        self.frame_searchCustomer.rbtn_Id=tkinter.ttk.Radiobutton(self.frame_searchCustomer.frame_rbtn, text="Search by ID", variable=self.frame_searchCustomer.var_rbtn, value=0, command=self.createFrame)
        self.frame_searchCustomer.rbtn_name=tkinter.ttk.Radiobutton(self.frame_searchCustomer.frame_rbtn, text="Search by Name", variable=self.frame_searchCustomer.var_rbtn, value=1, command=self.createFrame)
        self.frame_searchCustomer.rbtn_mob=tkinter.ttk.Radiobutton(self.frame_searchCustomer.frame_rbtn, text="Search by mobile number", variable=self.frame_searchCustomer.var_rbtn, value=2, command=self.createFrame)
        self.frame_searchCustomer.rbtn_Id.grid(row=0, column=0, padx=5, pady=10)
        self.frame_searchCustomer.rbtn_name.grid(row=0, column=1, padx=5)
        self.frame_searchCustomer.rbtn_mob.grid(row=0, column=2, padx=5)
        self.frame_searchCustomer.var_rbtn.set(0)

        self.frame_searchCustomer.frame = Frame(self.frame_searchCustomer)
        self.frame_searchCustomer.frame.pack()
        self.frame_searchCustomer.lbl_searchId = tkinter.ttk.Label(self.frame_searchCustomer.frame, text="Enter your Id")
        self.frame_searchCustomer.lbl_searchId.grid(row=0, column=0, pady=20, padx=5)
        self.frame_searchCustomer.ent_searchId = tkinter.ttk.Entry(self.frame_searchCustomer.frame, width=30)
        self.frame_searchCustomer.ent_searchId.grid(row=0, column=1, pady=10, padx=8)
        self.frame_searchCustomer.btnSubmit = tkinter.ttk.Button(self.frame_searchCustomer.frame, text="Search", padding=(8, 4))
        self.frame_searchCustomer.btnSubmit.grid(columnspan=2, pady=20)
        self.frame_searchCustomer.btnSubmit.bind("<Button-1>", self.action_search)
        self.frame_searchCustomer.txt = Text(self.frame_searchCustomer.frame, width=45, height=5, wrap=WORD)
        self.frame_searchCustomer.txt.grid(columnspan=2, pady=35)

        self.frame_searchCustomer.heading_frame = Frame(self.frame_searchCustomer, bg='lightgrey')
        self.frame_searchCustomer.heading_frame.place(x=0, y=362)
        self.frame_searchCustomer.lbl_heading = Label(self.frame_searchCustomer.heading_frame, text="Search Customer", font=('Times New Roman', '18', 'bold', 'italic'), bg='lightgrey', fg='grey')
        self.frame_searchCustomer.lbl_heading.grid(columnspan=2, pady=15, padx=108)

        # search code ends here

        # delete customer code
        self.frame_deleteCustomer.lbl_deleteId = tkinter.ttk.Label(self.frame_deleteCustomer, text="Enter the Id to be deleted")
        self.frame_deleteCustomer.lbl_deleteId.pack(pady=30, padx=20)
        self.frame_deleteCustomer.var_deleteId=StringVar()
        self.frame_deleteCustomer.ent_deleteId = tkinter.ttk.Entry(self.frame_deleteCustomer, width=40, textvariable=self.frame_deleteCustomer.var_deleteId)
        self.frame_deleteCustomer.ent_deleteId.pack(pady=5, padx=20)
        self.frame_deleteCustomer.btn_delete=tkinter.ttk.Button(self.frame_deleteCustomer, text="Delete", command=self.deleteCustomer, padding=(5, 3))
        self.frame_deleteCustomer.btn_delete.pack(pady=40)

        self.frame_deleteCustomer.heading_frame = Frame(self.frame_deleteCustomer, bg='lightgrey')
        self.frame_deleteCustomer.heading_frame.place(x=0, y=362)
        self.frame_deleteCustomer.lbl_heading = Label(self.frame_deleteCustomer.heading_frame, text="Delete Customer", font=('Times New Roman', '18', 'bold', 'italic'), bg='lightgrey',fg='grey')
        self.frame_deleteCustomer.lbl_heading.grid(columnspan=2, pady=15, padx=108)

        # delete customer code ends here

        # update customer code
        self.frame_updateCustomer.lbl_upId=Label(self.frame_updateCustomer, text="Enter Id to be modified")
        self.frame_updateCustomer.lbl_upId.grid(row=0, column=0, padx=10, pady=18)
        self.frame_updateCustomer.var_upid = StringVar()
        self.frame_updateCustomer.ent_upId=Entry(self.frame_updateCustomer, width=30, textvariable=self.frame_updateCustomer.var_upid)
        self.frame_updateCustomer.ent_upId.grid(row=0, column=1, padx=20, pady=18)
        self.frame_updateCustomer.ent_upId.bind("<Key>", self.update_textPressed)

        self.frame_updateCustomer.frame=Frame(self.frame_updateCustomer)
        self.frame_updateCustomer.frame.grid(columnspan=2, pady=20)
        self.frame_updateCustomer.var_rbtn=IntVar()
        self.frame_updateCustomer.rbtn_mid=tkinter.ttk.Radiobutton(self.frame_updateCustomer.frame, text="modify Id",state="disabled", variable=self.frame_updateCustomer.var_rbtn, value=1, command=self.update_frame)
        self.frame_updateCustomer.rbtn_mid.grid(row=0, column=0, pady=3, padx=4)
        self.frame_updateCustomer.rbtn_mname = tkinter.ttk.Radiobutton(self.frame_updateCustomer.frame, text="modify Name",state="disabled", variable=self.frame_updateCustomer.var_rbtn, value=2, command=self.update_frame)
        self.frame_updateCustomer.rbtn_mname.grid(row=0, column=1, pady=3, padx=4)
        self.frame_updateCustomer.rbtn_mage = tkinter.ttk.Radiobutton(self.frame_updateCustomer.frame, text="modify age",state="disabled", variable=self.frame_updateCustomer.var_rbtn, value=3, command=self.update_frame)
        self.frame_updateCustomer.rbtn_mage.grid(row=0, column=2, pady=3, padx=4)
        self.frame_updateCustomer.rbtn_mpassword = tkinter.ttk.Radiobutton(self.frame_updateCustomer.frame, text="modify password",state="disabled", variable=self.frame_updateCustomer.var_rbtn, value=4, command=self.update_frame)
        self.frame_updateCustomer.rbtn_mpassword.grid(row=0, column=3, pady=3, padx=4)
        self.frame_updateCustomer.var_rbtn.set(1)
        self.frame_updateCustomer.p=re.compile("[a-zA-Z0-9]")

        self.frame_updateCustomer.frame2 = Frame(self.frame_updateCustomer)
        self.frame_updateCustomer.frame2.grid(columnspan=2, pady=10)
        self.frame_updateCustomer.lbl_updatedid = tkinter.ttk.Label(self.frame_updateCustomer.frame2, text="Enter your new Id")
        self.frame_updateCustomer.lbl_updatedid.grid(row=0, column=0, pady=10, padx=5)
        self.frame_updateCustomer.var_updatedid=StringVar()
        self.frame_updateCustomer.ent_updatedid = tkinter.ttk.Entry(self.frame_updateCustomer.frame2, width=35, textvariable=self.frame_updateCustomer.var_updatedid)
        self.frame_updateCustomer.ent_updatedid.grid(row=0, column=1, padx=8, pady=10)
        self.frame_updateCustomer.btn_upsubmit = tkinter.ttk.Button(self.frame_updateCustomer.frame2, text="Submit", padding=(5, 4), command=self.btn_upsubmit_click)
        self.frame_updateCustomer.btn_upsubmit.grid(columnspan=2, pady=30)

        self.frame_updateCustomer.heading_frame = Frame(self.frame_updateCustomer, bg='lightgrey')
        self.frame_updateCustomer.heading_frame.place(x=0, y=362)
        self.frame_updateCustomer.lbl_heading = Label(self.frame_updateCustomer.heading_frame, text="Update Customer", font=('Times New Roman', '18', 'bold', 'italic'), bg='lightgrey', fg='grey')
        self.frame_updateCustomer.lbl_heading.grid(columnspan=2, pady=15, padx=108)

        #update customer code ends here

        self.frame_displayAll.headingframe = tkinter.ttk.Frame(self.frame_displayAll)
        self.frame_displayAll.headingframe.pack(pady=5)

        self.frame_displayAll.headingframe.heading = Label(self.frame_displayAll.headingframe,
                                                           text="Display all Customers",
                                                           font=("Times New Roman", "20", "bold", "italic"),
                                                           bg="lightgrey",
                                                           fg="grey")
        self.frame_displayAll.headingframe.heading.pack(padx=10, pady=30)

        self.frame_displayAll.containerframe = Frame(self.frame_displayAll)
        self.frame_displayAll.containerframe.pack(pady=10)
        self.frame_displayAll.btn_displayAll = tkinter.ttk.Button(self.frame_displayAll.containerframe,
                                                                  text="Display all customers", padding=(4, 4),
                                                                  command=self.btn_displayAll_click)
        self.frame_displayAll.btn_displayAll.pack(pady=20)
        self.frame_displayAll.textcontainer = Frame(self.frame_displayAll.containerframe)
        self.frame_displayAll.textcontainer.pack(side="left", pady=20)
        self.frame_displayAll.vscroll = tkinter.ttk.Scrollbar(self.frame_displayAll.containerframe)
        self.frame_displayAll.vscroll.pack(side=LEFT, fill=Y)
        self.frame_displayAll.hscroll = tkinter.ttk.Scrollbar(self.frame_displayAll.textcontainer, orient="horizontal")

        self.frame_displayAll.txt = Text(self.frame_displayAll.textcontainer, width=50, height=13, wrap="none")
        self.frame_displayAll.txt.config(xscrollcommand=self.frame_displayAll.hscroll.set)
        self.frame_displayAll.txt.config(yscrollcommand=self.frame_displayAll.vscroll.set)
        self.frame_displayAll.txt.pack()
        self.frame_displayAll.hscroll.pack(side="bottom", fill=X)
        self.frame_displayAll.vscroll.config(command=self.frame_displayAll.txt.yview)
        self.frame_displayAll.hscroll.config(command=self.frame_displayAll.txt.xview)

        self.frame_displayAll.rbtncontainer=Frame(self.frame_displayAll)
        self.frame_displayAll.rbtncontainer.pack(pady=10)
        self.frame_displayAll.rbtn_save_txt=tkinter.ttk.Radiobutton(self.frame_displayAll.rbtncontainer, text="Save as text file")
        self.frame_displayAll.rbtn_save_docx=tkinter.ttk.Radiobutton(self.frame_displayAll.rbtncontainer, text="Save as word file")
        self.frame_displayAll.rbtn_save_xls=tkinter.ttk.Radiobutton(self.frame_displayAll.rbtncontainer, text="Save as excel file")
        self.frame_displayAll.var_rbtn_saveAs=IntVar()
        self.frame_displayAll.rbtn_save_txt.config(variable=self.frame_displayAll.var_rbtn_saveAs, value=1, command=self.frame_displayAll_rbtn_save_click)
        self.frame_displayAll.rbtn_save_docx.config(variable=self.frame_displayAll.var_rbtn_saveAs, value=2, command=self.frame_displayAll_rbtn_save_click)
        self.frame_displayAll.rbtn_save_xls.config(variable=self.frame_displayAll.var_rbtn_saveAs, value=3, command=self.frame_displayAll_rbtn_save_click)
        self.frame_displayAll.var_rbtn_saveAs.set(1)
        self.frame_displayAll.rbtn_save_txt.pack(side=LEFT, padx=15)
        self.frame_displayAll.rbtn_save_docx.pack(side=LEFT, padx=15)
        self.frame_displayAll.rbtn_save_xls.pack(side=LEFT, padx=15)
        self.frame_displayAll.displayframe=Frame(self.frame_displayAll)
        self.frame_displayAll.displayframe.pack()

    def action_submit(self):
        val=askquestion("Info", "Do you really want to submit the details?")
        if(val=='yes'):
            cust=Customer()
            cust.custId=self.frame_addCustomer.var_userId.get()
            cust.custName=self.frame_addCustomer.var_name.get()
            cust.custAge=self.frame_addCustomer.var_age.get()
            cust.custPassword=self.frame_addCustomer.var_password.get()
            cust.custMob=self.frame_addCustomer.var_mob.get()
            cust.custPhoto=self.filepath[0]
            cust.add_Customer()
            showinfo("Notification", "Your data successfully added")
        else:
            pass

    def show_password(self):
        if(self.frame_addCustomer.chek_password.get()==1):
            self.frame_addCustomer.ent_password.config(show="")
        else:
            self.frame_addCustomer.ent_password["show"]="*"




root=Tk()

loginFrame=loginForm(root, 200, 100)
root.mainloop()

