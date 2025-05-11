from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="light blue", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # 1st image
        img_top = Image.open(r"C:\Users\Susmita Saha\Desktop\Face_recognition Sytem\image\face3.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # 2nd image
        img_bottom = Image.open(r"C:\Users\Susmita Saha\Desktop\Face_recognition Sytem\image\scan3.webp")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl2 = Label(self.root, image=self.photoimg_bottom)
        f_lbl2.place(x=650, y=55, width=950, height=700)

        # Face Recognition Button
        b1_1 = Button(f_lbl2, text="Face Recognition", command=self.face_recog, cursor="hand2", font=("tahoma", 18, "bold"), bg="light grey", fg="navy blue")
        b1_1.place(x=367, y=620, width=220, height=40)
    #---------------attendance-----------
    def mark_attendance(self,i,r,n,d):
        with open("susmita.csv","r+",newline="\n") as f:
            myDataList= f.readlines()
            name_list=[]
            for line in myDataList:          
                entry=line.strip().split(",")
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
    # ---------------- FACE RECOGNITION ------------------
    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
        coord = []

        for (x, y, w, h) in features:
            id, predict = clf.predict(gray_image[y:y + h, x:x + w])
            confidence = int((100 * (1 - predict / 300)))

            conn = mysql.connector.connect(host="localhost", user="root", password="WJ28@krhps", database="face_recognizer")
            my_cursor = conn.cursor()

            try:
                my_cursor.execute("SELECT Name FROM student WHERE Student_id=%s", (id,))
                n = "+".join(my_cursor.fetchone() or ["Unknown"])

                my_cursor.execute("SELECT Roll FROM student WHERE Student_id=%s", (id,))
                r = "+".join(my_cursor.fetchone() or ["Unknown"])

                my_cursor.execute("SELECT Dep FROM student WHERE Student_id=%s", (id,))
                d = "+".join(my_cursor.fetchone() or ["Unknown"])

                my_cursor.execute("SELECT Student_id FROM student WHERE Student_id=%s", (id,))
                i = "+".join(my_cursor.fetchone() or ["Unknown"])
 
            except Exception as e:
                print("MySQL Error:", e)
                return
            finally:
                conn.close()

           
 
            if confidence > 77:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                self.mark_attendance(i,r,n,d)
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

            coord = [x, y, w, h]
        return coord

    def recognize(self, img, clf, faceCascade):
        coord = self.draw_boundary(img, faceCascade, 1.1, 10, clf)
        return img

    def face_recog(self):
        print("Face Recognition function triggered")
        messagebox.showinfo("Info", "Face recognition starting...")  # TEMP debug
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        if not video_cap.isOpened():
            print("Webcam could not be accessed.")
            messagebox.showerror("Error", "Cannot access webcam.")
            return

        while True:
            ret, img = video_cap.read()
            if not ret:
                messagebox.showerror("Error", "Failed to grab frame.")
                break

            img = self.recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Enter key
                break

        video_cap.release()
        cv2.destroyAllWindows()

# ------------------- MAIN -----------------------
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
