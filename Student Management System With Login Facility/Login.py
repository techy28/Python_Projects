from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="white")
        #=======Background Image=============#
        self.bg=ImageTk.PhotoImage(file="F://Student Management System With Login Facility/images/bg2.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #=======left Image=============#
        self.left=ImageTk.PhotoImage(file="F://Student Management System With Login Facility/images/side1.jpg")
        bg=Label(self.root,image=self.left).place(x=260,y=120,width=400,height=500)
        #=========Login Frame====#
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=660,y=120,width=600,height=500)
        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="dark blue").place(x=50,y=30)
        
        #============FRAMES=======#
        email=Label(login_frame,text="E-Mail Address",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=50,y=110)
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=50,y=155,width=355,height=35)
        
        pass_=Label(login_frame,text="PASSWORD",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=50,y=225)
        self.txt_pass=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=50,y=275,width=350,height=35)
        btn_login=Button(login_frame,text="Login",font=("times new roman",20,"bold"),command=self.login,justify="center",bg="#B00857",fg="white",cursor="hand2").place(x=50,y=400,width=150,height=38)
        btn_reg=Button(login_frame,text="Register New Account?",font=("times new roman",15,"bold"),command=self.register_window,bd=0,justify="center",bg="white",fg="#B00857",cursor="hand2").place(x=50,y=330)
        btn_reg=Button(login_frame,text="Forget Password?",font=("times new roman",15,"bold"),command=self.forget_password_window,bd=0,justify="center",bg="white",fg="red",cursor="hand2").place(x=300,y=330)
        btn_exit=Button(self.root,text="Exit",width=11,font=("times new roman",15,"bold"),command=self.exit).place(x=1380,y=20)
    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass.delete(0,END)
        self.txt_email.delete(0,END)
    #===========Forget Password======#   
    def forget_pass(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and question=%s and answer=%s",(self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter the correct Security Question/ Answer",parent=self.root2)
                else:
                    cur.execute("update employee set password=%s where email=%s",(self.txt_new_pass.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your Password has been reset,Please login with New Password",parent=self.root2)
                    self.reset()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due To :  {str(es)}",parent=self.root)
    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter a E-mail Address to reset your password",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s",self.txt_email.get())
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter a Valid E-mail Address to reset your password",parent=self.root)
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("400x400+600+150")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    self.root2.config(bg="white")
                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold",),bg="white",fg="red").place(x=0,y=0,relwidth=1,relheight=0.1)
                    question=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=70,y=100)
                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13),state="readonly",justify=CENTER)
                    self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
                    self.cmb_quest.place(x=70,y=135,width=250)
                    self.cmb_quest.current(0)
                        
                    answer=Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=70,y=180)
                    self.txt_answer=Entry(self.root2,font=("times new roman",15),bg="lightgrey")
                    self.txt_answer.place(x=70,y=210,width=250)

                    new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=70,y=260)
                    self.txt_new_pass=Entry(self.root2,font=("times new roman",15),bg="lightgrey")
                    self.txt_new_pass.place(x=70,y=290,width=250)

                    btn_change_password=Button(self.root2,text="Reset Password",command=self.forget_pass,bg="green",fg="white",font=("times new roman",15,"bold")).place(x=115,y=340)
                     
            except Exception as es:
                messagebox.showerror("Error",f"Error Due To :  {str(es)}",parent=self.root)
            
    def register_window(self):
        self.root.destroy()
        import Register
    
    def login(self):
        if self.txt_email.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error","All Fields Are Required!",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and password=%s",
                (self.txt_email.get(),self.txt_pass.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username and Password",parent=self.root)
                    self.root.destroy()
                    import Register
                else:
                    messagebox.showinfo("Success","Welcome!",parent=self.root)    
                con.close() 
                self.root.destroy()
                import Student_Management_System
            except Exception as es:
                messagebox.showerror("Error",f"Error Due To :  {str(es)}",parent=self.root)
    def exit(self):
        self.root.destroy()
root=Tk()
obj=login_window(root)
root.mainloop()