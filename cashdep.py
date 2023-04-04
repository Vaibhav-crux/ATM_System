from tkinter import * #IMPORTING TKINTER MODULE
from PIL import  Image, ImageTk #IMPORTING PILLOW
from tkinter import messagebox #IMPORTING MESSAGEBOX
from datetime import date
import time
import mysql.connector #IMPORTING MYSQL CONNECTOR

class CashDeposite:
    def __init__(self,app):
        global cursor, my_db
        my_db = mysql.connector.connect(host="localhost", user="root", passwd="vaibn",
                                             database="atm_system")  # when databases have to define particulary
        cursor = self.my_db.cursor()
        cursor.execute("show databases")  # Used to fetch databses / my_cursor.execute("show databases")
        result = self.cursor.fetchall()
        app=app
        app.geometry("1366x768")

        #Grid.rowconfigure(app,0,weight=1)
        #Grid.columnconfigure(app,0,weight=1)
        app.attributes('-fullscreen',True)
        app.title("Indian Bank")
        background(app)

    def background(self,app):
        img = PhotoImage(file='D:\\Python\\B.tech_projects\\Images\\front_png.png')
        label = Label(app, image=self.img).place(x=0, y=0)
        Resampling = Image.open('D:/Python/B.tech_projects/Images/logo.png')
        resized = self.Resampling.resize((1362, 225))
        logo_pic = ImageTk.PhotoImage(self.resized)
        label1 = Label(app, image=self.logo_pic).grid(row=0, column=0)
        acc_no(app)


    def acc_no(self,app):
        #global acc_entry
        #LABEL CASH WITHDRAW
        comm_label= Label(app,text="Cash Deposite",font=("Arial",30),bg="#3BB9FF",fg="White").grid(row=2,column=0,pady=10)
        #LABEL ACCOUNT NUMBER
        acc_label = Label(app,text="Account Number",font=("Arial",25,"bold"),bg="#3BB9FF",fg="blue").grid(row=3,column=0,pady=10)

        #ENTRY ACCOUNT NUMBER
        acc_data=StringVar() #STORING VALUE WHICH USER IS ENTRYING
        acc_entry=Entry(app,textvariable=self.acc_data,bd=5,width=25,font=("bold")) #CREATING ENTRYING
        reg_acc_entry=app.register(self.fun_acc_entry)#CALLING FUNCTION TO CHECK IT IN A PROPER FORMAT
        acc_entry.config(validate="key",validatecommand=(self.reg_acc_entry,'%P')) #VALIDATION FUNCTION
        #ACCOUNT SUBMIT BUTTON
        acc_sub_but = Button(app,command=lambda :[self.user_pin(app)],text="SUBMIT", bg="#3BB9FF", fg="white", width=20, state="disabled")#CREATING ACCOUNT SUBMIT BUTTON

        #PACKING THE ENTRY SECTION
        acc_entry.grid(row=4,column=0,pady=10)
        #PACKING THE ENTRY BUTTON
        acc_sub_but.grid(row=5,column=0,pady=10)
        acc_data.trace('w', self.my_upd) #CALLING FUNCTION WHICH APPEARS SUBMIT BUTTON WHEN ENTERED DATA IS OK
    #VALIDATING THE SUBMIT BUTTON ACTIVE ONLY WHEN USER ENTER 10 VALUES IN ENTRY SECTION
    def my_upd(self,*args):

        #ENABLE BUTTON ONLY WHEN LENGTH OF VALUE IS 10
        if(acc_data.get().isalnum() and len(acc_data.get())==10):
            acc_sub_but.config(state='normal')
        #DISABLE BUTTON UNTILL LENGTH OF ENTERED VALUE IS NOT 10
        else:
            acc_sub_but.config(state='disabled')
    #VALIDATING THAT USER CAN ENTER ATLEAST 10 INTEGER VALUE
    def fun_acc_entry(self,acc_entry):
        if(acc_entry.isdigit() and len(acc_entry)<=10): #ENTRING ONLY INTEGER VALUE WITH LESS THEN 11 DIGIT
            return True
        elif acc_entry=="":#IF THE ENTRY IS EMPTY THEN IT CAN BE ACCEPTED (otherwise the 1st value inserted by user can't be deleted once inserted)
           return True
        else: #IT WILL NOT ACCEPT THE CHAR OR ANY SPECIAL VALUES
            return False

    def user_pin(self,app):
        # SQL QUERY TO GET ACCOUNT NUMBER
        sql_data = self.cursor.execute(f"select USER_ACCOUNT from generate_account where USER_ACCOUNT={self.acc_data.get()}")#GETTING ACCOUNT NUMBER FROM SQL DATABASE
        sql_data_value = self.cursor.fetchall() #FR=FETCHING VALUE FROM SQL
        sql_data_conv="" #TAKING OUT SQL FETCHED DATA FROM TUPLE TO LIST   (7777777777,)
        #LOOP TO STORE CONVERTING SQL DATA INTO STRING
        for i in self.sql_data_value:
            sql_data_conv=self.sql_data_conv+str(i)

        sql2_data=self.sql_data_conv[2:12]

        if(str(acc_data.get()) in sql_data_conv):

            acc_entry.config(state="disabled")#DISABLE THE ENTRY SECTION SO USER CANT ENTER NEW ACCOUNT NUMBER
            acc_sub_but.config(state="disabled")
            acc_label = Label(app,text="PIN",font=("Arial",25,"bold"),bg="#3BB9FF",fg="blue").grid(row=6,column=0,pady=15)
            pin_data=StringVar()
            pin_entry=Entry(app,textvariable=self.pin_data,show="*",bd=6,width=15,font=("bold"))
            reg_pin_entry=app.register(self.fun_pin_entry)
            pin_entry.config(validate="key",validatecommand=(self.reg_pin_entry,'%P'))

            pin_button=Button(app,command=lambda :[self.acc_balance(app)],text="Submit", bg="#3BB9FF", fg="white", width=20, state="disabled")

            pin_entry.grid(row=7,column=0,pady=10)
            pin_button.grid(row=8,column=0,pady=10)
            pin_data.trace('w',self.my_pin)
        else:
            messagebox.showinfo("INVALID","INVALID ACCOUNT")

    def my_pin(self,*args):
        if(pin_data.get().isalnum() and len(pin_data.get())==4):
            self.pin_button.config(state="normal")

        else:
            self.pin_button.config(state="disabled")

    def fun_pin_entry(self,pin_entry):
        if pin_entry.isdigit() and len(pin_entry)<=4:
            return True
        elif pin_entry=="":
            return True
        else:
            return False

    def acc_balance(self,app):
        sql_data = self.cursor.execute(f"select USER_PIN from generate_account where USER_ACCOUNT={self.acc_data.get()}")  # GETTING ACCOUNT NUMBER FROM SQL DATABASE
        sql_pin_value = self.cursor.fetchall()  # FR=FETCHING VALUE FROM SQL
        sql_pin_conv=""
        for i in self.sql_pin_value:
            sql_pin_conv+=str(i)

        if(str(pin_data.get()) in sql_pin_conv):
            pin_entry.config(state="disabled")
            pin_button.config(state="disabled")
            acc_bal_label=Label(app,text="ENTER AMOUNT",bg="#3BB9FF",font=('Arial',20,'bold'),fg="blue").grid(row=9,column=0,pady=5)
        #BALANACE ENTRY
            bal_data=StringVar()
            acc_bal_enter=Entry(app,textvariable=self.bal_data,bd=6,width=10,font=("bold"))
            reg_bal_entry=app.register(self.fun_bal_entry)
            acc_bal_enter.config(validate="key",validatecommand=(self.reg_bal_entry,'%P'))
        #BALANCE BUTTON
            acc_bal_button=Button(app,command=lambda :[self.cash_deposite_exit(app)],text="DEPOSITE CASH",bg="#3BB9FF",fg="White",width=20)
            acc_bal_enter.grid(row=10,column=0,pady=5)
            acc_bal_button.grid(row=11,column=0)
        else:
            messagebox.showerror("Invalid","Invalid PIN")


    def fun_bal_entry(self,acc_bal_entry):
        if(acc_bal_entry.isdigit() and len(acc_bal_entry)<=6):
            return True
        elif acc_bal_entry=="":
            return True
        else:
            return False

    def cash_deposite_exit(self,app):

        if(int(bal_data.get())>0):

            t = time.localtime()
            ct = time.strftime("%H:%M:%S", self.t)
            d = date.today()
            t = time.localtime()
            ct = time.strftime("%H:%M:%S", self.t)
            sql_data="INSERT INTO cash_deposite(USER_ACCOUNT,USER_DEPOSITE,DATE,TIME) VALUES (%s,%s,%s,%s)"
            sql_val=(self.acc_data.get(),self.bal_data.get(),self.d,self.ct)
            cursor.execute(self.sql_data,self.sql_val)
            my_db.commit()
            messagebox.showinfo("DONE", "Transmission Completed")
            app.destroy()
            deposite_transaction()

        else:
            messagebox.showwarning('INVALID','0 Balance cant deposite')
            app.destroy()

    def deposite_transaction(self):

        sql_acc_check = self.cursor.execute(f"select USER_ACCOUNT from amount where USER_ACCOUNT={self.acc_data.get()}")
        sql_acc_value = self.cursor.fetchall()
        sql_acc_conv = ""
        for i in self.sql_acc_value:
            sql_acc_conv += str(i)  # (77777777777,)
        pre_bal = self.sql_acc_conv[2:12]

        if (self.acc_data.get() in self.sql_acc_conv):
            sql_amount = self.cursor.execute(f"select TOTAL_BALANCE from amount where USER_ACCOUNT={self.acc_data.get()}")
            sql_amount_value = self.cursor.fetchall()
            sql_prev_bal = self.sql_amount_value[0][0]
            total_amount = int(self.sql_prev_bal) + int(self.bal_data.get())
            sql_find_update=self.cursor.execute(("update amount SET TOTAL_BALANCE ={} WHERE USER_ACCOUNT={} ").format(self.total_amount,self.acc_data.get()))
            my_db.commit()


        else:
            self.sql_data="INSERT INTO amount (USER_ACCOUNT,TOTAL_BALANCE) VALUES (%s,%s)"
            self.sql_val=(self.acc_data.get(),self.bal_data.get())
            self.cursor.execute(self.sql_data,self.sql_val)
            self.my_db.commit()
            
