import customtkinter as ctk
import mysql.connector as mysql
from time import sleep

con=mysql.connect(host="localhost",user="root",password="root",database="timetable")
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

def submit_timetable(options):
    tt=[]
    for i in range(0,5):
        ii=[]
        for j in range(0,4):
            jj=[]
            for k in range(0,10):
                jj.append(None)
            ii.append(jj)
        tt.append(ii)
    for i in range(0,len(options)):
        for j in range(0,len(options[i])):
            for k in range(0,len(options[i][j])):
                tt[i][j][k]=options[i][j][k].get()


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
    timetable=[[['EVS-Nazir', 'EVS-Nazir', 'Math-Danish', 'Math-Danish', 'Eng-Irfan', 'IInd Lang-Farah', 'IInd Lang-Farah', 'Science-Nalini', 'Science-Nalini', 'Science-Nalini'], ['Math-Danish', 'Math-Danish', 'Eng-Abdul', 'IInd Lang-Khurshid', 'EVS-Jasvinder', 'EVS-Jasvinder', 'EVS-Jasvinder', 'Science-Aishwarya', 'Science-Aishwarya', 'Science-Aishwarya'], ['Math-Indrajit', 'IInd Lang-Akbar', 'IInd Lang-Akbar', 'EVS-Nazir', 'EVS-Nazir', 'Math-Indrajit', 'Math-Indrajit', 'Science-Vasudha', 'Science-Vasudha', 'Science-Vasudha'], ['Science-Nalini', 'Science-Nalini', 'Science-Nalini', 'Eng-Abdul', 'EVS-Feroze', 'EVS-Feroze', 'EVS-Feroze', 'Math-Manpreet', 'Math-Manpreet', 'IInd Lang-Akbar']], [['IInd Lang-Farah', 'Eng-Irfan', 'EVS-Nazir', 'EVS-Nazir', 'EVS-Nazir', 'Science-Nalini', 'Science-Nalini', 'Science-Nalini', 'Math-Danish', 'Math-Danish'], ['EVS-Jasvinder', 'EVS-Jasvinder', 'EVS-Jasvinder', 'Eng-Abdul', 'Math-Danish', 'Math-Danish', 'IInd Lang-Khurshid', 'Science-Aishwarya', 'Science-Aishwarya', 'Science-Aishwarya'], ['Eng-Pallavi', 'Math-Indrajit', 'Math-Indrajit', 'IInd Lang-Akbar', 'Science-Vasudha', 'Science-Vasudha', 'Science-Vasudha', 'EVS-Nazir', 'EVS-Nazir', 'EVS-Nazir'], ['Science-Nalini', 'Science-Nalini', 'EVS-Feroze', 'EVS-Feroze', 'Science-Nalini', 'IInd Lang-Akbar', 'EVS-Feroze', 'Math-Manpreet', 'Math-Manpreet', 'Eng-Abdul']], [['IInd Lang-Farah', 'EVS-Nazir', 'EVS-Nazir', 'EVS-Nazir', 'Math-Danish', 'Math-Danish', 'Science-Nalini', 'Science-Nalini', 'Science-Nalini', 'Eng-Irfan'], ['Science-Aishwarya', 'Science-Aishwarya', 'Science-Aishwarya', 'IInd Lang-Khurshid', 'IInd Lang-Khurshid', 'EVS-Jasvinder', 'EVS-Jasvinder', 'Math-Danish', 'Math-Danish', 'Eng-Abdul'], ['EVS-Nazir', 'Math-Indrajit', 'Eng-Pallavi', 'Math-Indrajit', 'EVS-Nazir', 'EVS-Nazir', 'IInd Lang-Akbar', 'Science-Vasudha', 'Science-Vasudha', 'Science-Vasudha'], ['Eng-Abdul', 'Science-Nalini', 'EVS-Feroze', 'Math-Manpreet', 'Math-Manpreet', 'Science-Nalini', 'EVS-Feroze', 'EVS-Feroze', 'IInd Lang-Akbar', 'Science-Nalini']], [['Eng-Irfan', 'Eng-Irfan', 'EVS-Nazir', 'EVS-Nazir', 'Science-Nalini', 'Math-Danish', 'Math-Danish', 'Math-Danish', 'IInd Lang-Farah', 'IInd Lang-Farah'], ['Math-Danish', 'Math-Danish', 'Math-Danish', 'IInd Lang-Khurshid', 'IInd Lang-Khurshid', 'EVS-Jasvinder', 'EVS-Jasvinder', 'Eng-Abdul', 'Eng-Abdul', 'Science-Aishwarya'], ['EVS-Nazir', 'EVS-Nazir', 'Science-Vasudha', 'IInd Lang-Akbar', 'IInd Lang-Akbar', 'IInd Lang-Akbar', 'Eng-Pallavi', 'Math-Indrajit', 'Math-Indrajit', 'Math-Indrajit'], ['Eng-Abdul', 'Eng-Abdul', 'EVS-Feroze', 'Science-Nalini', 'Math-Manpreet', 'Math-Manpreet', 'Math-Manpreet', 'IInd Lang-Akbar', 'IInd Lang-Akbar', 'IInd Lang-Akbar']], [['Math-Danish', 'Eng-Irfan', 'Eng-Irfan', 'IInd Lang-Farah', 'Eng-Irfan', 'Eng-Irfan', 'Eng-Irfan', 'IInd Lang-Farah', 'IInd Lang-Farah', 'IInd Lang-Farah'], ['IInd Lang-Khurshid', 'IInd Lang-Khurshid', 'IInd Lang-Khurshid', 'Math-Danish', 'Eng-Abdul', 'Eng-Abdul', 'Eng-Abdul', 'Eng-Abdul', 'Eng-Abdul', 'IInd Lang-Khurshid'], ['Eng-Pallavi', 'Eng-Pallavi', 'Eng-Pallavi', 'Eng-Pallavi', 'Eng-Pallavi', 'Eng-Pallavi', 'Eng-Pallavi', 'IInd Lang-Akbar', 'IInd Lang-Akbar', 'IInd Lang-Akbar'], ['IInd Lang-Akbar', 'IInd Lang-Akbar', 'Eng-Abdul', 'Eng-Abdul', 'Math-Manpreet', 'IInd Lang-Akbar', 'IInd Lang-Akbar', 'Eng-Abdul', 'Eng-Abdul', 'Eng-Abdul']]]
    teachers_assigned={'I': ['Nalini-Science', 'Nazir-EVS', 'Danish-Math', 'Farah-IInd Lang', 'Irfan-Eng'], 'II': ['Aishwarya-Science', 'Jasvinder-EVS', 'Danish-Math', 'Khurshid-IInd Lang', 'Abdul-Eng'], 'III': ['Vasudha-Science', 'Nazir-EVS', 'Indrajit-Math', 'Akbar-IInd Lang', 'Pallavi-Eng'], 'IV': ['Nalini-Science', 'Feroze-EVS', 'Manpreet-Math', 'Akbar-IInd Lang', 'Abdul-Eng']}
    options=[]
    for i in range(0,5):
        ii=[]
        for j in range(0,4):
            jj=[]
            for k in range(0,10):
                jj.append(None)
            ii.append(jj)
        options.append(ii)
    for i in range(0,len(timetable)):
        day=days[i]
        for j in range(0,len(classes)):
            for k in range(0,len(timetable[i][j])):
                yy=[timetable[i][j][k]]
                yy.extend(list(set(teachers_assigned[classes[j]])-set(yy)))
                option=ctk.CTkOptionMenu(tabview.tab(day),width=50,values=yy)
                option.grid(row=j+1,column=k+1)
                options[i][j][k]=option
    for day in days:
        submit_button=ctk.CTkButton(tabview.tab(day),text="Submit",command=lambda: submit_timetable(options))
        submit_button.grid(column=1,row=5)

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