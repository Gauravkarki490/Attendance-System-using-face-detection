from csv import DictWriter
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
# from tkinter import filedialog

class Student:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x768+0+0")
        self.root.title("face Recognition System")

        #=========variable=========
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.serchTxt_var=StringVar()
        self.serch_var=StringVar()

        #first image
        img=Image.open(r"E:\Mini Project\img\smart-attendance.jpg")
        #used to resize the image 
        #Image.ANTIALIAS used to convert high resolution to low resolution
        img=img.resize((500,100),Image.ANTIALIAS)
        #storing image in a veriable
        self.photoimg=ImageTk.PhotoImage(img)
        #now setting img in window using label
        f_lbl=Label(self.root,image=self.photoimg)
        #image to show in on window
        f_lbl.place(x=0,y=0,width=500,height=100)
       
        #second image
        img1=Image.open(r"E:\Mini Project\img\girl.jpeg")
        img1=img1.resize((500,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)  
        f_lbl.place(x=500,y=0,width=500,height=100)

        #Third image
        img2=Image.open(r"E:\Mini Project\img\smart-attendance.jpg")
        img2=img2.resize((500,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=100)

        # bg image
        img3=Image.open(r"E:\Mini Project\img\bg.png")
        img3=img3.resize((1366,768),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_image=Label(self.root,image=self.photoimg3)
        bg_image.place(x=0,y=100,width=1366,height=768)

        #label title
        title_lbl=Label(bg_image,text="STUDENT MANAGEMENT SYSTEM",font=("times new romen",25,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1377,height=30)
        
        #creating frame for addinging different things
        main_frame=Frame(bg_image,bd=2,bg="white")
        main_frame.place(x=25,y=40,width=1300,height=550)

        #dividing frame now in 2 part left and right 
        #only difference is that we can add title in label frame
        
        #left frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=20,y=10,width=610,height=530)

        #image in left label
        img_left=Image.open(r"E:\Mini Project\img\left_frame.jpg")
        img_left=img_left.resize((600,100),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=3,y=0,width=600,height=100)

        #Current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=3,y=105,width=600,height=120)

        #Departement
        dep_label=Label(current_course_frame,text="Departement",font=("times new roman",12,"bold"),bg="white")
        #we are using grid for the row and columns
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="read only")
        #default values
        dep_combo["values"]=("Select Department","Computer","It","Civil","Mechnical")
        dep_combo.current(0)#current postion should come
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        #we are using grid for the row and columns
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="read only")
        #default values
        course_combo["values"]=("Select Course","FE","EE","CSE","BE")
        course_combo.current(0)#current postion should come
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        #we are using grid for the row and columns
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="read only")
        #default values
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)#current postion should come
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        Semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        #we are using grid for the row and columns
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)

        Semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="read only")
        #default values
        Semester_combo["values"]=("Select Semester","Sem-1","Sem-2","Sem-3","Sem-4")
        Semester_combo.current(0)#current postion should come
        Semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student Information
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=3,y=225,width=600,height=280)

        #Student ID
        studentID_label=Label(class_Student_frame,text="Student ID :",font=("times new roman",12,"bold"),bg="white")
        #we are using grid for the row and columns
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        #entry field student id
        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=16,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentName_label=Label(class_Student_frame,text="Student Name :",font=("times new roman",12,"bold"),bg="white")
        #we are using grid for the row and columns
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        #entry field student id
        studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=16,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class Division
        class_div_label=Label(class_Student_frame,text="Class Division :",font=("times new roman",12,"bold"),bg="white")
        #we are using grid for the row and columns
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #entry field student id

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=14,state="read only")
        #default values
        div_combo["values"]=("A","B","C")
        div_combo.current(0)#current postion should come
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        #Roll No
        roll_no_label=Label(class_Student_frame,text="Roll No :",font=("times new roman",12,"bold"),bg="white")
        #we are using grid for the row and columns
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        #entry field student id
        roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=16,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_Student_frame,text="Gender :",font=("times new roman",12,"bold"),bg="white")
        #we are using grid for the row and columns
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #entry field student id
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=14,state="read only")
        #default values
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)#current postion should come
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
        dob_label=Label(class_Student_frame,text="DOB :",font=("times new roman",12,"bold"),bg="white")
        #we are using grid for the row and columns
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        #entry field student id
        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=16,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        email_label=Label(class_Student_frame,text="Email :",font=("times new roman",12,"bold"),bg="white")
        #we are using grid for the row and columns
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        #entry field student id
        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=16,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone no
        phone_label=Label(class_Student_frame,text="Phone No :",font=("times new roman",12,"bold"),bg="white")
        #we are using grid for the row and columns
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        #entry field student id
        phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=16,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Addresss
        Add_label=Label(class_Student_frame,text="Address :",font=("times new roman",12,"bold"),bg="white")
        #we are using grid for the row and columns
        Add_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        #entry field student id
        Add_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=16,font=("times new roman",12,"bold"))
        Add_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Teacher name
        teacher_label=Label(class_Student_frame,text="Teacher Name :",font=("times new roman",12,"bold"),bg="white")
        #we are using grid for the row and columns
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        #entry field student id
        teacher_entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=16,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio Buttons
        self.var_radio1=StringVar()
        radioBtn1=ttk.Radiobutton(class_Student_frame,text="take Photo Smaple",variable=self.var_radio1,value="Yes")
        radioBtn1.grid(row=6,column=0)

        self.var_radio1=StringVar()
        radioBtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Smaple",value="No")
        radioBtn2.grid(row=6,column=1)

        #btn frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=3,y=200,width=590,height=30)

        #save btn
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=20,font=("times new roman",9,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=20,font=("times new roman",9,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=20,font=("times new roman",9,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=20,font=("times new roman",9,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=3,y=230,width=590,height=25)
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=41,font=("times new roman",9,"bold"),bg="blue",fg="white")
        take_photo_btn.place(x=0,y=0,width=595,height=25)

        # update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=41,font=("times new roman",9,"bold"),bg="blue",fg="white")
        # update_photo_btn.grid(row=0,column=1)

        #right frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=650,y=10,width=610,height=530)

        #image in Right label
        img_right=Image.open(r"E:\Mini Project\img\Right_frame.jpeg")
        img_right=img_right.resize((600,100),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=3,y=0,width=600,height=100)

        #=========== Search System =============
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=3,y=105,width=600,height=70)

        Search_label=Label(Search_frame,text="Search By :",font=("times new roman",15,"bold"),bg="red",fg="white")
        #we are using grid for the row and columns
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        Search_combo=ttk.Combobox(Search_frame,textvariable=self.serch_var,font=("times new roman",9,"bold"),width=14,state="read only")
        #default values
        Search_combo["values"]=("Select","Roll","Student_id")
        Search_combo.current(0)#current postion should come
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=14,textvariable=self.serchTxt_var,font=("times new roman",9,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Search_frame,text="Search",command=self.search_data,width=14,font=("times new roman",9,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # showAll_btn=Button(Search_frame,text="Show All",width=14,font=("times new roman",9,"bold"),bg="blue",fg="white")
        # showAll_btn.grid(row=0,column=4,padx=10,pady=5,sticky=W)

        #=============table Frame==============
        tabel_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        tabel_frame.place(x=3,y=175,width=600,height=330)

        #Scrollbar
        scroll_bar_x=ttk.Scrollbar(tabel_frame,orient=HORIZONTAL)
        scroll_bar_y=ttk.Scrollbar(tabel_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(tabel_frame,column=("Dep","Course","Year","Sem","Id","Name","Div","Roll","DOB","Email","Phone","Address","Teacher","Photo","Gender"),xscrollcommand=scroll_bar_x.set,yscrollcommand=scroll_bar_y.set)

        #pack
        scroll_bar_x.pack(side=BOTTOM,fill=X)
        scroll_bar_y.pack(side=RIGHT,fill=Y)
        scroll_bar_x.config(command=self.student_table.xview)
        scroll_bar_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("Id",text="StudentId")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Div",text="Division")
        self.student_table.heading("Roll",text="Roll No")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Teacher",text="Teacher")
        
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table.heading("Gender",text="Gender")
        
        

        self.student_table["show"]="headings"

        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)
        self.student_table.column("Gender",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
    #=====================function Declaration==========
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="face_re")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_id.get(),
                                                                                                            self.var_std_name.get(), 
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get(),
                                                                                                            self.var_gender.get()
                                                                                                            
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    #=======fecth data=========
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="face_re")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    #=========Get Cursor=========
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus();
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]), 
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_dob.set(data[8]),
       
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_teacher.set(data[12]),
        self.var_radio1.set(data[13]),
        self.var_gender.set(data[14])

    #====update function========
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Upadte","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="face_re")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s,Gender=%s where Student_id=%s",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            
                                                                                                            self.var_std_name.get(), 
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            self.var_std_id.get(),
                    ))
                else:
                    if  not Update:
                        return 
                messagebox.showinfo("Success","Student details successfylly update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",prent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="face_re")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   
    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_dob.set("")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Divison")
        self.var_roll.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        self.var_gender.set("Male")

    #==========================Generate data set Take photo Smaples=======
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="face_re")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s,Gender=%s where Student_id=%s",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            
                                                                                                            self.var_std_name.get(), 
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            self.var_std_id.get()==id+1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #===========Load predifiend data on face frontals from openCV====

                face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum Neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped 
                cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
                img_id=0
                while True:
                    try:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                    
                   
                        face=cv2.resize(face_cropped(my_frame), (450,450),cv2.INTER_AREA)
                        face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path="Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,250),2)
                        cv2.imshow("Cropped Face",face)
                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                    except:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result"," Generating data sets completed!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   
    

    def search_data(self):
        if self.serchTxt_var.get()=="" or self.serch_var.get()=="Select Option":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="face_re")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where " +str(self.serch_var.get())+" LIKE '%"+str(self.serchTxt_var.get())+"%'")
                rows=my_cursor.fetchall()         
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    

    
    


if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()