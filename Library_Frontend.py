from tkinter import*
from tkinter import ttk
import random
from datetime import datetime
from tkinter import messagebox
import mysql.connector


class Library:
       
       def __init__(self, root):
              self.root = root
              self.root.title('Library Management System')
              self.root.geometry('1520x820')
              self.root.config(bg = 'navajowhite')

       #===================================================Variables===================================================
              self.var_Mtype = StringVar()
              self.var_refno = IntVar()
              self.var_fname = StringVar()
              self.var_surname = StringVar()
              self.var_address = StringVar()
              self.var_post = StringVar()
              self.var_mobno = StringVar()
              self.var_ID = StringVar()
              self.var_title = StringVar()
              self.var_author = StringVar()
              self.var_borrow = StringVar()
              self.var_due = StringVar()
              self.var_loan = StringVar()
              self.var_yop = StringVar()
              self.var_edsn = StringVar()
              


       #================================================Functions======================================================
              # def BookRec(event):
              #        try:
              #               global selected_tuple
              #               index = self.Listbox_2.curselection()[0]
              #               selected_tuple = self.Listbox_2.get(index)

              #               self.Entry_0.delete(0, END)
              #               self.Entry_0.insert(END, selected_tuple[1])  
              #               self.Entry_1.delete(0, END)
              #               self.Entry_1.insert(END, selected_tuple[2])                           
              #               self.Entry_2.delete(0, END)
              #               self.Entry_2.insert(END, selected_tuple[3])
              #               self.Entry_3.delete(0, END)
              #               self.Entry_3.insert(END, selected_tuple[4])
              #               self.Entry_4.delete(0, END)
              #               self.Entry_4.insert(END, selected_tuple[5])
              #               self.Entry_5.delete(0, END)
              #               self.Entry_5.insert(END, selected_tuple[6])
              #               self.Entry_6.delete(0, END)
              #               self.Entry_6.insert(END, selected_tuple[7])
              #               self.Entry_7.delete(0, END)
              #               self.Entry_7.insert(END, selected_tuple[8])
              #               self.Entry_8.delete(0, END)
              #               self.Entry_8.insert(END, selected_tuple[9])
              #               self.Entry_9.delete(0, END)
              #               self.Entry_9.insert(END, selected_tuple[10])
              #               self.Entry_10.delete(0, END)
              #               self.Entry_10.insert(END, selected_tuple[11])
              #               self.Entry_11.delete(0, END)
              #               self.Entry_11.insert(END, selected_tuple[12])
              #               self.Entry_12.delete(0, END)
              #               self.Entry_12.insert(END, selected_tuple[13])
                             

              #        except IndexError:
              #               pass
              # def Insert():
              #        if(len(self.refno.get()) != 0):
              #               (self.Mtype.get(), self.var_refno.get(), self.var_fname.get(), self.var_surname.get()\
              #                                      , self.var_address.get(), self.var_post.get(), self.var_mobno.get(), self.var_ID.get()\
              #                                      , self.var_title.get(), self.var_author.get(), self.var_borrow.get(), self.var_due.get()\
              #                                      , self.var_loan.get())
              #               self.Listbox_2.delete(0, END)
              #               self.Listbox_2.insert(END , (self.var_Mtype.get(), self.var_refno.get(), self.var_fname.get(), self.var_surname.get()\
              #                                            , self.var_address.get(), self.var_post.get(), self.var_mobno.get(), self.var_ID.get()\
              #                                            , self.var_title.get(), self.var_author.get(), self.var_borrow.get(), self.var_due.get()\
              #                                            , self.var_loan.get()))
                            

              def Display():
                     self.Listbox_2.delete(0, END)
                     for row in ():
                            self.Listbox_2.insert(END, row, str(' '))  
                                                       
              def Exit():
                     Exit = messagebox.askyesno('Library Management System','Confirm if you want to Exit')
                     if Exit > 0:
                            root.destroy()
                            return
                                                                    
              def Reset():
                     self.var_Mtype.set('')
                     self.var_refno.set('')
                     self.var_fname.set('')
                     self.var_surname.set('')
                     self.var_address.set('')
                     self.var_post.set('')
                     self.var_mobno.set('')
                     self.var_ID.set('')
                     self.var_title.set('')
                     self.var_author.set('')
                     self.var_borrow.set('')
                     self.var_due.set('')
                     self.var_loan.set('')
                     self.Display.delete('1.0',END)
                     self.Listbox_2.delete(0, END)

              

        

              def Search():
                     self.Listbox_2.delete(0, END)
                     for row in (self.var_Mtype.get(), self.var_refno.get(), self.var_fname.get(), self.var_surname.get()\
                                                  , self.var_address.get(), self.var_post.get(), self.var_mobno.get(), self.var_ID.get()\
                                                  , self.var_title.get(), self.var_author.get(), self.var_borrow.get(), self.var_due.get()\
                                                  , self.var_loan.get()):
                            self.Listbox_2.insert(END, row, str(' '))

              def Details():
                     self.Display.delete('1.0',END)
                     self.Display.insert(END, 'Book ID: ' + self.var_ID.get() + '\n')
                     self.Display.insert(END, 'Title: ' + self.var_title.get() + '\n')
                     self.Display.insert(END, 'Author:  ' +  self.var_author.get() + '\n')
                     self.Display.insert(END, 'Edition: ' + self.var_edsn.get() + '\n')
                     self.Display.insert(END, 'Year of Publision: \t' + self.var_yop.get() + '\n')
                     self.Display.insert(END, 'Date Borrowed: ' + self.var_borrow.get() + '\n')
                     self.Display.insert(END, 'Date Due:' + self.var_due.get() + '\n')
                     self.Display.insert(END, 'Days in Loan: ' + self.var_loan.get() + '\n')
                             

       #=====================================================Frames=====================================================
              Main_Frame = Frame(self.root, bg = 'navajowhite')
              Main_Frame.grid()

              Title_Frame_1 = Frame(Main_Frame, width = 1350, bg = 'navajowhite', relief = RIDGE, bd = 15, padx = 20)
              Title_Frame_1.pack(side = TOP)

              self.lblTitle = Label(Title_Frame_1, font = ('arial',40,'bold'), text = '\tLibrary Management System\t', \
                                    bg = 'navajowhite', padx = 13)
              self.lblTitle.grid()

              Button_Frame = Frame(Main_Frame, width = 1350, height = 50, relief = RIDGE, bd = 10, bg = 'navajowhite')
              Button_Frame.pack(side = BOTTOM)

              Detail_Frame = Frame(Main_Frame, width = 1350, height = 100, relief = RIDGE, bd = 10, bg = 'navajowhite')
              Detail_Frame.pack(side = BOTTOM)

              Data_Frame = Frame(Main_Frame, width = 1350, height = 400, relief = RIDGE, bd = 15, bg = 'navajowhite')
              Data_Frame.pack(side = BOTTOM)

              Frame_1 = LabelFrame(Data_Frame, width = 800, height = 400, relief = RIDGE, bd = 10, bg = 'navajowhite', \
                              text = "Library Membership Info:", padx = 20, font = ('arial',15,'bold'))
              Frame_1.pack(side = LEFT, padx = 3)

              Frame_2 = LabelFrame(Data_Frame, width = 550, height = 400, relief = RIDGE, bd = 10, bg = 'navajowhite', \
                              text = "Book Details:", padx = 20, font = ('arial',15,'bold'))
              Frame_2.pack(side = RIGHT)


       #================================================Labels========================================================
              self.Label_1 = Label(Frame_1, text = 'Member_type', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_1.grid(row = 0, column = 0, sticky = W)
              self.Label_2 = Label(Frame_1, text = 'Reference_No.', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_2.grid(row = 1, column = 0, sticky = W)
              self.Label_3 = Label(Frame_1, text = 'First_Name', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_3.grid(row = 2, column = 0, sticky = W)
              self.Label_4 = Label(Frame_1, text = 'Surname', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_4.grid(row = 3, column = 0, sticky = W)
              self.Label_5 = Label(Frame_1, text = 'Address', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_5.grid(row = 4, column = 0, sticky = W)
              self.Label_6 = Label(Frame_1, text = 'Post_Code', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_6.grid(row = 5, column = 0, sticky = W)
              self.Label_7 = Label(Frame_1, text = 'Mobile_No', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_7.grid(row = 6, column = 0, sticky = W)
              self.Label_8 = Label(Frame_1, text = 'Book_ID', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_8.grid(row = 0, column = 2, sticky = W)
              self.Label_9 = Label(Frame_1, text = 'Book_Title', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_9.grid(row = 1, column = 2, sticky = W)
              self.Label_10 = Label(Frame_1, text = 'Author', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_10.grid(row = 2, column = 2, sticky = W)
              self.Label_11 = Label(Frame_1, text = 'Date_Borrowed', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_11.grid(row = 3, column = 2, sticky = W)
              self.Label_13 = Label(Frame_1, text = 'Date_Due', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_13.grid(row = 4, column = 2, sticky = W)
              self.Label_13 = Label(Frame_1, text = 'Days_in_Loan', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_13.grid(row = 5, column = 2, sticky = W)
              


       #================================================Entries========================================================
              self.Entry_0 = ttk.Combobox(Frame_1, values = (' ','Student','Faculty','Staff Member'),
                                          font = ('arial',13,'bold'), width = 23, textvariable =self.var_Mtype )
              self.Entry_0.grid(row = 0, column = 1)
              self.Entry_1 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.var_refno )
              self.Entry_1.grid(row = 1, column = 1, padx = 15)
              self.Entry_2 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.var_fname)
              self.Entry_2.grid(row = 2, column = 1, padx = 15)
              self.Entry_3 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.var_surname)
              self.Entry_3.grid(row = 3, column = 1, padx = 15)
              self.Entry_4 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.var_address)
              self.Entry_4.grid(row = 4, column = 1, padx = 15)
              self.Entry_5 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.var_post)
              self.Entry_5.grid(row = 5, column = 1, padx = 15)
              self.Entry_6 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.var_mobno)
              self.Entry_6.grid(row = 6, column = 1, padx = 15)
              self.Entry_7 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.var_ID)
              self.Entry_7.grid(row = 0, column = 4, padx = 15)
              self.Entry_8 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.var_title)
              self.Entry_8.grid(row = 1, column = 4, padx = 15)
              self.Entry_9 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.var_author)
              self.Entry_9.grid(row = 2, column = 4, padx = 15)
              self.Entry_10 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.var_borrow)
              self.Entry_10.grid(row = 3, column = 4, padx = 15)
              self.Entry_11 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.var_due)
              self.Entry_11.grid(row = 4, column = 4, padx = 15)
              self.Entry_12 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.var_loan)
              self.Entry_12.grid(row = 5, column = 4, padx = 15)                                        


       #=============================================Widgets=========================================================
              self.Display = Text(Frame_2, font = ('arial',13,'bold'), width = 28, height = 11)
              self.Display.grid(row = 0, column = 2)


              List_of_Books = [' C',' C++',' Java',' Python',' PHP',' Java Script',' My SQL',' Data Structure',' Linux',\
                               ' Operating System',' Web Developement',' Data Science',' Algorithms',' Android', \
                               ' VB.net']


       #===========================================Function for Books Details=========================================
              def SelectedBook(event):
                     value = str(self.Listbox_1.get(self.Listbox_1.curselection()))
                     v = value

                     if (v == ' C'):
                            self.var_ID.set('ISBN 525341')
                            self.var_title.set('Programming using C')
                            self.var_author.set('Yashwant Kanetkar')
                            self.var_yop.set('2019')
                            self.var_edsn.set('5th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 14)
                            d3 = (d1 + d2)
                            self.var_borrow.set(d1)
                            self.var_loan.set('14')
                            self.var_due.set(d3)
                            Details()
                     elif (v == ' C++'):
                            self.var_ID.set('ISBN 345687')
                            self.var_title.set('Programming using C++')
                            self.var_author.set('Yashwant Kanetkar')
                            self.var_yop.set('2019')
                            self.var_edsn.set('4th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 10)
                            d3 = (d1 + d2)
                            self.var_borrow.set(d1)
                            self.var_loan.set('10')
                            self.var_due.set(d3)
                            Details()
                     elif (v == ' Java'):
                            self.var_ID.set('ISBN 643842')
                            self.var_title.set('Java Programming')
                            self.var_author.set('Joshua Bloch')
                            self.var_yop.set('2019')
                            self.var_edsn.set('7th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 13)
                            d3 = (d1 + d2)
                            self.var_borrow.set(d1)
                            self.var_loan.set('13')
                            self.var_due.set(d3)
                            Details()
                     elif (v == ' Python'):
                            self.var_ID.set('ISBN 564524')
                            self.var_title.set('Python Programming')
                            self.var_author.set('John Zelle')
                            self.var_yop.set('2019')
                            self.var_edsn.set('3rd')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 13)
                            d3 = (d1 + d2)
                            self.var_borrow.set(d1)
                            self.var_loan.set('13')
                            self.var_due.set(d3)
                            Details()
                     elif (v == ' PHP'):
                            self.var_ID.set('ISBN 735893')
                            self.var_title.set('PHP Programming')
                            self.var_author.set('Alan Forbes')
                            self.var_yop.set('2019')
                            self.var_edsn.set('5th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 15)
                            d3 = (d1 + d2)
                            self.var_borrow.set(d1)
                            self.var_loan.set('15')
                            self.var_due.set(d3)
                            Details()
                     elif (v == ' Java Script'):
                            self.var_ID.set('ISBN 643842')
                            self.var_title.set('Java Script Programming')
                            self.var_author.set('Jon Duckett.')
                            self.var_yop.set('2019')
                            self.var_edsn.set('4th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 13)
                            d3 = (d1 + d2)
                            self.var_borrow.set(d1)
                            self.var_loan.set('13')
                            self.var_due.set(d3)
                            Details()
                     elif (v == ' My SQL'):
                            self.var_ID.set('ISBN 649635')
                            self.var_title.set('My SQL Programming')
                            self.var_author.set('Groff James')
                            self.var_yop.set('2019')
                            self.var_edsn.set('3rd')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 20)
                            d3 = (d1 + d2)
                            self.var_borrow.set(d1)
                            self.var_loan.set('20')
                            self.var_due.set(d3)
                            Details()
                     elif (v == ' Data Structure'):
                            self.var_ID.set('ISBN 531588')
                            self.var_title.set('Data Structure')
                            self.var_author.set('Karumanchi Narasimha')
                            self.var_yop.set('2019')
                            self.var_edsn.set('5th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 11)
                            d3 = (d1 + d2)
                            self.var_borrow.set(d1)
                            self.var_loan.set('11')
                            self.var_due.set(d3)
                            Details()
                     elif (v == ' Linux'):
                            self.var_ID.set('ISBN 356853')
                            self.var_title.set('Linux Administration')
                            self.var_author.set('SOYINKA')
                            self.var_yop.set('2019')
                            self.var_edsn.set('1st')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 6)
                            d3 = (d1 + d2)
                            self.var_borrow.set(d1)
                            self.var_loan.set('6')
                            self.var_due.set(d3)
                            Details()
                     elif (v == ' Operating System'):
                            self.var_ID.set('ISBN 536453')
                            self.var_title.set('OS Concepts ')
                            self.var_author.set('Silberschatz Abraham')
                            self.var_yop.set('2019')
                            self.var_edsn.set('4th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 12)
                            d3 = (d1 + d2)
                            self.var_borrow.set(d1)
                            self.var_loan.set('12')
                            self.var_due.set(d3)
                            Details()
                     elif (v == ' Web Developement'):
                            self.var_ID.set('ISBN 543548')
                            self.var_title.set('Web Developement ')
                            self.var_author.set('Paul McFedries')
                            self.var_yop.set('2019')
                            self.var_edsn.set('3rd')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 15)
                            d3 = (d1 + d2)
                            self.var_borrow.set(d1)
                            self.var_loan.set('15')
                            self.var_due.set(d3)
                            Details()
                     elif (v == ' Data Science'):
                            self.var_ID.set('ISBN 835764')
                            self.var_title.set('Data Science Concept ')
                            self.var_author.set('David Stephenson')
                            self.var_yop.set('2019')
                            self.var_edsn.set('3rd')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 15)
                            d3 = (d1 + d2)
                            self.var_borrow.set(d1)
                            self.var_loan.set('15')
                            self.var_due.set(d3)
                            Details()
                     elif (v == ' Algorithms'):
                            self.var_ID.set('ISBN 535674')
                            self.var_title.set('Basics of Algorithm ')
                            self.var_author.set('Karumanchi Narasimha')
                            self.var_yop.set('2019')
                            self.var_edsn.set('7th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 10)
                            d3 = (d1 + d2)
                            self.borrow.set(d1)
                            self.loan.set('10')
                            self.due.set(d3)
                            Details()
                     elif (v == ' Android'):
                            self.var_ID.set('ISBN 356452')
                            self.var_title.set('Android Programming')
                            self.var_author.set('Harwani B. M')
                            self.var_yop.set('2019')
                            self.var_edsn.set('4th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 9)
                            d3 = (d1 + d2)
                            self.var_borrow.set(d1)
                            self.var_loan.set('9')
                            self.var_due.set(d3)
                            Details()
                            
       #===========================================List Box and Scroll Bar==========================================                    
              sb_1 = Scrollbar(Frame_2)
              sb_1.grid(row =0, column = 1, sticky = 'ns')

              self.Listbox_1 = Listbox(Frame_2, font = ('arial',13,'bold'), width = 20, height = 10)
              self.Listbox_1.bind('<<ListboxSelect>>', SelectedBook)
              self.Listbox_1.grid(row = 0, column = 0)
              sb_1.config(command = self.Listbox_1.yview)

              
              sb_2 = Scrollbar(Detail_Frame)
              sb_2.grid(row = 1, column = 1, sticky = 'ns')

              self.Listbox_2 = Listbox(Detail_Frame, font = ('arial',13,'bold'), width = 144, height = 11)
              self.Listbox_2.bind('<<ListboxSelect>>')
              self.Listbox_2.grid(row = 1, column = 0)
              sb_2.config(command = self.Listbox_2.yview)

              for items in List_of_Books:
                     self.Listbox_1.insert(END, items)

              ###### fram data display
              table_frame=Frame(Main_Frame,bd=4,relief=RIDGE)
              table_frame.place(x=35,y=390,width=1310,height=210)

              Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
              Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
              self.student_table=ttk.Treeview(table_frame,column=("Mtype","refno","fname","surname","address","post","mobno","ID","title","author","borrow","due","loan"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)

              Scroll_x.pack(side=BOTTOM,fill=X)
              Scroll_y.pack(side=RIGHT,fill=Y)

              Scroll_x.config(command=self.student_table.xview)
              Scroll_y.config(command=self.student_table.yview)

              self.student_table.heading("Mtype",text="Member_type")
              self.student_table.heading("refno",text="Reference_No")
              self.student_table.heading("fname",text="First_Name")
              self.student_table.heading("surname",text="Surname")
              self.student_table.heading("address",text="Address")
              self.student_table.heading("post",text="Post_Code")
              self.student_table.heading("mobno",text="Mobile_No")
              self.student_table.heading("ID",text="Book_ID")
              self.student_table.heading("title",text="Book_Title")
              self.student_table.heading("author",text="Author")
              self.student_table.heading("borrow",text="Date_Borrowed")
              self.student_table.heading("due",text="Date_Due")
              self.student_table.heading("loan",text="Days_in_Loan")
              

              self.student_table["show"]="headings"
              self.student_table.column("Mtype",width=100)
              self.student_table.column("refno",width=100)
              self.student_table.column("fname",width=100)
              self.student_table.column("surname",width=100)
              self.student_table.column("address",width=100)
              self.student_table.column("post",width=100)
              self.student_table.column("mobno",width=100)
              self.student_table.column("ID",width=100)
              self.student_table.column("title",width=100)
              self.student_table.column("author",width=100)
              self.student_table.column("borrow",width=100)
              self.student_table.column("due",width=100)
              self.student_table.column("loan",width=100)
            


              self.student_table.pack(fill=BOTH,expand=1)
              self.student_table.bind("<ButtonRelease>",self.get_cuersor)
              self.fetch_data()


       #=============================================Buttons=========================================================
              Button_1 = Button(Button_Frame, text = 'SAVE',command=self.add_data,font = ('arial',15,'bold'), width = 10)
              Button_1.grid(row = 0, column = 0, padx = 8, pady = 5)
              Button_2 = Button(Button_Frame, text = 'DISPLAY', font = ('arial',15,'bold'), width = 10, command = Display)
              Button_2.grid(row = 0, column = 1, padx = 8)
              Button_3 = Button(Button_Frame, text = 'RESET', font = ('arial',15,'bold'), width = 10, command = Reset)
              Button_3.grid(row = 0, column = 2, padx = 8)
              # Button_4 = Button(Button_Frame, text = 'UPDATE', font = ('arial',15,'bold'), width = 10,command=self.update_data)
              # Button_4.grid(row = 0, column = 3, padx = 8)
              Button_5 = Button(Button_Frame, text = 'SEARCH', font = ('arial',15,'bold'), width = 10, command = Search)
              Button_5.grid(row = 0, column = 4, padx = 8)
              Button_6 = Button(Button_Frame, text = 'DELETE', font = ('arial',15,'bold'), width = 10,command=self.delete_data)
              Button_6.grid(row = 0, column = 5, padx = 8)
              Button_7 = Button(Button_Frame, text = 'EXIT', font = ('arial',15,'bold'), width = 10, command = Exit)
              Button_7.grid(row = 0, column = 6, padx = 8)

       def add_data(self):
        if (self.var_Mtype.get()=="" or self.var_refno.get()=="" or self.var_fname.get()==""):
           messagebox.showerror("Error","All Fields are Required")
        else:
            conn=mysql.connector.connect(host="localhost", user="root", password="Admin@123", database="collage")
            my_cursur=conn.cursor()
            my_cursur.execute("insert into Library1 values(%s,'%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                 
                                                                  self.var_Mtype.get(),
                                                                  self.var_refno.get(),
                                                                  self.var_fname.get(),
                                                                  self.var_surname.get(),
                                                                  self.var_address.get(),
                                                                  self.var_post.get(),
                                                                  self.var_mobno.get(),
                                                                  self.var_ID.get(),
                                                                  self.var_title.get(),
                                                                  self.var_author.get(),
                                                                  self.var_borrow.get(),
                                                                  self.var_due.get(),
                                                                  self.var_loan.get()
                                                                
                                                            ))
            conn.commit()
            #self.fetch_data()
            conn.close()
            messagebox.showinfo("Seccess","Student has been added",parent=self.root)

       def fetch_data(self):
         conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123", database="collage")
         my_cursur = conn.cursor()
         my_cursur.execute("select * from Library1")
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

        self.var_Mtype.set(rows[0])
        self.var_refno.set(rows[1])
        self.var_fname.set(rows[2])
        self.var_surname.set(rows[3])
        self.var_address.set(rows[4])
        self.var_post.set(rows[5])
        self.var_mobno.set(rows[6])
        self.var_ID.set(rows[7])
        self.var_title.set(rows[8])
        self.var_author.set(rows[9])
        self.var_borrow.set(rows[10])
        self.var_due.set(rows[11])
        self.var_loan.set(rows[12])

       
       # def update_data(self):
       #     if self.var_Mtype.get()=="" or self.var_fname.get()=="":
       #        messagebox.showerror("Error","All Fields Are required",parent=self.root)
       #     else:          
       #        conn=mysql.connector.connect(host="localhost",username="root",password="Admin@123",database="collage")
       #        my_cursor=conn.cursor() 
       #        my_cursor.execute("Update Library1 set Member_type=%s,First_Name=%s,Surname=%s,Address=%s,Post_Code=%s,Mobile_No=%s,Book_ID=%s,Book_Title=%s,Auther=%s,Data_Borrowed=%s,Data_Due=%s,Daya_in_Loan=%s where Reference_No=%s",(
                
       #                                                           self.var_Mtype.get(),
       #                                                           self.var_fname.get(),
       #                                                           self.var_surname.get(),
       #                                                           self.var_address.get(),
                                                                 
       #                                                           self.var_post.get(),
       #                                                           self.var_mobno.get(),
       #                                                           self.var_ID.get(),
       #                                                           self.var_title.get(),
       #                                                           self.var_author.get(),
       #                                                           self.var_borrow.get(),
       #                                                           self.var_due.get(),
       #                                                           self.var_loan.get(),
       #                                                           self.var_refno.get()
                                                                 

       #                                                      ))
                 
       #        conn.commit()
       #        self.fetch_data()
       #        conn.close()
       #        messagebox.showinfo("update","student details has been updated successfully",parent=self.root)
       

       def delete_data(self):
        if self.var_fname.get()=="":
            messagebox.showerror("Error","All Fields Are required")
        else:
          # try:
              #   Delete=messagebox.askyesno("Delete","Are sure delete this student")
              #   if Delete>0:
             conn=mysql.connector.connect(host="localhost",username="root",password="Admin@123",database="collage")
             my_cursor=conn.cursor() 
             sql="delete from Library1 where First_Name=%s"
             value=(self.var_fname.get(),)
             my_cursor.execute(sql,value)
              #   else:
              #       if not Delete:
              #           return
             conn.commit()
             self.fetch_data
             conn.close()
             messagebox.showinfo("Delete","your Student has been Deleted")




if __name__ == '__main__':
       root = Tk()
       applicaton = Library(root)
       root.mainloop()
