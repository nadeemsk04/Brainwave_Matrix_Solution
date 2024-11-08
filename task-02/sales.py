from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from tkinter import messagebox
import sqlite3
import os



class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+300+200")
        self.root.title("INVENTORY MANAGEMENT SYSTEM! Developed by Nadeem")
        self.root.config(bg="white")
        self.root.focus_force()

        self.bill_list=[]
        self.var_invoice=StringVar()

        # ------ Title -------
        lbl_title = Label(self.root, text="Views Customer Bills", font=("goudy old style", 30), bg="Green", fg="white", bd=4, relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=20)

        lbl_invoice = Label(self.root, text="Invoice No.", font=("times new roman", 15), bg="white").place(x=50, y=100)
        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("goudy old style", 18), bg="lightblue").place(x=160, y=100, width=180, height=28)
        

        btn_sercch=Button(self.root, text="Search", command=self.search, font=("times neew roman", 15, "bold"), bg="#2196f3", fg="white", activebackground="#2196f3", activeforeground="white", cursor="hand2").place(x=360, y=100, width=120, height=28)
        btn_clear=Button(self.root, text="Clear", command=self.clear, font=("times neew roman", 15, "bold"), bg="#607d8b", fg="white", activebackground="#607d8b", activeforeground="white",cursor="hand2").place(x=490, y=100, width=120, height=28)


        # ------- Sales Frame ------
        sales_frame=Frame(self.root, bd=4, relief=RIDGE)
        sales_frame.place(x=50, y=140, width=200, height=330)

        scrolly=Scrollbar(sales_frame, orient="vertical")

        self.sales_list=Listbox(sales_frame, font=("goudy old style", 15), bg="white", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.sales_list.yview)

        self.sales_list.pack(fill=BOTH, expand=1)
        self.sales_list.bind("<ButtonRelease-1>", self.get_data)


        # ------- Bill Area ------
        bill_frame=Frame(self.root, bd=4, relief=RIDGE)
        bill_frame.place(x=280, y=140, width=410, height=330)

        lbl_title = Label(bill_frame, text="Customer Bills Area", font=("goudy old style", 20), bg="#D5F5E3").pack(side=TOP, fill=X)


        scrolly2=Scrollbar(bill_frame, orient="vertical")

        self.bill_area=Text(bill_frame, bg="lightblue", yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH, expand=1)



        # ------- Image ------
        self.billPhoto = Image.open("images/cat2.jpg")
        self.billPhoto = self.billPhoto.resize((450, 300), Image.LANCZOS)
        self.billPhoto = ImageTk.PhotoImage(self.billPhoto)

        lbl_image=Label(self.root, image=self.billPhoto,bd=0, bg="white")
        lbl_image.place(x=700, y=110)


        self.show()


    # ----------------------------------------------------------------------
    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0,END)
        for i in os.listdir("bill"):
            if i.split(".")[-1]=="txt":
                self.sales_list.insert(END,i)
                self.bill_list.append(i.split(".")[0])




    def get_data(self,ev):
        index_=self.sales_list.curselection()
        file_name=self.sales_list.get(index_)

        self.bill_area.delete("1.0", END)

        fp=open(f"bill/{file_name}", "r")
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()
    


    def search(self):
        if self.var_invoice.get() == "":
            messagebox.showerror("Error", "Invoice No. Should be required", parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f"bill/{self.var_invoice.get()}.txt", "r")
                self.bill_area.delete("1.0",END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()

            else:
                messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)



    def clear(self):
        self.show()
        self.bill_area.delete("1.0",END)





if __name__=="__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()
