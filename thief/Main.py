#============================================Import Module=======================================================
import face_recognition as fr
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import mysql.connector as mysql
import tkinter.messagebox as msg
import cv2
import os
from tkcalendar import *
from tkinter import scrolledtext
import tkinter as tk
import numpy as np


#==================================================Select_image button=============================================


def select_image():
    try:
        global panelA
        panelA = None
        global Binarydata


        root.path= filedialog.askopenfilename(title='Image file select option')

        if len(root.path) > 0:

            image = cv2.imread(root.path)

            with open(root.path,"rb") as file:
                Binarydata=file.name
                print(Binarydata)


            image=cv2.resize(image,(400,400))
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            image = Image.fromarray(image)


            image = ImageTk.PhotoImage(image)

            if panelA is None:
                # the first panel will store our original image
                panelA = Label(image=image)

                panelA.image = image
                panelA.place(x=150,y=100)



            else:
                # update the pannels
                panelA.configure(image=image)

                panelA.image = image
    except:
        msg.showinfo("Alert","Sorry! Please select image again")

root = Tk()

#==================================================Frame position===================================================
root.title("Criminal Detector")
root.geometry('1300x600')
root.configure(bg='#3E4149')
root.resizable(width=FALSE,height=FALSE)
top=Frame(root,width=1300,height=50,bg='black')
top.pack(side=TOP)
bottom=Frame(root,width=1300,height=50,bg='black')
bottom.pack(side=BOTTOM)
left=Frame(root,width=750,height=500,bg='gray')
left.pack(side=LEFT)
right=Frame(root,width=550,height=500,bg='dark gray')
right.pack(side=RIGHT)

select = Button(left, text="Select an image",bg='black',fg='white', command=select_image)
select.place(x=0,y=180)

#======================================================Insert Button=================================================
def insert():
    try:
        Criminal_id=e_id.get()
        Fname=e_Fname.get()
        Lname=e_Lname.get()
        Age=e_Age.get()
        Crimed=e_Cdate.get()
        Thana=e_Thana.get()
        District=e_District.get()
        State=e_State.get()
        Crime_Type=e_Ctype.get()
        os.rename(Binarydata,'image/'+str(Criminal_id)+'.jpg')
        Binarydata1='image/'+str(Criminal_id)+'.jpg'



        if(Criminal_id=="" or Fname=="" or Lname=="" or panelA==None or Age=="" or Crimed=="" or Thana=="" or District=="" or State=="" or Crime_Type==""):
            msg.showinfo("Alert","All field must be required")
        else:
            con=mysql.connect(host="localhost",user="root",password="",database="project")
            cursor=con.cursor()

            cursor.execute("INSERT INTO Criminal VALUES ('"+Criminal_id+"','"+Fname+"','"+Lname+"','"+Age+"','"+Crimed+"','"+Thana+"','"+District+"','"+State+"','"+Crime_Type+"','"+Binarydata1+"')")
            cursor.execute("commit")

            msg.showinfo("Insert Status","Inserted successfully")
            con.close()
    except Exception as e:
        print(e)

#=======================================================Delete Button==============================================
def delete():
    try:
        id=e_id.get()
        if(id==""):
            msg.showinfo("Alert","Id must be required")
        else:
            con=mysql.connect(host="localhost",user="root",password="",database="project")
            cursor=con.cursor()
            run=cursor.execute("DELETE FROM `Criminal` WHERE Criminal_id='"+id+"'")
            os.remove('image/' + str(id) + '.jpg')
            msg.showinfo("Delete Status","Delete successfully")
            cursor.execute("commit")
            con.close()
    except:
        msg.showinfo("Alert","Please, Try again")
#=======================================================Update Button===============================================
def update():

    try:
        id=e_id.get()
        Fname=e_Fname.get()
        Lname=e_Lname.get()
        Age=e_Age.get()
        Crimed=e_Cdate.get()
        Thana=e_Thana.get()
        District=e_District.get()
        State=e_State.get()
        Crime_Type=e_Ctype.get()
        if(id==""):
            msg.showinfo("Alert","Id must be required")
        else:
            con=mysql.connect(host="localhost",user="root",password="",database="project")
            cursor=con.cursor()
            cursor.execute("UPDATE `Criminal` SET `Fname`='"+Fname+"',Lname='"+Lname+"',Age='"+Age+"',Crime_date='"+Crimed+"',Thana='"+Thana+"',District='"+District+"',State='"+State+"',Crime_Type='"+Crime_Type+"',`Image`='"+Binarydata+"' WHERE Criminal_Id='"+id+"'")
            cursor.execute("commit")
            msg.showinfo("Update Status","Update successfully")
            con.close()
    except:
        msg.showinfo("Alert","Please,Try again")
#===========================================================Get Button=============================================
def get():
    try:
        id=e_id.get()

        if id=="":
            msg.showinfo("Alert","Id must be required")

        else:
            con=mysql.connect(host="localhost",user="root",password="",database="project")
            cursor=con.cursor()
            cursor.execute("SELECT * FROM `Criminal` WHERE Criminal_Id='"+id+"'")
            rows=cursor.fetchall()

            for row in rows:
                e_Fname.insert(0,row[1])
                e_Lname.insert(0,row[2])
                e_Age.insert(0,row[3])
                e_Cdate.insert(0,row[4])
                e_Thana.insert(0,row[5])
                e_District.insert(0,row[6])
                e_State.insert(0,row[7])
                e_Ctype.insert(0,row[8])
                panelB=None
                text_area.insert(tk.END, ''.join("Criminal_Id:-%r\n" %row[0]))
                text_area.insert(tk.END, ''.join("First_Name:-%r\n" %row[1]))
                text_area.insert(tk.END, ''.join("Last_Name:-%r\n" %row[2]))
                text_area.insert(tk.END, ''.join("Age:-%r\n" %row[3]))
                text_area.insert(tk.END, ''.join("Crime_Date:-%r\n" %row[4]))
                text_area.insert(tk.END, ''.join("Thana:-%r\n" %row[5]))
                text_area.insert(tk.END, ''.join("District:-%r\n" %row[6]))
                text_area.insert(tk.END, ''.join("State:-%r\n" %row[7]))
                text_area.insert(tk.END, ''.join("Crime_Type:-%r\n" %row[8]))
                text_area.mark_set("insert", "1.1")
                if len(row[9]) > 0:

                    image = cv2.imread(row[9])
                    image=cv2.resize(image,(400,400))
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                    image = Image.fromarray(image)


                    image = ImageTk.PhotoImage(image)

                    if panelB is None:

                        panelB = Label(image=image)

                        panelB.image = image
                        panelB.place(x=150,y=100)



                    else:
                # update the pannels
                        panelB.configure(image=image)

                        panelB.image = image


            con.close()

    except:
        msg.showinfo("Alert","There is no data in dataset according to this")
#===========================================================refresh button=======================================
def Refresh():
    e_id.delete(0,'end')
    e_Fname.delete(0,'end')
    e_Lname.delete(0,'end')
    e_Age.delete(0,'end')
    e_Cdate.delete(0,'end')
    e_Thana.delete(0,'end')
    e_District.delete(0,'end')
    e_State.delete(0,'end')
    e_Ctype.delete(0,'end')
    text_area.delete("1.0","end")
    panelA=None
    panelB=None
#============================================================Face Detect============================================
def Face_Detect():
    try:
        classify_face(Binarydata)
    except:
        msg.showinfo("Alert","Sorry!there are some mistake in face detect")

def get_encoded_faces():
    encoded = {}
    for dirpath, dnames, fnames in os.walk("image/"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("image/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding


    return encoded
def classify_face(im):

    panelC = None

    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())


    img = cv2.imread(im, 1)
    #img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    #img = img[:,:,::-1]

    face_locations = fr.face_locations(img)
    unknown_face_encodings = fr.face_encodings(img, face_locations)

    face_names = []
    for face_encoding in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = fr.compare_faces(faces_encoded, face_encoding,tolerance=0.65)
        print(matches)
        name = "Unknown"

        # use the known face with the smallest distance to the new face
        face_distances = fr.face_distance(faces_encoded, face_encoding)
        print(face_distances)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            con=mysql.connect(host="localhost",user="root",password="",database="project")
            cursor=con.cursor()
            cursor.execute("SELECT * FROM `Criminal` WHERE Criminal_Id='"+name+"'")
            rows=cursor.fetchall()
            for row in rows:
                text_area.insert(tk.END, ''.join("Criminal_Id:-%r\n" %row[0]))
                text_area.insert(tk.END, ''.join("First_Name:-%r\n" %row[1]))
                text_area.insert(tk.END, ''.join("Last_Name:-%r\n" %row[2]))
                text_area.insert(tk.END, ''.join("Age:-%r\n" %row[3]))
                text_area.insert(tk.END, ''.join("Crime_Date:-%r\n" %row[4]))
                text_area.insert(tk.END, ''.join("Thana:-%r\n" %row[5]))
                text_area.insert(tk.END, ''.join("District:-%r\n" %row[6]))
                text_area.insert(tk.END, ''.join("State:-%r\n" %row[7]))
                text_area.insert(tk.END, ''.join("Crime_Type:-%r\n" %row[8]))
                text_area.mark_set("insert", "1.1")

        face_names.append(name)

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Draw a box around the face
            cv2.rectangle(img, (left-20, top-20), (right+20, bottom+20), (255, 0, 0), 2)

            # Draw a label with a name below the face
            cv2.rectangle(img, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(img, name, (left -20, bottom + 15), font, 1.0, (255, 255, 255), 2)


    # Display the resulting image
    while True:
        img=cv2.resize(img,(400,400))
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img=ImageTk.PhotoImage(img)
        if panelC is None:
            panelC=Label(image=img)
            panelC.image=img
            panelC.place(x=150,y=100)
        else:
            panelC.configure(image=img)
            panelC.image=img

        #cv2.imshow('Video', img)
        return face_names

def video():
    path = 'image/'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = fr.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    #### FOR CAPTURING SCREEN RATHER THAN WEBCAM
    # def captureScreen(bbox=(300,300,690+300,530+300)):
    #     capScr = np.array(ImageGrab.grab(bbox))
    #     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    #     return capScr

    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    # =======================================================VIDEO=====================================

    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        #img = captureScreen()
        print(img)
        imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        facesCurFrame = fr.face_locations(imgS)
        encodesCurFrame = fr.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = fr.compare_faces(encodeListKnown, encodeFace,tolerance=0.65)
            faceDis = fr.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()

                con = mysql.connect(host="localhost", user="root", password="", database="project")
                cursor = con.cursor()
                cursor.execute("SELECT * FROM `Criminal` WHERE Criminal_Id='" + name + "'")
                rows = cursor.fetchall()
                for row in rows:
                    text_area.insert(tk.END, ''.join("Criminal_Id:-%r\n" % row[0]))
                    text_area.insert(tk.END, ''.join("First_Name:-%r\n" % row[1]))
                    text_area.insert(tk.END, ''.join("Last_Name:-%r\n" % row[2]))
                    text_area.insert(tk.END, ''.join("Age:-%r\n" % row[3]))
                    text_area.insert(tk.END, ''.join("Crime_Date:-%r\n" % row[4]))
                    text_area.insert(tk.END, ''.join("Thana:-%r\n" % row[5]))
                    text_area.insert(tk.END, ''.join("District:-%r\n" % row[6]))
                    text_area.insert(tk.END, ''.join("State:-%r\n" % row[7]))
                    text_area.insert(tk.END, ''.join("Crime_Type:-%r\n" % row[8]))
                    text_area.mark_set("insert", "1.1")

                # print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                if name != "":
                    msg.showinfo("Criminal Detector", "Criminal Detect")
        cv2.imshow('Webcam', img)
        if cv2.waitKey(1) & 0xFF == ord('j'):
            break


#===========================================================Left Frame==============================================
Title=Label(top,text="Criminal Detector System",font=('bold',16),fg='black',bg='white')
Title.place(x=535,y=10)
id=Label(right,text="Criminal Id")
id.place(x=175,y=30)
First_Name=Label(right,text="First Name")
First_Name.place(x=175,y=60)
Last_Name=Label(right,text="Last Name")
Last_Name.place(x=175,y=90)
Age=Label(right,text="Age")
Age.place(x=175,y=120)
Crime_Date=Label(right,text="Crime Date")
Crime_Date.place(x=175,y=150)
Thana=Label(right,text="Thana")
Thana.place(x=175,y=180)
District=Label(right,text="District")
District.place(x=175,y=210)
State=Label(right,text="State")
State.place(x=175,y=240)
Crime_Type=Label(right,text="Crime Type")
Crime_Type.place(x=175,y=270)
text_area=scrolledtext.ScrolledText(right,wrap=tk.WORD,width=60,height=10)
text_area.place(x=30,y=315)






e_id=Entry(right)
e_id.place(x=300,y=30)
e_Fname=Entry(right)
e_Fname.place(x=300,y=60)
e_Lname=Entry(right)
e_Lname.place(x=300,y=90)
e_Age=Spinbox(right,from_=18,to=120,width=18)
e_Age.place(x=300,y=120)
e_Cdate=DateEntry(right,dateformat=3,width=17)
e_Cdate.place(x=300,y=150)
e_Thana=Entry(right)
e_Thana.place(x=300,y=180)
e_District=Entry(right)
e_District.place(x=300,y=210)
e_State=Entry(right)
e_State.place(x=300,y=240)
e_Ctype=Entry(right)
e_Ctype.place(x=300,y=270)

insert=Button(right,text="Insert",bg='black',fg='white',command=insert)
insert.place(x=0,y=65)
delete=Button(right,text="Delete",bg='black',fg='white',command=delete)
delete.place(x=0,y=105)
update=Button(right,text="Update",bg='black',fg='white',command=update)
update.place(x=0,y=145)
get=Button(right,text="Get",bg='black',fg='white',command=get)
get.place(x=0,y=185)
Refresh=Button(right,text="Refresh",bg='black',fg='white',command=Refresh)
Refresh.place(x=0,y=225)
select1 = Button(left, text="Face Detect",bg='black',fg='white', command=Face_Detect)
select1.place(x=0,y=230)
video = Button(left, text="Live Video",bg='black',fg='white', command=video)
video.place(x=0,y=280)

#======================================================================End========================================
root.mainloop()