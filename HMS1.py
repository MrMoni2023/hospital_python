import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


class Gui:
    """Gui class"""
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Login')
        self.root.geometry('925x500+300+200')
        self.root.config(bg= "cadetblue")
        self.root.resizable(False,False)

        frame = tk.Frame(self.root,width=350,height=350,bg='cadetblue')
        frame.place(x=480,y=70)

        heading = tk.Label(frame,text='Sign In',fg='white',bg='cadetblue',font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x=110,y=5)
        
        def on_enter(e):
            User.delete(0,'end')

        def on_leave(e):
            name = User.get()
            if name == '':
                User.insert(0,'Username')


        User = tk.Entry(frame,width=25,fg='white',border=0,bg='cadetblue',font=('Microsoft YaHei UI Light',11))
        User.place(x=30,y=80)
        User.insert(0,'Username')
        User.bind('<FocusIn>',on_enter)
        User.bind('<FocusOut>',on_leave)

        tk.Frame(frame,width=295,height=2,bg='white').place(x=25,y=107)


        #-----------------------------------------#

        def on_enter(e):
            code.delete(0,'end')

        def on_leave(e):
            Password = code.get()
            if Password == '':
                code.insert(0,'Password')

        code = tk.Entry(frame,width=25,fg='white',border=0,bg='cadetblue',font=('Microsoft YaHei UI Light',11))
        code.place(x=30,y=150)
        code.insert(0,'Password')
        code.bind('<FocusIn>',on_enter)
        code.bind('<FocusOut>',on_leave)

        tk.Frame(frame,width=295,height=2,bg='white').place(x=25,y=177)

        self.new_window = tk.Button(frame,width=39,pady=7,text='Sign In',bg='red',fg='white',border=0, command=self.new_window).place(x=35,y=204)
        
        self.root.mainloop()


    def new_window(self):
        self.wind = tk.Tk()
        self.wind.state('zoomed')
        self.wind.config(bg='black')

        #-----------------------------------------------------------------
        def ShowRecord():
            sqlCon = pymysql.connect(host="localhost", user="root", password="Mazam900", database="healthcare")
            cur = sqlCon.cursor()
            cur.execute("select * from healthcare")
            result = cur.fetchall()
            if(len(result)!=0):
                self.table.delete(* self.table.get_children())
                for row in result:
                    self.table.insert('',tk.END,values=row)
                sqlCon.commit()
            sqlCon.close()

        def Information(ev):
            viewInfo = self.table.focus()
            data = self.table.item(viewInfo)
            row = data['values']

            self.NameofDoc.set(row[0]) 
            self.Deases.set(row[1]) 
            self.NameOfTab.set(row[2]) 
            self.IssueDate.set(row[3]) 
            self.ExpDate.set(row[4]) 
            self.NoOfTab.set(row[5])
            self.PatID.set(row[6]) 
            self.NameOfPat.set(row[7])
            self.DOB.set(row[8])
            self.PatADD.set(row[9]) 
            self.PhoneNum.set(row[10])

        def update():
            sqlCon = pymysql.connect(host="localhost", user="root", password="Mazam900", database="healthcare")
            cur = sqlCon.cursor()
            cur.execute("update healthcare set PatID=%s,doctor=%s,Deases=%s,NameOfTab=%s,IssueDate=%s,ExpDate=%s,NoOfTab=%s,NameOfPat=%s,PatADD=%s,PhoneNum=%s  ",(
                self.PatID.get(),
                self.NameofDoc.get(),
                self.Deases.get(),
                self.NameOfTab.get(),
                self.IssueDate.get(),
                self.ExpDate.get(),
                self.NoOfTab.get(),
                self.NameOfPat.get(),
                self.PatADD.get(),
                self.PhoneNum.get()
            ))
            sqlCon.commit()
            ShowRecord()
            sqlCon.close()
            messagebox.showinfo("Data Entry Form","Record Updated")

        def DeleteDB():
            sqlCon = pymysql.connect(host="localhost", user="root", password="Mazam900", database="healthcare")
            cur = sqlCon.cursor()
            cur.execute("delete from healthcare where PatID=%s",PatID.get())
            sqlCon.commit()
            ShowRecord()
            sqlCon.close()
            messagebox.showinfo("Data Entry Form","Record Deleted!")


        def Add():
            if PatID.get() == "" or NameofDoc.get() == "" or Deases.get() == "" :
                messagebox.showerror("Invalid Details","Insert correct Informtion")
            else:
                sqlCon = pymysql.connect(host="localhost:3306", user="root", password="Mazam900", database="healthcare")
                cur = sqlCon.cursor()
                cur.execute("insert into healthcare values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.PatID.get(),
                    self.NameofDoc.get(),
                    self.Deases.get(),
                    self.NameOfTab.get(),
                    self.IssueDate.get(),
                    self.ExpDate.get(),
                    self.NoOfTab.get(),
                    self.NameOfPat.get(),
                    self.PatADD.get(),
                    self.PhoneNum.get()
                ))
                sqlCon.commit()
                ShowRecord()
                sqlCon.close()
                messagebox.showinfo("Data Entry Form","Data recorded successfully")



        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BUTTON FUNCTION~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        def SavePD():
            if e1.get() == "" and e2.get() == "":
                messagebox.showwarning("Error","Enter all Fields.")
            else:
                con = mysql.connector.connect(host = "localhost",username = "root", password = "Mazam900", database = "mydata")
                cur = con.cursor()
                cur.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    NameofDoc.get(),
                    Deases.get(),
                    NameOfTab.get(),
                    IssueDate.get(),
                    ExpDate.get(),
                    NoOfTab.get(),
                    PatID.get(),
                    DateOfBirth.get(),
                    PatADD.get(),
                    PhoneNum.get()
                ))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Record inserted.")




        #Heading
        tk.Label(self.wind,text='HEALTH CARE MANAGEMENT SYSTEM +',font='impact 31 bold',bg='cadetblue',fg='white').pack(fill=tk.X)

        #frame1
        frame1 = tk.Frame(self.wind,bd=10,relief=tk.RIDGE)
        frame1.place(x=0,y=54,width=1535,height=500)

        #Lable Frame for Patient Info
        lf1 = tk.LabelFrame(frame1,text='PATIENT INFORMATION',font='ariel 14 bold',bd=6,bg='grey',fg='#cc1231')
        lf1.place(x=10,y=0,width=950,height=380)

        #Lables for Patient Info
        tk.Label(lf1,text='NAME OF DOCTOR:',bg='grey',fg='white').place(x=10, y=20)
        tk.Label(lf1,text='QUALIFICATIONS:',bg='grey',fg='white').place(x=10, y=60)
        tk.Label(lf1,text='DEASES DIAGNOS:',bg='grey',fg='white').place(x=10, y=100)
        tk.Label(lf1,text='NAME OF TABLETS:',bg='grey',fg='white').place(x=10, y=140)
        tk.Label(lf1,text='ISSUE DATE:',bg='grey',fg='white').place(x=10, y=180)
        tk.Label(lf1,text='EXP DATE:',bg='grey',fg='white').place(x=10, y=220)
        tk.Label(lf1,text='DAILY DOSE:',bg='grey',fg='white').place(x=10, y=260)
        tk.Label(lf1,text='NO. OF TABLETS:',bg='grey',fg='white').place(x=10, y=300)

        tk.Label(lf1,text='BLOOD PRESURE:',bg='grey',fg='white').place(x=420, y=20)
        tk.Label(lf1,text='SUGAR LEVEL:',bg='grey',fg='white').place(x=420, y=60)
        tk.Label(lf1,text='CHECK-UP DAY:',bg='grey',fg='white').place(x=420, y=100)
        tk.Label(lf1,text='PATIENT ID:',bg='grey',fg='white').place(x=420, y=140)
        tk.Label(lf1,text='NAME OF PATIENT:',bg='grey',fg='white').place(x=420, y=180)
        tk.Label(lf1,text='DOB:',bg='grey',fg='white').place(x=420, y=220)
        tk.Label(lf1,text='PATIENT ADDRESS:',bg='grey',fg='white').place(x=420, y=260)
        tk.Label(lf1,text='PHONE NUMBER:',bg='grey',fg='white').place(x=420, y=300)

        #TextVaraible for Every Text Field
        NameofDoc = tk.StringVar()
        QualifOfDoc = tk.StringVar()
        Deases = tk.StringVar()
        NameOfTab = tk.StringVar()
        IssueDate = tk.StringVar()
        ExpDate = tk.StringVar()
        DailyDose = tk.StringVar()
        NoOfTab = tk.StringVar()
        BP = tk.StringVar()
        SugarLevel = tk.StringVar()
        CheckUpDay = tk.StringVar()
        PatID = tk.StringVar()
        NameOfPat = tk.StringVar()
        DateOfBirth = tk.StringVar()
        PatADD = tk.StringVar()
        PhoneNum = tk.StringVar()

        #Entry Fields for all lables
        
        e1 = tk.Entry(lf1,bd=4,textvariable=NameofDoc)
        e1.place(x=160,y=20,width=200)

        e2 = tk.Entry(lf1,bd=4, textvariable= QualifOfDoc)
        e2.place(x=160,y=60,width=200)

        e3 = tk.Entry(lf1,bd=4, textvariable=Deases)
        e3.place(x=160,y=100,width=200)

        e4 = tk.Entry(lf1,bd=4, textvariable=NameOfTab)
        e4.place(x=160,y=140,width=200)

        e5 = tk.Entry(lf1,bd=4, textvariable=IssueDate)
        e5.place(x=160,y=180,width=200)

        e6 = tk.Entry(lf1,bd=4,textvariable=ExpDate)
        e6.place(x=160,y=220,width=200)

        e7 = tk.Entry(lf1,bd=4,textvariable=DailyDose)
        e7.place(x=160,y=260,width=200)

        e8 = tk.Entry(lf1,bd=4,textvariable=NoOfTab)
        e8.place(x=160,y=300,width=200)

        e9 = tk.Entry(lf1,bd=4, textvariable=BP)
        e9.place(x=560,y=20,width=200)

        e10 = tk.Entry(lf1,bd=4, textvariable=SugarLevel)
        e10.place(x=560,y=60,width=200)

        e11 = tk.Entry(lf1,bd=4,textvariable=CheckUpDay)
        e11.place(x=560,y=100,width=200)

        e12 = tk.Entry(lf1,bd=4,textvariable=PatID)
        e12.place(x=560,y=140,width=200)

        e13 = tk.Entry(lf1,bd=4,textvariable=NameOfPat)
        e13.place(x=560,y=180,width=200)

        e14 = tk.Entry(lf1,bd=4,textvariable=DateOfBirth)
        e14.place(x=560,y=220,width=200)

        e15 = tk.Entry(lf1,bd=4,textvariable=PatADD)
        e15.place(x=560,y=260,width=200)

        e16 = tk.Entry(lf1,bd=4,textvariable=PhoneNum)
        e16.place(x=560,y=300,width=200)


        #Lable Frame for Prescription
        lf2 = tk.LabelFrame(frame1,text='PRESCRITION',font='ariel 14 bold',bd=6,fg='#cc1231')
        lf2.place(x=963,y=0,width=550,height=380)

        #Textbox for prescription
        text_box = tk.Text(lf2,font='impack 10 bold',width=40,height=30,bg='cadetblue',fg='red')
        text_box.pack(fill=tk.BOTH)

        #frame2
        frame2 = tk.Frame(self.wind,bd=10,relief=tk.RIDGE)
        frame2.place(x=0,y=450,width=1535,height=310)

        #Button
        #Delete Button
        d_btn = tk.Button(self.wind,text='DELETE',font='ariel 15 bold',bg='cadetblue',fg='white',bd=6,cursor='hand2')
        d_btn.place(x=0,y=750,width=300)

        #Prescription Button
        p_btn = tk.Button(self.wind,text='PRESCRIPTION',font='ariel 15 bold',bg='cadetblue',fg='white',bd=6,cursor='hand2')
        p_btn.place(x=300,y=750,width=300)

        #Save Prescription Button
        sp_btn = tk.Button(self.wind,text='SAVE PRESCRIPTION',font='ariel 15 bold',bg='cadetblue',fg='white',bd=6,cursor='hand2',command=SavePD())
        sp_btn.place(x=600,y=750,width=300)

        #Clear Button
        c_btn = tk.Button(self.wind,text='CLEAR ',font='ariel 15 bold',bg='cadetblue',fg='white',bd=6,cursor='hand2')
        c_btn.place(x=900,y=750,width=300)

        #Exit Button
        p_btn = tk.Button(self.wind,text='EXIT',font='ariel 15 bold',bg='red',fg='white',bd=6,cursor='hand2')
        p_btn.place(x=1200,y=750,width=375)

        #scroll bar for prescrition data
        scrollX = ttk.Scrollbar(frame2,orient=tk.HORIZONTAL)
        scrollX.pack(side='bottom',fill='x')
        scrollY = ttk.Scrollbar(frame2,orient=tk.VERTICAL)
        scrollY.pack(side='right',fill='y')

        table = ttk.Treeview(frame2,columns=('doctor','deases','tablet','issue','exp','No.Tab','ID','PN','DOB','PA','PhNum'),xscrollcommand=scrollY.set,yscrollcommand=scrollX.set)
        scrollX = ttk.Scrollbar(command=table.xview)
        scrollY = ttk.Scrollbar(command=table.yview )

        #Heading for Prescription Data
        table.heading('ID',text='Patient ID')
        table.heading('doctor',text='Doctor')
        table.heading('deases',text='Deases')
        table.heading('tablet',text='Tablet Name')
        table.heading('issue',text='Issue')
        table.heading('exp',text='Exp')
        table.heading('No.Tab',text='No. Tablets')
        table.heading('PN',text='Pateint Name')
        table.heading('DOB',text='Date of Birth')
        table.heading('PA',text='Patient Address')
        table.heading('PhNum',text='Phone Number')
        table['show'] = 'headings'
        table.pack(fill=tk.BOTH,expand=1)


        table.column('ID',width=120)
        table.column('doctor',width=120)
        table.column('deases',width=120)
        table.column('tablet',width=120)
        table.column('issue',width=120)
        table.column('exp',width=120)
        table.column('No.Tab',width=120)
        table.column('PN',width=120)
        table.column('DOB',width=120)
        table.column('PA',width=120)
        table.column('PhNum',width=120)

        table.pack(fill=tk.BOTH,expand=1)
        table.bind("<ButtonRelease-1>")
        


        #Lable Frame for Prescription
        lf2 = tk.LabelFrame(frame1,text='PRESCRITION',font='ariel 14 bold',bd=6,fg='white',bg='#cf293a')
        lf2.place(x=963,y=0,width=550,height=380)

if __name__ == '__main__':
    Gui()