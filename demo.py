from tkinter import *
root=Tk()
root.title("login")
root.geometry("1540x820")

l1=Label(root,text="first Name").place(x=10,y=10)
e1=Entry(root,width=30,font=("Microsoft YaHei UI Light",11)).place(x=100,y=10)

l2=Label(root,text="Last Name").place(x=10,y=50)
e2=Entry(root,width=30,font=("Microsoft YaHei UI Light",11)).place(x=100,y=50)
root.mainloop()