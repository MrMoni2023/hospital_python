import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Gui:
    """Gui class"""
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Login')
        self.root.geometry('925x500+300+200')
        self.root.config(bg= "#cc1231")
        self.root.resizable(False,False)
        
        def signin():
            username = User.get()
            password = code.get()

            if username == 'admin' and password =='1234':
                self.new_window
            else:
                messagebox.showerror("Invalid","Insert Coorect Data")
        img = tk.PhotoImage(file='3.png')
        tk.Label(self.root,image=img,bg='black').place(x=50,y=67)

        frame = tk.Frame(self.root,width=350,height=350,bg='#cc1231')
        frame.place(x=480,y=70)

        heading = tk.Label(frame,text='Sign In',fg='white',bg='#cc1231',font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x=110,y=5)

        #-------------------------------------------#

        def on_enter(e):
            User.delete(0,'end')

        def on_leave(e):
            name = User.get()
            if name == '':
                User.insert(0,'Username')


        User = tk.Entry(frame,width=25,fg='white',border=0,bg='#cc1231',font=('Microsoft YaHei UI Light',11))
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

        code = tk.Entry(frame,width=25,fg='white',border=0,bg='#cc1231',font=('Microsoft YaHei UI Light',11))
        code.place(x=30,y=150)
        code.insert(0,'Password')
        code.bind('<FocusIn>',on_enter)
        code.bind('<FocusOut>',on_leave)

        tk.Frame(frame,width=295,height=2,bg='white').place(x=25,y=177)

        self.new_window = tk.Button(frame,width=39,pady=7,text='Sign In',bg='red',fg='white',border=0, command=self.new_window).place(x=35,y=204)
        #


        self.root.mainloop()
    def new_window(self):
        """Create a new top level window"""
        new_window = tk.Toplevel()
        tk.Label(master=new_window, text="This is a new window").pack()


if __name__ == '__main__':
    Gui()