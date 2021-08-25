#use to form gui 
from tkinter import*
#tkk  imported because it has some stylies toolkit
from tkinter import ttk
from tkinter.messagebox import askyesno

#pillow used to import images
from PIL import Image,ImageTk
from student import Student
from Train import Train
from face_recog import Face_rec
from Attendance import Attendance
import os
class Face_Recognition_System:
    #to call constructor
    def __init__(self,root):
        self.root=root
        #geometry is used to set size of window 
        self.root.geometry("1300x768+0+0")
        #title use to set title of window
        self.root.title("face Recognition System")
        #adding image in window

        #first image
        img=Image.open(r"img\university.jpg")
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
        img1=Image.open(r"img\facialrecognition.png")
        img1=img1.resize((500,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)  
        f_lbl.place(x=500,y=0,width=500,height=100)

        #Third image
        img2=Image.open(r"img\university2.jpg")
        img2=img2.resize((500,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=100)
        
        # bg image
        img3=Image.open(r"img\bg.png")
        img3=img3.resize((1366,768),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_image=Label(self.root,image=self.photoimg3)
        bg_image.place(x=0,y=100,width=1366,height=768)

        #label title
        title_lbl=Label(bg_image,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new romen",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1366,height=30)

       


        #student button 
        img4=Image.open(r"img\student.jpg")
        img4=img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_image,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=70,width=200,height=200)

        b1_1=Button(bg_image,text="Student Details",command=self.student_details,cursor="hand2",font=("times new romen",10,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=270,width=200,height=40)

        #Detect face button
        img5=Image.open(r"img\face_detector1.jpg")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_image,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=70,width=200,height=200)

        b1_1=Button(bg_image,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new romen",10,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=270,width=200,height=40)

        #Attendence face button
        img6=Image.open(r"img\smart-attendance.jpg")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_image,image=self.photoimg6,cursor="hand2",command=self.attan_data)
        b1.place(x=900,y=70,width=200,height=200)

        b1_1=Button(bg_image,text="Attendence",cursor="hand2",command=self.attan_data,font=("times new romen",10,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=900,y=270,width=200,height=40)

        

        #Train button
        img8=Image.open(r"img\dev.jpg")
        img8=img8.resize((200,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_image,image=self.photoimg8,cursor="hand2",command=self.Train_data)
        b1.place(x=100,y=340,width=200,height=200)

        b1_1=Button(bg_image,text="Train",cursor="hand2",command=self.Train_data,font=("times new romen",10,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=540,width=200,height=40)

        # photos button
        img9=Image.open(r"img\Stuphoto.jpg")
        img9=img9.resize((200,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_image,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=340,width=200,height=200)

        b1_1=Button(bg_image,text="Photos",cursor="hand2",command=self.open_img,font=("times new romen",10,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=540,width=200,height=40)

     
        #Exit button
        img11=Image.open(r"img\exit.jpg")
        img11=img11.resize((200,200),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_image,image=self.photoimg11,command=self.iexit,cursor="hand2")
        b1.place(x=900,y=340,width=200,height=200)

        b1_1=Button(bg_image,text="Exit",cursor="hand2",command=self.iexit,font=("times new romen",10,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=900,y=540,width=200,height=40)

    
    def open_img(self):
        os.startfile("Data")


       


    #===========Functions Button=============
    def student_details(self):
        #Toplevel because we have to open student window above main
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def Train_data(self):
        #Toplevel because we have to open student window above main
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        #Toplevel because we have to open student window above main
        self.new_window=Toplevel(self.root)
        self.app=Face_rec(self.new_window)
    
    def attan_data(self):
        #Toplevel because we have to open student window above main
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def iexit(self):
        self.iexit=askyesno("Face Recognition","Are you sure to exit")
        if self.iexit>0:
            self.root.destroy()
        else:
            return
    

    







if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()