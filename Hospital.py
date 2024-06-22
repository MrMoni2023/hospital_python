from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.config(bg= "#cc1231")
root.resizable(False,False)


def signin():
    username = User.get()
    password = code.get()

    if username == 'admin' and password =='1234':
        win= Tk()
        win.state('zoomed')
        win.config('black')
        #heading
        Label(win,text='Hospital management system',font='impack 31 bold ',bg= 'blue',fg='white').pack(fill=X)
        
        win.mainloop()
    elif username != 'admin' and password != '1234':
        messagebox.showerror("Invalid","Invalid Username and Password")
    elif password != '1234':
        messagebox.showerror("Invalid","Invalid Password")
    elif username != 'admin':
        messagebox.showerror("Invalid","Invalid Username")

img = PhotoImage(file='3.png')
Label(root,image=img,bg='black').place(x=50,y=67)

frame = Frame(root,width=350,height=350,bg='#cc1231')
frame.place(x=480,y=70)

heading = Label(frame,text='Sign In',fg='white',bg='#cc1231',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=110,y=5)
#-------------------------------------------------------#
def on_enter(e):
    User.delete(0,'end')

def on_leave(e):
    name = User.get()
    if name == '':
        User.insert(0,'Username')

User = Entry(frame,width=25,fg='white',border=0,bg='#cc1231',font=('Microsoft YaHei UI Light',11))
User.place(x=30,y=80)
User.insert(0,'Username')
User.bind('<FocusIn>',on_enter)
User.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='white').place(x=25,y=107)

########---------------------------------------##########
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    Password = code.get()
    if Password == '':
        code.insert(0,'Password')

code = Entry(frame,width=25,fg='white',border=0,bg='#cc1231',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='white').place(x=25,y=177)

#---------------------------------------------------------#
Button(frame,width=39,pady=7,text='Sign In',bg='red',fg='white',border=0,command=signin).place(x=35,y=204)
label = Label(frame,text="We make sure you feel healthy <3",fg='white',bg='#cc1231',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

root.mainloop()