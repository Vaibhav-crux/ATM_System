from tkinter import * #IMPORTING TKINTER MODULE
from PIL import  Image, ImageTk #IMPORTING PILLOW
from tkinter import messagebox #IMPORTING MESSAGEBOX
from datetime import date
import time
import mysql.connector #IMPORTING MYSQL CONNECTOR


class CashWithdraw:
    def __init__(self,app):
        global cursor, my_db
        self.my_db = mysql.connector.connect(host="localhost", user="root", passwd="ankit",
                                             database="atm_system")  # when databases have to define particulary
        self.cursor = self.my_db.cursor()
        self.cursor.execute("show databases")  # Used to fetch databses / my_cursor.execute("show databases")
        self.result = self.cursor.fetchall()
        self.app=app
        app.geometry("1366x768")
        app.attributes('-fullscreen',True)
        app.title("Indian Bank")
        self.background(app)

    def background(self,app):
        self.img = PhotoImage(file='D:\\Python\\B.tech_projects\\Images\\front_png.png')
        self.label = Label(app, image=self.img).place(x=0, y=0)
        self.Resampling = Image.open('D:/Python/B.tech_projects/Images/logo.png')
        self.resized = self.Resampling.resize((1362, 225))
        self.logo_pic = ImageTk.PhotoImage(self.resized)
        self.label1 = Label(app, image=self.logo_pic).grid(row=0, column=0)
        self.acc_no(app)


    def acc_no(self,app):
        #global acc_entry
        #LABEL CASH WITHDRAW
        self.comm_label= Label(app,text="Cash Withdraw",font=("Arial",30),bg="#3BB9FF",fg="White").grid(row=2,column=0,pady=10)
        #LABEL ACCOUNT NUMBER
        self.acc_label = Label(app,text="Account Number",font=("Arial",25,"bold"),bg="#3BB9FF",fg="blue").grid(row=3,column=0,pady=10)

        #ENTRY ACCOUNT NUMBER
        self.acc_data=StringVar() #STORING VALUE WHICH USER IS ENTRYING
        self.acc_entry=Entry(app,textvariable=self.acc_data,bd=5,width=25,font=("bold")) #CREATING ENTRYING
        self.reg_acc_entry=app.register(self.fun_acc_entry)#CALLING FUNCTION TO CHECK IT IN A PROPER FORMAT
        self.acc_entry.config(validate="key",validatecommand=(self.reg_acc_entry,'%P')) #VALIDATION FUNCTION
        #ACCOUNT SUBMIT BUTTON
        self.acc_sub_but = Button(app,command=lambda :[self.user_pin(app)],text="SUBMIT", bg="#3BB9FF", fg="white", width=20, state="disabled")#CREATING ACCOUNT SUBMIT BUTTON

        #PACKING THE ENTRY SECTION
        self.acc_entry.grid(row=4,column=0,pady=10)
        #PACKING THE ENTRY BUTTON
        self.acc_sub_but.grid(row=5,column=0,pady=10)
        self.acc_data.trace('w', self.my_upd) #CALLING FUNCTION WHICH APPEARS SUBMIT BUTTON WHEN ENTERED DATA IS OK
    #VALIDATING THE SUBMIT BUTTON ACTIVE ONLY WHEN USER ENTER 10 VALUES IN ENTRY SECTION
    def my_upd(self,*args):

        #ENABLE BUTTON ONLY WHEN LENGTH OF VALUE IS 10
        if(self.acc_data.get().isalnum() and len(self.acc_data.get())==10):
            self.acc_sub_but.config(state='normal')
        #DISABLE BUTTON UNTILL LENGTH OF ENTERED VALUE IS NOT 10
        else:
            self.acc_sub_but.config(state='disabled')
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
        self.sql_data = self.cursor.execute(f"select USER_ACCOUNT from generate_account where USER_ACCOUNT={self.acc_data.get()}")#GETTING ACCOUNT NUMBER FROM SQL DATABASE
        self.sql_data_value = self.cursor.fetchall() #FR=FETCHING VALUE FROM SQL
        self.sql_data_conv="" #TAKING OUT SQL FETCHED DATA FROM TUPLE TO LIST   (7777777777,)
        #LOOP TO STORE CONVERTING SQL DATA INTO STRING
        for i in self.sql_data_value:
            self.sql_data_conv=self.sql_data_conv+str(i)

        self.sql2_data=self.sql_data_conv[2:12]

        if(str(self.acc_data.get()) in self.sql_data_conv):

            self.acc_entry.config(state="disabled")#DISABLE THE ENTRY SECTION SO USER CANT ENTER NEW ACCOUNT NUMBER
            self.acc_sub_but.config(state="disabled")
            self.acc_label = Label(app,text="PIN",font=("Arial",25,"bold"),bg="#3BB9FF",fg="blue").grid(row=6,column=0,pady=15)
            self.pin_data=StringVar()
            self.pin_entry=Entry(app,textvariable=self.pin_data,show="*",bd=6,width=15,font=("bold"))
            self.reg_pin_entry=app.register(self.fun_pin_entry)
            self.pin_entry.config(validate="key",validatecommand=(self.reg_pin_entry,'%P'))

            self.pin_button=Button(app,command=lambda :[self.acc_balance(app)],text="Submit", bg="#3BB9FF", fg="white", width=20, state="disabled")

            self.pin_entry.grid(row=7,column=0,pady=10)
            self.pin_button.grid(row=8,column=0,pady=10)
            self.pin_data.trace('w',self.my_pin)
        else:
            messagebox.showinfo("INVALID","INVALID ACCOUNT")
            app.destroy()

    def my_pin(self,*args):
        if(self.pin_data.get().isalnum() and len(self.pin_data.get())==4):
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
        self.pin_entry.config(state='disabled')
        self.pin_button.config(state='disabled')
        self.sql_check_acc=self.cursor.execute(f"select USER_ACCOUNT from amount where USER_ACCOUNT={self.acc_data.get()}")
        self.sql_acc_value=self.cursor.fetchall()
        self.sql_acc_conv=""
        for i in self.sql_acc_value:
            self.sql_acc_conv+=str(i)

        if(str(self.acc_data.get()) in self.sql_acc_conv):
            self.sql_balance_acc = self.cursor.execute(f"select TOTAL_BALANCE from amount where USER_ACCOUNT={self.acc_data.get()}")
            self.sql_balance_value=self.cursor.fetchall()
            self.sql_balance_conv1=int(self.sql_balance_value[0][0])
            if(self.sql_balance_conv1==0):
                messagebox.showerror('Invalid', "Insufficient balance for withdraw")
                app.destroy()
            else:
                self.cash_withdraw_label=Label(app,text="ENTER AMOUNT",font=("Arial",25),bg="#3BB9FF",fg="White").grid(row=9,column=0,pady=10)

                self.withdraw_amount=StringVar()
                self.cash_withdraw_entry=Entry(app,bd=5,textvariable=self.withdraw_amount)
                self.reg_withdraw_entry = app.register(self.fun_withdraw_entry)
                self.cash_withdraw_entry.config(validate="key", validatecommand=(self.reg_withdraw_entry, '%P'))

                self.cash_withdraw_button=Button(app,text="Withdraw cash",command=lambda:[self.cash_update(app)], bg="#3BB9FF", fg="white", width=20)

                self.cash_withdraw_entry.grid(row=10,column=0)
                self.cash_withdraw_button.grid(row=11, column=0,pady=10)

        else:
            messagebox.showerror('Invalid', "No Data Found")
            app.destroy()

    def fun_withdraw_entry(self,cash_withdraw_entry):
        if cash_withdraw_entry.isdigit() and len(cash_withdraw_entry)<=6:
            return True
        elif cash_withdraw_entry == "":
            return True
        else:
            return False

    def cash_update(self,app):
        if(int(self.withdraw_amount.get())<=int(self.sql_balance_conv1)):
            self.t = time.localtime()
            self.ct = time.strftime("%H:%M:%S", self.t)
            self.d = date.today()
            self.t = time.localtime()
            self.ct = time.strftime("%H:%M:%S", self.t)
            self.sql_data = "INSERT INTO cash_withdraw(USER_ACCOUNT,USER_WITHDRAW,DATE,TIME) VALUES (%s,%s,%s,%s)"
            self.sql_val = (self.acc_data.get(), self.withdraw_amount.get(), self.d, self.ct)
            self.cursor.execute(self.sql_data, self.sql_val)
            self.my_db.commit()
            messagebox.showinfo("DONE", "Transmission Completed")
            self.app.destroy()
            self.deposite_transaction()
        else:
            messagebox.showerror('Invalid', "Insufficient balance for withdraw")
            app.destroy()

    def deposite_transaction(self):
        self.sql_amount = self.cursor.execute(f"select TOTAL_BALANCE from amount where USER_ACCOUNT={self.acc_data.get()}")
        self.sql_amount_value = self.cursor.fetchall()
        self.sql_prev_bal = self.sql_amount_value[0][0]
        self.total_amount = int(self.sql_prev_bal) - int(self.withdraw_amount.get())
        self.sql_find_update = self.cursor.execute(("update amount SET TOTAL_BALANCE ={} WHERE USER_ACCOUNT={} ").format(self.total_amount,self.acc_data.get()))
        self.my_db.commit()
