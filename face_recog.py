from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recog:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Detect Face")

        title_lbl = Label(self.root, text="FACE DETECTOR", 
                          font=("times new roman", 45, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=15, width=1530, height=70)

        img_top = Image.open(r"college_images/guyface.jpg")
        img_top = img_top.resize((800, 700), Image.ADAPTIVE)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        bg_img = Label(self.root, image=self.photoimg_top)
        bg_img.place(x=20, y=84, width=800, height=710)

        img_bottom = Image.open(r"college_images/phone-face-recognize-unlock.jpg")
        img_bottom = img_bottom.resize((600, 700), Image.ADAPTIVE)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        bg_img = Label(self.root, image=self.photoimg_bottom)
        bg_img.place(x=800, y=85, width=600, height=700)

        b1_1 = Button(bg_img ,text="DETECT FACE", cursor="hand2", command=self.face_recog, font=("times new roman", 18, "bold"), bg="blue", fg="white") 
        b1_1.place(x=185, y=470, width=230, height=50)
    #========================attendance===================================
    def mark_attendance(self,n,c):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((",")) 
                name_list.append(entry[0])
            if ((n not in name_list)and (c not in name_list)):
                 now=datetime.now()
                 d1=now.strftime("%d/%m/%Y")
                 dtString=now.strftime("%H:%M:%S")
                 f.writelines(f"\n{n},{c},{dtString},{d1}, Present")

    #=========================Face Recognition=====================================
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))
                print(f"ID: {id}, Confidence: {confidence}")

                conn = mysql.connector.connect(host="localhost",username="root",password="ashwindave1010",port="3306",database="stdnts")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT name FROM student WHERE student_id=%s", (str(id),))
                result = my_cursor.fetchone()
                n = result[0] if result else "Unknown"

                my_cursor.execute("SELECT course FROM student WHERE student_id=%s", (str(id),))
                result = my_cursor.fetchone()
                c = result[0] if result else "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"Name: {n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Course: {c}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(n,c)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        
        # Path to classifier file
        classifier_file_path = "classifier.xml"
        
        if not os.path.exists(classifier_file_path):
            print(f"Error: {classifier_file_path} does not exist.")
            return

        try:
            clf.read(classifier_file_path)
        except cv2.error as e:
            print(f"Error reading classifier file: {e}")
            return

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Failed to capture image")
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            key = cv2.waitKey(1)
            if key == 13:  # Enter key
                break
            elif key == 27:  # Esc key
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recog(root)
    root.mainloop()
