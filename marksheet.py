from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
#from home_page_collage import collageSystem


class fee_but:
    def __init__(self,root):
       self.root=root
       self.root.title("collage management System")
       self.root.geometry("1550x800+0+0")

       self.Var_name = StringVar()
       self.var_roll = StringVar()
      
       self.var_scl = StringVar()
       
       self.var_m1 = IntVar()
       self.var_m2 = IntVar()
       self.var_m3 = IntVar()
       self.var_m4 = IntVar()
       self.var_m5 = IntVar()
       self.var_gt = IntVar()
       self.var_per = IntVar()
       self.var_cgpa = IntVar()
       self.var_grade = StringVar()
       self.var_div = StringVar()
       self.var_result = StringVar()



       
       def Exit():
              Exit = messagebox.askyesno('Marksheet','Confirm if you want to Exit')
              if Exit > 0:
                    # obj=collageSystem(self.root)

                     root.destroy()
                     return

       
       def Compute():
              x1 = (self.var_m1.get());      x2 = (self.var_m2.get());    x3 = (self.var_m3.get());      x4 = (self.var_m4.get());    x5 = (self.var_m5.get())

              if x1 > 100:
                     messagebox.askokcancel('Attention','Please enter Correct Marks')
                     return
              if x2 > 100:
                     messagebox.askokcancel('Attention','Please enter Correct Marks')
                     return
              if x3 > 100:
                     messagebox.askokcancel('Attention','Please enter Correct Marks')
                     return
              if x4 > 100:
                     messagebox.askokcancel('Attention','Please enter Correct Marks')
                     return
              if x5 > 100:
                     messagebox.askokcancel('Attention','Please enter Correct Marks')
                     return
                     
       
              tot = x1+x2+x3+x4+x5
              self.var_gt.set(tot)
              
              Per = ((x1+x2+x3+x4+x5) * 100)/500
              self.var_per.set(Per)


              cg = (((x1+x2+x3+x4+x5) * 100)/500) / 9.5
              self.var_cgpa.set(round(cg,1))

              if cg > 10:
                     self.var_cgpa.set(10)


              if (((x1+x2+x3+x4+x5) * 100)/500) <= 40:
                     grd = 'G'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 50:
                     grd = 'F'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 60:
                     grd = 'E'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 70:
                     grd = 'D'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 80:
                     grd = 'C'
              elif (((x1+x2+x3+x4+x5) * 100)/500) <= 90:
                     grd = 'B'
              else:
                     grd = 'A'

              self.var_grade.set(grd)

              count = 0
              if x1 < 33:
                     count = count + 1
              if x2 < 33:
                     count = count + 1
              if x3 < 33:
                     count = count + 1
              if x4 < 33:
                     count = count + 1
              if x5 < 33:
                     count = count + 1

              if (count == 0):
                     self.var_result.set('PASS')
              elif (count == 1 or count == 2 ):
                     self.var_result.set('SUPPLY')
              else:
                     self.var_result.set('FAIL')

              if Per <= 45 and self.var_result != "FAIL":
                     self.var_div.set('THIRD')
              elif Per <= 60 and self.var_result != "FAIL":
                     self.var_div.set('SECOND')
              elif Per <= 100:
                     self.var_div.set('FIRST')     

       def Reset():
              self.Var_name.set(' ')
              self.var_roll.set(' ')
              
              self.var_scl.set('')
           
              self.var_m1.set(' ')
              self.var_m2.set(' ')
              self.var_m3.set(' ')
              self.var_m4.set(' ')
              self.var_m5.set(' ')
              self.var_gt.set(' ')
              self.var_per.set(' ')
              self.var_cgpa.set(' ')
              self.var_grade.set(' ')
              self.var_div.set(' ')
              self.var_result.set(' ')  
       



       Frame_1 = LabelFrame(self.root, width = 1000, height = 400, font = ('arial',20,'bold'), bg = 'Navajo white', bd = 10, \
                            text = 'Student Details', relief = 'ridge')
       # Frame_1.grid(row = 1, column = 0, pady = 10, padx = 10)
       Frame_1.place(x=100,y=10)

       Frame_3 = LabelFrame(self.root, width =710, height = 180, font = ('arial',20,'bold'), bg = 'Navajo white', bd = 10, \
                            text = 'Student Details', relief = 'ridge')
       # Frame_1.grid(row = 1, column = 0, pady = 10, padx = 10)
       Frame_3.place(x=800,y=10)


       Label_Name = Label(Frame_1, text = 'School Name', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Name.grid(row = 4, column = 0, padx = 80)
       Entry_Name = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = self.Var_name)
       Entry_Name.grid(row = 4, column = 1, padx = 40)

       Label_Roll_no = Label(Frame_1, text = 'Roll Number', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_Roll_no.grid(row = 0, column = 0, padx = 80)
       Entry_Roll_no = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = self.var_roll)
       Entry_Roll_no.grid(row = 0, column = 1, padx = 5, pady = 5)

   
       btnAdd=Button(Frame_1,text="Search ",font=("arial",13,"bold"),bg="black",fg="gold",width=9)
       btnAdd.grid(row=2,column=1,padx=3)



       Label_School = Label(Frame_1, text = ' Student Name', font = ('arial',15,'bold'), bg = 'Navajo white')
       Label_School.grid(row = 3, column = 0, padx = 80)
       Entry_School = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = self.var_scl)
       Entry_School.grid(row = 3, column = 1, padx = 5, pady = 5)



         #========================================================Frame_2==================================================================       
       Frame_2 = LabelFrame(self.root, width = 1200, height = 400, font = ('arial',20,'bold'), bg = 'Navajo white', bd = 10 \
                            , text = 'Grades Point Obtained', relief = 'ridge')
       # Frame_2.grid(row = 3, column = 0)
       Frame_2.place(x=100,y=250)

       table_frame=Frame(self.root,bd=4,relief=RIDGE)
       table_frame.place(x=815,y=40,width=680,height=145)

       Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
       Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
       self.student_table=ttk.Treeview(table_frame,column=("name","roll","sc1","m1","m2","m3","m4","m5","gt","per","cgpa","grade","div","result"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)

       Scroll_x.pack(side=BOTTOM,fill=X)
       Scroll_y.pack(side=RIGHT,fill=Y)

       Scroll_x.config(command=self.student_table.xview)
       Scroll_y.config(command=self.student_table.yview)


       self.student_table.heading("name",text="School_Name")
       self.student_table.heading("roll",text="Roll_Number")
       self.student_table.heading("sc1",text="Name")
       self.student_table.heading("m1",text="MATHEMATICS")
       self.student_table.heading("m2",text="PHYSICS")
       self.student_table.heading("m3",text="CHEMISTRY")
       self.student_table.heading("m4",text="HINDI")
       self.student_table.heading("m5",text="ENGLISH")
       self.student_table.heading("gt",text="GRAND_TOTAL")
       self.student_table.heading("per",text="PERCENTAGE")
       self.student_table.heading("cgpa",text="CGPA")
       self.student_table.heading("grade",text="GRADE")
       self.student_table.heading("div",text="DIVISION")
       self.student_table.heading("result",text="RESULT")

       self.student_table["show"]="headings"
       self.student_table.column("name",width=100)
       self.student_table.column("roll",width=100)
       self.student_table.column("sc1",width=100)
       self.student_table.column("m1",width=100)
       self.student_table.column("m2",width=100)
       self.student_table.column("m3",width=100)
       self.student_table.column("m4",width=100)
       self.student_table.column("m5",width=100)
       self.student_table.column("gt",width=100)
       self.student_table.column("per",width=100)
       self.student_table.column("cgpa",width=100)
       self.student_table.column("grade",width=100)
       self.student_table.column("div",width=100)
       self.student_table.column("result",width=100)


       self.student_table.pack(fill=BOTH,expand=1)
       self.student_table.bind("<ButtonRelease>",self.get_cuersor)
       self.fetch_data()

      


         #======================================================Labels of Frame_2===========================================================

       Label_Subject = Label(Frame_2, text = 'SUBJECT', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_Subject.grid(row = 3, column = 0, padx = 50, pady = 10)

       Label_obt_Marks = Label(Frame_2, text = 'MARKS OBTAINED', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_obt_Marks.grid(row = 3, column = 1, padx = 20)

       Label_Subject = Label(Frame_2, text = 'PASSING MARKS', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_Subject.grid(row = 3, column = 2, padx = 20)

       Label_obt_Marks = Label(Frame_2, text = 'TOTAL MARKS', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_obt_Marks.grid(row = 3, column = 3, padx = 20)

       Label_1 = Label(Frame_2, text = 'JAVA', font = ('arial',14), bg = 'Navajo white')
       Label_1.grid(row = 4, column = 0)
       Label_2 = Label(Frame_2, text = 'PYTHON', font = ('arial',14), bg = 'Navajo white')
       Label_2.grid(row = 5, column = 0)
       Label_3 = Label(Frame_2, text = 'C#', font = ('arial',14), bg = 'Navajo white')
       Label_3.grid(row = 6, column = 0)
       Label_4 = Label(Frame_2, text = 'TCS', font = ('arial',14), bg = 'Navajo white')
       Label_4.grid(row = 7, column = 0)
       Label_5 = Label(Frame_2, text = 'ENGLISH', font = ('arial',14), bg = 'Navajo white')
       Label_5.grid(row = 8, column = 0)
       Label_6 = Label(Frame_2, text = 'GRAND TOTAL', font = ('arial',16), bg = 'Navajo white')
       Label_6.grid(row = 9, column = 0)
       Label_7 = Label(Frame_2, text = 'PERCENTAGE', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_7.grid(row = 10, column = 0)
       Label_8 = Label(Frame_2, text = 'CGPA', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_8.grid(row = 10, column = 2)
       Label_9 = Label(Frame_2, text = 'GRADE', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_9.grid(row = 10, column = 4)
       Label_10 = Label(Frame_2, text = 'DIVISION', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_10.grid(row = 11, column = 0)
       Label_10 = Label(Frame_2, text = 'RESULT', font = ('arial',16,'bold'), bg = 'Navajo white')
       Label_10.grid(row = 11, column = 2)


       var_1 = StringVar(Frame_2, value = '33')
       var_2 = StringVar(Frame_2, value = '100')
       var_3 = StringVar(Frame_2, value = '500')

       Entry__MATHEMATICS1 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = self.var_m1)
       Entry__MATHEMATICS1.grid(row = 4, column = 1)

       Entry__PHYSICS2 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = self.var_m2)
       Entry__PHYSICS2.grid(row = 5, column = 1)

       Entry__CHEMISTRY3 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = self.var_m3)
       Entry__CHEMISTRY3.grid(row = 6, column = 1)

       Entry__HINDI4 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = self.var_m4)
       Entry__HINDI4.grid(row = 7, column = 1)

       Entry__ENGLISH5 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = self.var_m5)
       Entry__ENGLISH5.grid(row = 8, column = 1)

       Entry__GRANDTOTAL6 = Entry(Frame_2, font = ('arial',14), width = 5, textvariable = self.var_gt, state = 'readonly')
       Entry__GRANDTOTAL6.grid(row = 9, column = 1, pady = 8)

       Entry__PERCENTAGE7 = Entry(Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = self.var_per, state = 'readonly')
       Entry__PERCENTAGE7.grid(row = 10, column = 1, pady = 8)

       Entry__CGPA8 = Entry(Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = self.var_cgpa, state = 'readonly')
       Entry__CGPA8.grid(row = 10, column = 3, pady = 8)

       Entry__GRADE9 = Entry(Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = self.var_grade, state = 'readonly')
       Entry__GRADE9.grid(row = 10, column = 5, padx = 20, pady = 8)

       Entry__DIVISION10 = Entry(Frame_2, font = ('arial',14,'bold'), width = 8, textvariable = self.var_div, state = 'readonly')
       Entry__DIVISION10.grid(row = 11, column = 1, padx = 20, pady = 8)

       Entry__RESULT11 = Entry(Frame_2, font = ('arial',14,'bold'), width = 7, textvariable = self.var_result, state = 'readonly')
       Entry__RESULT11.grid(row = 11, column = 3, padx = 20, pady = 8)
       
       Entry_1_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5, state = 'readonly')
       Entry_1_2.grid(row = 4, column = 2, pady = 5)
       Entry_1_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5, state = 'readonly')
       Entry_1_3.grid(row = 4, column = 3)
       Entry_2_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5, state = 'readonly')
       Entry_2_2.grid(row = 5, column = 2, pady = 5)
       Entry_2_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5, state = 'readonly')
       Entry_2_3.grid(row = 5, column = 3)
       Entry_3_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5, state = 'readonly')
       Entry_3_2.grid(row = 6, column = 2, pady = 5)
       Entry_3_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5, state = 'readonly')
       Entry_3_3.grid(row = 6, column = 3)
       Entry_4_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5, state = 'readonly')
       Entry_4_2.grid(row = 7, column = 2, pady = 5)
       Entry_4_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5, state = 'readonly')
       Entry_4_3.grid(row = 7, column = 3)
       Entry_5_2 = Entry(Frame_2, textvariable = var_1, font = ('arial',16), width = 5, state = 'readonly')
       Entry_5_2.grid(row = 8, column = 2, pady = 5)
       Entry_5_3 = Entry(Frame_2, textvariable = var_2, font = ('arial',16), width = 5, state = 'readonly')
       Entry_5_3.grid(row = 8, column = 3)
       Entry_6_3 = Entry(Frame_2, textvariable = var_3, font = ('arial',16), width = 5, state = 'readonly')
       Entry_6_3.grid(row = 9, column = 3)

       Btn_Compute = Button(Frame_2, text = 'COMPUTE', font = ('arial',12,'bold'), width = 10, command = Compute)
       Btn_Compute.grid(row = 4, column = 4, padx = 50, pady = 6)
       Btn_Save = Button(Frame_2, text = 'SAVE', font = ('arial',12,'bold'), width = 10,command=self.add_data)
       Btn_Save.grid(row = 5, column = 4, padx = 50, pady = 6)
       Btn_Update = Button(Frame_2, text = 'UPDATE', font = ('arial',12,'bold'), width = 10,command=self.update_data)
       Btn_Update.grid(row = 6, column = 4, padx = 50, pady = 6)
       Btn_Cancel = Button(Frame_2, text = 'RESET', font = ('arial',12,'bold'), width = 10, command = Reset)
       Btn_Cancel.grid(row = 7, column = 4, padx = 50, pady = 6)
       Btn_Exit = Button(Frame_2, text = 'EXIT', font = ('arial',12,'bold'), width = 10, command =exit)
       Btn_Exit.grid(row = 8, column = 4, padx = 50, pady = 6)

      # self.root.mainloop()



    def add_data(self):
           if (self.Var_name.get()=="" or self.var_roll.get()=="" or self.var_scl.get()==""):
              messagebox.showerror("Error","All Fields are Required")
           else:
               conn=mysql.connector.connect(host="localhost", user="root", password="Admin@123", database="collage")
               my_cursur=conn.cursor()
               my_cursur.execute("insert into marksheet1 values(%s,%s,%s,'%s','%s','%s','%s','%s','%s','%s','%s',%s,%s,%s)",(
                                                                 self.Var_name.get(),
                                                                 self.var_roll.get(),
                                                                 self.var_scl.get(),
                                                                 self.var_m1.get(),
                                                                 self.var_m2.get(),
                                                                 self.var_m3.get(),
                                                                 self.var_m4.get(),
                                                                 self.var_m5.get(),
                                                                 self.var_gt.get(),
                                                                 self.var_per.get(),
                                                                 self.var_cgpa.get(),
                                                                 self.var_grade.get(),
                                                                 self.var_div.get(),
                                                                 self.var_result.get()
                                                            ))
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("Seccess","Student has been added",parent=self.root)


    def fetch_data(self):
         conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123", database="collage")
         my_cursur = conn.cursor()
         my_cursur.execute("select * from  marksheet1")
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

        self.Var_name.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_scl.set(rows[2])
        self.var_m1.set(rows[3])
        self.var_m2.set(rows[4])
        self.var_m3.set(rows[5])
        self.var_m4.set(rows[6])
        self.var_m5.set(rows[7])
        self.var_gt.set(rows[8])
        self.var_per.set(rows[9])
        self.var_cgpa.set(rows[10])
        self.var_grade.set(rows[11])
        self.var_div.set(rows[12])
        self.var_result.set(rows[13])    
       
    
    def update_data(self):
        if self.Var_name.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("Error","All Fields Are required",parent=self.root)
        else:          
            conn=mysql.connector.connect(host="localhost",username="root",password="Admin@123",database="collage")
            my_cursor=conn.cursor() 
            my_cursor.execute("Update marksheet1 set School_Name=%s, Name=%s, MATHEMATICS=%s, PHYSICS=%s,CHEMISTRY=%s,HINDI=%s,ENGLISH=%s, GRAND_TOTAL=%s, PERCENTAGE=%s,CGPA=%s, GRADE=%s,DIVISION=%s,RESULT=%s where Roll_Number=%s",(
                
                                                                 self.Var_name.get(),
                                                                 self.var_scl.get(),
                                                                 self.var_m1.get(),
                                                                 self.var_m2.get(),
                                                                 
                                                                 self.var_m3.get(),
                                                                 self.var_m4.get(),
                                                                 self.var_m5.get(),
                                                                 self.var_gt.get(),
                                                                 self.var_per.get(),
                                                                 self.var_cgpa.get(),
                                                                 self.var_grade.get(),
                                                                 self.var_div.get(),
                                                                 self.var_result.get(),
                                                                 self.var_roll.get()

                                                            ))
                  
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","student details has been updated successfully",parent=self.root)

              

       









if __name__ == "__main__":
    root=Tk()
    obj=fee_but(root)
    root.mainloop()