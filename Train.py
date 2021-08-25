from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os           #for access the folder
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x768+0+0")
        self.root.title("face Recognition System")
        
        
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1376,height=45)

        img_top=Image.open(r"E:\Mini Project\img\left_frame.jpg")
        img_top=img_top.resize((1000,200),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top,bg="white")
        f_lbl.place(x=0,y=45,width=1376,height=300)

        #----button-----
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0,y=345,width=1376,height=60)

        title_lbl=Label(self.root,text="CLICK ON ABOVE  BUTTON",font=("times new roman",20,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=400,width=1376,height=45)



        img_bottom=Image.open(r"E:\Mini Project\img\left_frame.jpg")
        img_bottom=img_bottom.resize((1000,200),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=500,width=1376,height=200)



       
    def train_classifier(self):
        data_dir=("Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')          #gray scale image 
            imageNp=np.array(img,'uint8')               #unit8--->datatype
            id=int(os.path.split(image)[1].split('.')[1])


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)

        #---------train classifier and save------
        clf=cv2.face.LBPHFaceRecognizer_create()            #---use LBPH algorithm--
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed..!!! ")
    









if __name__== "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()