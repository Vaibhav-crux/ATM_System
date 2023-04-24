from tkinter import * #IMPORTING TKINTER MODULE
from PIL import  Image, ImageTk #IMPORTING PILLOW
from tkinter import messagebox #IMPORTING MESSAGEBOX
import mysql.connector #IMPORTING MYSQL CONNECTOR
def background_for(a):
    app=Toplevel()
    app.geometry("1366x768")
    app.attributes('-fullscreen',True)
    global cursor, my_db
    my_db = mysql.connector.connect(host="localhost", user="root", passwd="ankit",
                                         database="atm_system")  # when databases have to define particulary
    cursor = my_db.cursor()
    cursor.execute("show databases")  # Used to fetch databses / my_cursor.execute("show databases")
    result = cursor.fetchall()
    app.title("Indian Bank")
    background(app,a)

def background(app,a):
    img = PhotoImage(file='D:\\Python\\B.tech_projects\\Images\\front_png.png')
    label = Label(app, image=img).place(x=0, y=0)
    Resampling = Image.open('D:/Python/B.tech_projects/Images/logo.png')
    resized = Resampling.resize((1362, 225))
    logo_pic = ImageTk.PhotoImage(resized)
    label1 = Label(app, image=logo_pic).grid(row=0, column=0)
    new_pin(app,a)
    app.mainloop()
def new_pin(app,a):
        #NEW PIN ENTRY
    label1_pin=Label(app,text="Enter New PIN",font=("arial",30,'bold'),bg="#3BB9FF",fg="blue").grid(row=1,column=0,pady=20)
    new_pin_data=StringVar()
    new_pin_entry=Entry(app,textvariable=new_pin_data,show="*",bd=6,width=15,font=("bold"))
    reg_new_pin_entry=app.register(fun_new_pin_entry)
    new_pin_entry.config(validate='key',validatecommand=(reg_new_pin_entry,'%P'))


        #CONF NEW PIN ENTRY
    label1_pin = Label(app, text="Re-enter New PIN", font=("arial", 30, 'bold'), bg="#3BB9FF", fg="blue").grid( row=3, column=0, pady=20)
    new_pin_conf_data=StringVar()
    new_pin_conf_entry=Entry(app,textvariable=new_pin_conf_data,show="*",bd=6,width=15,font=("bold"))
    reg_new_conf_pin_entry=app.register(fun_conf_new_pin_entry)
    new_pin_conf_entry.config(validate='key', validatecommand=(reg_new_conf_pin_entry, '%P'))

        #CONF PIN BUTTON
    new_pin_button=Button(app,text="Submit",command=lambda :[check_pin(app,a,new_pin_data,new_pin_conf_data)],bg="#3BB9FF", fg="white", width=20)

    new_pin_entry.grid(row=2,column=0,pady=10)
    new_pin_conf_entry.grid(row=4,column=0,pady=10)
    new_pin_button.grid(row=8, column=0, pady=10)
        
def fun_new_pin_entry(new_pin_entry):
    if(new_pin_entry.isdigit() and len(new_pin_entry)<=4): #ENTRING ONLY INTEGER VALUE WITH LESS THEN 11 DIGIT
        return True
    elif new_pin_entry=="":#IF THE ENTRY IS EMPTY THEN IT CAN BE ACCEPTED (otherwise the 1st value inserted by user can't be deleted once inserted)
        return True
    else: #IT WILL NOT ACCEPT THE CHAR OR ANY SPECIAL VALUES
        return False

def fun_conf_new_pin_entry(new_pin_conf_entry):
    if (new_pin_conf_entry.isdigit() and len(new_pin_conf_entry) <= 4):  # ENTRING ONLY INTEGER VALUE WITH LESS THEN 11 DIGIT
        return True
    elif new_pin_conf_entry == "":  # IF THE ENTRY IS EMPTY THEN IT CAN BE ACCEPTED (otherwise the 1st value inserted by user can't be deleted once inserted)
        return True
    else:  # IT WILL NOT ACCEPT THE CHAR OR ANY SPECIAL VALUES
        return False

def check_pin(app,a,new_pin_data,new_pin_conf_data):
    if((new_pin_data.get())==(new_pin_conf_data.get())):

        sql_update_pin=cursor.execute(f"select USER_PIN from generate_account where USER_ACCOUNT={a}")
        sql_acc=cursor.fetchall()
        acc_conv=sql_acc[0][0]
        if(acc_conv==new_pin_data.get()):
            messagebox.showerror("Invalid","Repeated PIN Invalid")
        else:
            sql_pin_update=cursor.execute(f"update generate_account SET USER_PIN ={new_pin_data.get()} WHERE USER_ACCOUNT={a} ")
            my_db.commit()
            messagebox.showinfo("Valide", "PIN Changed")
            app.destroy()


    else:
        messagebox.showerror("Invalid","PIN Does Not Match")
    app.mainloop()
