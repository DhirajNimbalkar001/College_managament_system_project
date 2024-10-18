from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime



class Fee():
    def __init__(self, master):
        self.master = master
        self.master.title('Fee Report')
        self.master.geometry('1550x810')
        self.master.config(bg='Navajo white')

        # ==================================================Variables=================================================
        self.var_Receipt_No = StringVar()
        self.var_Student_Name = StringVar()
        self.var_Admission_No = StringVar()
      
        self.var_Branch = StringVar()
        self.var_Semester = StringVar()
        self.var_TOTAL_AMOUNT = IntVar()
        self.var_PAID_AMOUNT = IntVar()
        self.var_BALANCE = IntVar()


        def Tuple(event):
            try:
                global st
                index = self.list.curselection()[0]
                st = self.list.get(index)

                self.recpt_entry.delete(0, END)
                self.recpt_entry.insert(END, st[1])
                self.name_entry.delete(0, END)
                self.name_entry.insert(END, st[2])
                self.admsn_entry.delete(0, END)
                self.admsn_entry.insert(END, st[3])
                self.Date_entry.delete(0, END)
                self.Date_entry.insert(END, st[4])
                self.branch_entry.delete(0, END)
                self.branch_entry.insert(END, st[5])
                self.sem_entry.delete(0, END)
                self.sem_entry.insert(END, st[6])
                self.total_entry.delete(0, END)
                self.total_entry.insert(END, st[7])
                self.paid_entry.delete(0, END)
                self.paid_entry.insert(END, st[8])
                self.due_entry.delete(0, END)
                self.due_entry.insert(END, st[9])
            except IndexError:
                pass

        # ==================================================Functions=================================================
      




        def Receipt():
            self.Display.delete('1.0', END)
            self.Display.insert(END, '\t\tRECEIPT' + '\n\n')
            self.Display.insert(
                END, '\tReceipt No.\t     :' + self.var_Receipt_No.get() + '\n')
            self.Display.insert(END, '\tStudent Name  :' +
                                self.var_Student_Name.get() + '\n')
            self.Display.insert(END, '\tAdmission No.\t:' +
                                self.var_Admission_No.get() + '\n')
         
            self.Display.insert(
                END, '\tBranch\t          :' + self.var_Branch.get() + '\n')
            self.Display.insert(
                END, '\tSemester \t        :' + self.var_Semester.get() + '\n\n')

            x1 = (self.var_TOTAL_AMOUNT.get())
            x2 = (self.var_PAID_AMOUNT.get())
            x3 = (x1 - x2)
            

            self.Display.insert(END, '\tTotal Amount  :' + str(x1) + '\n')
            self.Display.insert(END, '\tPaid Amount   :' + str(x2) + '\n')
            self.Display.insert(END, '\tBalance\t     :' + str(x3) + '\n')

            self.var_BALANCE.set(x3)


        def Exit():
                     Exit = messagebox.askyesno('home_page_collage','Confirm if you want to Exit')
                     if Exit > 0:
                            root.destroy()
                            return
        
     


    

        


        # ==================================================Frames===================================================
        Main_Frame = Frame(self.master, bg='Navajo white')
        Main_Frame.grid()

        Title_Frame = LabelFrame(
            Main_Frame, width=1350, height=100, bg='Navajo white', relief='ridge', bd=15)
        Title_Frame.pack(side=TOP)

        self.lblTitle = Label(Title_Frame, font=('arial', 40, 'bold'), text='FEE REPORT',
                              bg='navajowhite', padx=13)
        self.lblTitle.grid(padx=400)

        Data_Frame = Frame(Main_Frame, width=1350, height=350,
                           bg='Navajo white', relief='ridge', bd=15)
        Data_Frame.pack(side=TOP, padx=15)

        Frame_1 = LabelFrame(Data_Frame, width=850, height=350, bg='Navajo white', relief='ridge', bd=8,
                             text='Informations', font=('arial', 15, 'bold'))
        Frame_1.pack(side=LEFT, padx=10)

        Frame_2 = LabelFrame(Data_Frame, width=495, height=350, bg='Navajo white', relief='ridge', bd=8,
                             text='Fee Receipt', font=('arial', 15, 'bold'))
        Frame_2.pack(side=RIGHT, padx=10)

        List_Frame = Frame(Main_Frame, width=1350, height=150,
                           bg='Navajo white', relief='ridge', bd=15)
        List_Frame.pack(side=TOP, padx=15)

        Button_Frame = Frame(Main_Frame, width=1350, height=80,
                              relief='ridge', bd=15)
        Button_Frame.pack(side=TOP)

        table_frame=Frame(Main_Frame,bd=4,relief=RIDGE)
        table_frame.place(x=55,y=440,width=1330,height=130)

        Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("Receipt_No","Student_Name","Admission_No","Branch","Semester","TOTAL_AMOUNT","PAID_AMOUNT","BALANCE"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.student_table.xview)
        Scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Receipt_No",text="Receipt_No")
        self.student_table.heading("Student_Name",text="Student_Name")
        self.student_table.heading("Admission_No",text="Admission_No")
        self.student_table.heading("Branch",text="Branch")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("TOTAL_AMOUNT",text="TOTAL_AMOUNT")
        self.student_table.heading("PAID_AMOUNT",text="PAID_AMOUNT")
        self.student_table.heading("BALANCE",text="Remaining BALANCE")

        self.student_table["show"]="headings"
        self.student_table.column("Receipt_No",width=100)
        self.student_table.column("Student_Name",width=100)
        self.student_table.column("Admission_No",width=100)
        self.student_table.column("Branch",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("TOTAL_AMOUNT",width=100)
        self.student_table.column("PAID_AMOUNT",width=100)
        self.student_table.column("BALANCE",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cuersor)
        self.fetch_data()

        # ===================================================Labels================================================
        self.recpt_label = Label(Frame_1, text='Receipt_No. : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.recpt_label.grid(row=0, column=0, padx=15, sticky=W)

        self.name_label = Label(Frame_1, text='Student_Name : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.name_label.grid(row=1, column=0, padx=15, sticky=W)

        self.admsn_label = Label(Frame_1, text='Admission_No. : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.admsn_label.grid(row=2, column=0, padx=15, sticky=W)



        self.branch_label = Label(Frame_1, text='Branch : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.branch_label.grid(row=4, column=0, padx=15, sticky=W)

        self.sem_label = Label(Frame_1, text='Semester : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.sem_label.grid(row=5, column=0, padx=15, sticky=W)

        self.var_com_search=StringVar()
        com_search=ttk.Combobox(Frame_1,textvariable=self.var_com_search,font=("arial",12,"bold"),width=18)
        com_search["value"]=("Select Option","Receipt_No","Student_Name")
        com_search.current(0)
        com_search.grid(row=1,column=2,padx=5,sticky=W)


        self.total_label = Label(Frame_1, text='TOTAL_AMOUNT : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.total_label.grid(row=2, column=2, padx=5, sticky=W)

        self.paid_label = Label(Frame_1, text='PAID_AMOUNT : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.paid_label.grid(row=3, column=2, padx=5, sticky=W)

        self.due_label = Label(Frame_1, text='Remaining BALANCE : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.due_label.grid(row=4, column=2, padx=5, sticky=W)

        # ==================================================Entries=================================================
        self.var_TOTAL_AMOUNT = IntVar(Frame_1, value='36265')
   

        self.recpt_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.var_Receipt_No)
        self.recpt_entry.grid(row=0, column=1, padx=15, pady=5)

        self.name_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.var_Student_Name)
        self.name_entry.grid(row=1, column=1, padx=15, pady=5)

        self.admsn_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.var_Admission_No)
        self.admsn_entry.grid(row=2, column=1, padx=15, pady=5)

   

        self.branch_entry = ttk.Combobox(Frame_1, values=(' ', 'Bcs-I', 'Bcs-II', 'Bcs-III', 'Mechanical', 'Civil', 'EE', 'EEE'),
                                         font=('arial', 14), width=19, textvariable=self.var_Branch)
        self.branch_entry.grid(row=4, column=1, padx=15, pady=5)

        self.sem_entry = ttk.Combobox(Frame_1, values=(' ', 'FIRST', 'SECOND', 'THIRD', 'FOURTH', 'FIFTH', 'SIXTH',
                                                       'SEVENTH', 'EIGHTH'), font=('arial', 14), width=19,
                                      textvariable=self.var_Semester)
        self.sem_entry.grid(row=5, column=1, padx=15, pady=5)

        self.var_search=StringVar()
        txt_search=ttk.Entry(Frame_1,textvariable=self.var_search,width=22,font=("arial",11,"bold"))
        txt_search.grid(row=1,column=3,sticky=W,padx=8,pady=7)

        self.total_entry = Entry(Frame_1, font=(
            'arial', 14), width=10, textvariable=self.var_TOTAL_AMOUNT, state='readonly')
        self.total_entry.grid(row=2, column=3, padx=8, pady=5)

        self.paid_entry = Entry(Frame_1, font=(
            'arial', 14), width=10, textvariable=self.var_PAID_AMOUNT)
        self.paid_entry.grid(row=3, column=3, pady=5)

        self.due_entry = Entry(Frame_1, font=(
            'arial', 14), width=10, textvariable=self.var_BALANCE)
        self.due_entry.grid(row=4, column=3, pady=7)

        # ==================================================Frame_2=================================================
        self.Display = Text(Frame_2, width=42, height=12,
                            font=('arial', 14, 'bold'))
        self.Display.grid(row=0, column=0, padx=3)

        
        # =============================================List box and scrollbar===========================================
       

        # ==================================================Buttons=================================================
        btnSave = Button(Button_Frame, text='SAVE',command=self.add_data,font=(
            'arial',14,'bold'),width=10)
        btnSave.grid(row=0, column=0, padx=5, pady=5)

        btnDisplay = Button(Button_Frame, text='DISPLAY Data',command=self.fetch_data,font=(
            'arial', 14, 'bold'),width=10)
        btnDisplay.grid(row=0, column=1, padx=5, pady=5)

        btnReset = Button(Button_Frame, text='RESET', command=self.reset_data,font=(
            'arial', 14, 'bold'),width=10)
        btnReset.grid(row=0, column=2, padx=5, pady=5)

        btnReset = Button(Button_Frame, text='UPDATE',command=self.update_data,font=(
            'arial', 14, 'bold'),width=10)
        btnReset.grid(row=0, column=3, padx=5, pady=5)

        btnSearch = Button(Button_Frame, text='SEARCH', command=self.search_data,font=(
            'arial', 14, 'bold'),width=10)
        btnSearch.grid(row=0, column=4, padx=5, pady=5)

        btnDelete = Button(Button_Frame, text='DELETE',command=self.delete_data, font=(
            'arial', 14, 'bold'),width=10)
        btnDelete.grid(row=0, column=5, padx=5, pady=5)

        btnReceipt = Button(Button_Frame, text='RECEIPT', font=(
            'arial', 14, 'bold'),width=10, command=Receipt)
        btnReceipt.grid(row=0, column=6, padx=5, pady=5)

        btnExit = Button(Button_Frame, text='EXIT', font=(
            'arial', 14, 'bold'),width=10, command=Exit)
        btnExit.grid(row=0, column=7, padx=5, pady=5)


    def add_data(self):
        if (self.var_Receipt_No.get()=="" or self.var_Admission_No.get()=="" or self.var_Student_Name.get()==""):
            messagebox.showerror("Error","All Fields are Required")
        else:
            conn=mysql.connector.connect(host="localhost", user="root", password="Admin@123", database="collage")
            my_cursur=conn.cursor()
            my_cursur.execute("insert into fee2 values(%s,%s,%s,%s,%s,'%s','%s','%s')",(
                                                                 self.var_Receipt_No.get(),
                                                                 self.var_Student_Name.get(),
                                                                 self.var_Admission_No.get(),
                                                                 
                                                                 self.var_Branch.get(),
                                                                 self.var_Semester.get(),
                                                                 self.var_TOTAL_AMOUNT.get(),
                                                                 self.var_PAID_AMOUNT.get(),
                                                                 self.var_BALANCE.get()
                                                                
                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Seccess","Student has been added",parent=self.master)

    def fetch_data(self):
         conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123", database="collage")
         my_cursur = conn.cursor()
         my_cursur.execute("select * from fee2")
         data=my_cursur.fetchall()
         if len(data)!=0:
             self.student_table.delete(*self.student_table.get_children())
             for i in data:
                 self.student_table.insert("",END,values=i)
             conn.commit()
         conn.close() 

    def get_cuersor(self,event=""):
        cusrsor_row=self.student_table.focus()
        content=self.student_table.item(cusrsor_row)
        rows=content["values"]

        self.var_Receipt_No.set(rows[0])
        self.var_Student_Name.set(rows[1])
        self.var_Admission_No.set(rows[2])
        self.var_Branch.set(rows[3])
        self.var_Semester.set(rows[4])
        self.var_TOTAL_AMOUNT.set(rows[5])
        self.var_PAID_AMOUNT.set(rows[6])
        self.var_BALANCE.set(rows[7])

    def update_data(self):
        if self.var_Receipt_No.get()=="" or self.var_Student_Name.get()=="":
            messagebox.showerror("Error","All Fields Are required",parent=self.root)
        else:          
            conn=mysql.connector.connect(host="localhost",username="root",password="Admin@123",database="collage")
            my_cursor=conn.cursor() 
            my_cursor.execute("Update fee2 set Student_Name=%s, Admission_No=%s, Branch=%s, Semester=%s,TOTAL_AMOUNT=%s,PAID_AMOUNT=%s,BALANCE=%s where Receipt_No=%s",(
                
                                                                 self.var_Student_Name.get(),
                                                                 self.var_Admission_No.get(),
                                                                 self.var_Branch.get(),
                                                                 self.var_Semester.get(),
                                                                 
                                                                 self.var_TOTAL_AMOUNT.get(),
                                                                 self.var_PAID_AMOUNT.get(),
                                                                 self.var_BALANCE.get(),
                                                                 self.var_Receipt_No.get()
                                                                 
                                                               

                                                            ))
                # else:
                #     if not update:
                #         return    
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","student details has been updated successfully",parent=self.master)


    def delete_data(self):
        if self.var_Receipt_No.get()=="":
            messagebox.showerror("Error","All Fields Are required")
        else:
          # try:
                # Delete=messagebox.askyesno("Delete","Are sure delete this student")
                # if Delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Admin@123",database="collage")
            my_cursor=conn.cursor() 
            sql="delete from fee2 where  Receipt_No=%s"
            value=(self.var_Receipt_No.get(),)
            my_cursor.execute(sql,value)
                # else:
                #     if not Delete:
                #         return
            conn.commit()
            self.fetch_data
            conn.close()
            messagebox.showinfo("Delete","your Student has been Deleted",parent=self.master)

    def reset_data(self):
        
        self.var_Receipt_No.set("")
        self.var_Student_Name.set("")
        self.var_Admission_No.set("")
        self.var_Branch.set("")
        self.var_Semester.set("")
        #self.var_TOTAL_AMOUNT.set("")
        self.var_PAID_AMOUNT.set("")
        self.var_BALANCE.set("")
        
    def search_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="Admin@123",database="collage")
         my_cursor=conn.cursor() 

         my_cursor.execute("select * from fee2 where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.student_table.delete(*self.student_table.get_children())
             for i in rows:
                 self.student_table.insert("",END,values=i)

             conn.commit()
         conn.close()
    













        
if __name__ == "__main__":


   root = Tk()
   obj = Fee(root)
   root.mainloop()
