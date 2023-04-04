from tkinter import * #IMPORTING TKINTER MODULE
from PIL import  Image, ImageTk #IMPORTING PILLOW
from tkinter import messagebox #IMPORTING MESSAGEBOX
from datetime import date
import time
import mysql.connector #IMPORTING MYSQL CONNECTOR


class CashWithdraw:
    def __init__(self,app):
        global cursor, my_db
        my_db = mysql.connector.connect(host="localhost", user="root", passwd="vaibn",
                                             database="atm_system")  # when databases have to define particulary
        cursor = my_db.cursor()
        cursor.execute("show databases")  # Used to fetch databses / my_cursor.execute("show databases")
        result = cursor.fetchall()
        app=app
        app.geometry("1366x768")
        app.attributes('-fullscreen',True)
        app.title("Indian Bank")
        background(app)

    def background(self,app):
        img = PhotoImage(file='D:\\Python\\B.tech_projects\\Images\\front_png.png')
        label = Label(app, image=img).place(x=0, y=0)
        Resampling = Image.open('D:/Python/B.tech_projects/Images/logo.png')
        resized = Resampling.resize((1362, 225))
        logo_pic = ImageTk.PhotoImage(resized)
        label1 = Label(app, image=logo_pic).grid(row=0, column=0)
        acc_no(app)


    def acc_no(self,app):
        #global acc_entry
        #LABEL CASH WITHDRAW
        comm_label= Label(app,text="Cash Withdraw",font=("Arial",30),bg="#3BB9FF",fg="White").grid(row=2,column=0,pady=10)
        #LABEL ACCOUNT NUMBER
        acc_label = Label(app,text="Account Number",font=("Arial",25,"bold"),bg="#3BB9FF",fg="blue").grid(row=3,column=0,pady=10)

        #ENTRY ACCOUNT NUMBER
        acc_data=StringVar() #STORING VALUE WHICH USER IS ENTRYING
        acc_entry=Entry(app,textvariable=acc_data,bd=5,width=25,font=("bold")) #CREATING ENTRYING
        reg_acc_entry=app.register(fun_acc_entry)#CALLING FUNCTION TO CHECK IT IN A PROPER FORMAT
        acc_entry.config(validate="key",validatecommand=(reg_acc_entry,'%P')) #VALIDATION FUNCTION
        #ACCOUNT SUBMIT BUTTON
        acc_sub_but = Button(app,command=lambda :[user_pin(app)],text="SUBMIT", bg="#3BB9FF", fg="white", width=20, state="disabled")#CREATING ACCOUNT SUBMIT BUTTON

        #PACKING THE ENTRY SECTION
        acc_entry.grid(row=4,column=0,pady=10)
        #PACKING THE ENTRY BUTTON
        acc_sub_but.grid(row=5,column=0,pady=10)
        acc_data.trace('w', my_upd) #CALLING FUNCTION WHICH APPEARS SUBMIT BUTTON WHEN ENTERED DATA IS OK
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
        sql_data = cursor.execute(f"select USER_ACCOUNT from generate_account where USER_ACCOUNT={acc_data.get()}")#GETTING ACCOUNT NUMBER FROM SQL DATABASE
        sql_data_value = cursor.fetchall() #FR=FETCHING VALUE FROM SQL
        sql_data_conv="" #TAKING OUT SQL FETCHED DATA FROM TUPLE TO LIST   (7777777777,)
        #LOOP TO STORE CONVERTING SQL DATA INTO STRING
        for i in sql_data_value:
            sql_data_conv=sql_data_conv+str(i)

        sql2_data=sql_data_conv[2:12]

        if(str(acc_data.get()) in sql_data_conv):

            acc_entry.config(state="disabled")#DISABLE THE ENTRY SECTION SO USER CANT ENTER NEW ACCOUNT NUMBER
            acc_sub_but.config(state="disabled")
            acc_label = Label(app,text="PIN",font=("Arial",25,"bold"),bg="#3BB9FF",fg="blue").grid(row=6,column=0,pady=15)
            pin_data=StringVar()
            pin_entry=Entry(app,textvariable=pin_data,show="*",bd=6,width=15,font=("bold"))
            reg_pin_entry=app.register(fun_pin_entry)
            pin_entry.config(validate="key",validatecommand=(reg_pin_entry,'%P'))

            pin_button=Button(app,command=lambda :[acc_balance(app)],text="Submit", bg="#3BB9FF", fg="white", width=20, state="disabled")

            pin_entry.grid(row=7,column=0,pady=10)
            pin_button.grid(row=8,column=0,pady=10)
            pin_data.trace('w',my_pin)
        else:
            messagebox.showinfo("INVALID","INVALID ACCOUNT")
            app.destroy()

    def my_pin(self,*args):
        if(pin_data.get().isalnum() and len(pin_data.get())==4):
            pin_button.config(state="normal")

        else:
            pin_button.config(state="disabled")

    def fun_pin_entry(self,pin_entry):
        if pin_entry.isdigit() and len(pin_entry)<=4:
            return True
        elif pin_entry=="":
            return True
        else:
            return False

    def acc_balance(self,app):
        pin_entry.config(state='disabled')
        pin_button.config(state='disabled')
        sql_check_acc=cursor.execute(f"select USER_ACCOUNT from amount where USER_ACCOUNT={acc_data.get()}")
        sql_acc_value=cursor.fetchall()
        sql_acc_conv=""
        for i in sql_acc_value:
            sql_acc_conv+=str(i)

        if(str(acc_data.get()) in sql_acc_conv):
            sql_balance_acc = cursor.execute(f"select TOTAL_BALANCE from amount where USER_ACCOUNT={acc_data.get()}")
            sql_balance_value=cursor.fetchall()
            sql_balance_conv1=int(sql_balance_value[0][0])
            if(sql_balance_conv1==0):
                messagebox.showerror('Invalid', "Insufficient balance for withdraw")
                app.destroy()
            else:
                cash_withdraw_label=Label(app,text="ENTER AMOUNT",font=("Arial",25),bg="#3BB9FF",fg="White").grid(row=9,column=0,pady=10)

                withdraw_amount=StringVar()
                cash_withdraw_entry=Entry(app,bd=5,textvariable=withdraw_amount)
                reg_withdraw_entry = app.register(fun_withdraw_entry)
                cash_withdraw_entry.config(validate="key", validatecommand=(reg_withdraw_entry, '%P'))

                cash_withdraw_button=Button(app,text="Withdraw cash",command=lambda:[cash_update(app)], bg="#3BB9FF", fg="white", width=20)

                cash_withdraw_entry.grid(row=10,column=0)
                cash_withdraw_button.grid(row=11, column=0,pady=10)

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
        if(int(withdraw_amount.get())<=int(sql_balance_conv1)):
            ct = time.strftime("%H:%M:%S", t)
            d = date.today()
            t = time.localtime()
            ct = time.strftime("%H:%M:%S", t)
            sql_data = "INSERT INTO cash_withdraw(USER_ACCOUNT,USER_WITHDRAW,DATE,TIME) VALUES (%s,%s,%s,%s)"
            sql_val = (acc_data.get(), withdraw_amount.get(), d, ct)
            cursor.execute(sql_data, sql_val)
            my_db.commit()
            messagebox.showinfo("DONE", "Transmission Completed")
            app.destroy()
            deposite_transaction()
        else:
            messagebox.showerror('Invalid', "Insufficient balance for withdraw")
            app.destroy()

    def deposite_transaction(self):
        sql_amount = cursor.execute(f"select TOTAL_BALANCE from amount where USER_ACCOUNT={acc_data.get()}")
        sql_amount_value = cursor.fetchall()
        sql_prev_bal = sql_amount_value[0][0]
        total_amount = int(sql_prev_bal) - int(withdraw_amount.get())
        sql_find_update = cursor.execute(("update amount SET TOTAL_BALANCE ={} WHERE USER_ACCOUNT={} ").format(total_amount,acc_data.get()))
        my_db.commit()
