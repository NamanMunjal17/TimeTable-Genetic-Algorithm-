import customtkinter as ctk
import mysql.connector as mysql

con=mysql.connect(host="localhost",user="root",password="",database="timetable")
cur=con.cursor()

ctk.set_appearance_mode("dark")

app=ctk.CTk()
app.geometry("700x500")

signIn=ctk.CTkFrame(app)
page_admin=ctk.CTkFrame(app)

'''
CHANGE FRAMES
def change():
    global signIn
    global page
    page.pack(fill='both',expand=1)
    signIn.pack_forget()

signIn.pack(fill='both',expand=1)
btn1=ctk.CTkButton(signIn,text="switch",command=change)
btn1.pack(padx=20)
'''

def change_to_admin():
    global signIn
    global page_admin
    page_admin.pack(fill='both',expand=1)
    page_admin.columnconfigure(0,weight=2)
    for i in range(1,11):
        page_admin.columnconfigure(i,weight=1)
    page_admin.columnconfigure(11,weight=2)
    page_admin.rowconfigure(0,weight=2)
    for i in range(1,7):
        page_admin.rowconfigure(i,weight=1)
    page_admin.rowconfigure(7,weight=2)
    signIn.pack_forget()

signIn.columnconfigure(0,weight=1)
for i in range(1,4):
    signIn.rowconfigure(i,weight=1)
signIn.rowconfigure(0,weight=25)
signIn.rowconfigure(4,weight=25)

username=ctk.CTkEntry(signIn,placeholder_text="Username")
username.grid(column=0, row=1)
password=ctk.CTkEntry(signIn,placeholder_text="Password",show="*")
password.grid(column=0,row=2)

def check_login():
    global username
    global password
    global cur
    user=username.get()
    pas=password.get()
    cur.execute(f'select * from users where username like "{user}"')
    result=cur.fetchall()
    if len(result)==0:
        username.configure(fg_color="red")
        password.configure(fg_color="red")
    else:
        result=result[0]
        if result[3]==pas:
            if result[1]==1:
                change_to_admin()
        else:
            password.configure(fg_color="red")


login=ctk.CTkButton(signIn,text="Login",command=check_login)
login.grid(column=0,row=3)

signIn.pack(fill='both',expand=1)

app.mainloop()