"""
Created on Sun Sep 18 21:53:23 2022
@author: Vaibhav Tiwari
"""
# atm_system DATABASE NAME

from datetime import *
from tkinter import *
from PIL import Image, ImageTk


import mysql.connector
my_db = mysql.connector.connect(host="localhost", user="root",
                                passwd="ankit")  # , database="atm_system") when databases have to define particulary
cursor = my_db.cursor()
cursor.execute("show databases")  # Used to fetch databses / my_cursor.execute("show databases")
result = cursor.fetchall()

datasaver = ''
z = True
while z:
    s = (input("DO YOU WANT TO DELETE PREVIOUS DATA OF atm_system(YES OR NO):"))
    s = s.upper()
    if ((s == "YES") or (s == "NO")):
        z = False
if (s == "YES"):
    c = 0
    tb1 = ('atm_system',)
    for i in range(len(result) - 1):
        if (result[i] == tb1):
            cursor.execute("drop database atm_system")
            c = 1
    if (c == 1):
        cursor.execute("create database atm_system")
    else:
        cursor.execute("create database atm_system")

d = 0
if (s == "NO"):
    c = 0
    tb1 = ("atm_system",)
    for i in result:
        if (i == tb1):
            d = 1
    if (d == 1):
        pass
    else:
        cursor.execute("create database atm_system")

date_time = datetime.now()
print(time)

cursor.execute("use atm_system")
if (c == 1):
    cursor.execute("""CREATE TABLE GENERATE_ACCOUNT
                   (
                    USER_ACCOUNT VARCHAR(12) NOT NULL UNIQUE,
                    USER_PIN VARCHAR(4) ,                     
                    DATE1 VARCHAR(11),
                    TIME1 VARCHAR(11)

                   )""")
    

    cursor.execute(""" CREATE TABLE AMOUNT
                   (
                    USER_ACCOUNT VARCHAR(12) NOT NULL UNIQUE,
                    TOTAL_BALANCE VARCHAR(7) NOT NULL   

                    )""")

    cursor.execute("""CREATE TABLE CASH_DEPOSITE
                   (
                    USER_ACCOUNT VARCHAR(12) NOT NULL,
                    USER_DEPOSITE VARCHAR(12),
                    DATE VARCHAR(11),
                    TIME VARCHAR(15)                                      
                   )""")
    cursor.execute("""CREATE TABLE CASH_WITHDRAW
                       (
                        USER_ACCOUNT VARCHAR(12) NOT NULL,
                        USER_WITHDRAW VARCHAR(12),
                        DATE VARCHAR(11),
                        TIME VARCHAR(15)                                      
                       )""")

app = Tk()
app.title("INDIAN ATM")
app.geometry('1366x768')

app.attributes('-fullscreen',True)


def genpin():
    import accgen as ag
    root = Toplevel()
    cw = ag.OpenAccount(root)
    root.mainloop()




def cash_depos():
    import cashdep as cd
    root = Toplevel()
    cw = cd.CashDeposite(root)
    root.mainloop()



def cash_with():
    import cashwithdraw as cwi
    root = Toplevel()
    cw = cwi.CashWithdraw(root)
    root.mainloop()





def reset_c_pin():
    import resetpin as rp
    root = Toplevel()
    cw = rp.ResetPIN(root)
    root.mainloop()


def main():
    img = PhotoImage(file='D:\\Python\\B.tech_projects\\Images\\front_png.png')
    label = Label(app, image=img).place(x=0, y=0)

    Resampling = Image.open('D:/Python/B.tech_projects/Images/logo.png')
    resized = Resampling.resize((1362, 225))
    logo_pic = ImageTk.PhotoImage(resized)
    label1 = Label(app, image=logo_pic).grid(row=0, column=0)

    widraw_lb = Button(app, text="Cash Withdraw", command=cash_with, bg="#3BB9FF", font=("Arial", 20), width=20).grid(
        row=1, column=0, pady=25)
    depo_lb = Button(app, text="Cash Deposite", command=cash_depos, bg="#3BB9FF", font=("Arial", 20), width=20).grid(
        row=2, column=0, pady=25)
    genpin_lb = Button(app, text="Create Account", command=genpin, bg="#3BB9FF", font=("Arial", 20), width=20).grid(
        row=3, column=0, pady=25)
    resetpin_bu = Button(app, text="Reset Pin", command=reset_c_pin, bg="#3BB9FF", font=("Arial", 20), width=20).grid(
        row=4, column=0, pady=25)
    app.mainloop()

main()

