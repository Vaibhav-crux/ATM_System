from tkinter import * #IMPORTING TKINTER MODULE
from PIL import  Image, ImageTk #IMPORTING PILLOW
from tkinter import messagebox #IMPORTING MESSAGEBOX
import mysql.connector #IMPORTING MYSQL CONNECTOR

class ResetPIN:
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
        global acc_data
        self.comm_label= Label(app,text="Reset PIN",font=("Arial",30),bg="#3BB9FF",fg="White").grid(row=2,column=0,pady=10)
        #LABEL ACCOUNT NUMBER
        self.acc_label = Label(app,text="Account Number",font=("Arial",25,"bold"),bg="#3BB9FF",fg="blue").grid(row=3,column=0,pady=10)
        #ENTRY ACCOUNT NUMBER
        self.acc_data=StringVar() #STORING VALUE WHICH USER IS ENTRYING
        self.acc_entry=Entry(app,textvariable=self.acc_data,bd=5,width=25,font=("bold")) #CREATING ENTRYING
        self.reg_acc_entry=app.register(self.fun_acc_entry)#CALLING FUNCTION TO CHECK IT IN A PROPER FORMAT
        self.acc_entry.config(validate="key",validatecommand=(self.reg_acc_entry,'%P')) #VALIDATION FUNCTION
        #ACCOUNT SUBMIT BUTTON
        self.store_acc_data=self.acc_data.get()
        self.new_pin_data=""
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
            self.pin_button=Button(app,text="Submit", command=lambda :[self.reset_pin(app)],bg="#3BB9FF", fg="white", width=20, state="disabled")
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

    def reset_pin(self,app):
        self.sql_pin_verify=self.cursor.execute(f"select USER_PIN from generate_account where USER_ACCOUNT={self.acc_data.get()}")
        self.sql_pin_data=self.cursor.fetchall()
        self.sql_pin_data_conv=(self.sql_pin_data[0][0])
        if(self.pin_data.get()==self.sql_pin_data_conv):
            '''import resetpinconf as rpc
            root = Toplevel()
            cw = rpc.OldPinReset(root)
            cw.check_pin(self.acc_data)
            root.mainloop()'''

            import funresetpinconf as frpc
            self.a=self.acc_data.get()
            self.app.destroy()
        # print(self.a)
            frpc.background_for(self.a)

        else:
            messagebox.showwarning('Invalid','Wrong PIN')
            app.destroy()
