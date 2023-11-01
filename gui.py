import customtkinter as ctk
import mysql.connector as mysql

con=mysql.connect(host="localhost",user="root",password="",database="timetable")
cur=con.cursor()

ctk.set_appearance_mode("dark")

app=ctk.CTk()
app.geometry("900x600")

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
    
    signIn.pack_forget()
    tabview=ctk.CTkTabview(master=page_admin)
    tabview.pack(expand=1,fill="both")
    days=["Mon","Tue","Wed","Thurs","Fri"]
    for day in days:
        tabview.add(day)
        page=tabview.tab(day)
        page.columnconfigure(0,weight=2)
        for i in range(1,12):
            page.columnconfigure(i,weight=1)
        page.columnconfigure(13,weight=2)
        page.rowconfigure(0,weight=2)
        classes=["I","II","III","IV"]
        for i in range(1,5):
            page.rowconfigure(i,weight=1)
            label=ctk.CTkLabel(tabview.tab(day),text=f'{classes[i-1]}')
            label.grid(row=i,column=0)
        page.rowconfigure(5,weight=2)
        for i in range(1,11):
            label=ctk.CTkLabel(tabview.tab(day),text=f'{i}')
            label.grid(row=0,column=i)
    tabview.set("Mon")
    timetable=[[['Math-Indrajit', 'Math-Indrajit', 'Eng-Irfan', 'IInd Lang-Akbar', 'Science-Nalini', 'Science-Nalini', 'Science-Nalini', 'EVS-Jasvinder', 'EVS-Jasvinder', 'EVS-Jasvinder'], ['EVS-Feroze', 'EVS-Feroze', 'EVS-Feroze', 'IInd Lang-Khurshid', 'Math-Indrajit', 'Math-Indrajit', 'Eng-Zaman', 'Science-Aishwarya', 'Science-Aishwarya', 'Science-Aishwarya'], ['Science-Vasudha', 'Science-Vasudha', 'Science-Vasudha', 'EVS-Feroze', 'EVS-Feroze', 'EVS-Feroze', 'EVS-Feroze', 'EVS-Feroze', 'Math-Prashant', 'Math-Prashant'], ['Science-Darshan', 'Science-Darshan', 'Science-Darshan', 'Math-Manpreet', 'Math-Manpreet', 'Eng-Abdul', 'IInd Lang-Akbar', 'EVS-Mitul', 'EVS-Mitul', 'EVS-Mitul']], [['EVS-Jasvinder', 'EVS-Jasvinder', 'EVS-Jasvinder', 'IInd Lang-Akbar', 'Science-Nalini', 'Science-Nalini', 'Science-Nalini', 'Eng-Irfan', 'Math-Indrajit', 'Math-Indrajit'], ['Eng-Zaman', 'IInd Lang-Khurshid', 'IInd Lang-Khurshid', 'Math-Indrajit', 'Math-Indrajit', 'Science-Aishwarya', 'Science-Aishwarya', 'Science-Aishwarya', 'EVS-Feroze', 'EVS-Feroze'], ['EVS-Feroze', 'EVS-Feroze', 'Eng-Irfan', 'Science-Vasudha', 'Science-Vasudha', 'Science-Vasudha', 'IInd Lang-Farah', 'EVS-Feroze', 'Math-Prashant', 'Math-Prashant'], ['EVS-Mitul', 'EVS-Mitul', 'Science-Darshan', 'Science-Darshan', 'Science-Darshan', 'Math-Manpreet', 'Math-Manpreet', 'IInd Lang-Akbar', 'IInd Lang-Akbar', 'Eng-Abdul']], [['IInd Lang-Akbar', 'IInd Lang-Akbar', 'Math-Indrajit', 'Math-Indrajit', 'EVS-Jasvinder', 'EVS-Jasvinder', 'Science-Nalini', 'Science-Nalini', 'Science-Nalini', 'Eng-Irfan'], ['Math-Indrajit', 'Math-Indrajit', 'Eng-Zaman', 'Science-Aishwarya', 'Science-Aishwarya', 'Science-Aishwarya', 'EVS-Feroze', 'EVS-Feroze', 'EVS-Feroze', 'IInd Lang-Khurshid'], ['Math-Prashant', 'Math-Prashant', 'EVS-Feroze', 'EVS-Feroze', 'Eng-Irfan', 'IInd Lang-Farah', 'IInd Lang-Farah', 'Science-Vasudha', 'Science-Vasudha', 'Science-Vasudha'], ['EVS-Mitul', 'EVS-Mitul', 'IInd Lang-Akbar', 'EVS-Mitul', 'Eng-Abdul', 'Science-Darshan', 'Science-Darshan', 'Science-Darshan', 'Math-Manpreet', 'Math-Manpreet']], [['Eng-Irfan', 'Eng-Irfan', 'Math-Indrajit', 'Math-Indrajit', 'Math-Indrajit', 'Science-Nalini', 'IInd Lang-Akbar', 'IInd Lang-Akbar', 'EVS-Jasvinder', 'EVS-Jasvinder'], ['Math-Indrajit', 'IInd Lang-Khurshid', 'IInd Lang-Khurshid', 'IInd Lang-Khurshid', 'Eng-Zaman', 'Math-Indrajit', 'Math-Indrajit', 'Science-Aishwarya', 'EVS-Feroze', 'EVS-Feroze'], ['Science-Vasudha', 'IInd Lang-Farah', 'Eng-Irfan', 'Eng-Irfan', 'Eng-Irfan', 'IInd Lang-Farah', 'IInd Lang-Farah', 'Math-Prashant', 'Math-Prashant', 'Math-Prashant'], ['IInd Lang-Akbar', 'EVS-Mitul', 'EVS-Mitul', 'Eng-Abdul', 'Eng-Abdul', 'IInd Lang-Akbar', 'Science-Darshan', 'Math-Manpreet', 'Math-Manpreet', 'Math-Manpreet']], [['IInd Lang-Akbar', 'IInd Lang-Akbar', 'IInd Lang-Akbar', 'Math-Indrajit', 'Eng-Irfan', 'Eng-Irfan', 'Eng-Irfan', 'Eng-Irfan', 'Eng-Irfan', 'IInd Lang-Akbar'], ['Math-Indrajit', 'IInd Lang-Khurshid', 'IInd Lang-Khurshid', 'IInd Lang-Khurshid', 'Eng-Zaman', 'Eng-Zaman', 'Eng-Zaman', 'Eng-Zaman', 'Eng-Zaman', 'Eng-Zaman'], ['Eng-Irfan', 'Eng-Irfan', 'Eng-Irfan', 'Eng-Irfan', 'IInd Lang-Farah', 'IInd Lang-Farah', 'Math-Prashant', 'IInd Lang-Farah', 'IInd Lang-Farah', 'Eng-Irfan'], ['Eng-Abdul', 'Eng-Abdul', 'Eng-Abdul', 'IInd Lang-Akbar', 'IInd Lang-Akbar', 'Eng-Abdul', 'Eng-Abdul', 'IInd Lang-Akbar', 'IInd Lang-Akbar', 'Math-Manpreet']]]
    for i in range(0,len(timetable)):
        day=days[i]
        for j in range(0,len(classes)):
            for k in range(0,len(timetable[i][j])):
                option=ctk.CTkOptionMenu(tabview.tab(day),width=50,values=[timetable[i][j][k]])
                option.grid(row=j+1,column=k+1)    

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