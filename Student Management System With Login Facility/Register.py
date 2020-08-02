from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
class Register:
    def __init__(self,root1):
        self.root1=root1
        self.root1.title("Registration Window")
        self.root1.geometry("1920x1080+0+0")
        self.root1.config(bg="white")
        #=======Background Image=============#
        self.bg=ImageTk.PhotoImage(file="F://Student Management System With Login Facility/images/bg2.jpg")
        bg=Label(self.root1,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #=======left Image=============#
        self.left=ImageTk.PhotoImage(file="F://Student Management System With Login Facility/images/side1.jpg")
        bg=Label(self.root1,image=self.left).place(x=200,y=120,width=400,height=500)
        #=========Registration Frame====#
        frame1=Frame(self.root1,bg="white")
        frame1.place(x=590,y=120,width=800,height=500)
        
        title=Label(frame1,text="REGISTER HERE",font=("times new roman",30,"bold"),bg="white",fg="dark blue").place(x=50,y=30)
        
        #=========Row1=======#
        
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_lname.place(x=370,y=130,width=250)
        
        #=========Row2=====#
        
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame1,text="E-Mail",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_email.place(x=370,y=200,width=250)
        
        #=========Row3=====#
        
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=240)
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify=CENTER)
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)
        
        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_answer.place(x=370,y=270,width=250)

        #=========Row4=====#
        
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_password.place(x=50,y=340,width=250)
        
        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_cpassword.place(x=370,y=340,width=250)
        #========Terms=====#
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree To The Terms And Conditions.",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",12),bg="white").place(x=50,y=380)
        self.btn_img=ImageTk.PhotoImage(file="F://Student Management System With Login Facility/images/Register.png")
        btn=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=55,y=420)
        btn_login=Button(self.root1,text="Sign In",font=("times new roman",20),command=self.login_window,bd=0,cursor="hand2").place(x=305,y=480,width=180)
        btn_exit=Button(self.root1,text="Exit",width=11,font=("times new roman",15,"bold"),command=self.exit).place(x=1380,y=20)
    def login_window(self):
        self.root1.destroy()
        import Login
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmb_quest.current(0)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)

    def register_data(self):
        if self.txt_fname.get()=='' or self.txt_email.get()=='' or self.txt_contact.get()=='' or self.cmb_quest.get()=='Select' or self.txt_answer.get()=='' or self.txt_password.get()=='' or self.txt_cpassword.get()=='':
            messagebox.showerror("Error","All Fields Are Required!",parent=self.root1)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password Should Be Same.",parent=self.root1)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms And Conditions",parent=self.root1)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s",self.txt_email.get())
                row=cur.fetchone()
                if row!=None:
                     messagebox.showerror("Error","User Already Exists,Please Try with another Email",parent=self.root1)
                else:
                    cur.execute("insert into employee(f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                (self.txt_fname.get(),
                                self.txt_lname.get(),
                                self.txt_contact.get(),
                                self.txt_email.get(),
                                self.cmb_quest.get(),
                                self.txt_answer.get(),
                                self.txt_password.get()
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Successfully.",parent=self.root1)
                    self.clear()
            except Exception as es:
                messagebox.showinfo("Error",f"Error due to: {str(es)}",parent=self.root1)
            
    def exit(self):
        self.root1.destroy()

root1=Tk()
obj=Register(root1)
root1.mainloop()