# -*- coding: utf-8 -*-
"""
Created on Thu May 20 08:02:48 2021

@author: User
"""

from tkinter import *
import tkinter.messagebox
import mysql.connector

#FE UI class

class Book:
    def __init__ (self,root):
       
        #create object reference
        b = Database()
        b.conn()
       
        
        self.root = root
        self.root.title("BookStore")
        self.root.geometry("1500x1000")
        self.root.config(bg="LightBlue1")
       
        bId = StringVar()
        bName=StringVar()
        bPrice=StringVar()
        bYear=StringVar()
        bPublisher=StringVar()
        bAuthor=StringVar()
        bQuantity=StringVar()
        
        def close():
            print("Book : close method called")
            close = tkinter.messagebox.askyesno("BOOKS \
              SALES PURCHARSE MANAGEMENT SYSTEM","Do you want to close the system")
            if close >0:
                  root.destroy()
                  print("Book : close method finished\n")
                  return
        def clear():
           print("Book : clear method called")
           self.txtbID.delete(0,END)
           self.txtbName.delete(0,END)
           self.txtbPrice.delete(0,END)
           self.txtbYear.delete(0,END)
           self.txtbPublisher.delete(0,END)
           self.txtbAuthor.delete(0,END)
           self.txtbQuantity.delete(0,END)
           print("Book : clear method finished\n")
           
        def insert():
             print("Product : insert method call")
             if (len(bId.get()) !=0):
                 b.insert(bId.get(),bName.get(),bPrice.get(),bYear.get(),bPublisher.get(),bAuthor.get(),bQuantity.get())
                 bookList.delete(0,END)
                 bookList.insert(END,bId.get(),bName.get(),bPrice.get(),bYear.get(),bPublisher.get(),bAuthor.get(),bQuantity.get())
                 showInBookList()
             else:
                 tkinter.messagebox.askyesno("BOOKS \
              SALES PURCHARSE MANAGEMENT SYSTEM","Enter the Book Id")
                 print("Book : insert method finished\n")
          
        def showInBookList():
              print("Book : showInBookList method called")
              bookList.delete(0,END)
              for row in b.show():
                  bookList.insert(END,row,str(""))
              print("Book : bookList method finished\n")    
       
              #add data to bar
        def bookRec(event):
           print("Book : bookRec method called")
           global bk
           
           searchBk = bookList.curselection()[0]
           bk = bookList.get(searchBk)
           
           self.txtbID.delete(0,END)
           self.txtbID.insert(END,bk[0])
                
           self.txtbName.delete(0,END)
           self.txtbName.insert(END,bk[1])
           
           self.txtbPrice.delete(0,END)
           self.txtbPrice.insert(END,bk[2])
           
           self.txtbYear.delete(0,END)
           self.txtbYear.insert(END,bk[3])
           
           self.txtbPublisher.delete(0,END)
           self.txtbPublisher.insert(END,bk[4])
           
           self.txtbAuthor.delete(0,END)
           self.txtbAuthor.insert(END,bk[5])
           
           self.txtbQuantity.delete(0,END)
           self.txtbQuantity.insert(END,bk[6])
           
           print('Book : book Rec method called')
              
        #function to delete the data record form database table
        def delete():
             print("Book : delete method called")
             if (len(bId.get())!=0):
                 b.delete(bk[0])   
                 clear()
                 showInBookList()
             print("Book : delete method finished\n")   
            
             
        '''Create the frame'''
        
        
        MainFrame = Frame(self.root,bg="white")
        MainFrame.grid()
        
        HeadFrame =Frame(MainFrame, bd=1, padx=50,pady=10,bg='green',relief=RIDGE)
        HeadFrame.pack(side=TOP)
        
        self.ITitle = Label(HeadFrame, font=('arial',50,'bold'),fg='black',text='      BookStore Management System      ',bg='white')
        self.ITitle.grid()
        
        OperationFrame = Frame(MainFrame,bd=2,width=1400,height=70,padx=50,pady=20,bg='white',relief=RIDGE)
        OperationFrame.pack(side=BOTTOM)
        
        BodyFrame = Frame(MainFrame,bd=2,width=1300,height=500,padx=50,pady=20,bg='yellow',relief=RIDGE)
        BodyFrame.pack(side=BOTTOM)
        LeftBodyFrame = LabelFrame(BodyFrame, bd=2,width=500,height=380,padx=20,pady=10,bg='yellow',relief=RIDGE, font=('arial',15,'bold'),
                              text='Book Details:')
        LeftBodyFrame.pack(side=LEFT)
        RightBodyFrame = LabelFrame(BodyFrame, bd=2,width=600,height=380,padx=20,pady=10,bg='yellow',relief=RIDGE, font=('arial',15,'bold'),
                              text='Book Information:')
        RightBodyFrame.pack(side=RIGHT)
         
        
        self.labelbID=Label(LeftBodyFrame, font=('arial',15,'bold'), text="Book ID",padx=2, bg='white',fg='blue')
        self.labelbID.grid(row=0,column=0,sticky=W)
        self.txtbID = Entry(LeftBodyFrame, font=('arial',20,'bold'),textvariable=bId,width=30)
        self.txtbID.grid(row=0,column=1,sticky=W)
        
        self.labelbName=Label(LeftBodyFrame, font=('arial',15,'bold'), text="Book Name",padx=2, bg='white',fg='blue')
        self.labelbName.grid(row=1,column=0,sticky=W)
        self.txtbName = Entry(LeftBodyFrame, font=('arial',20,'bold'),textvariable=bName,width=30)
        self.txtbName.grid(row=1,column=1,sticky=W)
        
        self.labelbPrice=Label(LeftBodyFrame, font=('arial',15,'bold'), text="Price",padx=2, bg='white',fg='blue')
        self.labelbPrice.grid(row=2,column=0,sticky=W)
        self.txtbPrice = Entry(LeftBodyFrame, font=('arial',20,'bold'),textvariable=bPrice,width=30)
        self.txtbPrice.grid(row=2,column=1,sticky=W)
        
        self.labelbYear=Label(LeftBodyFrame, font=('arial',15,'bold'), text="Year",padx=2, bg='white',fg='blue')
        self.labelbYear.grid(row=3,column=0,sticky=W)
        self.txtbYear = Entry(LeftBodyFrame, font=('arial',20,'bold'),textvariable=bYear,width=30)
        self.txtbYear.grid(row=3,column=1,sticky=W)
        
        self.labelbPublisher=Label(LeftBodyFrame, font=('arial',15,'bold'), text="Publisher",padx=2, bg='white',fg='blue')
        self.labelbPublisher.grid(row=4,column=0,sticky=W)
        self.txtbPublisher = Entry(LeftBodyFrame, font=('arial',20,'bold'),textvariable=bPublisher,width=30)
        self.txtbPublisher.grid(row=4,column=1,sticky=W)
        
        self.labelbAuthor=Label(LeftBodyFrame, font=('arial',15,'bold'), text="Author",padx=2, bg='white',fg='blue')
        self.labelbAuthor.grid(row=5,column=0,sticky=W)
        self.txtbAuthor = Entry(LeftBodyFrame, font=('arial',20,'bold'),textvariable=bAuthor,width=30)
        self.txtbAuthor.grid(row=5,column=1,sticky=W)
        
        self.labelbQuantity=Label(LeftBodyFrame, font=('arial',15,'bold'), text="Quantity",padx=2, bg='white',fg='blue')
        self.labelbQuantity.grid(row=6,column=0,sticky=W)
        self.txtbQuantity = Entry(LeftBodyFrame, font=('arial',20,'bold'),textvariable=bQuantity,width=30)
        self.txtbQuantity.grid(row=6,column=1,sticky=W)
        
        self.labelC1=Label(LeftBodyFrame,padx=2,pady=2)
        self.labelC1.grid(row=6,column=0,sticky=W)
        
        self.labelbC2=Label(LeftBodyFrame,padx=2,pady=2)
        self.labelbC2.grid(row=6,column=0,sticky=W)
        
        self.labelbC3=Label(LeftBodyFrame,padx=2,pady=2)
        self.labelbC3.grid(row=6,column=0,sticky=W)
        
        self.labelbC4=Label(LeftBodyFrame,padx=2,pady=2)
        self.labelbC4.grid(row=6,column=0,sticky=W)
        
        ''' Scroll bar '''
        scroll = Scrollbar(RightBodyFrame)
        scroll.grid(row=0, column = 1 ,sticky='ns')
        
        bookList=Listbox(RightBodyFrame,width=40,height=16,font=('arial',12,'bold'),
                yscrollcommand=scroll.set)
        #called above created bookRec function of init
        bookList.bind('<<ListboxSelect>>',bookRec)
        bookList.grid(row=0,column=0,padx=8)
        scroll.config(command=bookList.yview)
        
        ''' Add the button into operation Frame'''
        self.buttonSave = Button(OperationFrame,text='Save',font=('arial',15,'bold'),height=2,width=10,bd=5,command=insert)
        self.buttonSave.grid(row=0,column=0)
        
        self.buttonList = Button(OperationFrame,text='List all',font=('arial',15,'bold'),height=2,width=10,bd=5,command=showInBookList)
        self.buttonList.grid(row=0,column=1)
        
        self.buttonClear = Button(OperationFrame,text='Clear',font=('arial',15,'bold'),height=2,width=10,bd=5,command=clear)
        self.buttonClear.grid(row=0,column=2)
        
        self.buttonDelete = Button(OperationFrame,text='Delete',font=('arial',15,'bold'),height=2,width=10,bd=5,command=delete)
        self.buttonDelete.grid(row=0,column=3)
        
        self.buttonUpdate = Button(OperationFrame,text='Update',font=('arial',15,'bold'),height=2,width=10,bd=5)
        self.buttonUpdate.grid(row=0,column=4)
        
        self.buttonSearch = Button(OperationFrame,text='Search',font=('arial',15,'bold'),height=2,width=10,bd=5)
        self.buttonSearch.grid(row=0,column=5)
        
        self.buttonClose = Button(OperationFrame,text='Close',font=('arial',15,'bold'),height=2,width=10,bd=5,command=close)
        self.buttonClose.grid(row=0,column=6)
        
        
   #Back End Database operations
   
      

class Database:
  def conn(self):
     print("Database : connection method called")
     db = mysql.connector.connect(host="localhost", user="root", password="", database="book")
     cur = db.cursor()
     query = "create table if not exists book(bid integer primary key,bname text,price text,year text,publisher text ,author text, quantity text)"
     cur.execute(query)
     db.commit()
     db.close()
     print("Database : connection method finished\n")
  def insert(self,bid,name,price,year,publisher,author,quantity):
          print("Database : insert method called")
          db = mysql.connector.connect(host="localhost", user="root", password="", database="book")
          cur = db.cursor()
          query=("INSERT INTO book" " (bid,name,price,year,publisher,author,quantity)" " VALUES (%s, %s, %s, %s, %s, %s, %s)") 
          cur.execute(query,(bid,name,price,year,publisher,author,quantity))
          db.commit()
          db.close()
          print("Database : insert method finished")
     
  def show(self):
      print("Database : show method called")
      db = mysql.connector.connect(host="localhost", user="root", password="", database="book")
      cur = db.cursor()
      query="select * from book"
      cur.execute(query)
      rows=cur.fetchall()
      db.close()
      print("Database : show method finished\n")
      return rows
  def delete(self,bid):
      print("Database : delete method called")
      db = mysql.connector.connect(host="localhost", user="root", password="", database="book")
      cur = db.cursor()
      cur.execute("DELETE FROM book WHERE bId = %s ",(bid,))
      db.commit()
      db.close()
      print(bid,"Database : delete method finished\n")
  def search(self,bid="",name="",price="",year="",publisher="",author="",quantity=""):
      print("Database search method called\n",bid)
      db = mysql.connector.connect(host="localhost", user="root", password="", database="book")
      cur = db.cursor()
      cur.execute("select * from book where bid=? or bname=? or \
                  price=? or year=? or publisher=? or author=? or quantity=?")
      row=cur.fetchall()
      db.close()
      print("Database : search method finished\n")
      return row
  
  def update(self,bid="",name="",price="",year="",publisher="",author="",quantity=""):
      print("Database update method called\n",bid)
      db = mysql.connector.connect(host="localhost", user="root", password="", database="book")
      cur = db.cursor()
      cur.execute("update book set bid=? or bname=? or \
                  price=? or year=? or publisher=? or author=? or quantity=? where bid=?",(bid,name,price,year,publisher,author,quantity))
      db.commit()
      db.close()            
      print(bid,"Database : update method finished\n")
    

      
         

             
      
if __name__=='__main__':
    root=Tk()
    application = Book(root)
    root.mainloop()
        
        
        
