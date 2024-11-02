from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from tkinter import messagebox
import sqlite3


class productClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+300+200")
        self.root.title("INVENTORY MANAGEMENT SYSTEM! Developed by Nadeem")
        self.root.config(bg="white")
        self.root.focus_force()


         # -----------------------------------------------------
        # ------- All variables --------
        self.var_search_by=StringVar()
        self.var_search_text=StringVar()
        
        self.var_product_id=StringVar()
        self.var_product_category=StringVar()
        self.cat_list=[]
        self.fetch_category()
        self.var_product_name=StringVar()
        self.var_product_quantity=StringVar()
        self.var_product_price=StringVar()
        self.var_product_status=StringVar()

    

        # ------ Search Frame -----
        searchFrame=LabelFrame(self.root, text="Search Products", font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        searchFrame.place(x=250,y=0,width=600,height=70)


        # ----- Options ------
        cmb_search=ttk.Combobox(searchFrame,textvariable=self.var_search_by,values=("Select", "product_name", "product_category","product_price"), state="readonly", justify=CENTER, font=("goudy old style",12))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(searchFrame,textvariable=self.var_search_text,font=("goudy old style",15),bg="lightyellow").place(x=200, y=10)
        btn_search=Button(searchFrame,text="Search", command=self.search, font=("goudy old style",15),bg="#4caf50", fg="white", cursor="hand2").place(x=430, y=8,width=150, height=30)
        


        # ------ Title -----
        title=Label(self.root, text="Products Details", bd=4, relief=RIDGE, font=("goudy old style",15), bg="Green", fg="white").place(x=50, y=100, width=1000)


        # ------- Conatent ------
        # -------Category-------
        lbl_productCategory=Label(self.root, text="Category", font=("goudy old style",10), bg="white").place(x=30, y=150)
        cmb_category=ttk.Combobox(self.root,textvariable=self.var_product_category,values=self.cat_list, state="readonly", justify=CENTER, font=("goudy old style",12))
        cmb_category.place(x=140,y=150,width=180)
        cmb_category.current(0)

        # -------Name-------
        lbl_productname=Label(self.root, text="Name", font=("goudy old style",10), bg="white").place(x=30, y=190)
        txt_productname=Entry(self.root, textvariable=self.var_product_name, font=("goudy old style",13), bg="lightblue").place(x=140, y=190, width=180)

        # -------Quantity-------
        lbl_productquantity=Label(self.root, text="Quantity", font=("goudy old style",10), bg="white").place(x=30, y=230)
        txt_productquantity=Entry(self.root, textvariable=self.var_product_quantity, font=("goudy old style",13), bg="lightblue").place(x=140, y=230, width=180)

        # -------Price-------
        lbl_productPrice=Label(self.root, text="Price", font=("goudy old style",10), bg="white").place(x=30, y=280)
        txt_productPrice=Entry(self.root, textvariable=self.var_product_price, font=("goudy old style",13), bg="lightblue").place(x=140, y=280, width=180)

        # -------Status-------
        lbl_productStatus=Label(self.root, text="Status", font=("goudy old style",10), bg="white").place(x=30, y=320)
        cmb_status=ttk.Combobox(self.root,textvariable=self.var_product_status,values=("Active","Inactive"), state="readonly", justify=CENTER, font=("goudy old style",12))
        cmb_status.place(x=140,y=320,width=180)
        cmb_status.current(0)    

        # ------- Buttons -------
        btn_add = Button(self.root, text="ADD", command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="white", activebackground="#2196f3", activeforeground="white", cursor="hand2").place(x=30, y=450, width=110, height=30)
        btn_Edit = Button(self.root, text="Edit", command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white", activebackground="#4caf50", activeforeground="white", cursor="hand2").place(x=150, y=450, width=110, height=30)
        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white", activebackground="#f44336", activeforeground="white", cursor="hand2").place(x=270, y=450, width=110, height=30)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white", activebackground="#607d8b", activeforeground="white", cursor="hand2").place(x=390, y=450, width=110, height=30)



        # ------ Product Details -------
        # ------- Create a style for the Treeview -------
        style = ttk.Style()
        style.configure("Treeview.Heading",
                        background="lightblue",
                        foreground="black",
                        font=("goudy old style", 10, "bold"),
                        relief="solid",       # Set relief to solid to create the border effect
                        borderwidth=1)
        

        product_frame=Frame(self.root,bd=3, relief=RIDGE)
        product_frame.place(x=340, y=150, width=700, height=255)

        scrolly=Scrollbar(product_frame,orient=VERTICAL)
        scrollx=Scrollbar(product_frame,orient=HORIZONTAL)

        self.productTable=ttk.Treeview(product_frame,columns=("product_id","product_category", "product_name", "product_quantity", "product_price", "product_status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)


        self.productTable.heading("product_id", text="Product ID")
        self.productTable.heading("product_category", text="Category")
        self.productTable.heading("product_name", text="Name")
        self.productTable.heading("product_quantity", text="Quantity")
        self.productTable.heading("product_price", text="Price")
        self.productTable.heading("product_status", text="Status")


        self.productTable["show"]="headings"

        self.productTable.column("product_id", width=100)
        self.productTable.column("product_category", width=100)
        self.productTable.column("product_name", width=100)
        self.productTable.column("product_quantity", width=100)
        self.productTable.column("product_price", width=100)
        self.productTable.column("product_status", width=100)


        self.productTable.pack(fill=BOTH, expand=1)
        self.productTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()


   
# -----------------------------------------------------------------------
    def fetch_category(self):
        con = sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
            c.execute("Select category_name from category")
            cat=c.fetchall()

            self.cat_list.append("Empty")
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

        
        except Exception as ex:
            messagebox.showerror("Error:", f"Error due to {str(ex)}", parent=self.root)

    
    
    
    def add(self):
        con = sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
            if self.var_product_category.get() == "Select" or self.var_product_category.get() == "Empty" or self.var_product_name.get() == "Select" or self.var_product_quantity.get() == "Select" or self.var_product_price.get() == "Select" or self.var_product_status.get() == "Select":
                messagebox.showerror("Error", "All Field Are Required", parent=self.root)
            else:
                c.execute("Select * from product where product_name=?", (self.var_product_name.get(),))
                row = c.fetchone()

                if row is not None:
                    messagebox.showerror("Error", "This Product Is Already Present, TRY Diffrenet", parent=self.root)
                else:
                    c.execute("Insert into product (product_category, product_name, product_quantity, product_price, product_status) values(?, ?, ?, ?, ?)", (
                        self.var_product_category.get(),
                        self.var_product_name.get(),
                        self.var_product_quantity.get(),
                        self.var_product_price.get(),
                        self.var_product_status.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Product Added Successfully", parent=self.root)

                    self.show()

        except Exception as ex:
            messagebox.showerror("Error:", f"Error due to {str(ex)}", parent=self.root)




    def show(self):
        con=sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
            c.execute("Select * from product")
            rows=c.fetchall()
            self.productTable.delete(*self.productTable.get_children())

            for row in rows:
                self.productTable.insert("", END, values=row)
            


        except Exception as ex:
            messagebox.showerror("Error:", f"Error due to {str(ex)}", parent=self.root)



    def get_data(self, ev):
        f = self.productTable.focus()
        content = self.productTable.item(f)
        row = content["values"]

        self.var_product_id.set(row[0])
        self.var_product_category.set(row[1])
        self.var_product_name.set(row[2])
        self.var_product_quantity.set(row[3])
        self.var_product_price.set(row[4])
        self.var_product_status.set(row[5])



    def update(self):
        con = sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
            if self.var_product_id.get() == "":
                messagebox.showerror("Error", "Please Select Product From List", parent=self.root)
            else:
                c.execute("Select * from product where product_id=?", (self.var_product_id.get(),))
                row = c.fetchone()

                if row == None:
                    messagebox.showerror("Error", " Invalid Product.", parent=self.root)
                else:
                    c.execute("Update product set product_category=?, product_name=?, product_quantity=?, product_price=?, product_status=? where product_id=?", (
                        self.var_product_category.get(),
                        self.var_product_name.get(),
                        self.var_product_quantity.get(),
                        self.var_product_price.get(),
                        self.var_product_status.get(),
                        self.var_product_id.get(),  

                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Product Edited Successfully", parent=self.root)

                    self.show()

        except Exception as ex:
            messagebox.showerror("Error:", f"Error due to {str(ex)}", parent=self.root)





    def delete(self):
        con = sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
            if self.var_product_id.get() == "":
                messagebox.showerror("Error", "Please Select Product  From List", parent=self.root)
            else:
                c.execute("Select * from product where product_id=?", (self.var_product_id.get(),))
                row = c.fetchone()

                if row == None:
                    messagebox.showerror("Error", " Invalid Product.", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you want to delete this Product?", parent=self.root)
                    if op == True:

                        c.execute("delete from product where product_id=?",(self.var_product_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Product Deleted Successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)



    def clear(self):
        self.var_product_id.set(""),
        self.var_product_name.set(""),
        self.var_product_quantity.set(""),
        self.var_product_category.set("Select"),
        self.var_product_price.set(""),
        self.var_product_status.set("Active"),

        self.var_search_by.set("Select")
        self.var_search_text.set("")

        self.show()



    def search(self):
        con = sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
        # Check if search option and input text are provided
            if self.var_search_by.get() == "Select":
                messagebox.showerror("Error", "Select Search By Option", parent=self.root)
            elif self.var_search_text.get() == "":
                messagebox.showerror("Error", "Search Input Should Be Required.", parent=self.root)
            else:
            # Build query with column name
                query = f"SELECT * FROM product WHERE {self.var_search_by.get().replace(' ', '_').lower()} LIKE ?"
                c.execute(query, (f"%{self.var_search_text.get()}%",))
                rows = c.fetchall()  # This must be indented to be part of the try block
            
            # Display results or show error if no records found
                if rows:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "No Record Found.", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error:", f"Error due to {str(ex)}", parent=self.root)








if __name__=="__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()




