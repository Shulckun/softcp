from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re
from tkinter import *
from tkinter import messagebox

#Creating the window
wn = Tk()
wn.title('softcp result finder')
wn.geometry('700x700')
wn.config(bg='Red')


#Function to generate the QR code and save it
def fa():
    #Creating a QRCode object of the size specified by the user
    url = (text.get()) #Adding the data to be encoded to the QRCode object
    my_url = "{}".format(url)
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    tag = loc.get()
    ci = name.get()
    class1 = size.get()
    containers = page_soup.findAll("{}".format(tag),{"{}".format(ci): "{}".format(class1)})
    messagebox.showinfo("Softcp","result is shown in the shell")
    print(containers[int(0)].text.split("\n"))
    print(containers[int(1)].text.split("\n"))
    print(containers[int(2)].text.split("\n"))
    print(containers[int(3)].text.split("\n"))
    print(containers[int(4)].text.split("\n"))
    print(containers[int(5)].text.split("\n"))
    print(containers[int(6)].text.split("\n"))
    print(containers[int(7)].text.split("\n"))
    print(containers[int(8)].text.split("\n"))
    print(containers[int(9)].text.split("\n"))
    print(containers[int(10)].text.split("\n"))
    print(containers[int(11)].text.split("\n"))
    print(containers[int(12)].text.split("\n"))
    print(containers[int(13)].text.split("\n"))
    print(containers[int(15)].text.split("\n"))
    print(containers[int(16)].text.split("\n"))
    print(containers[int(17)].text.split("\n"))
    print(containers[int(18)].text.split("\n"))
    print(containers[int(19)].text.split("\n"))
    print(containers[int(20)].text.split("\n"))
    print(containers[int(21)].text.split("\n"))
    print(containers[int(22)].text.split("\n"))
    print(containers[int(23)].text.split("\n"))
    print(containers[int(24)].text.split("\n"))
    print(containers[int(25)].text.split("\n"))
    print(containers[int(26)].text.split("\n"))
    print(containers[int(27)].text.split("\n"))
    print(containers[int(28)].text.split("\n"))
    print(containers[int(29)].text.split("\n"))
    print(containers[int(30)].text.split("\n"))
    print(containers[int(31)].text.split("\n"))
    print(containers[int(32)].text.split("\n"))
    print(containers[int(33)].text.split("\n"))
    print(containers[int(34)].text.split("\n"))
    print(containers[int(35)].text.split("\n"))
    print(containers[int(36)].text.split("\n"))
    print(containers[int(37)].text.split("\n"))
    print(containers[int(38)].text.split("\n"))
    print(containers[int(39)].text.split("\n"))
    print(containers[int(40)].text.split("\n"))
    print(containers[int(41)].text.split("\n"))
    print(containers[int(42)].text.split("\n"))
    print(containers[int(43)].text.split("\n"))
    print(containers[int(44)].text.split("\n"))
    print(containers[int(45)].text.split("\n"))
    print(containers[int(46)].text.split("\n"))
    print(containers[int(47)].text.split("\n"))
    print(containers[int(48)].text.split("\n"))
    print(containers[int(49)].text.split("\n"))
    print(containers[int(50)].text.split("\n"))
    print(containers[int(51)].text.split("\n"))
    print(containers[int(52)].text.split("\n"))
    print(containers[int(53)].text.split("\n"))
    print(containers[int(54)].text.split("\n"))
    print(containers[int(55)].text.split("\n"))
    print(containers[int(56)].text.split("\n"))
    print(containers[int(57)].text.split("\n"))
    print(containers[int(58)].text.split("\n"))
    print(containers[int(59)].text.split("\n"))
    print(containers[int(60)].text.split("\n"))
    

headingFrame = Frame(wn,bg="red",bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame, text="find result in website with softcp", bg='red', font=('Times',20,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


Frame1 = Frame(wn,bg="red")
Frame1.place(relx=0.1,rely=0.15,relwidth=0.7,relheight=0.3)
    
lable1 = Label(Frame1,text="Enter the URL: ",bg="red",fg='azure',font=('Courier',13,'bold'))
lable1.place(relx=0.05,rely=0.2, relheight=0.08)

text = Entry(Frame1,font=('Century 12'))
text.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#Getting input of the location to save QR Code
Frame2 = Frame(wn,bg="red")
Frame2.place(relx=0.1,rely=0.35,relwidth=0.7,relheight=0.3)

lable2 = Label(Frame2,text="enter the tag: ",bg="red",fg='azure',font=('Courier',13,'bold'))
lable2.place(relx=0.05,rely=0.2, relheight=0.08)

loc = Entry(Frame2,font=('Century 12'))
loc.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#Getting input of the QR Code image name 
Frame3 = Frame(wn,bg="red")
Frame3.place(relx=0.1,rely=0.55,relwidth=0.7,relheight=0.3)

lable3 = Label(Frame3,text="i want to find my tag with: ",bg="red",fg='azure',font=('Courier',13,'bold'))
lable3.place(relx=0.05,rely=0.2, relheight=0.08)

name = Entry(Frame3,font=('Century 12'))
name.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#Getting the input of the size of the QR Code
Frame4 = Frame(wn,bg="red")
Frame4.place(relx=0.1,rely=0.75,relwidth=0.7,relheight=0.2)

lable4 = Label(Frame4,text="write the of the tag: ",bg="red",fg='azure',font=('Courier',13,'bold'))
lable4.place(relx=0.05,rely=0.2, relheight=0.08)

size = Entry(Frame4,font=('Century 12'))
size.place(relx=0.05,rely=0.4, relwidth=0.5, relheight=0.2)

#Button to generate and save the QR Code
button = Button(wn, text='find result',font=('Courier',15,'normal'),command=fa)
button.place(relx=0.35,rely=0.9, relwidth=0.25, relheight=0.05)

#Runs the window till it is closed manually
wn.mainloop()
