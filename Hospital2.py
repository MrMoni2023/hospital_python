from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
wind = Tk()
wind.state('zoomed')
wind.config(bg='black')

#----------------------------BUTTON FUNCTION-----------------------------
def pd():

    if e1.get() == "" or e2.get() == "":
        messagebox.showerror("Error","All Fields are Required !")
    else:
        con = mysql.connector.connect(host = "localhost:3306",username = "root",password = "Mazam900",database = "hospitaldata")
        my_cursor = con.cursor()
        my_cursor.execute("insert into hmsdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)",(
            
            string fname=NoofTab.get(),
            Ref.get(),
            dose.get(),
            issue.get(),
            Exp.get(),
            DailyDose.get(),
            sideEff.get(),
            NamePat.get(),
            dob.get(),
            PatADD.get(),
            PatNum.get()
            insert into table name () values('"+abc+"')

            
        ))
        con.commit()
        con.close()
        messagebox.showinfo("Suucess","All Records Inserted Successfully !")



#Heading
Label(wind,text='HEALTH CARE MANAGEMENT SYSTEM +',font='impact 31 bold',bg='#cc1231',fg='white').pack(fill=X)

#frame1
frame1 = Frame(wind,bd=10,relief=RIDGE)
frame1.place(x=0,y=54,width=1535,height=500)

#Lable Frame for Patient Info
lf1 = LabelFrame(frame1,text='PATIENT INFORMATION',font='ariel 14 bold',bd=6,bg='grey',fg='#cc1231')
lf1.place(x=10,y=0,width=950,height=380)

#Lables for Patient Info
Label(lf1,text='NAME OF MEDICENE:',bg='grey',fg='white').place(x=10, y=20)
Label(lf1,text='REFRENCE No.:',bg='grey',fg='white').place(x=10, y=60)
Label(lf1,text='DOSE:',bg='grey',fg='white').place(x=10, y=100)
Label(lf1,text='NO. OF TABLETS:',bg='grey',fg='white').place(x=10, y=140)
Label(lf1,text='ISSUE DATE:',bg='grey',fg='white').place(x=10, y=180)
Label(lf1,text='EXP DATE:',bg='grey',fg='white').place(x=10, y=220)
Label(lf1,text='DAILY DOSE:',bg='grey',fg='white').place(x=10, y=260)
Label(lf1,text='SIDE EFFECT:',bg='grey',fg='white').place(x=10, y=300)

Label(lf1,text='BLOOD PRESURE:',bg='grey',fg='white').place(x=420, y=20)
Label(lf1,text='STORAGE DEVICE:',bg='grey',fg='white').place(x=420, y=60)
Label(lf1,text='MEDICATION:',bg='grey',fg='white').place(x=420, y=100)
Label(lf1,text='PATIENT ID:',bg='grey',fg='white').place(x=420, y=140)
Label(lf1,text='NAME OF PATIENT:',bg='grey',fg='white').place(x=420, y=180)
Label(lf1,text='DOB:',bg='grey',fg='white').place(x=420, y=220)
Label(lf1,text='PATIENT ADDRESS:',bg='grey',fg='white').place(x=420, y=260)
Label(lf1,text='PHONE NUMBER:',bg='grey',fg='white').place(x=420, y=300)

#TextVaraible for Rvevry Text Field
nameofTab = StringVar()
Ref = StringVar()
dose = StringVar()
NoofTab = StringVar()
issue = StringVar()
Exp = StringVar()
DailyDose = StringVar()
sideEff = StringVar()
BP = StringVar()
SDevices = StringVar()
Med = StringVar()
PatID = StringVar()
NamePat = StringVar()
dob = StringVar()
PatADD = StringVar()
PatNum = StringVar()

#Entry Fields for all lables
e1 = Entry(lf1,bd=4,textvariable=nameofTab)
e1.place(x=160,y=20,width=200)

e2 = Entry(lf1,bd=4, textvariable= Ref)
e2.place(x=160,y=60,width=200)

e3 = Entry(lf1,bd=4, textvariable=dose)
e3.place(x=160,y=100,width=200)

e4 = Entry(lf1,bd=4, textvariable=NoofTab)
e4.place(x=160,y=140,width=200)

e5 = Entry(lf1,bd=4, textvariable=issue)
e5.place(x=160,y=180,width=200)

e6 = Entry(lf1,bd=4,textvariable=Exp)
e6.place(x=160,y=220,width=200)

e7 = Entry(lf1,bd=4,textvariable=DailyDose)
e7.place(x=160,y=260,width=200)

e8 = Entry(lf1,bd=4,textvariable=sideEff)
e8.place(x=160,y=300,width=200)

e9 = Entry(lf1,bd=4, textvariable=BP)
e9.place(x=560,y=20,width=200)

e10 = Entry(lf1,bd=4, textvariable=SDevices)
e10.place(x=560,y=60,width=200)

e11 = Entry(lf1,bd=4,textvariable=Med)
e11.place(x=560,y=100,width=200)

e12 = Entry(lf1,bd=4,textvariable=PatID)
e12.place(x=560,y=140,width=200)

e13 = Entry(lf1,bd=4,textvariable=NamePat)
e13.place(x=560,y=180,width=200)

e14 = Entry(lf1,bd=4,textvariable=dob)
e14.place(x=560,y=220,width=200)

e15 = Entry(lf1,bd=4,textvariable=PatADD)
e15.place(x=560,y=260,width=200)

e16 = Entry(lf1,bd=4,textvariable=PatNum)
e16.place(x=560,y=300,width=200)


#Lable Frame for Prescription
lf2 = LabelFrame(frame1,text='PRESCRITION',font='ariel 14 bold',bd=6,fg='#cc1231')
lf2.place(x=963,y=0,width=550,height=380)

#Textbox for prescription
text_box = Text(lf2,font='impack 10 bold',width=40,height=30,bg='yellow',fg='red')
text_box.pack(fill=BOTH)

#frame2
frame2 = Frame(wind,bd=10,relief=RIDGE)
frame2.place(x=0,y=450,width=1535,height=310)

#Button
#Delete Button
d_btn = Button(wind,text='DELETE',font='ariel 15 bold',bg='#cc1231',fg='white',bd=6,cursor='hand2')
d_btn.place(x=0,y=750,width=300)

#Prescription Button
p_btn = Button(wind,text='PRESCRIPTION',font='ariel 15 bold',bg='#cc1231',fg='white',bd=6,cursor='hand2')
p_btn.place(x=300,y=750,width=300)

#Save Prescription Button
sp_btn = Button(wind,text='SAVE PRESCRIPTION',font='ariel 15 bold',bg='#cc1231',fg='white',bd=6,cursor='hand2')
sp_btn.place(x=600,y=750,width=300)

#Clear Button
c_btn = Button(wind,text='CLEAR ',font='ariel 15 bold',bg='#cc1231',fg='white',bd=6,cursor='hand2')
c_btn.place(x=900,y=750,width=300)

#Exit Button
p_btn = Button(wind,text='EXIT',font='ariel 15 bold',bg='red',fg='white',bd=6,cursor='hand2')
p_btn.place(x=1200,y=750,width=375)

#scroll bar for prescrition data
scrollX = ttk.Scrollbar(frame2,orient=HORIZONTAL)
scrollX.pack(side='bottom',fill='x')
scrollY = ttk.Scrollbar(frame2,orient=VERTICAL)
scrollY.pack(side='right',fill='y')

table = ttk.Treeview(frame2,columns=('not','ref','dose','isseD','expD','DD','SD','PN','DOB','PA','PhNum'),xscrollcommand=scrollY.set,yscrollcommand=scrollX.set)
scrollX = ttk.Scrollbar(command=table.xview)
scrollY = ttk.Scrollbar(command=table.yview )

#Heading for Prescription Data
table.heading('not',text='No of Tablet')
table.heading('ref',text='Refrence No.')
table.heading('dose',text='Dose')
table.heading('isseD',text='Issue Date')
table.heading('expD',text='Exp Date')
table.heading('DD',text='Daily Dose')
table.heading('SD',text='Side Effect')
table.heading('PN',text='Pateint Name')
table.heading('DOB',text='Date of Birth')
table.heading('PA',text='Patient Address')
table.heading('PhNum',text='Phone Number')
table['show'] = 'headings'
table.pack(fill=BOTH,expand=1)


table.column('not',width=120)
table.column('ref',width=120)
table.column('dose',width=120)
table.column('isseD',width=120)
table.column('expD',width=120)
table.column('DD',width=120)
table.column('SD',width=120)
table.column('PN',width=120)
table.column('DOB',width=120)
table.column('PA',width=120)
table.column('PhNum',width=120)

mainloop()