from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details")

        # Variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_age = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_lecturer = StringVar()

        # First image
        img = Image.open(r"C:\Users\USER\Downloads\FRAS\college_images\bg.jpg")
        img = img.resize((1530, 790), Image.ADAPTIVE)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", 
                          font=("times new roman", 45, "bold"), bg="red", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=70)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=80, width=1500, height=630)

        # Left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=720, height=580)

        img_left = Image.open(r"C:\Users\USER\Downloads\FRAS\college_images\studentss.jpg")
        img_left = img_left.resize((720, 130), Image.ADAPTIVE)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        bg_img = Label(Left_frame, image=self.photoimg_left)
        bg_img.place(x=5, y=0, width=700, height=130)

        # Current course
        currentcourse_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        currentcourse_frame.place(x=10, y=135, width=695, height=110)

        # Department
        dep_label = Label(currentcourse_frame, text="Department", font=("times new roman", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(currentcourse_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), width=17, state="read only")
        dep_combo['values'] = ("Select Department", "Computer", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)

        # Course
        course_label = Label(currentcourse_frame, text="Course", font=("times new roman", 12, "bold"))
        course_label.grid(row=0, column=2, padx=10)

        course_combo = ttk.Combobox(currentcourse_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"), width=17, state="read only")
        course_combo['values'] = ("Select Course", "MEA", "MEB", "EE", "CE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10)

        # Year
        year_label = Label(currentcourse_frame, text="Year", font=("times new roman", 12, "bold"))
        year_label.grid(row=1, column=0, padx=10)

        year_combo = ttk.Combobox(currentcourse_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), width=17, state="read only")
        year_combo['values'] = ("Select Year", "2022-2025", "2019-2022", "2016-2019", "2013-2016", "2010-2013", "2007-2010", "2004-2007", "2001-2004")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10)

        # Semester
        sem_label = Label(currentcourse_frame, text="Semester", font=("times new roman", 12, "bold"))
        sem_label.grid(row=1, column=2, padx=10)

        sem_combo = ttk.Combobox(currentcourse_frame, textvariable=self.var_semester, font=("times new roman", 12, "bold"), width=17, state="read only")
        sem_combo['values'] = ("Select Semester", "Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6", "Semester 7")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10)

        # Class student info
        classstudent_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        classstudent_frame.place(x=10, y=250, width=695, height=300)

        # Student ID
        studentID_label = Label(classstudent_frame, text="Student ID:", font=("times new roman", 12, "bold"))
        studentID_label.grid(row=0, column=0, padx=10, pady=10)

        studentID_entry = ttk.Entry(classstudent_frame, textvariable=self.var_std_id, width=20, font=("times new roman", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, pady=10)

        # Name
        studentname_label = Label(classstudent_frame, text="Student Name:", font=("times new roman", 12, "bold"))
        studentname_label.grid(row=0, column=2, padx=10, pady=10)
        
        studentname_entry = ttk.Entry(classstudent_frame, textvariable=self.var_std_name, width=20, font=("times new roman", 12, "bold"))
        studentname_entry.grid(row=0, column=3, padx=10, pady=10)
        
        # Age
        studentage_label = Label(classstudent_frame, text="Student Age:", font=("times new roman", 12, "bold"))
        studentage_label.grid(row=3, column=0, padx=10, pady=10)
        
        studentage_entry = ttk.Entry(classstudent_frame, textvariable=self.var_age, width=20, font=("times new roman", 12, "bold"))
        studentage_entry.grid(row=3, column=1, padx=10, pady=10)

        # Gender
        studentgender_label = Label(classstudent_frame, text="Student Gender:", font=("times new roman", 12, "bold"))
        studentgender_label.grid(row=3, column=2, padx=10, pady=10)
        
        #studentgender_entry = ttk.Entry(classstudent_frame, textvariable=self.var_gender, width=20, font=("times new roman", 12, "bold"))
        #studentgender_entry.grid(row=3, column=3, padx=10, pady=10)
        gender_combo = ttk.Combobox(classstudent_frame, textvariable=self.var_gender, font=("times new roman", 12, "bold"), width=17, state="read only")
        gender_combo['values'] = ("Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=3, column=3, padx=2, pady=10)

        # Phone no
        studentphone_label = Label(classstudent_frame, text="Student Phone No:", font=("times new roman", 12, "bold"))
        studentphone_label.grid(row=5, column=0, padx=10, pady=10)
        
        studentphone_entry = ttk.Entry(classstudent_frame, textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        studentphone_entry.grid(row=5, column=1, padx=10, pady=10)

        # Email
        studentemail_label = Label(classstudent_frame, text="Student Email:", font=("times new roman", 12, "bold"))
        studentemail_label.grid(row=5, column=2, padx=10, pady=10)
        
        studentemail_entry = ttk.Entry(classstudent_frame, textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        studentemail_entry.grid(row=5, column=3, padx=10, pady=10)

        # Address
        studentaddr_label = Label(classstudent_frame, text="Student Address:", font=("times new roman", 12, "bold"))
        studentaddr_label.grid(row=7, column=0, padx=10, pady=10)
        
        studentaddr_entry = ttk.Entry(classstudent_frame, textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        studentaddr_entry.grid(row=7, column=1, padx=10, pady=10)

        # Lecturer name
        studentlecname_label = Label(classstudent_frame, text="Lecturer Name:", font=("times new roman", 12, "bold"))
        studentlecname_label.grid(row=7, column=2, padx=10, pady=10)
        
        studentlecname_entry = ttk.Entry(classstudent_frame, textvariable=self.var_lecturer, width=20, font=("times new roman", 12, "bold"))
        studentlecname_entry.grid(row=7, column=3, padx=10, pady=10)

        # Radio buttons
        self.var_radio1 = StringVar()
        radionbtn1 = ttk.Radiobutton(classstudent_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radionbtn1.grid(row=9, column=0)

        radionbtn2 = ttk.Radiobutton(classstudent_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radionbtn2.grid(row=9, column=1)

        # Button frame
        btn_frame = Frame(classstudent_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=205, width=690, height=35)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        btn1_frame = Frame(classstudent_frame, bd=2, relief=RIDGE, bg="white")
        btn1_frame.place(x=0, y=240, width=690, height=35)

        takephoto_btn = Button(btn1_frame, command=self.generate_dataset, text="Take Photo Sample", width=37, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        takephoto_btn.grid(row=1, column=0)

        updatephoto_btn = Button(btn1_frame, text="Update Photo Sample", width=37, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        updatephoto_btn.grid(row=1, column=1)

        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=760, y=10, width=720, height=580)

        img_right = Image.open(r"C:\Users\USER\Downloads\FRAS\college_images\stnd.png")
        img_right = img_right.resize((720, 160), Image.ADAPTIVE)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        bg_img = Label(Right_frame, image=self.photoimg_right)
        bg_img.place(x=5, y=0, width=710, height=130)

        # Search System
        searchsystem_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        searchsystem_frame.place(x=10, y=135, width=700, height=80)

        searchsystem_label = Label(searchsystem_frame, text="Search By:", font=("times new roman", 16, "bold"), bg='red', fg="white")
        searchsystem_label.grid(row=0, column=0, padx=10, pady=10)

        search_combo = ttk.Combobox(searchsystem_frame, font=("times new roman", 12, "bold"), width=17, state="read only")
        search_combo['values'] = ("Select", "Phone No", "Email")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10)

        search_entry = ttk.Entry(searchsystem_frame, width=15, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=10)

        search_btn = Button(searchsystem_frame, text="Search", width=12, font=("times new roman", 11, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=5)

        showAll_btn = Button(searchsystem_frame, text="Show All", width=12, font=("times new roman", 11, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=5)

        # Table Frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=220, width=700, height=300)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "semester", "std_id", "std_name", "age", "gender", "email", "phone", "address", "lecturer", "photosample"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("std_id", text="ID")
        self.student_table.heading("std_name", text="Name")
        self.student_table.heading("age", text="Age")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("lecturer", text="Lecturer")
        self.student_table.heading("photosample", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("semester", width=100)
        self.student_table.column("std_id", width=100)
        self.student_table.column("std_name", width=100)
        self.student_table.column("age", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("lecturer", width=100)
        self.student_table.column("photosample", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ===================Function declaration======================
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "" or self.var_email.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="ashwindave1010",
                    port="3306",
                    database="stdnts"
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO student (dep, course, year, semester, student_id, name, age, gender, email, phone, address, lecturer, photosample) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_lecturer.get(),
                        self.var_radio1.get()
                    )
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student Details have been added", parent=self.root)
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {str(err)}", parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error", f"An unexpected error occurred: {str(ex)}", parent=self.root)

    #=================Fetch Database========================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="ashwindave1010",port="3306",database="stdnts")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
#====================get cursor========================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_age.set(data[6])
        self.var_gender.set(data[7])
        self.var_email.set(data[8])
        self.var_phone.set(data[9])
        self.var_address.set(data[10])
        self.var_lecturer.set(data[11])
        self.var_radio1.set(data[12])

        # Store the original student ID to use in the update query
        self.original_std_id = data[4]

    # update function=============================================================
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details?", parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="ashwindave1010",port="3306",database="stdnts")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s, student_id=%s, name=%s,age=%s,gender=%s,email=%s,phone=%s,address=%s,lecturer=%s,photosample=%s where student_id=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_lecturer.get(),
                        self.var_radio1.get(),
                        self.original_std_id
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root)

    # delete function===========================================================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student?", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="ashwindave1010",port="3306",database="stdnts")
                    my_cursor = conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted Student", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root)

    # reset function===================================================================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_age.set("")
        self.var_gender.set("Male")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_lecturer.set("")
        self.var_radio1.set("")

    #========================= Generate data set or Take Photo Samples================================
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="ashwindave1010",port="3306",database="stdnts")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,age=%s,gender=%s,email=%s,phone=%s,address=%s,lecturer=%s,photosample=%s where student_id=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_lecturer.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #======Load Predefined data on Face frontals from opencv====

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #minimum neighbor = 5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face,str(img_id), (100,100), cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data Sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
