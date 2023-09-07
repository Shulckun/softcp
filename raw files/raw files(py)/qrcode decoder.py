import cv2
from tkinter import *
from tkinter import messagebox

#Creating the window
wn = Tk()
wn.title('QRcode Reader')
wn.geometry('700x700')
wn.config(bg='Red')

    
def rq():
    #Function to generate the QR code and save it
    filename = (text.get())
    image = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
    print(data)
    messagebox.showinfo("qrcode decoded",data)
#Label for the window
headingFrame = Frame(wn,bg="red",bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame, text="decode QRcode with softcp", bg='red', font=('Times',20,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

#Taking the input of the text or URL to get QR code 
Frame1 = Frame(wn,bg="red")
Frame1.place(relx=0.1,rely=0.15,relwidth=0.7,relheight=0.3)
    
lable1 = Label(Frame1,text="write the name of the qrcode with the path(example: C:/users/user/desktop/qrcode.png): ",bg="red",fg='azure',font=('Courier',13,'bold'))
lable1.place(relx=0.05,rely=0.2, relheight=0.08)

text = Entry(Frame1,font=('Century 12'))
text.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#Button to generate and save the QR Code
button = Button(wn, text='decode qrcode',font=('Courier',15,'normal'),command=rq)
button.place(relx=0.1,rely=0.35,relwidth=0.25,relheight=0.05)

#Runs the window till it is closed manually
wn.mainloop()
