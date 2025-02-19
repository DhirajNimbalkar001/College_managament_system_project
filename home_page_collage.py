
from tkinter import*
from PIL import Image,ImageTk
from Home import Student_Win
from Fee_Frontend import Fee
from Library_Frontend import Library
from marksheet import fee_but




class collageSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("college management System")
        self.root.geometry("1550x800+0+0")

        img1=Image.open("dhiraj12.png")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=100)

        

        #===================== img ==========================

       # img2=Image.open("logo.jpg")
        #img2=img2.resize((230,100), Image.ANTIALIAS)
       # self.photoimg2=ImageTk.PhotoImage(img2)
        # 

       # lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        #lblimg.place(x=0,y=0,width=230,height=100)


        #===========================title =================================

        lbl_title=Label( self.root,text="COLLEGE MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=100,width=1550,height=50)

        #======================= Frame ===========================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=150,width=1550,height=620)


        #=======================menu===============================
        lbl_menu=Label( main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        #=============================button frame===============
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_but=Button(btn_frame,text="RAGISTAR",command=self.Student_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_but.grid(row=0,column=0,pady=1)

        fee_but=Button(btn_frame,text="Fee REPORT",command=self.Student_1,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        fee_but.grid(row=1,column=0,pady=1)

        mark_but=Button(btn_frame,text="MARK REPORT",command=self.Student_3,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        mark_but.grid(row=2,column=0,pady=1)

        libry_but=Button(btn_frame,text="LIBRARY REPORT",command=self.Student_2,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        libry_but.grid(row=3,column=0,pady=1)

        log_but=Button(btn_frame,text="LOG OUT",command=self.Logout_p,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        log_but.grid(row=4,column=0,pady=1)

        #======================right side image====================
        img3=Image.open("DB.jpg")
        img3=img3.resize((1310,650),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=650)



        ###= = = = = = = = = = = = = = = = = down image = = = = = = = = = = =####

        img4=Image.open("computer.jpg")
        img4=img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=225,width=230,height=210)



        img5=Image.open("school.jpg")
        img5=img5.resize((230,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=420,width=230,height=190)


    def Student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student_Win(self.new_window)

    
    def Student_1(self):
        self.new_window=Toplevel(self.root)
        self.app=Fee(self.new_window)


    
    def Student_2(self):
        self.new_window=Toplevel(self.root)
        self.app=Library(self.new_window)

    def Student_3(self):
        self.new_window=Toplevel(self.root)
        self.app=fee_but(self.new_window)

    def Logout_p(self):
        self.root.destroy()
       

if __name__ == "__main__":
    root=Tk()
    obj=collageSystem(root)
    root.mainloop()
