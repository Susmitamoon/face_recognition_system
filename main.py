from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first image
        img=Image.open(r"C:\Users\Susmita Saha\Desktop\Face_recognition Sytem\image\first1.jpeg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        #second image
        img2=Image.open(r"C:\Users\Susmita Saha\Desktop\Face_recognition Sytem\image\third.jpeg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=550,height=130)


        #third image
        img1=Image.open(r"C:\Users\Susmita Saha\Desktop\Face_recognition Sytem\image\sec.jpeg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=1010,y=0,width=560,height=130)



        #bg image
        img3=Image.open(r"C:\Users\Susmita Saha\Desktop\Face_recognition Sytem\image\dash1.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="  FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35, "bold"), bg="black", fg="#FFA500")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #----------TIME--------------
        def time():
            string= strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl =Label(title_lbl, font = ('times new roman',14,'bold'),background='black',foreground='orange')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        #student button
        img4=Image.open(r"C:\Users\Susmita Saha\Desktop\Face_recognition Sytem\image\stu.jpg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2", bd=0)
        b1.place(x=200,y=100, width=220, height=220)

        b1_1=Button(bg_img,text="STUDENT DETAILS",command=self.student_details, cursor="hand2",font=("tahoma",15, "bold"), bg="black", fg="brown")
        b1_1.place(x=200,y=300,width=220,height=40)

        #detect face
        img5=Image.open(r"C:\Users\Susmita Saha\Desktop\Face_recognition Sytem\image\d.webp")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data, bd=0)
        b1.place(x=500,y=100, width=220, height=220)

        b1_1=Button(bg_img,text="FACE DETECTOR",cursor="hand2",command=self.face_data,font=("tahoma",15, "bold"), bg="black", fg="brown")
        b1_1.place(x=500,y=300,width=220,height=40)

    

        #attendance face button
        img6=Image.open(r"C:\Users\Susmita Saha\Desktop\Face_recognition Sytem\image\att.jpg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data, bd=0)
        b1.place(x=800,y=100, width=220, height=220)

        b1_1=Button(bg_img,text="ATTENDANCE",cursor="hand2",command=self.attendance_data,font=("tahoma",15, "bold"), bg="black", fg="brown")
        b1_1.place(x=800,y=300,width=220,height=40)

        #help desk
        img10=Image.open(r"C:\Users\Susmita Saha\Desktop\Face_recognition Sytem\image\help.jpg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.help_data, bd=0)
        b1.place(x=1100,y=100, width=220, height=220)

        b1_1=Button(bg_img,text="HELP DESK",cursor="hand2",command=self.help_data,font=("tahoma",15, "bold"), bg="black", fg="brown")
        b1_1.place(x=1100,y=300,width=220,height=40)


        #train face button
        img7=Image.open(r"C:\Users\Susmita Saha\Desktop\Face_recognition Sytem\image\training2.png")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2", command=self.train_data,bd=0)
        b1.place(x=200,y=400, width=220, height=220)

        b1_1=Button(bg_img,text="TRAIN FACE",cursor="hand2",font=("tahoma",15, "bold"), bg="black", fg="brown")
        b1_1.place(x=200,y=600,width=220,height=40)



        #photo face button
        img8=Image.open(r"C:\Users\Susmita Saha\Desktop\Face_recognition Sytem\image\photo.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.open_img,bd=0)
        b1.place(x=500,y=400, width=220, height=220)

        b1_1=Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_img,font=("tahoma",15, "bold"), bg="black", fg="brown")
        b1_1.place(x=500,y=600,width=220,height=40)

        #DEVELOPER
        img11=Image.open(r"C:\Users\Susmita Saha\Desktop\Face_recognition Sytem\image\girl2.webp")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.developer_data ,bd=0)
        b1.place(x=800,y=400, width=220, height=220)

        b1_1=Button(bg_img,text="DEVELOPER",cursor="hand2",command=self.developer_data,font=("tahoma",15, "bold"), bg="black", fg="brown")
        b1_1.place(x=800,y=600,width=220,height=40)



        #exit button
        img9=Image.open(r"C:\Users\Susmita Saha\Desktop\Face_recognition Sytem\image\exit.png")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=400, width=220, height=220)

        b1_1=Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,font=("tahoma",15, "bold"), bg="black", fg="brown")
        b1_1.place(x=1100,y=600,width=220,height=40)


    def open_img(self):
        os.startfile("data")


    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit this project?",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return


        #==============FUNCTION BUTTONS=====================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window) 

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
