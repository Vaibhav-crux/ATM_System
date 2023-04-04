from tkinter import *
from PIL import  Image, ImageTk
from tkinter import messagebox
import random
from datetime import date
import time
import mysql.connector
class OpenAccount:
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
        a=messagebox.askyesno('Creation','Want to open ACCOUNT')
        if(a is True):
            acc_label=Label(app,text="Account Number",font=("Arial",30,'bold'),fg='navy',bg='#3BB9FF').grid(row=1,column=0,pady=10)
            acc_gen_no=""
            for i in range(10):
                acc_gen = random.randint(0,9)
                acc_gen_no+=str(acc_gen)
            sql_acc_no=cursor.execute(f"Select USER_ACCOUNT from GENERATE_ACCOUNT where USER_ACCOUNT={acc_gen_no}")
            sql_fetch_data=cursor.fetchall()
            sql_acc_conv=""
            for k in sql_fetch_data:
                sql_acc_conv=sql_acc_conv+str(k)

            if(str(acc_gen_no) not in sql_acc_conv):
                acc_no_label=Label(app,text=acc_gen_no,fg='white',bg='#3BB9FF',font=('arial',27,'bold')).grid(row=2,column=0,pady=20)
                acc_pin=Label(app,text="Account PIN",fg='navy',bg='#3BB9FF',font=('arial',30,'bold')).grid(row=3,column=0,pady=10)
                pin_gen_no = ""
                for i in range(4):
                    pin_gen = random.randint(0, 9)
                    pin_gen_no+= str(pin_gen)

                pin_label=Label(app,text=pin_gen_no,fg='white',bg='#3BB9FF',font=('arial',27,'bold')).grid(row=4,column=0,pady=30)
                conf_button=Button(app,text="CONFIRM",bg="#3BB9FF",command=lambda :[sql_database(app)],font=('arial',15,'bold')).grid(row=5,column=0)

            else:
                messagebox.showwarning("Invalid","User Already Exist")

        else:
            app.destroy()
    def sql_database(self,app):
        d = date.today()
        t = time.localtime()
        ct = time.strftime("%H:%M:%S", t)
        sql_data = "INSERT INTO generate_account (USER_ACCOUNT,USER_PIN,DATE1,TIME1) VALUES (%s,%s,%s,%s)"
        sql_val = (acc_gen_no,pin_gen_no,d,ct)
        cursor.execute(sql_data, sql_val)
        my_db.commit()
        messagebox.showinfo("Valid","Account Generated")
        app.destroy()
