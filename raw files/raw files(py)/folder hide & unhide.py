from tkinter import *
from tkinter import messagebox
import os

wn = Tk()
wn.title('folder hider/unhider')
wn.geometry('700x700')
wn.config(bg='Red')

    
def rc():
    fn = (text.get())
    hu = loc.get()
    if hu == "hide":
        os.system("attrib +s +h +r {}".format(fn))
        messagebox.showinfo("softcp", "directory hided sucessfuly")
    if hu == "unhide":
        os.system("attrib -s -h -r {}".format(fn))
        messagebox.showinfo("softcp", "directory unhided sucessfuly")
        rc(end)

headingFrame = Frame(wn,bg="red",bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame, text="folder hider/unhider", bg='red', font=('Times',20,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


Frame1 = Frame(wn,bg="red")
Frame1.place(relx=0.1,rely=0.15,relwidth=0.7,relheight=0.3)
    
lable1 = Label(Frame1,text="enter the file/mp3/... with the path(for example: C:/users/user/desktop/example.txt): ",bg="red",fg='azure',font=('Courier',13,'bold'))
lable1.place(relx=0.05,rely=0.2, relheight=0.08)

text = Entry(Frame1,font=('Century 12'))
text.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

Frame2 = Frame(wn,bg="red")
Frame2.place(relx=0.1,rely=0.35,relwidth=0.7,relheight=0.3)

lable2 = Label(Frame2,text="i want to hide/unhide the folder: ",bg="red",fg='azure',font=('Courier',13,'bold'))
lable2.place(relx=0.05,rely=0.2, relheight=0.08)

loc = Entry(Frame2,font=('Century 12'))
loc.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

button = Button(wn, text='hide/unhide',font=('Courier',15,'normal'),command=rc)
button.place(relx=0.35,rely=0.9,relwidth=0.25,relheight=0.05)

wn.mainloop()
