from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class Student_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("collage management System")
        self.root.geometry("1550x800+0+0")

        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_DOB=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        

        #+++++1st Img No 1
        img1=Image.open("DB.jpg")
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1)
        lblimg.place(x=0,y=0,width=520,height=160)

        #======2st img
        img2=Image.open("img1.jpg")
        img2=img2.resize((500,160),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(self.root,image=self.photoimg2)
        lblimg2.place(x=520,y=0,width=500,height=160)

        #==========3st img

        img3=Image.open("dhiraj12.png")
        img3=img3.resize((540,160),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg3=Label(self.root,image=self.photoimg3)
        lblimg3.place(x=1000,y=0,width=520,height=160)

        #=======4st img

        img4=Image.open("hotel1.png")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_lbl=Label(self.root,image=self.photoimg4,bd=4,relief=RIDGE)
        bg_lbl.place(x=0,y=160,width=1530,height=710)

        lbl_title=Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),fg="blue",bg="white")
        lbl_title.place(x=0,y=0,width=1530,height=50)


        Manage_frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg="white")
        Manage_frame.place(x=15,y=55,width=1500,height=560)

        button1=Button(bg_lbl,text="Go Back",font=("arial",11,"bold"),width=8,bg="blue",fg="white")
        button1.place(x=355,y=525)


  

        #left frame

        DataLeftFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        DataLeftFrame.place(x=10,y=10,width=660,height=540)

        img6=Image.open("dhiraj12.png")
        img6=img6.resize((650,120),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        my_img=Label(DataLeftFrame,image=self.photoimg6,bd=2,relief=RIDGE)
        my_img.place(x=0,y=0,width=650,height=120)

        # current course LabelFream Information
        std_lbl_info_frame=LabelFrame(DataLeftFrame,bd=2,relief=RIDGE,padx=2,text="Current Course  Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        std_lbl_info_frame.place(x=0,y=120,width=650,height=120)

        #label and combobox=====

        lbl_dep=Label(std_lbl_info_frame,text="Department",font=("arial",12,"bold"),bg="white")
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_dep,font=("arial",12,"bold"),width=17,state="readonly")
        combo_dep["value"]=("Select Department","Computer science","IT","Civil")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #### course  
        course_std=Label(std_lbl_info_frame,font=("arial",12,"bold"),text="Courses:",bg="white")
        course_std.grid(row=0,column=2,sticky=W,padx=2,pady=10)

        combo_txtcouurse_std=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_course,font=("arial",12,"bold"),width=17,state="readonly")
        combo_txtcouurse_std["value"]=("Select Course","BCS-I","BCS-II","BCS-III")
        combo_txtcouurse_std.current(0)
        combo_txtcouurse_std.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #### Year  
        current_year=Label(std_lbl_info_frame,font=("arial",12,"bold"),text="Year:",bg="white")
        current_year.grid(row=1,column=0,sticky=W,padx=2,pady=10)

        com_txt_currunt_year=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_year,font=("arial",12,"bold"),width=17, state="readonly")
        com_txt_currunt_year["value"]=("Select Year","2021-2022","2022-2023","2023-2024","2024-2025")
        com_txt_currunt_year.current(0)
        com_txt_currunt_year.grid(row=1,column=1,padx=2,sticky=W)

        #### semster
        label_Semster=Label(std_lbl_info_frame,font=("arial",12,"bold"),text="Semster:",bg="white")
        label_Semster.grid(row=1,column=2,sticky=W,padx=2,pady=10)

        comSemester=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_sem,font=("arial",12,"bold"),width=17,state="readonly")
        comSemester["value"]=("Select Semester","Semster-1","Semster-2")
        comSemester.current(0)
        comSemester.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Student class LabelFream Information
        std_lbl_class_frame=LabelFrame(DataLeftFrame,bd=2,relief=RIDGE,padx=2,text="Class Course  Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        std_lbl_class_frame.place(x=0,y=235,width=650,height=235)

        label_id=Label(std_lbl_class_frame,font=("arial",12,"bold"),text="StudentID:",bg="white")
        label_id.grid(row=0,column=0,sticky=W,padx=2,pady=7)

        id_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_id,font=("arial",11,"bold"),width=22)
        id_entry.grid(row=0,column=1,sticky=W,padx=2,pady=7)

        ##name
        label_Name=Label(std_lbl_class_frame,font=("arial",12,"bold"),text="Student Name:",bg="white")
        label_Name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        name_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_name,font=("arial",11,"bold"))
        name_entry.grid(row=0,column=3,sticky=W,padx=2,pady=7)

        ###Division

        label_div=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Class Division:",bg="white")
        label_div.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        com_div=ttk.Combobox(std_lbl_class_frame,textvariable=self.var_div,font=("arial",12,"bold"),width=18,state="readonly")
        com_div["value"]=("Select Division","A","B","C")
        com_div.current(0)
        com_div.grid(row=1,column=1,padx=2,pady=7,sticky=W)

        ##Roll
        label_roll=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Roll No:",bg="white")
        label_roll.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        name_roll=ttk.Entry(std_lbl_class_frame,textvariable=self.var_roll,font=("arial",11,"bold"))
        name_roll.grid(row=1,column=3,sticky=W,padx=2,pady=7)

        #########gender

        label_GENDER=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Gender:",bg="white")
        label_GENDER.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        com_gender=ttk.Combobox(std_lbl_class_frame,textvariable=self.var_gender,font=("arial",12,"bold"),width=18,state="readonly")
        com_gender["value"]=("Male","Female","Other")
        com_gender.current(0)
        com_gender.grid(row=2,column=1,padx=2,pady=7,sticky=W)

        #+++date of birth

        label_DOB=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="DOB:",bg="white")
        label_DOB.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        name_DOB=ttk.Entry(std_lbl_class_frame,textvariable=self.var_DOB,font=("arial",11,"bold"))
        name_DOB.grid(row=2,column=3,sticky=W,padx=2,pady=7)

        ### Email

        label_email=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Email ID:",bg="white")
        label_email.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        name_email=ttk.Entry(std_lbl_class_frame,textvariable=self.var_email,font=("arial",11,"bold"))
        name_email.grid(row=3,column=1,sticky=W,padx=2,pady=7)

        #####phone

        label_phone=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Phone NO:",bg="white")
        label_phone.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        name_phone=ttk.Entry(std_lbl_class_frame,textvariable=self.var_phone,font=("arial",11,"bold"))
        name_phone.grid(row=3,column=3,sticky=W,padx=2,pady=7)

        ####Address
        label_Address=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Address:",bg="white")
        label_Address.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        name_Address=ttk.Entry(std_lbl_class_frame,textvariable=self.var_address,font=("arial",11,"bold"))
        name_Address.grid(row=4,column=1,sticky=W,padx=2,pady=7)

        ####Teacher
        label_Techer=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Techer Name:",bg="white")
        label_Techer.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        name_Techer=ttk.Entry(std_lbl_class_frame,textvariable=self.var_teacher,font=("arial",11,"bold"))
        name_Techer.grid(row=4,column=3,sticky=W,padx=2,pady=7)

        # Button Fream
        btn_frame=Frame(DataLeftFrame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=470,width=650,height=38)

        btn_Add=Button(btn_frame,text="save",command=self.add_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_Add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",command=self.update_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_reset.grid(row=0,column=3,padx=1)





        #right frame

        
        DataRightFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        DataRightFrame.place(x=680,y=10,width=800,height=540)

        ###img1



        img5=Image.open("DB.jpg")
        img5=img5.resize((780,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg5=Label(DataRightFrame,image=self.photoimg5,bd=2,relief=RIDGE)
        lblimg5.place(x=0,y=0,width=790,height=200)

        ######Right Frame

                
        Search_Frame=LabelFrame(DataRightFrame,bd=4,relief=RIDGE,padx=2,text=" Search Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        Search_Frame.place(x=0,y=200,width=790,height=60)

        search_by=Label(Search_Frame,font=("arial",11,"bold"),text="Search By:",bg="black",fg="red")
        search_by.grid(row=0,column=0,sticky=W,padx=2,pady=7)


        # search
        self.var_com_search=StringVar()
        com_search=ttk.Combobox(Search_Frame,textvariable=self.var_com_search,font=("arial",12,"bold"),width=18)
        com_search["value"]=("Select Option","Roll_No","Phone","student_id")
        com_search.current(0)
        com_search.grid(row=0,column=1,padx=5,sticky=W)
        
        self.var_search=StringVar()
        txt_search=ttk.Entry(Search_Frame,textvariable=self.var_search,width=22,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        btn_search=Button(Search_Frame,text="Search",command=self.search_data,font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn_search.grid(row=0,column=3,padx=5)

        btn_ShowAll=Button(Search_Frame,text="ShowAll",command=self.fetch_data,font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn_ShowAll.grid(row=0,column=4,padx=1)

        #### student Table and Scroll bar===
        table_frame=Frame(DataRightFrame,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=260,width=790,height=250)

        Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","Roll_No","gender","DOB","email","phone","address","teacher"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.student_table.xview)
        Scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("div",text="Class Div")
        self.student_table.heading("Roll_No",text="Roll_No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher Name")

        self.student_table["show"]="headings"
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("Roll_No",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cuersor)
        self.fetch_data()


    def add_data(self):
        if (self.var_dep.get()=="" or self.var_email.get()=="" or self.var_id.get()==""):
            messagebox.showerror("Error","All Fields are Required")
        else:
            conn=mysql.connector.connect(host="localhost", user="root", password="Admin@123", database="collage")
            my_cursur=conn.cursor()
            my_cursur.execute("insert into studentnew values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                 self.var_dep.get(),
                                                                 self.var_course.get(),
                                                                 self.var_year.get(),
                                                                 self.var_sem.get(),
                                                                 self.var_id.get(),
                                                                 self.var_name.get(),
                                                                 self.var_div.get(),
                                                                 self.var_roll.get(),
                                                                 self.var_gender.get(),
                                                                 self.var_DOB.get(),
                                                                 self.var_email.get(),
                                                                 self.var_phone.get(),
                                                                 self.var_address.get(),
                                                                 self.var_teacher.get()
                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Seccess","Student has been added",parent=self.root)
            
                
    ###fetch data
    def fetch_data(self):
         conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123", database="collage")
         my_cursur = conn.cursor()
         my_cursur.execute("select * from studentnew")
         data=my_cursur.fetchall()
         if len(data)!=0:
             self.student_table.delete(*self.student_table.get_children())
             for i in data:
                 self.student_table.insert("",END,values=i)
             conn.commit()
         conn.close()

    #### get cursor####
    def get_cuersor(self,event=""):
        cusrsor_row=self.student_table.focus()
        content=self.student_table.item(cusrsor_row)
        rows=content["values"]

        self.var_dep.set(rows[0])
        self.var_course.set(rows[1])
        self.var_year.set(rows[2])
        self.var_sem.set(rows[3])
        self.var_id.set(rows[4])
        self.var_name.set(rows[5])
        self.var_div.set(rows[6])
        self.var_roll.set(rows[7])
        self.var_gender.set(rows[8])
        self.var_DOB.set(rows[9])
        self.var_email.set(rows[10])
        self.var_phone.set(rows[11])
        self.var_address.set(rows[12])
        self.var_teacher.set(rows[13])

    def update_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error","All Fields Are required",parent=self.root)
        else:          
            conn=mysql.connector.connect(host="localhost",username="root",password="Admin@123",database="collage")
            my_cursor=conn.cursor() 
            my_cursor.execute("Update studentnew set Department=%s, Course=%s, Year=%s, Semester=%s,Student_Name=%s,Class_Div=%s,Roll_No=%s, Gender=%s, DOB=%s,Email=%s, Phone_No=%s,Address=%s,Teacher_Name=%s where StudentID=%s",(
                
                                                                 self.var_dep.get(),
                                                                 self.var_course.get(),
                                                                 self.var_year.get(),
                                                                 self.var_sem.get(),
                                                                 
                                                                 self.var_name.get(),
                                                                 self.var_div.get(),
                                                                 self.var_roll.get(),
                                                                 self.var_gender.get(),
                                                                 self.var_DOB.get(),
                                                                 self.var_email.get(),
                                                                 self.var_phone.get(),
                                                                 self.var_address.get(),
                                                                 self.var_teacher.get(),
                                                                 self.var_id.get()

                                                            ))
                    
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","student details has been updated successfully",parent=self.root)


    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","All Fields Are required")
        else:
          # try:
                # Delete=messagebox.askyesno("Delete","Are sure delete this student")
                # if Delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Admin@123",database="collage")
            my_cursor=conn.cursor() 
            sql="delete from studentnew where StudentID=%s"
            value=(self.var_id.get(),)
            my_cursor.execute(sql,value)
                # else:
                #     if not Delete:
                #         return
            conn.commit()
            self.fetch_data
            conn.close()
            messagebox.showinfo("Delete","your Student has been Deleted")



      ###### reset data 
                  
    def reset_data(self):
        
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_DOB.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")  


    # search data

    def search_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="Admin@123",database="collage")
         my_cursor=conn.cursor() 

         my_cursor.execute("select * from studentnew where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.student_table.delete(*self.student_table.get_children())
             for i in rows:
                 self.student_table.insert("",END,values=i)

             conn.commit()
         conn.close()

       
            



            






if __name__ == "__main__":
    root=Tk()
    obj=Student_Win(root)
    root.mainloop()       

