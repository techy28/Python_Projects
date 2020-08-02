from tkinter import*
from PIL import Image,ImageTk
class index_page:
    def __init__(self,root):
        self.root=root
        self.root.title("Welcome")
        self.root.geometry("480x300+500+150")
        self.root.config(bg="white")
        #=======Background Image=============#
        self.bg=ImageTk.PhotoImage(file="F://Student Management System With Login Facility/images/bg2.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        title=Label(self.root,text="Welcome",bd=5,relief=GROOVE,font=("times new roman",25,"bold"),fg="white",bg="black")
        title.pack(side=TOP,fill=X)

        choice=Label(self.root,text="What Do You Want To Do :- ",bd=2,font=("times new roman",20,"bold"),fg="white",bg="black")
        choice.place(x=10,y=60)
        login_btn=Button(self.root,text="Sign In",width=11,height=1,font=("times new roman",15,"bold"),fg="white",bg="black",command=self.login).place(x=80,y=150)
        register_btn=Button(self.root,text="Sign Up",width=11,font=("times new roman",15,"bold"),fg="white",bg="black",command=self.register).place(x=250,y=150)
        exit_btn=Button(self.root,text="Exit",width=11,font=("times new roman",15,"bold"),fg="white",bg="black",command=self.exit).place(x=160,y=200)
    def login(self):
        self.root.destroy()
        import Login
    def register(self):
        self.root.destroy()
        import Register
    def exit(self):
        self.root.destroy()
root=Tk()
obj=index_page(root)
root.mainloop()