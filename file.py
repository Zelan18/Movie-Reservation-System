#FILE1(SIGN UP PAGE)
from tkinter import *
from tkinter import font
from tkinter import messagebox
import mysql.connector
import sys
from mysql.connector import Error
from mysql.connector import errorcode

global Username
global password
global Rewrite_Password


def reg():
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="jugaldb")
        mycursor = mydb.cursor()
        username = Username.get()
        print(username)
        password = Password.get()
        print(password)
        rewrite_password = Rewrite_Password.get()
        print(rewrite_password)
        sql = "insert into signup(Username,Password,Rewrite_Password) values (%s,%s,%s)"
        val = (username, password,rewrite_password)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Successfully inserted")
        messagebox.showinfo("status", "jugaldb")
    except mysql.connector.Error as error:
        print("failed to update record to database: {}".format(error))


def singleclk(event):
    button.configure(bg="green", fg="yellow")


def cancel():
    messagebox.showinfo("cancel", "canceled")
    sys.exit()


def clk(event):
    button.configure(bg="red", fg="yellow")


win = Tk()
win.minsize(600, 450)
# title
win.title("USERNAME")
# heading
myFont = font.Font(family="cooper", size=20, weight="bold")
lable = Label(win, text="SignUp", font=myFont, bg="white", fg="black")
lable.grid(row=0, column=3)

# for image
# photo = PhotoImage(file="show.png")
# label = Label(image=photo)
# label.pack()

# Username
label1 = Label(win, text="Username")
label1.grid(row=1, column=0)
Username = Entry(win, bd=5)
Username.grid(row=1, column=1)

# password
label2 = Label(win, text="Password")
label2.grid(row=2, column=0)
Password = Entry(win, bd=5)
Password.grid(row=2, column=1)

#RE-WRITE PASSWORD
label3 = Label(win, text="Rewrite_Password")
label3.grid(row=3, column=0)
Rewrite_Password = Entry(win, bd=5)
Rewrite_Password.grid(row=3, column=1)

# submit
button = Button(win, text="Submit", command=reg)
button.grid(row=4, column=0)
button.bind('<Enter>', singleclk)
# cancel
button1 = Button(win, text="cancel", command=cancel)
button1.grid(row=4, column=1)
button1.bind('<Enter>', clk)
win.mainloop()




#FILE2(LOGIN PAGE)
from tkinter import *
from tkinter import font
from tkinter import messagebox
import mysql.connector
import sys
from mysql.connector import Error
from mysql.connector import errorcode




def reg():
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="jugaldb")
        mycursor = mydb.cursor()
        username = Username.get()
        print(username)
        password = Password.get()
        print(password)
        sql = "insert into login(Username,Password) values (%s,%s)"
        val = (username, password)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Successfully Login")
        messagebox.showinfo("status", "jugaldb")
    except mysql.connector.Error as error:
        print("failed to update record to database: {}".format(error))


def singleclk(event):
    button.configure(bg="green", fg="yellow")


from tkinter import *
from tkinter import font
from tkinter import messagebox
import mysql.connector
import sys
from mysql.connector import Error
from mysql.connector import errorcode




def reg():
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="jugaldb")
        mycursor = mydb.cursor()
        username = Username.get()
        print(username)
        password = Password.get()
        print(password)
        sql = "insert into login(Username,Password) values (%s,%s)"
        val = (username, password)
        mycursor.execute(sql, val)
        mydb.commit()
        print("inserted")
        messagebox.showinfo("status", "jugaldb")
    except mysql.connector.Error as error:
        print("failed to update record to database: {}".format(error))


def cancel():
    messagebox.showinfo("cancel", "canceled")
    sys.exit()


def clk(event):
    button.configure(bg="red", fg="yellow")


win = Tk()
win.minsize(600, 450)
# title
win.title("USERNAME")
# heading
myFont = font.Font(family="cooper", size=20, weight="bold")
lable = Label(win, text="Login page", font=myFont, bg="white", fg="black")
lable.grid(row=0, column=3)

# for image
# photo = PhotoImage(file="show.png")
# label = Label(image=photo)
# label.pack()

# Username
label1 = Label(win, text="Username")
label1.grid(row=1, column=0)
Username = Entry(win, bd=5)
Username.grid(row=1, column=1)
# password
label2 = Label(win, text="Password")
label2.grid(row=2, column=0)
Password = Entry(win, bd=5)
Password.grid(row=2, column=1)
# submit
button = Button(win, text="Submit", command=reg)
button.grid(row=3, column=0)
button.bind('<Enter>', singleclk)
# cancel
button1 = Button(win, text="cancel", command=cancel)
button1.grid(row=3, column=1)
button1.bind('<Enter>', clk)
win.mainloop()






#MAIN FILE (BOOKMYMOVIE)
import tkinter
from tkinter import *
import webbrowser
import tkinter.font as font
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import sys
from mysql.connector import Error
from mysql.connector import errorcode

global Name
global Email
global MovieName
global No_of_ticket
global Timing
global Above18


def ok():
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="jugaldb")
        mycursor = mydb.cursor()
        Name = e1.get()
        print(Name)
        Email = e2.get()
        print(Email)
        MovieName = e3.get()
        print(MovieName)
        No_of_ticket = dropdown.get()
        print(No_of_ticket)
        Timing = var.get()
        print(Timing)
        Above18 = var1.get()
        print(Above18)

        sql = "insert into movie(Name,Email,MovieName,No_of_ticket,Timing,Above18) values (%s,%s,%s,%s,%s,%s)"
        val = (Name,Email,MovieName,No_of_ticket,Timing,Above18)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Successfully inserted!!!")
        messagebox.showinfo("status", "Your ticket is successfully booked")
    except mysql.connector.Error as error:
        print("failed to update record to database: {}".format(error))


master = tk.Tk()
master.title("BOOK MY MOVIE")
master.configure(bg='#483C32')


def go_to_first():
    f1.pack()
    f2.pack_forget()


Label(master, text="Book my Movie", bd=2, font=("Comic Sans MS", 55), relief=RIDGE, bg="#990012", fg="#E4287C",width="100", height="2").pack()


def go_to_second():
    f1.pack_forget()
    f2.pack()




def onClick(x):
    webbrowser.open(x, new=1)
url = "https://youtu.be/tsxemFX0a7k"



f1 = tk.Frame(master)

pilImage = Image.open("imgmovie.jpg")
i = ImageTk.PhotoImage(pilImage)
a = Label(image=i)
a.pack()

f2 = tk.Frame(master)

b1 = tk.Button(f1, text="Book Tickets", width=20, bd=5, relief=RIDGE, font=("Arial Black", 20), bg="green", fg="white",command=go_to_second).grid(row=1, column=1)

b2 = tk.Button(f1, text="Watch Trailer", width=20, bd=5, relief=RIDGE, font=("Arial Black", 20), bg="blue", fg="black",command=lambda:onClick(url)).grid(row=1, column=2)
master.configure(bg='#483C32')
l1 = Label(f2, text="Enter Name", font=("Arial Black", 10), fg="#D4A017").grid(row=0, column=0)
e1 = Entry(f2, width=19)
e1.grid(row=0, column=1)

l2 = Label(f2, text="Enter Email-Id", font=("Arial Black", 10), fg="#D4A017").grid(row=1, column=0)
e2 = Entry(f2, width=19)
e2.grid(row=1, column=1)

l2 = Label(f2, text="Enter Name of the Movie", font=("Arial Black", 10), fg="#D4A017").grid(row=2, column=0)


e3 = Entry(f2)
e3.grid(row=2, column=1)
v2 = StringVar()
l3 = Label(f2, text="No of Tickets", font=("Arial Black", 10), fg="#D4A017").grid(row=3, column=0)
dropdown = Spinbox(f2, from_=1, to=40)
dropdown.grid(row=3, column=1)

l4 = Label(f2, text="Timing", font=("Arial Black", 10), fg="#D4A017").grid(row=4, column=0)
var = IntVar()
ge = Radiobutton(f2, text="11:00am to 2:00pm", font=("Arial Black", 10), fg="#D4A017", variable=var, value=1)
ge.grid(row=4, column=1)

gb = Radiobutton(f2, text="4:00pm to 7:00pm", font=("Arial Black", 10), fg="#D4A017", variable=var, value=2)
gb.grid(row=4,column=2)

var1 = IntVar()
l5 = Label(f2, text="Terms&condition", font=("Arial Black", 10), fg="#D4A017").grid(row=6, column=0)
ck = Checkbutton(f2, text="Above18 ", font=("Arial Black", 10), fg="#D4A017", variable=var1, height=2, width=10,onvalue=1, offvalue=0)
ck.grid(row=6, column=1)

b2 = tk.Button(f2, text="Back", bd=3, font=("Arial Black", 20), bg="#617C58", fg="#6CBB3C", width=16, command=go_to_first).grid(row=7, column=0)
b2 = tk.Button(f2, text="Confirm", bd=3, font=("Arial Black", 20), bg="#617C58", fg="#6CBB3C", width=16, command=ok).grid(row=7,column=3)
b2 = tk.Button(f2, text="Update Booking", bd=3, font=("Arial Black", 20), bg="#617C58", fg="#6CBB3C", width=16, command=ok).grid(row=7, column=1)
b2 = tk.Button(f2, text="Cancel Booking", bd=3, font=("Arial Black", 20), bg="#617C58", fg="#6CBB3C", width=16, command=cancel).grid(row=7, column=2)

f1.pack()
master.mainloop()

name = tk

