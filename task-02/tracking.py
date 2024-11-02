from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class inventoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+300+200")
        self.root.title("INVENTORY TRACKING SYSTEM! Developed by Nadeem")
        self.root.config(bg="white")
        self.root.focus_force()

        # All variables
        self.var_product_id = StringVar()
        self.var_product_name = StringVar()
        self.var_product_quantity = StringVar()
        self.var_recorder_level = StringVar()
        self.var_search_by = StringVar()
        self.var_search_text = StringVar()

        # Search Frame
        searchFrame = LabelFrame(self.root, text="Search Products", font=("goudy old style", 12, "bold"), bd=2, relief=RIDGE, bg="white")
        searchFrame.place(x=250, y=0, width=600, height=70)

        # Options
        cmb_search = ttk.Combobox(searchFrame, textvariable=self.var_search_by, values=("Select", "Product ID", "Product Name"), state="readonly", justify=CENTER, font=("goudy old style", 12))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(searchFrame, textvariable=self.var_search_text, font=("goudy old style", 15), bg="lightyellow").place(x=200, y=10)
        btn_search = Button(searchFrame, text="Search", command=self.search_product, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=430, y=8, width=150, height=30)

        # ------- Title -------
        title = Label(self.root, text="Track Inventory Levels", bd=4, relief=RIDGE, font=("goudy old style", 15), bg="green", fg="white").place(x=25, y=100, width=1040)

        # ------- Row 1 -------
        lbl_productid = Label(self.root, text="Product ID", font=("goudy old style", 10), bg="white").place(x=30, y=150)
        lbl_productname = Label(self.root, text="Product Name", font=("goudy old style", 10), bg="white").place(x=350, y=150)

        txt_productid = Entry(self.root, textvariable=self.var_product_id, font=("goudy old style", 13), bg="lightblue").place(x=140, y=150, width=180)
        txt_productname = Entry(self.root, textvariable=self.var_product_name, font=("goudy old style", 13), bg="lightblue").place(x=480, y=150, width=180)

        # ------- Row 2 -------
        lbl_productQuantity = Label(self.root, text="Product Quantity", font=("goudy old style", 10), bg="white").place(x=30, y=190)
        lbl_recorderLevel = Label(self.root, text="Recorder Level", font=("goudy old style", 10), bg="white").place(x=350, y=190)

        txt_productQuantity = Entry(self.root, textvariable=self.var_product_quantity, font=("goudy old style", 13), bg="lightblue").place(x=140, y=190, width=180)
        txt_recorderLevel = Entry(self.root, textvariable=self.var_recorder_level, font=("goudy old style", 13), bg="lightblue").place(x=480, y=190, width=180)

        # ------ Buttons -------
        btn_log = Button(self.root, text="Log Change", command=self.log_inventory_change, font=("goudy old style", 15), bg="#2196f3", fg="white", activebackground="#2196f3", activeforeground="white", cursor="hand2").place(x=500, y=275, width=130, height=30)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white", activebackground="#607d8b", activeforeground="white", cursor="hand2").place(x=650, y=275, width=130, height=30)

        # ------- Product Details -------
        # ------- Create a style for the Treeview -------
        style = ttk.Style()
        style.configure("Treeview.Heading",
                        background="lightblue",
                        foreground="black",
                        font=("goudy old style", 10, "bold"),
                        relief="solid",       
                        borderwidth=1)
        
        
        product_frame = Frame(self.root, bd=3, relief=RIDGE)
        product_frame.place(x=0, y=312, relwidth=1, height=185)

        scrolly = Scrollbar(product_frame, orient=VERTICAL)
        scrollx = Scrollbar(product_frame, orient=HORIZONTAL)

        self.productTable = ttk.Treeview(product_frame, columns=("product_id", "product_name", "product_quantity", "recorder_level"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)

        self.productTable.heading("product_id", text="Product ID")
        self.productTable.heading("product_name", text="Product Name")
        self.productTable.heading("product_quantity", text="Quantity")
        self.productTable.heading("recorder_level", text="Recorder Level")

        self.productTable["show"] = "headings"
        self.productTable.column("product_id", width=200)
        self.productTable.column("product_name", width=200)
        self.productTable.column("product_quantity", width=200)
        self.productTable.column("recorder_level", width=200)

        self.productTable.pack(fill=BOTH, expand=1)
        self.productTable.bind("<ButtonRelease-1>", self.get_data)

        # Show all products initially
        self.show_products()


#-----------------------------------------------------------------------------------
    def show_products(self):
        con = sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
            c.execute("SELECT * FROM product")
            rows = c.fetchall()
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
        self.var_product_name.set(row[1])
        self.var_product_quantity.set(row[2])
        self.var_recorder_level.set(row[3])




    def search_product(self):
        """Search for a product based on Product ID or Product Name."""
        con = sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
            if self.var_search_by.get() == "Select":
                messagebox.showerror("Error", "Select Search By Option", parent=self.root)
            elif self.var_search_text.get() == "":
                messagebox.showerror("Error", "Search Input Should Be Required.", parent=self.root)
            else:
                query = f"SELECT * FROM product WHERE {self.var_search_by.get().replace(' ', '_').lower()} LIKE ?"
                c.execute(query, (f"%{self.var_search_text.get()}%",))
                rows = c.fetchall()

                if rows:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "No Record Found.", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error:", f"Error due to {str(ex)}", parent=self.root)



    def log_inventory_change(self):
        """Log inventory change based on user input."""
        product_id = self.var_product_id.get()
        product_name = self.var_product_name.get()
        quantity = self.var_product_quantity.get()
        recorder_level = self.var_recorder_level.get()

    # Basic validation
        if self.var_product_id.get() == "":
            messagebox.showerror("Error", "Product ID must be required", parent=self.root)

    # Try to log the inventory change
        con = sqlite3.connect(database=r"inventory.db")
        try:
            con.execute("PRAGMA foreign_keys = ON")  # Enable foreign key constraints
            c = con.cursor()
        
            c.execute('''INSERT INTO tracking (product_id, product_name, quantity, recorder_level)
                         VALUES (?, ?, ?, ?)''', 
                      (product_id, product_name, quantity, recorder_level))
        
            con.commit()
            messagebox.showinfo("Success", "Inventory change logged successfully.", parent=self.root)
    
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while logging the inventory change: {e}", parent=self.root)

        finally:
            con.close()  # Ensure the connection is closed



    def clear(self):
        """Clear all input fields."""
        self.var_product_id.set("")
        self.var_product_name.set("")
        self.var_product_quantity.set("")
        self.var_recorder_level.set("")
        self.show_products()




if __name__ == "__main__":
    root = Tk()
    obj = inventoryClass(root)
    root.mainloop()
