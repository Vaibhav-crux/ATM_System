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
        self.my_db = mysql.connector.connect(host="localhost", user="root", passwd="vaibn",
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
        self.a=messagebox.askyesno('Creation','Want to open ACCOUNT')
        if(self.a is True):
            self.acc_label=Label(app,text="Account Number",font=("Arial",30,'bold'),fg='navy',bg='#3BB9FF').grid(row=1,column=0,pady=10)
            self.acc_gen_no=""
            for i in range(10):
                self.acc_gen = random.randint(0,9)
                self.acc_gen_no+=str(self.acc_gen)
            self.sql_acc_no=self.cursor.execute(f"Select USER_ACCOUNT from GENERATE_ACCOUNT where USER_ACCOUNT={self.acc_gen_no}")
            self.sql_fetch_data=self.cursor.fetchall()
            self.sql_acc_conv=""
            for k in self.sql_fetch_data:
                self.sql_acc_conv=self.sql_acc_conv+str(k)

            if(str(self.acc_gen_no) not in self.sql_acc_conv):
                self.acc_no_label=Label(app,text=self.acc_gen_no,fg='white',bg='#3BB9FF',font=('arial',27,'bold')).grid(row=2,column=0,pady=20)
                self.acc_pin=Label(app,text="Account PIN",fg='navy',bg='#3BB9FF',font=('arial',30,'bold')).grid(row=3,column=0,pady=10)
                self.pin_gen_no = ""
                for i in range(4):
                    self.pin_gen = random.randint(0, 9)
                    self.pin_gen_no+= str(self.pin_gen)

                self.pin_label=Label(app,text=self.pin_gen_no,fg='white',bg='#3BB9FF',font=('arial',27,'bold')).grid(row=4,column=0,pady=30)
                self.conf_button=Button(app,text="CONFIRM",bg="#3BB9FF",command=lambda :[self.sql_database(app)],font=('arial',15,'bold')).grid(row=5,column=0)

            else:
                messagebox.showwarning("Invalid","User Already Exist")

        else:
            app.destroy()
    def sql_database(self,app):
        self.d = date.today()
        self.t = time.localtime()
        self.ct = time.strftime("%H:%M:%S", self.t)
        self.sql_data = "INSERT INTO generate_account (USER_ACCOUNT,USER_PIN,DATE1,TIME1) VALUES (%s,%s,%s,%s)"
        self.sql_val = (self.acc_gen_no,self.pin_gen_no,self.d,self.ct)
        self.cursor.execute(self.sql_data, self.sql_val)
        self.my_db.commit()
        messagebox.showinfo("Valid","Account Generated")
        self.app.destroy()
