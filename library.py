from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox
import tkinter
import datetime
class librarymanagementsystem:
    def _init_(self,root):
        self.root=root
        self.root.title("READERS HEAVEN")


        self.membertype_var= StringVar()
        self.RollNo_var=StringVar()
        self.FirstName_var=StringVar()
        self.LastName_var=StringVar()
        self.Mobileno_var=StringVar()
        self.Booktitle_var=StringVar()
        self.Author_var=StringVar()
        self.Dateofborrowed_var=StringVar()
        self.Datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.DateofReturn_var=StringVar()

         
        lbltitle=Label(self.root,text="READERS HEAVEN",bg="light green",fg="RED",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="light green")
        frame.place(x=0,y=130,width=1530,height=400)

        
        DataFrameLeft=LabelFrame(frame,text="MEMBERSHIP INFORMATION",bg="light green",fg="RED",bd=12,relief=RIDGE,font=("times new roman",15,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember=Label( DataFrameLeft,bg="light green",text="membertype",font=("arial",20,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)
        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.membertype_var,font=("times new roman",12,"bold"),width=15,state="readonly")
        comMember["values"]=("Adminstaff","student","Lecturer")
        comMember.grid(row=0,column=1)

        

        lblTitle=Label( DataFrameLeft,bg="light green",text="RollNo", font=("arial",20,"bold"),padx=2)
        lblTitle.grid(row=1,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,textvariable=self.RollNo_var,font=("arial",12,"bold"),width=20)
        txtTitle.grid(row=1,column=1)

        lblFirstName=Label( DataFrameLeft,bg="light green",text="FirstName",font=("arial",20,"bold"),padx=2,pady=4)
        lblFirstName.grid(row=2,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.FirstName_var,width=20)
        txtFirstName.grid(row=2,column=1)

        lblLastName=Label( DataFrameLeft,bg="light green",text="LastName",font=("arial",20,"bold"),padx=2,pady=4)
        lblLastName.grid(row=3,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.LastName_var,width=20)
        txtLastName.grid(row=3,column=1)

        lblMobileno=Label( DataFrameLeft,bg="light green",text="Mobileno",font=("arial",20,"bold"),padx=2,pady=4)
        lblMobileno.grid(row=4,column=0,sticky=W)
        txtMobileno=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Mobileno_var,width=20)
        txtMobileno.grid(row=4,column=1)

        lblBooktitle=Label( DataFrameLeft,bg="light green",text="Booktitle",font=("arial",20,"bold"),padx=2,pady=4)
        lblBooktitle.grid(row=5,column=0,sticky=W)
        txtBooktitle=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Booktitle_var)
        txtBooktitle.grid(row=5,column=1)


        lblAuthor=Label( DataFrameLeft,bg="light green",text="Author",font=("arial",20,"bold"),padx=2,pady=4)
        lblAuthor.grid(row=0,column=3,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Author_var,width=20)
        txtAuthor.grid(row=0,column=4)

        lblDateofborrowed=Label( DataFrameLeft,bg="light green",text="Dateofborrowed",font=("arial",20,"bold"),padx=2,pady=4)
        lblDateofborrowed.grid(row=1,column=3,sticky=W)
        txtDateofborrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Dateofborrowed_var,width=20)
        txtDateofborrowed.grid(row=1,column=4)

        lblDatedue=Label( DataFrameLeft,bg="light green",text="Datedue",font=("arial",20,"bold"),padx=2,pady=4)
        lblDatedue.grid(row=2,column=3,sticky=W)
        txtDatedue=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Datedue_var,width=20)
        txtDatedue.grid(row=2,column=4)

        lbldaysonbook=Label( DataFrameLeft,bg="light green",text="daysonbook",font=("arial",20,"bold"),padx=2,pady=4)
        lbldaysonbook.grid(row=3,column=3,sticky=W)
        txtdaysonbook=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.daysonbook_var,width=20)
        txtdaysonbook.grid(row=3,column=4)
        
        lbllatereturnfine=Label( DataFrameLeft,bg="light green",text="latereturnfine",font=("arial",20,"bold"),padx=2,pady=4)
        lbllatereturnfine.grid(row=4,column=3,sticky=W)
        txtlatereturnfine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.latereturnfine_var,width=20)
        txtlatereturnfine.grid(row=4,column=4)
        

        lblDateofReturn=Label( DataFrameLeft,bg="light green",text="DateofReturn",font=("arial",20,"bold"),padx=2,pady=4)
        lblDateofReturn.grid(row=5,column=3,sticky=W)
        txtDateofReturn=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.DateofReturn_var,width=20)
        txtDateofReturn.grid(row=5,column=4)
        

        

        
        
        
        
        

        DataFrameRight=LabelFrame(frame,text="BOOK DETAILS",bg="light green",fg="RED",bd=12,relief=RIDGE,font=("times new roman",15,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        self.txtBox=Text(DataFrameRight,font=("arial",20,"bold"),width=22,height=10,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listbooks=['Algorithms and Data Structures','Compilers',
                 'Operating Systems','Probability and Statistics','Software Engineering','Advanced Computer Architecture','Complex Analysis',
                 'Database Management Systems','Computer Organization and Architecture','Analysis of Data Structures and Algorithms','Digital Principles and System Design','Transform Calculus',
                 'Discrete Mathematics']
        

        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if(x=="Algorithms and Data Structures"):
              
                self.Booktitle_var.set("Algorithms and Data Structures")
                self.Author_var.set("paul")


                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.Dateofborrowed_var.set(d3)
                self.Datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("RS.50")
            elif(x=="Compilers"):
              
                self.Booktitle_var.set("Compilers")
                self.Author_var.set("berry")


                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=6)
                d3=d1+d2
                self.Dateofborrowed_var.set(d3)
                self.Datedue_var.set(d3)
                self.daysonbook_var.set(6)
                self.latereturnfine_var.set("RS.40")

            elif(x=="Operating Systems"):
              
                self.Booktitle_var.set("Operating Systems")
                self.Author_var.set("andrew")


                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.Dateofborrowed_var.set(d3)
                self.Datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.latereturnfine_var.set("RS.30")

            elif(x=="Probability and Statastics"):
              
                self.Booktitle_var.set("Probability and Statastics")
                self.Author_var.set("john")


                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=11)
                d3=d1+d2
                self.Dateofborrowed_var.set(d3)
                self.Datedue_var.set(d3)
                self.daysonbook_var.set(11)
                self.latereturnfine_var.set("RS.20")
            elif(x=="Software Engineering"):
              
                self.Booktitle_var.set("Software Engineering")
                self.Author_var.set("klin")


                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=12)
                d3=d1+d2
                self.Dateofborrowed_var.set(d3)
                self.Datedue_var.set(d3)
                self.daysonbook_var.set(12)
                self.latereturnfine_var.set("RS.60")
            elif(x=="Advanced Computer Architecture"):
              
                self.Booktitle_var.set("Advanced Computer Architecture")
                self.Author_var.set("nicholas")


                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=13)
                d3=d1+d2
                self.Dateofborrowed_var.set(d3)
                self.Datedue_var.set(d3)
                self.daysonbook_var.set(13)
                self.latereturnfine_var.set("RS.45")
            elif(x=="Complex Analysis"):
              
                self.Booktitle_var.set("Complex Analysis")
                self.Author_var.set("kiran")


                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=16)
                d3=d1+d2
                self.Dateofborrowed_var.set(d3)
                self.Datedue_var.set(d3)
                self.daysonbook_var.set(16)
                self.latereturnfine_var.set("RS.35")

            elif(x=="Database Management System"):
              
                self.Booktitle_var.set("Database Management System")
                self.Author_var.set("onam")


                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.Dateofborrowed_var.set(d3)
                self.Datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("RS.50")
            elif(x=="Computer Organization and Architecture"):
              
                self.Booktitle_var.set("Computer Organization and Architecture")
                self.Author_var.set("johnson")


                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.Dateofborrowed_var.set(d3)
                self.Datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("RS.40")
            elif(x=="Analysis of Data Structures and Algorithms"):
              
                self.Booktitle_var.set("Analysis of Data Structures and Algorithms")
                self.Author_var.set("holoon")


                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=18)
                d3=d1+d2
                self.Dateofborrowed_var.set(d3)
                self.Datedue_var.set(d3)
                self.daysonbook_var.set(18)
                self.latereturnfine_var.set("RS.60")
            elif(x=="Digital Principles and System Design"):
              
                self.Booktitle_var.set("Digital Principles and System Design")
                self.Author_var.set("kinh")


                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.Dateofborrowed_var.set(d3)
                self.Datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("RS.50")
            elif(x=="Transform Calculus"):
              
                self.Booktitle_var.set("Transform Calculus")
                self.Author_var.set("king")


                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.Dateofborrowed_var.set(d3)
                self.Datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("RS.50")
            elif(x=="Discrete Mathematics"):
              
                self.Booktitle_var.set("Discrete Mathematics")
                self.Author_var.set("albert")


                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.Dateofborrowed_var.set(d3)
                self.Datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("RS.50")
                
                



        listBox=Listbox(DataFrameRight,font=("arial",18,"bold"),width=10,height=10)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listbooks:
            listBox.insert(END,item)






    

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="light green")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data",font=("arial",18,"bold"),width=16,bg="lightblue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",18,"bold"),width=17,bg="lightblue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",18,"bold"),width=16,bg="lightblue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",18,"bold"),width=17,bg="lightblue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("arial",18,"bold"),width=15,bg="lightblue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",18,"bold"),width=15,bg="lightblue",fg="white")
        btnAddData.grid(row=0,column=5)


        
        Framedetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="light green")
        Framedetails.place(x=0,y=600,width=1530,height=195)

        Table_frame=Frame(Framedetails,bd=6,relief=RIDGE,padx=20,bg="light green")
        Table_frame.place(x=0,y=2,width=1460,height=175)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        
        self.library_table=ttk.Treeview(Table_frame,column=("membertype","RollNo","FirstName","LastName","Mobileno","Booktitle","Author","Dateofborrowed","Datedue","daysonbook","latereturnfine","DateofReturn"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)



        self.library_table.heading("membertype",text="membertype")
        self.library_table.heading("RollNo",text="RollNo")
        self.library_table.heading("FirstName",text="FirstName")
        self.library_table.heading("LastName",text="LastName")
        self.library_table.heading("Mobileno",text="Mobileno")
        self.library_table.heading("Booktitle",text="BookTitle")
        self.library_table.heading("Author",text="Author")
        self.library_table.heading("Dateofborrowed",text="Dateofborrowed")
        self.library_table.heading("Datedue",text="Datedue")
        self.library_table.heading("daysonbook",text="daysonbook")
        self.library_table.heading("latereturnfine",text="latereturnfine")
        self.library_table.heading("DateofReturn",text="DateofReturn")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)


        self.library_table.column("membertype",width=100)
        self.library_table.column("RollNo",width=100)
        self.library_table.column("FirstName",width=100)
        self.library_table.column("LastName",width=100)
        self.library_table.column("Mobileno",width=100)
        self.library_table.column("Booktitle",width=100)
        self.library_table.column("Author",width=100)
        self.library_table.column("Dateofborrowed",width=100)
        self.library_table.column("Datedue",width=100)
        self.library_table.column("daysonbook",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("DateofReturn",width=100)
        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
 
    
    def adda_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="1234",database="harshitha")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                              self.membertype_var.get(),
                                                                                              self.RollNo_var.get(),
                                                                                              self.FirstName_var.get(),
                                                                                              self.LastName_var.get(),
                                                                                              self.Mobileno_var.get(),
                                                                                              self.Booktitle_var.get(),
                                                                                              self.Author_var.get(),
                                                                                              self.Dateofborrowed_var.get(),
                                                                                              self.Datedue_var.get(),
                                                                                              self.daysonbook_var.get(),
                                                                                              self.latereturnfine_var.get(),
                                                                                              self.DateofReturn_var.get()))

        conn.commit()
        self.fatch_data()
        conn.close()
        
        messagebox.showinfo("Succeess","Member has been inserted successfully")



    def update(self):
        conn=pymysql.connect(host="localhost",user="root",password="1234",database="harshitha")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set membertype=%s,FirstName=%s,LastName=%s,Mobileno=%s,Booktitle=%s,Author=%s,Dateofborrowed=%s,Datedue=%s,daysonbook=%s,latereturnfine=%s,DateofReturn=%s where RollNo=%s",(
                                                                                              self.membertype_var.get(),
                                                                                              self.FirstName_var.get(),
                                                                                              self.LastName_var.get(),
                                                                                              self.Mobileno_var.get(),
                                                                                              self.Booktitle_var.get(),
                                                                                              self.Author_var.get(),
                                                                                              self.Dateofborrowed_var.get(),
                                                                                              self.Datedue_var.get(),
                                                                                              self.daysonbook_var.get(),
                                                                                              self.latereturnfine_var.get(),
                                                                                              self.DateofReturn_var.get(),
                                                                                              self.RollNo_var.get(),
                                                                                                                     ))
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("success","memeber has been updated")







    def fatch_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="1234",database="harshitha")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if rows!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content["values"]

        self.membertype_var.set(row[0]),
        self.RollNo_var.set(row[1]),
        self.FirstName_var.set(row[2]),
        self.LastName_var.set(row[3]),
        self.Mobileno_var.set.row([4]),
        self.Booktitle_var.set.row([5]),
        self.Author_var.set.row([6]),
        self.Dateofborrowed_var.set.row([7]),
        self.Datedue_var.set.row([8]),
        self.daysonbook_var.set.row([9]),
        self.latereturnfine_var.set.row([10]),
        self.DateofReturn_var.set.row([11])


    def showData(self):
        self.txtBox.insert(END,"membertype:\t "+ self.membertype_var.get()+"\n")
        self.txtBox.insert(END,"Rollno:\t "+ self.RollNo_var.get()+"\n")
        self.txtBox.insert(END,"FirstName:\t "+ self.FirstName_var.get()+"\n")
        self.txtBox.insert(END,"LastName:\t "+ self.LastName_var.get()+"\n")
        self.txtBox.insert(END,"Mobileno:\t "+ self.Mobileno_var.get()+"\n")
        self.txtBox.insert(END,"Boktitle:\t "+ self.Booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Author:\t "+ self.Author_var.get()+"\n")
        self.txtBox.insert(END,"Dateofborrowed:\t "+ self.Dateofborrowed_var.get()+"\n")
        self.txtBox.insert(END,"Datedue:\t "+ self.Datedue_var.get()+"\n")
        self.txtBox.insert(END,"daysonbook:\t "+ self.daysonbook_var.get()+"\n")
        self.txtBox.insert(END,"latereuturnfine:\t "+ self.latereturnfine_var.get()+"\n")
        self.txtBox.insert(END,"DateofReturn:\t "+ self.DateofReturn_var.get()+"\n")


    def reset(self):
        self.membertype_var.set(""),
        self.RollNo_var.set(""),
        self.FirstName_var.set(""),
        self.LastName_var.set(""),
        self.Mobileno_var.set(""),
        self.Booktitle_var.set(""),
        self.Author_var.set(""),
        self.Dateofborrowed_var.set(""),
        self.Datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.DateofReturn_var.set("")
        self.txtBox.delete("1.0",END)


    def iExit(self):
        iExit=tkinter.messagebox.askyesno("LIBRARY MANAGEMENT SYSTEM","Do you want to exit" )
        if iExit>0:
            self.root.destroy()
            return
        


    def delete(self):
        if self.RollNo_var.get()=="" or self.membertype_var.get()=="":
            messagebox.showerror("error","first select the member")
        else:
               conn=pymysql.connect(host="localhost",user="root",password="1234",database="harshitha")
               my_cursor=conn.cursor()
               query="delete from library where RollNo=%s"
               value=(self.RollNo_var.get(),)
               my_cursor.execute(query,value)

               conn.commit()
               self.fatch_data()
               self.reset()
               conn.close()

               messagebox.showinfo("Success","Member has been deleted")
 

if _name== "main_":
    root=Tk()
    obj=librarymanagementsystem(root)
    root.mainloop()