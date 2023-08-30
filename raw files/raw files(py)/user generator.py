from tkinter import *
from tkinter import messagebox
import os

wn = Tk()
wn.title('user generator')
wn.geometry('700x700')
wn.config(bg='Red')

    
def cu():
    messagebox.showinfo("softcp", "please run this program as administrator(if you don't, this program will not work and if you run it as adminstrator just ignor this error and enjoy!)")
    un = (text.get())
    up = loc.get()
    os.system("net user {} /add".format(un))
    os.system("net user {} {}".format(un, up))
    messagebox.showinfo("softcp", "user generated sucssesfuly(if the program is runned as administrator)")  

headingFrame = Frame(wn,bg="red",bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame, text="user generator", bg='red', font=('Times',20,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


Frame1 = Frame(wn,bg="red")
Frame1.place(relx=0.1,rely=0.15,relwidth=0.7,relheight=0.3)
    
lable1 = Label(Frame1,text="enter the user: ",bg="red",fg='azure',font=('Courier',13,'bold'))
lable1.place(relx=0.05,rely=0.2, relheight=0.08)

text = Entry(Frame1,font=('Century 12'))
text.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

Frame2 = Frame(wn,bg="red")
Frame2.place(relx=0.1,rely=0.35,relwidth=0.7,relheight=0.3)

lable2 = Label(Frame2,text="enter the new user password: ",bg="red",fg='azure',font=('Courier',13,'bold'))
lable2.place(relx=0.05,rely=0.2, relheight=0.08)

loc = Entry(Frame2,font=('Century 12'))
loc.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)


button = Button(wn, text='create account',font=('Courier',15,'normal'),command=cu)
button.place(relx=0.35,rely=0.9,relwidth=0.25,relheight=0.05)

wn.mainloop()
