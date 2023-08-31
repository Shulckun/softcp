from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re

wn = Tk()
wn.title('QRcode Reader')
wn.geometry('700x700')
wn.config(bg='Red')

    
def rc():
    my_url = (text.get())
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    print(page_soup)
    messagebox.showinfo("softcp", "the result is shown in the shell")  

headingFrame = Frame(wn,bg="red",bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame, text="read websites codes with softcp", bg='red', font=('Times',20,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


Frame1 = Frame(wn,bg="red")
Frame1.place(relx=0.1,rely=0.15,relwidth=0.7,relheight=0.3)
    
lable1 = Label(Frame1,text="enter the URL: ",bg="red",fg='azure',font=('Courier',13,'bold'))
lable1.place(relx=0.05,rely=0.2, relheight=0.08)

text = Entry(Frame1,font=('Century 12'))
text.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)


button = Button(wn, text='read code',font=('Courier',15,'normal'),command=rc)
button.place(relx=0.1,rely=0.35,relwidth=0.25,relheight=0.05)

wn.mainloop()
