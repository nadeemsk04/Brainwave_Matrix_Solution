from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class reportClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+300+200")
        self.root.title("INVENTORY REPORTS SYSTEM")
        self.root.config(bg="white")
        self.root.focus_force()

        # Search Variables
        self.var_category = StringVar()
        self.var_search_text = StringVar()
        self.var_search_by = StringVar()

        # ------ Search Frame -----
        searchFrame = LabelFrame(self.root, text="Search Products", font=("goudy old style", 12, "bold"), bd=2, relief=RIDGE, bg="white")
        searchFrame.place(x=250, y=0, width=600, height=70)

        # ----- Options -----
        cmb_search = ttk.Combobox(searchFrame, textvariable=self.var_search_by, values=("Select", "product_name", "product_category", "product_price"), state="readonly", justify=CENTER, font=("goudy old style", 12))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(searchFrame, textvariable=self.var_search_text, font=("goudy old style", 15), bg="lightyellow")
        txt_search.place(x=200, y=10)
        btn_search = Button(searchFrame, text="Search", command=self.search, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2")
        btn_search.place(x=430, y=8, width=150, height=30)

        # ------- Title ------
        title = Label(self.root, text="Inventory Reports", bd=4, relief=RIDGE, font=("goudy old style", 20), bg="green", fg="white")
        title.place(x=50, y=100, width=1000)

        # ------- Buttons -------
        btn_all_products = Button(self.root, text="Show All Products", command=self.show_all_products, font=("goudy old style", 15), bg="#2196f3", fg="white", activebackground="#2196f3", activeforeground="white", cursor="hand2")
        btn_all_products.place(x=300, y=150, width=200, height=40)

        btn_low_stock = Button(self.root, text="Low Stock Report", command=self.check_low_stock, font=("goudy old style", 15), bg="#f44336", fg="white", activebackground="#f44336", activeforeground="white", cursor="hand2")
        btn_low_stock.place(x=520, y=150, width=200, height=40)

        # ------- Product Details -------
        # ------- Create a style for the Treeview -------
        style = ttk.Style()
        style.configure("Treeview.Heading",
                        background="lightblue",
                        foreground="black",
                        font=("goudy old style", 10, "bold"),
                        relief="solid",       # Set relief to solid to create the border effect
                        borderwidth=1)
        

        product_frame = Frame(self.root, bd=3, relief=RIDGE)
        product_frame.place(x=0, y=210, relwidth=1, height=250)

        scrolly = Scrollbar(product_frame, orient=VERTICAL)
        scrollx = Scrollbar(product_frame, orient=HORIZONTAL)

        self.productTable = ttk.Treeview(product_frame, columns=("product_id", "product_category", "product_name", "product_quantity", "product_price"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)

        self.productTable.heading("product_id", text="Product ID")
        self.productTable.heading("product_category", text="Category")
        self.productTable.heading("product_name", text="Name")
        self.productTable.heading("product_quantity", text="Quantity")
        self.productTable.heading("product_price", text="Price")

        self.productTable["show"] = "headings"
        self.productTable.column("product_id", width=100)
        self.productTable.column("product_category", width=150)
        self.productTable.column("product_name", width=200)
        self.productTable.column("product_quantity", width=100)
        self.productTable.column("product_price", width=100)

        self.productTable.pack(fill=BOTH, expand=1)

    def show_all_products(self):
        """Display all products from the product table."""
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

        finally:
            con.close()

    def check_low_stock(self):
        """Check for products that are below the low stock threshold."""
        threshold = 10  # Set your low stock threshold
        con = sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
            c.execute("SELECT * FROM product WHERE product_quantity < ?", (threshold,))
            low_stock_items = c.fetchall()

            if low_stock_items:
                self.productTable.delete(*self.productTable.get_children())
                for item in low_stock_items:
                    self.productTable.insert("", END, values=item)
            else:
                messagebox.showinfo("Low Stock Report", "All products are in stock.", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error:", f"Error due to {str(ex)}", parent=self.root)

        finally:
            con.close()

    def search(self):
        """Search products based on the selected criteria."""
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
                    messagebox.showinfo("Info", "No Record Found.", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error:", f"Error due to {str(ex)}", parent=self.root)

        finally:
            con.close()

if __name__ == "__main__":
    root = Tk()
    obj = reportClass(root)
    root.mainloop()
