from tkinter import *
from tkinter import ttk
import tkinter
import os
import tkinter.messagebox
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recog import Face_Recog
from attendance import Attendance



class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # 1st img
        img = Image.open(r"C:\Users\USER\Downloads\FRAS\college_images\bg.jpg")
        img = img.resize((1530, 790), Image.ADAPTIVE)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", 
                          font=("times new roman", 43, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=70)

        #================Time==================================

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman', 14, 'bold'), background='white', foreground='blue')
        lbl.place(x=1,y=26,width=110,height=50)
        time()

        # STUDENTS BUTTON
        img4 =Image.open(r"C:\Users\USER\Downloads\FRAS\college_images\buttonstnd.jpg")
        img4 =img4.resize((220, 220), Image.ADAPTIVE)
        self.photoimg4 =ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image= self.photoimg4,command=self.student_details, cursor="hand2") 
        b1.place(x=350, y=100, width=220, height=220)

        b1_1 = Button(bg_img,text="Student Details",command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white") 
        b1_1.place(x=350, y=300, width=220, height=40)


        # DETECT FACE  BUTTON
        img5 =Image.open(r"C:\Users\USER\Downloads\FRAS\college_images\face.png")
        img5 =img5.resize((220, 220), Image.ADAPTIVE)
        self.photoimg5 =ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image= self.photoimg5, cursor="hand2", command=self.face_data) 
        b1.place(x=650, y=100, width=220, height=220)

        b1_1 = Button(bg_img,text="Face Detector", cursor="hand2", command=self.face_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white") 
        b1_1.place(x=650, y=300, width=220, height=40)


        # ATTENDANCE FACE  BUTTON
        img6 =Image.open(r"C:\Users\USER\Downloads\FRAS\college_images\attendance.jpg")
        img6 =img6.resize((220, 220), Image.ADAPTIVE)
        self.photoimg6 =ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image= self.photoimg6, cursor="hand2",command=self.attendance_data,) 
        b1.place(x=950, y=100, width=220, height=220)

        b1_1 = Button(bg_img,text="Attendance", cursor="hand2",command=self.attendance_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white") 
        b1_1.place(x=950, y=300, width=220, height=40)


        # HELP BUTTON
        #img7 =Image.open(r"C:\Users\USER\Downloads\FRAS\college_images\help.png")
        #img7 =img7.resize((220, 220), Image.ADAPTIVE)
        #self.photoimg7 =ImageTk.PhotoImage(img7)

        #b1 = Button(bg_img, image= self.photoimg7, cursor="hand2") 
        #b1.place(x=1100, y=100, width=220, height=220)

        #b1_1 = Button(bg_img,text="Help", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white") 
        #b1_1.place(x=1100, y=300, width=220, height=40)


        # TEST FACE BUTTON
        img8 =Image.open(r"C:\Users\USER\Downloads\FRAS\college_images\test.png")
        img8 =img8.resize((220, 220), Image.ADAPTIVE)
        self.photoimg8 =ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image= self.photoimg8, cursor="hand2", command=self.train_data) 
        b1.place(x=350, y=380, width=220, height=220)

        b1_1 = Button(bg_img,text="Test", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white") 
        b1_1.place(x=350, y=580, width=220, height=40)


        # PHOTOS FACE BUTTON
        img9 =Image.open(r"C:\Users\USER\Downloads\FRAS\college_images\photos.jpg")
        img9 =img9.resize((220, 220), Image.ADAPTIVE)
        self.photoimg9 =ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image= self.photoimg9, cursor="hand2", command=self.open_img) 
        b1.place(x=650, y=380, width=220, height=220)

        b1_1 = Button(bg_img,text="Photos", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white") 
        b1_1.place(x=650, y=580, width=220, height=40)


        # DEVELOPER ACCESS BUTTON
        #img10 =Image.open(r"C:\Users\USER\Downloads\FRAS\college_images\developer.jpg")
        #img10 =img10.resize((220, 220), Image.ADAPTIVE)
        #self.photoimg10 =ImageTk.PhotoImage(img10)

        #b1 = Button(bg_img, image= self.photoimg10, cursor="hand2") 
        #b1.place(x=800, y=380, width=220, height=220)

        #b1_1 = Button(bg_img,text="Developer", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white") 
        #b1_1.place(x=800, y=580, width=220, height=40)


        # EXIT BUTTON
        img11 =Image.open(r"C:\Users\USER\Downloads\FRAS\college_images\exit.jpg")
        img11 =img11.resize((220, 220), Image.ADAPTIVE)
        self.photoimg11 =ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image= self.photoimg11, cursor="hand2", command=self.iExit) 
        b1.place(x=950, y=380, width=220, height=220)

        b1_1 = Button(bg_img,text="Exit", cursor="hand2",command=self.iExit , font=("times new roman", 15, "bold"), bg="darkblue", fg="white") 
        b1_1.place(x=950, y=580, width=220, height=40)
        
    def open_img(self):
        os.startfile("data")
    
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("face Recognition", "Are you sure to exit?", parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return
    #==============Functions Button=================#
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recog(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
