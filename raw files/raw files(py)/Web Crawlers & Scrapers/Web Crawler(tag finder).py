from bs4 import BeautifulSoup
import requests
from tkinter import messagebox
from tkinter import *

#Creating the window
wn = Tk()
wn.title('tag finder')
wn.geometry('700x700')
wn.config(bg='Red')


#Function to generate the QR code and save it
#Adding the data to be encoded to the QRCode object




def fa():    
    url = (text.get()) 
    tag = (loc.get())
    o = requests.get(url)
    soup = BeautifulSoup(o.content)
    print(soup.find_all(tag))
    messagebox.showinfo("softcp", "the result is shown in the shell")
    
#Label for the window
headingFrame = Frame(wn,bg="red",bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame, text="tag finder", bg='red', font=('Times',20,'bold'))
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

lable2 = Label(Frame2,text="write your tag(example: p): ",bg="red",fg='azure',font=('Courier',13,'bold'))
lable2.place(relx=0.05,rely=0.2, relheight=0.08)

loc = Entry(Frame2,font=('Century 12'))
loc.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#Button to generate and save the QR Code
button = Button(wn, text='find tag',font=('Courier',15,'normal'),command=fa)
button.place(relx=0.35,rely=0.9, relwidth=0.25, relheight=0.05)

#Runs the window till it is closed manually
wn.mainloop()