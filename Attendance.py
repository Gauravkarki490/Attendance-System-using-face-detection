from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os           #for access the folder
import numpy as np
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x768+0+0")
        self.root.title("face Recognition System")

        #variables
        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()

        #first image
        img=Image.open(r"E:\Mini Project\img\left_frame.jpg")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=650,height=200)

        #second image
        img1=Image.open(r"E:\Mini Project\img\left_frame.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=650,y=0,width=750,height=200)

        title_lbl=Label(self.root,text="STUDENT ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=200,width=1360,height=45)

         #main frame   
        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=10,y=246,width=1360,height=600)

         #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text=" Student Attendance Detail",font=("times new roman",12,"bold"))
        Left_frame.place(x=5,y=10,width=650,height=440)

        img_left=Image.open(r"E:\Mini Project\img\girl.jpeg")
        img_left=img_left.resize((650,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=640,height=130)


        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=135,width=640,height=370)

        #Labelland entry
        # Attendence id
        attendenceId_label=Label(left_inside_frame,text="AttendenceID:",font=("times new roman",13,"bold"),bg="white")
        attendenceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendenceID_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_attend_id,font=("times new roman",13,"bold"))
        attendenceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Roll
        rolllabel=Label(left_inside_frame,text="Roll:",font=("times new roman",13,"bold"),bg="white")
        rolllabel.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        attend_roll=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_attend_roll,font=("times new roman",13,"bold"))
        attend_roll.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Name
        namelabel=Label(left_inside_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
        namelabel.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        attend_name=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_attend_name,font=("times new roman",13,"bold"))
        attend_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Department
        deplabel=Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        deplabel.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        attend_dep=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_attend_dep,font=("times new roman",13,"bold"))
        attend_dep.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # time
        timelabel=Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        timelabel.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        attend_time=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_attend_time,font=("times new roman",13,"bold"))
        attend_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # date
        datelabel=Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        datelabel.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        attend_date=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_attend_date,font=("times new roman",13,"bold"))
        attend_date.grid(row=2,column=3,padx=10,pady=5,sticky=W)

         #---attendance---
        attendenceLabel=Label(left_inside_frame,text="Attendence Status",font=("times new roman",13,"bold"),bg="white")
        attendenceLabel.grid(row=3,column=0,padx=10,pady=5,sticky=W)


        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_attend_attendance,font=("times new roman",13,"bold"),state="readonly",width=13)
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #button frame

        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=212,width=640,height=125)

        import_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=34,font=("times new roman",13,"bold"),bg="green",fg="white")
        import_btn.grid(row=0,column=0)

        

        export_btn=Button(btn_frame,text="Export",width=34,command=self.exportCsv,font=("times new roman",13,"bold"),bg="green",fg="white")
        export_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update",width=34,command=self.action,font=("times new roman",13,"bold"),bg="green",fg="white")
        update_btn.grid(row=1,column=0)

        reset_btn=Button(btn_frame,text="Reset",width=34,command=self.reset_data,font=("times new roman",13,"bold"),bg="green",fg="white")
        reset_btn.grid(row=1,column=1)



         #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Detail",font=("times new roman",12,"bold"))
        Right_frame.place(x=660,y=10,width=685,height=440)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5,width=670,height=400)

        #---scroll bar and table----
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.getcursor)


#         #-----fetch data-------

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


        #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",".csv"),("All File",".*")),parent=self.root)           #getcwd==current working directory
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

        #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found To Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",".csv"),("All File",".*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported To "+os.path.basename(fln)+" Successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)        

    def getcursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])


    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")

       
# export update
    def action(self):
        id=self.var_attend_id.get()
        roll=self.var_attend_roll.get()
        name=self.var_attend_name.get()
        dep=self.var_attend_dep.get()
        time=self.var_attend_time.get()
        date=self.var_attend_date.get()
        attendn=self.var_attend_attendance.get()

        # write to csv file
        try:
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV file",".csv"),("All File",".*")),parent=self.root)
            with open(fln,mode="a",newline="\n") as f:
                dict_writer=csv.DictWriter(f,fieldnames=(["ID","Roll","Name","Department","Time","Date","Attendance"]))
                dict_writer.writeheader()
                dict_writer.writerow({
                "ID":id,
                "Roll":roll,
                "Name":name,
                "Department":dep,
                "Time":time,
                "Date":date,
                "Attendance":attendn 
                    })
            messagebox.showinfo("Data Exported","Your data exported to " +os.path.basename(fln)+ " Successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)






if __name__== "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()