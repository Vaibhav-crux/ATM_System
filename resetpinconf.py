from tkinter import * #IMPORTING TKINTER MODULE
from PIL import  Image, ImageTk #IMPORTING PILLOW
from tkinter import messagebox #IMPORTING MESSAGEBOX
import mysql.connector #IMPORTING MYSQL CONNECTOR
from resetpin import ResetPIN

class OldPinReset():
    def __init__(self,app):
        global cursor, my_db
        self.my_db = mysql.connector.connect(host="localhost", user="root", passwd="vaibn",
                                             database="atm_system")  # when databases have to define particulary
        self.cursor = self.my_db.cursor()
        self.cursor.execute("show databases")  # Used to fetch databses / my_cursor.execute("show databases")
        self.result = self.cursor.fetchall()
        self.app=app
        app.geometry("1920x1024")
        app.title("Indian Bank")
        self.background(app)

    def background(self,app):
        self.img = PhotoImage(file='D:\\Python\\B.tech_projects\\Images\\front_png.png')
        self.label = Label(app, image=self.img).place(x=0, y=0)
        self.Resampling = Image.open('D:/Python/B.tech_projects/Images/logo.png')
        self.resized = self.Resampling.resize((1530, 225))
        self.logo_pic = ImageTk.PhotoImage(self.resized)
        self.label1 = Label(app, image=self.logo_pic).grid(row=0, column=0)
        self.new_pin(app)
    def new_pin(self,app):
        #NEW PIN ENTRY
        self.label1_pin=Label(app,text="Enter New PIN",font=("arial",30,'bold'),bg="#3BB9FF",fg="blue").grid(row=1,column=0,pady=20)
        self.new_pin_data=StringVar()
        self.new_pin_entry=Entry(app,textvariable=self.new_pin_data,show="*",bd=6,width=15,font=("bold"))
        self.reg_new_pin_entry=app.register(self.fun_new_pin_entry)
        self.new_pin_entry.config(validate='key',validatecommand=(self.reg_new_pin_entry,'%P'))
        #CONF NEW PIN ENTRY
        self.label1_pin = Label(app, text="Re-enter New PIN", font=("arial", 30, 'bold'), bg="#3BB9FF", fg="blue").grid( row=3, column=0, pady=20)
        self.new_pin_conf_data=StringVar()
        self.new_pin_conf_entry=Entry(app,textvariable=self.new_pin_conf_data,show="*",bd=6,width=15,font=("bold"))
        self.reg_new_conf_pin_entry=app.register(self.fun_conf_new_pin_entry)
        self.new_pin_conf_entry.config(validate='key', validatecommand=(self.reg_new_conf_pin_entry, '%P'))
        #CONF PIN BUTTON
        self.new_pin_button=Button(app,text="Submit",command=lambda :[self.check_pin()],bg="#3BB9FF", fg="white", width=20, state="disabled")
        self.new_pin_entry.grid(row=2,column=0,pady=10)
        self.new_pin_conf_entry.grid(row=4,column=0,pady=10)
        self.new_pin_button.grid(row=8, column=0, pady=10)
        self.new_pin_conf_data.trace('w', self.my_pin)
    def fun_new_pin_entry(self,new_pin_entry):
        if(new_pin_entry.isdigit() and len(new_pin_entry)<=4): #ENTRING ONLY INTEGER VALUE WITH LESS THEN 11 DIGIT
            return True
        elif new_pin_entry=="":#IF THE ENTRY IS EMPTY THEN IT CAN BE ACCEPTED (otherwise the 1st value inserted by user can't be deleted once inserted)
           return True
        else: #IT WILL NOT ACCEPT THE CHAR OR ANY SPECIAL VALUES
            return False

    def fun_conf_new_pin_entry(self,new_pin_conf_entry):
        if (new_pin_conf_entry.isdigit() and len(new_pin_conf_entry) <= 4):  # ENTRING ONLY INTEGER VALUE WITH LESS THEN 11 DIGIT
            return True
        elif new_pin_conf_entry == "":  # IF THE ENTRY IS EMPTY THEN IT CAN BE ACCEPTED (otherwise the 1st value inserted by user can't be deleted once inserted)
            return True
        else:  # IT WILL NOT ACCEPT THE CHAR OR ANY SPECIAL VALUES
            return False

    def my_pin(self,*args):
        if(self.new_pin_conf_data.get().isalnum() and len(self.new_pin_conf_data.get())==4):
            self.new_pin_button.config(state="normal")

        else:
            self.new_pin_button.config(state="disabled")

    def check_pin(self):
        if((self.new_pin_data.get())==(self.new_pin_conf_data.get())):
            self.aa=self.new_pin_data.get()
        else:
            messagebox.showerror("Invalid","Password not matched")
