from tkinter import*
from tkinter import ttk,messagebox
import pymysql
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="dark gray")
        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),fg="dark blue",bg="gray")
        title.pack(side=TOP,fill=X)
        exitbtn=Button(title,text="Exit",width=11,command=self.exit).place(x=1400,y=20)
        signout_btn=Button(title,text="Sign Out",width=11,command=self.signout).place(x=1300,y=20)
    #======All Variables==========#
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.DOB_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
        #====Manage Frame=====#
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="dark blue")
        Manage_Frame.place(x=20,y=100,width=500,height=680)
        m_title=Label(Manage_Frame,text="Manage Students",font=("times new roman",20,"bold"),bg="dark blue",fg="white")
        m_title.grid(row=0,columnspan=2,pady=15)
        
        #=====Roll No.=====#
        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="dark blue",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=15,padx=20,sticky="w")
        txt_roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=15,padx=20,sticky="w")
        
        #========Name========#
        lbl_name=Label(Manage_Frame,text="Name",bg="dark blue",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=15,padx=20,sticky="w")
        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=15,padx=20,sticky="w")
        
        #======Email=====#
        lbl_email=Label(Manage_Frame,text="E-Mail Address",bg="dark blue",fg="white",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=15,padx=20,sticky="w")
        txt_email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=15,padx=20,sticky="w")
        
        #======Gender=======#
        lbl_gender=Label(Manage_Frame,text="Gender",bg="dark blue",fg="white",font=("times new roman",20,"bold"))
        lbl_gender.grid(row=4,column=0,pady=15,padx=20,sticky="w")
        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state="readonly")
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=20,pady=15)
        
        #====Contact=======#
        lbl_contact=Label(Manage_Frame,text="Contact No.",bg="dark blue",fg="white",font=("times new roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=15,padx=20,sticky="w")
        txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=15,padx=20,sticky="w")
        
        #======DOB======#
        lbl_DOB=Label(Manage_Frame,text="D.O.B",bg="dark blue",fg="white",font=("times new roman",20,"bold"))
        lbl_DOB.grid(row=6,column=0,pady=15,padx=20,sticky="w")
        txt_DOB=Entry(Manage_Frame,textvariable=self.DOB_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_DOB.grid(row=6,column=1,pady=15,padx=20,sticky="w")
        
        #======Address====#
        lbl_address=Label(Manage_Frame,text="Address",bg="dark blue",fg="white",font=("times new roman",20,"bold"))
        lbl_address.grid(row=7,column=0,pady=15,padx=20,sticky="w")
        self.txt_address=Text(Manage_Frame,width=24,height=4,font=("times new roman",13,"bold"))
        self.txt_address.grid(row=7,column=1,pady=15,padx=20,sticky="w")
#========Buttons Frame========#
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="black")
        btn_Frame.place(x=25,y=600,width=440)

        Addbtn=Button(btn_Frame,text="Add",command=self.add_students,width=11)
        Addbtn.grid(row=0,column=0,padx=10,pady=10)

        updatebtn=Button(btn_Frame,command=self.update_data,text="Update",width=11)
        updatebtn.grid(row=0,column=1,padx=10,pady=10)

        deletebtn=Button(btn_Frame,command=self.delete_data,text="Delete",width=11)
        deletebtn.grid(row=0,column=2,padx=10,pady=10)

        Clearbtn=Button(btn_Frame,command=self.clear,text="Clear",width=11)
        Clearbtn.grid(row=0,column=3,padx=10,pady=10)
        
        #====Detail Frame=====#
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="dark blue")
        Detail_Frame.place(x=550,y=100,width=940,height=680)
        
        lbl_search=Label(Detail_Frame,text="Search By",bg="dark blue",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        self.combo_search=ttk.Combobox(Detail_Frame,width=15,textvariable=self.search_by,font=("times new roman",13,"bold"),state="readonly")
        self.combo_search['values']=("Select","Roll_No","Name","Contact")
        self.combo_search.grid(row=0,column=1,padx=10,pady=20)
        self.combo_search.current(0)
        
        txt_search=Entry(Detail_Frame,font=("times new roman",15,"bold"),textvariable=self.search_txt,width=30,bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        
        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,pady=10,padx=10)
        showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,pady=10,padx=10)
        
#=========Table Frame==========#
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="Dark Blue")
        Table_Frame.place(x=10,y=70,width=910,height=590)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll",text="Roll No.")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="E-Mail Address")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact No.")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("address",text="Address")
        
        self.Student_table.column("roll",width=70)
        self.Student_table.column("name",width=130)
        self.Student_table.column("email",width=130)
        self.Student_table.column("gender",width=110)
        self.Student_table.column("contact",width=110)
        self.Student_table.column("dob",width=110)
        self.Student_table.column("address",width=220)
        self.Student_table['show']='headings'
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
#========================================================================================================================================#        
    def add_students(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.gender_var.get()=="" or self.contact_var.get()=="":
            messagebox.showerror("Error","All Fields Are Mandatory!!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.Roll_No_var.get(),
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.DOB_var.get(),
                                                                            self.txt_address.get('1.0',END)
                                                                            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record Added Successfully.")
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.DOB_var.set("")
        self.txt_address.delete("1.0",END)
        self.search_txt.set("")
        self.combo_search.current(0)
    def get_cursor(self,event):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.DOB_var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                        self.name_var.get(),
                                                                        self.email_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.contact_var.get(),
                                                                        self.DOB_var.get(),
                                                                        self.txt_address.get('1.0',END),
                                                                        self.Roll_No_var.get() 
                                                                        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success","Record Updated Successfully!")
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    def search_data(self): 
        con = pymysql.connect(host="localhost", user="root", password="",database="stm") 
        cur = con.cursor() 
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall() 
        if len(rows)!= 0: 
            self.Student_table.delete(*self.Student_table.get_children()) 
            for row in rows: 
                self.Student_table.insert('', END, values=row) 
        else:
            messagebox.showerror("Error","Record Not Found!!")    
            con.commit() 
        con.close()
    def signout(self):
        self.root.destroy()
        import Register
    def exit(self):
        self.root.destroy()

root=Tk()
obj=Student(root)
root.mainloop()