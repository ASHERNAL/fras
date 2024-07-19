from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

myData = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance")

        #===============variables====================
        self.var_atten_name=StringVar()
        self.var_atten_course=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        img = Image.open(r"C:\Users\USER\Downloads\FRAS\college_images\bg.jpg")
        img = img.resize((1530, 790), Image.ADAPTIVE)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        title_lbl = Label(bg_img, text="STUDENT ATTENDANCE SYSTEM", 
                          font=("times new roman", 45, "bold"), bg="blue", fg="white")
        title_lbl.place(x=0, y=40, width=1530, height=70)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=120, width=1500, height=630)

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Detail", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=720, height=590)

        # Attendance ID
        #AttendanceID_label = Label(Left_frame, text="Attendance ID:", font=("times new roman", 12, "bold"))
        #AttendanceID_label.grid(row=0, column=0, padx=10, pady=10)
        #AttendanceID_entry = ttk.Entry(Left_frame, width=20, font=("times new roman", 12, "bold"))
        #AttendanceID_entry.grid(row=0, column=1, padx=10, pady=10)

        # Name
        name_label = Label(Left_frame, text="Attendance Name:", font=("times new roman", 12, "bold"))
        name_label.grid(row=1, column=0, padx=10, pady=10)
        name_entry = ttk.Entry(Left_frame, width=20, textvariable=self.var_atten_name, font=("times new roman", 12, "bold"))
        name_entry.grid(row=1, column=1, padx=10, pady=10)

        # Time
        date_label = Label(Left_frame, text="Time:", font=("times new roman", 12, "bold"))
        date_label.grid(row=2, column=0, padx=10, pady=10)
        date_entry = ttk.Entry(Left_frame, width=20, textvariable=self.var_atten_time, font=("times new roman", 12, "bold"))
        date_entry.grid(row=2, column=1, padx=10, pady=10)

        # Course
        department_label = Label(Left_frame, text="Course:", font=("times new roman", 12, "bold"))
        department_label.grid(row=3, column=0, padx=10, pady=10)
        department_entry = ttk.Entry(Left_frame, width=20,textvariable=self.var_atten_course, font=("times new roman", 12, "bold"))
        department_entry.grid(row=3, column=1, padx=10, pady=10)

        # Date
        time_label = Label(Left_frame, text="Date:", font=("times new roman", 12, "bold"))
        time_label.grid(row=4, column=0, padx=10, pady=10)
        time_entry = ttk.Entry(Left_frame, width=20,textvariable=self.var_atten_date, font=("times new roman", 12, "bold"))
        time_entry.grid(row=4, column=1, padx=10, pady=10)

        # Attendance
        attendance_label = Label(Left_frame, text="Attendance Status:", font=("times new roman", 12, "bold"))
        attendance_label.grid(row=5, column=0, padx=10, pady=10)
        
        self.atten_status = ttk.Combobox(Left_frame, width=20,textvariable=self.var_atten_attendance, font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=5, column=1, pady=8)
        self.atten_status.current(0)

        # Buttons frame
        btn_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=280, width=690, height=35)

        save_btn = Button(btn_frame, text="Import CSV", command=self.importCSV, width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export CSV", width=18,command=self.exportCSV, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update", width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance", font=("times new roman", 12, "bold"))
        Right_frame.place(x=760, y=10, width=720, height=590)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=6, y=5, width=690, height=260)

        # Scroll Bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=( "std_name", "course", "time",  "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        #self.AttendanceReportTable.heading("std_id", text="Attendance ID")
        self.AttendanceReportTable.heading("std_name", text="Attendance Name")
        self.AttendanceReportTable.heading("course", text="Course")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")
        self.AttendanceReportTable["show"] = "headings"

        #self.AttendanceReportTable.column("std_id", width=100)
        self.AttendanceReportTable.column("std_name", width=100)
        self.AttendanceReportTable.column("course", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for row in rows:
            self.AttendanceReportTable.insert("", END, values=row)

    def importCSV(self):
        global myData
        myData.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV file", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for row in csvread:
                myData.append(row)
            self.fetchData(myData)


    def exportCSV(self):
        try:
            if len(myData)<1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV file", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for row in myData:
                    exp_write.writerow(row)
                messagebox.showinfo("Data Exported", "Your Data exported to"+os.path.basename(fln)+"Successfully")
        except Exception as es:
                    messagebox.showerror("Error",f"Due to :{str(es)}", parent=self.root)

    def get_cursor(self,event=""):
         cursor_row=self.AttendanceReportTable.focus()
         content=self.AttendanceReportTable.item(cursor_row)
         rows=content['values']
         self.var_atten_name.set(rows[0])
         self.var_atten_course.set(rows[1])
         self.var_atten_time.set(rows[2])
         self.var_atten_date.set(rows[3])
         self.var_atten_attendance.set(rows[4])


    #def reset_data(self):
