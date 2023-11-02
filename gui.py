import customtkinter as ctk
import mysql.connector as mysql
import pickle
from time import sleep
from main import final_schedule

con=mysql.connect(host="localhost",user="root",password="",database="timetable")
cur=con.cursor()

ctk.set_appearance_mode("dark")

app=ctk.CTk()
app.geometry("900x600")
ops=None
t=None
signIn=ctk.CTkFrame(app)
page_admin=ctk.CTkFrame(app)
student=ctk.CTkFrame(app)
teacher=ctk.CTkFrame(app)

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
    global cur
    grades=["first","second","third","fourth"]
    for i in grades:
        cur.execute(f"drop table if exists {i};")
        cur.execute(f'create table {i}(day varchar(10) primary key,I varchar(20),II varchar(20),III varchar(20),IV varchar(20),V varchar(20),VI varchar(20),VII varchar(20),VIII varchar(20),IX varchar(20),X varchar(20));')
    days=["Mon","Tue","Wed","Thur","Fri"]
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
    tt_restructure=[]
    for i in range(0,len(tt[0])):
        cl=[]
        for j in range(0,len(tt)):
            cl.append(tt[j][i])
        tt_restructure.append(cl)
    for i in range(0,len(tt_restructure)):
        grade=tt_restructure[i]
        for j in range(0,len(days)):
            sched=grade[j]
            print(days[j],grades[i])
            print(f"insert into {grades[i]} values('{days[j]}','{sched[0]}','{sched[1]}','{sched[2]}','{sched[3]}','{sched[4]}','{sched[5]}','{sched[6]}','{sched[7]}','{sched[8]}','{sched[9]}')")
            cur.execute(f"insert into {grades[i]} values('{days[j]}','{sched[0]}','{sched[1]}','{sched[2]}','{sched[3]}','{sched[4]}','{sched[5]}','{sched[6]}','{sched[7]}','{sched[8]}','{sched[9]}');")
    con.commit()
    with open("teachers.bin","wb") as file:
        pickle.dump(t,file)


def change_to_student(cl):
    global signIn
    global student
    global cur
    class_list={"I":"first","II":"second","III":"third","IV":"fourth"}
    cur.execute(f"select * from {class_list[cl]};")
    fetched_tt=cur.fetchall()
    signIn.pack_forget()
    student.pack(fill='both',expand=1)
    page=student
    page.columnconfigure(0,weight=2)
    for i in range(1,12):
        page.columnconfigure(i,weight=1)
    page.columnconfigure(13,weight=2)
    page.rowconfigure(0,weight=2)
    days=["Mon","Tue","Wed","Thur","Fri"]
    for i in range(1,6):
        page.rowconfigure(i,weight=1)
        label=ctk.CTkLabel(page,text=f'{days[i-1]}')
        label.grid(row=i,column=0)
    page.rowconfigure(6,weight=2)
    for i in range(1,11):
        label=ctk.CTkLabel(page,text=f'{i}')
        label.grid(row=0,column=i)
    for i in range(0,len(fetched_tt)):
        row=days.index(fetched_tt[i][0])
        classes=fetched_tt[i][1:]
        for i in range(0,len(classes)):
            label=ctk.CTkLabel(page,text="\n".join(classes[i].split("-")))
            label.grid(column=i+1,row=row+1)
    l=ctk.CTkLabel(page,text=f'Grade {cl}')
    l.grid(column=0,row=0)

def change_to_teacher(name):
    global signIn
    global teacher
    global cur
    signIn.pack_forget()
    teacher.pack(fill='both',expand=1)
    tt=[]
    for i in range(0,5):
        x=[]
        for i in range(0,10):
            x.append("")
        tt.append(x)
    grades=["first","second","third","fourth"]
    grades_con={"first":"I","second":"II","third":"III","fourth":"IV"}
    days=["Mon","Tue","Wed","Thur","Fri"]
    for i in range(0,len(grades)):
        cur.execute(f'select * from {grades[i]}')
        sched=cur.fetchall()
        for j in sched:
            for k in range(1,len(j)):
                day=days.index(j[0])
                print(j[k])
                if j[k].split("-")[1]==name:
                    tt[day][k-1]=grades_con[grades[i]]
    page=teacher
    page.columnconfigure(0,weight=2)
    for i in range(1,12):
        page.columnconfigure(i,weight=1)
    page.columnconfigure(13,weight=2)
    page.rowconfigure(0,weight=2)
    days=["Mon","Tue","Wed","Thur","Fri"]
    for i in range(1,6):
        page.rowconfigure(i,weight=1)
        label=ctk.CTkLabel(page,text=f'{days[i-1]}')
        label.grid(row=i,column=0)
    page.rowconfigure(6,weight=2)
    for i in range(0,len(days)):
        label=ctk.CTkLabel(page,text=days[i])
        label.grid(column=0,row=i+1)
    for i in range(0,10):
       label=ctk.CTkLabel(page,text=f'{i+1}')
       label.grid(column=i+1,row=0)
    for i in range(0,len(tt)):
        for j in range(0,len(tt[i])):
            label=ctk.CTkLabel(page,text=tt[i][j] if len(tt[i][j])!=0 else "-")
            label.grid(column=j+1,row=i+1)
    l=ctk.CTkLabel(page,text=name)
    l.grid(column=0,row=0)


def change_to_admin():
    global signIn
    global page_admin
    global cur
    global t
    global ops
    page_admin.pack(fill='both',expand=1)
    signIn.pack_forget()
    tabview=ctk.CTkTabview(master=page_admin)
    tabview.pack(expand=1,fill="both")
    days=["Mon","Tue","Wed","Thur","Fri"]
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
    cur.execute("select * from first;")
    def schedule():
        global ops
        global t
        if ops!=None:
            for i in ops:
                for j in i:
                    for k in j:
                        k.grid_forget()
            ops=None
        x=final_schedule()
        while x=="failed":
            x=final_schedule()
        timetable=x[0]
        teachers_assigned=x[1]
        t=teachers_assigned
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
        ops=options
    if len(cur.fetchall())!=0:
        with open("teachers.bin","rb") as file:
            teachers_assigned=pickle.load(file)
        days=["Mon","Tue","Wed","Thur","Fri"]
        timetable=[]
        for i in range(5):
            timetable.append([])
        scheds=[]
        grades=["first","second","third","fourth"]
        for i in range(0,len(grades)):
            cur.execute(f"select * from {grades[i]}")
            scheds.append(cur.fetchall())
        for sched in scheds:
            for i in range(0,len(sched)):
                day_sched=sched[i]
                timetable[days.index(day_sched[0])].append(list(day_sched)[1:])
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
        ops=options
        t=teachers_assigned
    else:
        schedule()
    for day in days:
        reschedule=ctk.CTkButton(tabview.tab(day),text="Reschedule",command=schedule)
        submit_button=ctk.CTkButton(tabview.tab(day),text="Submit",command=lambda: submit_timetable(ops))
        submit_button.grid(column=2,row=5)
        reschedule.grid(column=1,row=5)

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
        print(result)
        if result[4]==pas:
            if result[1]==1:
                change_to_admin()
            elif result[1]==0 and result[2]==0:
                change_to_student(result[5])
            elif result[2]==1:
                change_to_teacher(result[6])
        else:
            password.configure(fg_color="red")


login=ctk.CTkButton(signIn,text="Login",command=check_login)
login.grid(column=0,row=3)

signIn.pack(fill='both',expand=1)

app.mainloop()