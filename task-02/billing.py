from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import time
import os
import tempfile




class billingClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+70+50")
        self.root.title("INVENTORY MANAGEMENT SYSTEM! Developed by Nadeem")
        self.root.config(bg="#E9ECEF")


        self.cart_list=[]
        self.chk_print=0

        # ------- Title -------
        self.icon_title = PhotoImage(file="images\\logo1.png")
        title = Label(self.root, text="INVENTORY MANAGEMENT SYSTEM", image=self.icon_title, compound=LEFT, font=("times new roman", 40, "bold"), bg="green", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        # ------ Logout Button ------
        btn_logout = Button(self.root, text="Logout", command=self.logout, font=("times new roman", 15, "bold"), bg="yellow", activebackground="yellow", bd=3, relief=RIDGE, cursor="hand2").place(x=1200, y=10, height=50, width=120)

        # ------ Clock -------
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System \t\t Date: DD-MM-YYYY \t\t Time:HH:MM:SS", font=("times new roman", 15), bg="gray", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)



        # ------- Product Frame - Main ------
        product_frame1=Frame(self.root, bd=4, relief=RIDGE, bg="white")
        product_frame1.place(x=6, y=110, width=410, height=550)


        product_title=Label(product_frame1, text="All Products", font=("times new roman", 20, "bold"), bg="#262626", fg="white").pack(side=TOP, fill=X)


        # ------- Search Frame in Product Frame  -------
        self.var_search=StringVar()

        product_frame2=Frame(product_frame1, bd=4, relief=RIDGE, bg="white")
        product_frame2.place(x=2, y=42, width=398, height=90)

        lbl_search=Label(product_frame2, text="Search By Product Name", font=("times ner roman", 15, "bold"), bg="white", fg="green").place(x=2, y=5)
        lbl_name=Label(product_frame2, text="Product Name", font=("times ner roman", 15, "bold"), bg="white").place(x=2, y=45)

        txt_search=Entry(product_frame2,textvariable=self.var_search, font=("times ner roman", 15), bg="lightblue").place(x=142, y=50, width=150, height=22)
        btn_search=Button(product_frame2, text="Search", command=self.search, font=("old giudy style", 14), bg="#28A745", fg="white", activebackground="#28A745", activeforeground="white", bd=3, relief=RIDGE, cursor="hand2").place(x=296, y=48,width=90, height=26)
        btn_show_all=Button(product_frame2, text="Show ALL", command=self.show, font=("old giudy style", 13), bg="#083531", fg="white", activebackground="#083531", activeforeground="white", bd=3, relief=RIDGE, cursor="hand2").place(x=296, y=10,width=90, height=26)



        # ------- Product Details Frame in Product Frame ------
        product_frame3=Frame(product_frame1,bd=4, relief=RIDGE)
        product_frame3.place(x=2, y=134, width=398, height=380)

        scrolly=Scrollbar(product_frame3,orient=VERTICAL, bg="gray", bd=4, relief=RIDGE)
        scrollx=Scrollbar(product_frame3,orient=HORIZONTAL, bg="gray", bd=4, relief=RIDGE)

        self.productTable=ttk.Treeview(product_frame3,columns=("product_id", "product_name", "product_price", "product_quantity", "product_status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)


        self.productTable.heading("product_id",text="Product ID")
        self.productTable.heading("product_name",text="Name")
        self.productTable.heading("product_price",text="Price")
        self.productTable.heading("product_quantity",text="Quantity")
        self.productTable.heading("product_status",text="Status")

        self.productTable["show"]="headings"

        self.productTable.column("product_id", width=72)
        self.productTable.column("product_name", width=75)
        self.productTable.column("product_price", width=75)
        self.productTable.column("product_quantity", width=75)
        self.productTable.column("product_status", width=75)
        
        self.productTable.pack(fill=BOTH, expand=1)
        self.productTable.bind("<ButtonRelease-1>", self.get_data)

        lbl_note=Label(product_frame1, text="Note: 'Enter Quantity to Remove the Product from Cart'", font=("times new roman", 13), anchor="w", bg="white", fg="red").pack(side=BOTTOM, padx=0, pady=2)



        # ------ Customer Deatils Frame ------
        self.var_customer_name=StringVar()
        self.var_customer_contact=StringVar()


        customer_frame=Frame(self.root, bd=4, relief=RIDGE, bg="white")
        customer_frame.place(x=420, y=110, width=530, height=70)


        customer_title=Label(customer_frame, text="Customer Details", font=("times new roman", 15), bg="lightgray").pack(side=TOP, fill=X)
        
        lbl_customer_name=Label(customer_frame, text="Name", font=("times ner roman", 15), bg="white").place(x=5, y=30)
        txt_customer_name=Entry(customer_frame,textvariable=self.var_customer_name, font=("times ner roman", 13), bg="lightblue").place(x=63, y=34, width=170)

        
        lbl_customer_contact=Label(customer_frame, text="Contact No.", font=("times ner roman", 15), bg="white").place(x=252, y=30)
        txt_customer_contact=Entry(customer_frame,textvariable=self.var_customer_contact, font=("times ner roman", 13), bg="lightblue").place(x=360, y=34, width=160)



        # ------- Claculator And Cart Frame ------
        cal_cart_frame=Frame(self.root, bd=3, relief=RIDGE, bg="white")
        cal_cart_frame.place(x=420, y=190, width=530, height=360)



        # ------ Calclulator Frame ------
        self.var_calculator_input=StringVar()
        calculator_frame=Frame(cal_cart_frame, bd=9, relief=RIDGE, bg="white")
        calculator_frame.place(x=5, y=10, width=268, height=340)


        txt_cal_input=Entry(calculator_frame, textvariable=self.var_calculator_input, font=("arial", 15, "bold"), width=22, bd=10, relief=GROOVE, state="readonly", justify=RIGHT)
        txt_cal_input.grid(row=0, columnspan=4)


        btn_7=Button(calculator_frame,text="7", font=("arial", 15, "bold"), command=lambda:self.get_input(7), bd=5, width=4, pady=10, cursor="hand2").grid(row=1, column=0)
        btn_8=Button(calculator_frame,text="8", font=("arial", 15, "bold"), command=lambda:self.get_input(8), bd=5, width=4, pady=10, cursor="hand2").grid(row=1, column=1)
        btn_9=Button(calculator_frame,text="9", font=("arial", 15, "bold"), command=lambda:self.get_input(9), bd=5, width=4, pady=10, cursor="hand2").grid(row=1, column=2)
        btn_plus=Button(calculator_frame,text="+", font=("arial", 15, "bold"), command=lambda:self.get_input("+"), bd=5, width=4, pady=10, cursor="hand2").grid(row=1, column=3)


        btn_4=Button(calculator_frame,text="4", font=("arial", 15, "bold"), command=lambda:self.get_input(4), bd=5, width=4, pady=10, cursor="hand2").grid(row=2, column=0)
        btn_5=Button(calculator_frame,text="5", font=("arial", 15, "bold"), command=lambda:self.get_input(5), bd=5, width=4, pady=10, cursor="hand2").grid(row=2, column=1)
        btn_6=Button(calculator_frame,text="6", font=("arial", 15, "bold"), command=lambda:self.get_input(6), bd=5, width=4, pady=10, cursor="hand2").grid(row=2, column=2)
        btn_minus=Button(calculator_frame,text="-", font=("arial", 15, "bold"), command=lambda:self.get_input("-"), bd=5, width=4, pady=10, cursor="hand2").grid(row=2, column=3)


        btn_1=Button(calculator_frame,text="1", font=("arial", 15, "bold"), command=lambda:self.get_input(1), bd=5, width=4, pady=10, cursor="hand2").grid(row=3, column=0)
        btn_2=Button(calculator_frame,text="2", font=("arial", 15, "bold"), command=lambda:self.get_input(2), bd=5, width=4, pady=10, cursor="hand2").grid(row=3, column=1)
        btn_3=Button(calculator_frame,text="3", font=("arial", 15, "bold"), command=lambda:self.get_input(3), bd=5, width=4, pady=10, cursor="hand2").grid(row=3, column=2)
        btn_multipy=Button(calculator_frame,text="*", font=("arial", 15, "bold"), command=lambda:self.get_input("*"), bd=5, width=4, pady=10, cursor="hand2").grid(row=3, column=3)


        btn_0=Button(calculator_frame,text="0", font=("arial", 15, "bold"), command=lambda:self.get_input(0), bd=5, width=4, pady=15, cursor="hand2").grid(row=4, column=0)
        btn_c=Button(calculator_frame,text="C", font=("arial", 15, "bold"), command=self.clear_cal, bd=5, width=4, pady=15, cursor="hand2").grid(row=4, column=1)
        btn_equalto=Button(calculator_frame,text="=", font=("arial", 15, "bold"), command=self.perform_cal, bd=5, width=4, pady=15, cursor="hand2").grid(row=4, column=2)
        btn_divide=Button(calculator_frame,text="/", font=("arial", 15, "bold"), command=lambda:self.get_input("/"), bd=5, width=4, pady=15, cursor="hand2").grid(row=4, column=3)

        # ------ Cart Frame ------
        cart_frame=Frame(cal_cart_frame, bd=3, relief=RIDGE, bg="white")
        cart_frame.place(x=280, y=8, width=245, height=342)

        self.cart_title=Label(cart_frame, text="Cart \t Total Product: [0]", font=("times new roman", 15), bg="lightgray")
        self.cart_title.pack(side=TOP, fill=X)


        scrolly=Scrollbar(cart_frame,orient=VERTICAL, bg="gray", bd=4, relief=RIDGE)
        scrollx=Scrollbar(cart_frame,orient=HORIZONTAL, bg="gray", bd=4, relief=RIDGE)

        self.cartTable=ttk.Treeview(cart_frame,columns=("product_id", "product_name", "product_price", "product_quantity"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.cartTable.xview)
        scrolly.config(command=self.cartTable.yview)


        self.cartTable.heading("product_id",text="Product ID")
        self.cartTable.heading("product_name",text="Name")
        self.cartTable.heading("product_price",text="Price")
        self.cartTable.heading("product_quantity",text="Quantity")

        self.cartTable["show"]="headings"

        self.cartTable.column("product_id", width=72)
        self.cartTable.column("product_name", width=75)
        self.cartTable.column("product_price", width=72)
        self.cartTable.column("product_quantity", width=72)
        
        self.cartTable.pack(fill=BOTH, expand=1)
        self.cartTable.bind("<ButtonRelease-1>", self.get_data_cart)



        # ------ ADD Cart Buttons Frame -------
        self.var_product_id=StringVar()
        self.var_product_name=StringVar()
        self.var_product_price=StringVar()
        self.var_product_quantity=StringVar()
        self.var_product_stock=StringVar()
        
        cart_buttons_frame=Frame(self.root, bd=3, relief=RIDGE, bg="white")
        cart_buttons_frame.place(x=420, y=550, width=530, height=110)

        lbl_product_name=Label(cart_buttons_frame, text="Product Name", font=("times new roman", 15), bg="white").place(x=5, y=5)
        txt_product_name=Entry(cart_buttons_frame, textvariable=self.var_product_name, font=("times new roman", 15), bg="lightblue", state="readonly", bd=2, relief=RIDGE).place(x=5, y=35, width=190, height=22)


        lbl_product_price=Label(cart_buttons_frame, text="Price per QTY", font=("times new roman", 15), bg="white").place(x=230, y=5)
        txt_product_price=Entry(cart_buttons_frame, textvariable=self.var_product_price, font=("times new roman", 15), bg="lightblue", state="readonly", bd=2, relief=RIDGE).place(x=230, y=35, width=122, height=22)


        lbl_product_quantity=Label(cart_buttons_frame, text="Quantity", font=("times new roman", 15), bg="white").place(x=390, y=5)
        txt_product_quantity=Entry(cart_buttons_frame, textvariable=self.var_product_quantity, font=("times new roman", 15), bg="lightblue", bd=2, relief=RIDGE).place(x=390, y=35, width=100, height=22)


        self.lbl_product_stock=Label(cart_buttons_frame, text="In Stock", font=("times new roman", 15), bg="white")
        self.lbl_product_stock.place(x=5, y=70)


        btn_clear=Button(cart_buttons_frame, text="Clear", command=self.clear_cart, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, bg="lightgray", activebackground="lightgray", cursor="hand2").place(x=180, y=68, width=110, height=30)
        btn_add=Button(cart_buttons_frame, text="ADD | Update Cart", command=self.add_cart_update, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, bg="orange", activebackground="orange", cursor="hand2").place(x=300, y=68, width=200, height=30)


        # ------ Customer Biling Area -------
        bill_frame=Frame(self.root, bd=3, relief=RIDGE, bg="white")
        bill_frame.place(x=950, y=110, width=400, height=410)


        bill_title=Label(bill_frame, text="Customer Bill Area", font=("times new roman", 20, "bold"), bg="#f44336", fg="white").pack(side=TOP, fill=X)

        scrolly=Scrollbar(bill_frame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        self.txt_bill_area=Text(bill_frame, yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_bill_area.yview)



        # ------- Billing Butttons -------
        bill_menu_frame=Frame(self.root, bd=3, relief=RIDGE, bg="white")
        bill_menu_frame.place(x=950, y=520, width=400, height=140)


        self.lbl_amount=Label(bill_menu_frame, text="Bill Amount\n[0]", font=("old goudy style", 15, "bold"), bd=3, relief=RIDGE, bg="#3f51b5", fg="white")
        self.lbl_amount.place(x=2, y=5, width=120, height=70)


        self.lbl_discount=Label(bill_menu_frame, text="Discount\n[5%]", font=("old goudy style", 15, "bold"), bd=3, relief=RIDGE, bg="#8bc34a", fg="white")
        self.lbl_discount.place(x=124, y=5, width=120, height=70)


        self.lbl_net_pay=Label(bill_menu_frame, text="Net PAY\n[0]", font=("old goudy style", 15, "bold"), bd=3, relief=RIDGE, bg="#607d8b", fg="white")
        self.lbl_net_pay.place(x=246, y=5, width=148, height=70)


        btn_print=Button(bill_menu_frame, text="Print", command=self.print_bill, font=("old goudy style", 15, "bold"), bd=3, relief=RIDGE, bg="lightgreen", fg="black", activebackground="lightgreen", activeforeground="black", cursor="hand2")
        btn_print.place(x=2, y=80, width=120, height=50)


        btn_clear_all=Button(bill_menu_frame, text="Clear ALL", command=self.clear_all, font=("old goudy style", 15, "bold"), bd=3, relief=RIDGE, bg="gray", activebackground="gray", cursor="hand2")
        btn_clear_all.place(x=124, y=80, width=120, height=50)


        btn_generate=Button(bill_menu_frame, text="Generate/\nSave Bill", command=self.generate_bill, font=("old goudy style", 13, "bold"), bd=3, relief=RIDGE, bg="#009688", activebackground="#009688", cursor="hand2")
        btn_generate.place(x=246, y=80, width=148, height=50)




        # ------ Footer ------
        footer=Label(self.root, text="IMS-Inventory Management System | Developed by Nadeem\n For any tecnical issue contact : sk.nadeem@gmail.com", font=("times new roman", 11), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)



        self.show()
        
        self.update_date_time()

    # ------- All Functions ------


    def get_input(self, num):
           anum=self.var_calculator_input.get()+str(num)
           self.var_calculator_input.set(anum)



    def clear_cal(self):
         self.var_calculator_input.set("")


    def perform_cal(self):
         result=self.var_calculator_input.get()
         self.var_calculator_input.set(eval(result))



    def show(self):
        con=sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
            c.execute("Select product_id, product_name, product_price, product_quantity, product_status from product where product_status='Active'")
            rows=c.fetchall()
            self.productTable.delete(*self.productTable.get_children())

            for row in rows:
                self.productTable.insert("", END, values=row)
            


        except Exception as ex:
            messagebox.showerror("Error:", f"Error due to {str(ex)}", parent=self.root)




    def search(self):
        con = sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
        # Check if search option and input text are provided
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Search Input Should Be Required.", parent=self.root)
            else:
            # Build query with column name
                c.execute("SELECT product_id, product_name, product_price, product_quantity, product_status FROM product WHERE product_name LIKE '%"+self.var_search.get()+"%' and product_status='Active' ")
                rows = c.fetchall()  # This must be indented to be part of the try block
        
                if len(rows) != 0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "No Record Found.", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error:", f"Error due to {str(ex)}", parent=self.root)




    def get_data(self, ev):
        f = self.productTable.focus()
        content = self.productTable.item(f)
        row = content["values"]

        self.var_product_id.set(row[0])
        self.var_product_name.set(row[1])
        self.var_product_price.set(row[2])
        self.lbl_product_stock.config(text=f"In Stock [{str(row[3])}]")
        self.var_product_stock.set(row[3])
        self.var_product_quantity.set("1")


    def get_data_cart(self, ev):
        f = self.cartTable.focus()
        content = self.cartTable.item(f)
        row = content["values"]

        self.var_product_id.set(row[0])
        self.var_product_name.set(row[1])
        self.var_product_price.set(row[2])
        self.var_product_quantity.set(row[3])
        self.lbl_product_stock.config(text=f"In Stock [{str(row[4])}]")
        self.var_product_stock.set(row[4])



    def add_cart_update(self):
        if self.var_product_id.get()=="":
            messagebox.showerror("Error", "Please Select Product From the List.")
        elif self.var_product_quantity.get()=="":
            messagebox.showerror("Error", "Quantity is Required", parent=self.root)
        elif int(self.var_product_quantity.get()) > int(self.var_product_stock.get()):
            messagebox.showerror("Error", "Invalid Quantity!", parent=self.root)
        
        else:
            # price_calculator=int(float(self.var_product_quantity.get())*float(self.var_product_price.get()))
            # price_calculator=float(price_calculator)
            
            price_calculator=self.var_product_price.get()

            cart_data=[self.var_product_id.get(), self.var_product_name.get(), price_calculator, self.var_product_quantity.get(), self.var_product_stock.get()]

            # ------- Update Cart -------
            present="no"
            index_=0

            for row in self.cart_list:
                if self.var_product_id.get()==row[0]:
                    
                    present="yes"
                    break
                index_+=1

            if present=="yes":
                op=messagebox.askyesno("Confirm", "Product Alredy Present\nDo you Wnat to Update | Remove from the Cart List.", parent=self.root)
                if op == True:
                    if self.var_product_quantity.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        # self.cart_list[index_][2]=price_calculator # Calculating Price
                        self.cart_list[index_][3]=self.var_product_quantity.get() # Quantity
            else:
                self.cart_list.append(cart_data)

            self.show_cart()
            self.bill_updates()


    def bill_updates(self):
        self.bill_amount=0
        self.net_pay=0
        for row in self.cart_list:
            self.bill_amount=self.bill_amount+(float(row[2])*int(row[3]))
        
        self.discount=(self.bill_amount*5)/100
        self.net_pay= self.bill_amount-self.discount

        self.lbl_amount.config(text=f"Bill Amount\n{str(self.bill_amount)}")
        self.lbl_net_pay.config(text=f"Net Pay\n{str(self.net_pay)}")
        self.cart_title.config(text=f"Cart \t Total Product: [{str(len(self.cart_list))}]")



    def show_cart(self):
        try:
            self.cartTable.delete(*self.cartTable.get_children())

            for row in self.cart_list:
                self.cartTable.insert("", END, values=row)
            


        except Exception as ex:
            messagebox.showerror("Error:", f"Error due to {str(ex)}", parent=self.root)



    def generate_bill(self):
        if self.var_customer_name.get=="" or self.var_customer_contact.get()=="":
            messagebox.showerror("Error", "Customer details Must Be Required", parent=self.root)
        
        elif len(self.cart_list)==0:
            messagebox.showerror("Error", "Please Add Product in to the Cart")
        
        
        else:
            #------- Bill Top ------
            self.bill_top()
            #------- Bill Middle ------
            self.bill_middle()
            #------- Bill Bottom ------
            self.bill_bottom()

            fp=open(f"bill/{str(self.invoice)}.txt","w")
            fp.write(self.txt_bill_area.get("1.0", END))
            fp.close()
            messagebox.showinfo("Saved", "Bill has been Genrated/Save in Backend", parent=self.root)

            self.chk_print=1





    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%Y"))
        bill_top_template=f'''
\t\tIntern-Inventory
\tContact: sk.nadeem@gmail.com
{str("-"*46)}
 Customer Name: {self.var_customer_name.get()}
 Phone Number: {self.var_customer_contact.get()}
 Bill Number: {str(self.invoice)}\t\t\t  Date: {str(time.strftime("%d/%m/%y"))}
{str("-"*46)}
{str("-"*46)}
 Product Name:\t\t\tQTY:\tPrice:
{str("-"*46)}
        '''
        self.txt_bill_area.delete("1.0",END)
        self.txt_bill_area.insert("1.0", bill_top_template)


    def bill_middle(self):
        con = sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
            for row in self.cart_list:
                pid=row[0]
                name=row[1]
                qty=int(row[4])-int(row[3])
                if int(row[3]) == int(row[4]):
                    status="Inactive"
                if int(row[3]) < int(row[4]):
                    status="Active"

                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,"\n "+name+"\t\t\t"+row[3]+"\tRs."+price)

                # ------ Update Quantity in Product Table
                c.execute("Update product set product_quantity=?, product_status=? where product_id=?",(
                    qty,
                    status,
                    pid
                ))
                con.commit()

            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error:", f"Error due to {str(ex)}", parent=self.root)








    def bill_bottom(self):
        bill_bottom_template=f'''
{str("-"*46)}
{str("-"*46)}
 Bill Amount:\t\t\tRs.{self.bill_amount}
 Discount:\t\t\tRs.{self.discount}
 Net Pay:\t\t\tRs.{self.net_pay}
{str("-"*46)}\n
        '''
        self.txt_bill_area.insert(END, bill_bottom_template)




    def clear_cart(self):
        self.var_product_id.set("")
        self.var_product_name.set("")
        self.var_product_price.set("")
        self.var_product_quantity.set("")
        self.lbl_product_stock.config(text=f"In Stock")
        self.var_product_stock.set("")


    
    def clear_all(self):
        del self.cart_list[:]
        self.var_customer_name.set("")
        self.var_customer_contact.set("")
        self.txt_bill_area.delete("1.0", END)
        self.cart_title.config(text=f"Cart \t Total Product: [0]")
        self.var_search.set("")
        self.clear_cart()
        self.show()
        self.show_cart()

        self.chk_print=0
        


    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%y")
        self.lbl_clock.config(text=f"Welcome to Inventory Management System \t\t Date: {str(date_)} \t\t Time: {str(time_)}", font=("times new roman", 15), bg="gray", fg="white")
        self.lbl_clock.after(200,self.update_date_time)


    def logout(self):
        self.root.destroy()
        os.system("python login.py")
    



    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo("Print", "Please Wait While Printing", parent=self.root)
            new_file=tempfile.mktemp(".txt")
            open(new_file, 'w').write(self.txt_bill_area.get("1.0",END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror("Print", "Please Generate Bill to Print the Receipt", parent=self.root)



if __name__=="__main__":
    root = Tk()
    obj = billingClass(root)
    root.mainloop()

