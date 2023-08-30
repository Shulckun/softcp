import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from tkinter import messagebox
from tkinter import *

#Creating the window
wn = Tk()
wn.title('softcp')
wn.geometry('700x700')
wn.config(bg='Red')


#Function to generate the QR code and save it
#Adding the data to be encoded to the QRCode object




def fa():    
    url = (text.get()) 
    req = Request(url)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "html.parser")
    links = []
    tag = (loc.get())
    h = (name.get())
    for link in soup.findAll(tag):
        links.append(link.get(h))


    print(links)
    input()
    fa()
    
#Label for the window
headingFrame = Frame(wn,bg="red",bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame, text="b finder from a softcp", bg='red', font=('Times',20,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

#Taking the input of the text or URL to get QR code 
Frame1 = Frame(wn,bg="red")
Frame1.place(relx=0.1,rely=0.15,relwidth=0.7,relheight=0.3)
    
lable1 = Label(Frame1,text="Enter the URL: ",bg="red",fg='azure',font=('Courier',13,'bold'))
lable1.place(relx=0.05,rely=0.2, relheight=0.08)

text = Entry(Frame1,font=('Century 12'))
text.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#Getting input of the location to save QR Code
Frame2 = Frame(wn,bg="red")
Frame2.place(relx=0.1,rely=0.35,relwidth=0.7,relheight=0.3)

lable2 = Label(Frame2,text="write your tag: ",bg="red",fg='azure',font=('Courier',13,'bold'))
lable2.place(relx=0.05,rely=0.2, relheight=0.08)

loc = Entry(Frame2,font=('Century 12'))
loc.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#Getting input of the QR Code image name 
Frame3 = Frame(wn,bg="red")
Frame3.place(relx=0.1,rely=0.55,relwidth=0.7,relheight=0.3)

lable3 = Label(Frame3,text="i want to find 1 from my tag(for example i want to find href from a): ",bg="red",fg='azure',font=('Courier',13,'bold'))
lable3.place(relx=0.05,rely=0.2, relheight=0.08)

name = Entry(Frame3,font=('Century 12'))
name.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#Button to generate and save the QR Code
button = Button(wn, text='find b from a',font=('Courier',15,'normal'),command=fa)
button.place(relx=0.35,rely=0.9, relwidth=0.25, relheight=0.05)

#Runs the window till it is closed manually
wn.mainloop()
