from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data")

        img_top = Image.open(r"college_images\facialrecognition.png")
        img_top = img_top.resize((1530, 450), Image.ADAPTIVE)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        bg_img = Label(self.root, image=self.photoimg_top)
        bg_img.place(x=0, y=13, width=1530, height=450)

        title_lbl = Label(self.root, text="TRAIN DATA SET", 
                          font=("times new roman", 45, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=15, width=1530, height=70)

        img_bottom = Image.open(r"college_images/facial-recognition-clearview.jpg")
        img_bottom = img_bottom.resize((1530, 450), Image.ADAPTIVE)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        bg_img = Label(self.root, image=self.photoimg_bottom)
        bg_img.place(x=0, y=380, width=1530, height=450)

        b1_1 = Button(self.root ,text="TRAIN DATA",command=self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="red", fg="white") 
        b1_1.place(x=0, y=370, width=1530, height=45)
        

    def train_classifier(self):
        data_dir=("data")
        path= [ os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        
        
        faces=[]
        ids=[]

        for image in path:
            try:
                img=Image.open(image).convert('L') #gray scale image
                imageNp=np.array(img,'uint8')
                id=int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1)==13
            except Exception as e:
                print(f"Error processing image {image}: {e}")
        ids=np.array(ids)


        #=============== Train the classifier and save==================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets Completed!!!")




if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()