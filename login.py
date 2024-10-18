from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
from home_page_collage import collageSystem

root=Tk()
root.title("login")
root.geometry("1540x820")
root.configure(bg="#fff")
root.resizable(False,False)

def singin():
    username=user.get()
    password=code.get()

    if username=="Admin" and password=="1234":
        new_window=Toplevel(root)
        app=collageSystem(new_window)             
         
         
img = PhotoImage(file="login.png")
Label(root,image=img,bg="white").place(x=250,y=200)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=750,y=200)

heading=Label(frame,text="Sign In",fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
heading.place(x=100,y=5)


#############------------------------------------------
def on_enter(e):
    user.delete(0,"end")

def on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,"User Name")


user= Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
user.place(x=30,y=80)
user.insert(0,"UserName")
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)


#######-------------------------------
def on_enter(e):
        code.delete(0,"end")

def on_leave(e):
        name=code.get()
        if name=="":
          code.insert(0,"Password")

code= Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11), show="*")
code.place(x=30,y=150)
code.insert(0,"PassWord")
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)



Button(frame,width=39,pady=7,text="Sign in",bg="#57a1f8",command=singin,fg="white",border=0).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg="black",bg="white",font=("Microsoft YaHei UI Light",9))
label.place(x=75,y=270)

sing_up=Button(frame,width=6,text="Sign up",border=0,bg="white",cursor="hand2",fg="#57a1f8")
sing_up.place(x=215,y=270)


root.mainloop()