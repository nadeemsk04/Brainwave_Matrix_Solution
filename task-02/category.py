from tkinter import *
from PIL import Image, ImageTk, ImageOps
from tkinter import ttk, messagebox
import sqlite3

class categoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+300+200")
        self.root.title("INVENTORY MANAGEMENT SYSTEM! Developed by Nadeem")
        self.root.config(bg="white")
        self.root.focus_force()

        # ------- Variables -------
        self.var_category_id = StringVar()
        self.var_category_name = StringVar()

        # ------- Title ------
        lbl_title = Label(self.root, text="Manage Product Category", font=("goudy old style", 30), bg="Green", fg="white", bd=4, relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=20)

        lbl_name = Label(self.root, text="Enter Category Name", font=("goudy old style", 30), bg="white").place(x=50, y=100)
        txt_name = Entry(self.root, textvariable=self.var_category_name, font=("goudy old style", 18), bg="lightblue").place(x=50, y=170, width=300)

        btn_add = Button(self.root, text="ADD", command=self.add, font=("goudy old style", 18), bg="green", fg="white", activebackground="green", activeforeground="white", cursor="hand2").place(x=360, y=170, width=150, height=30)
        btn_delete = Button(self.root, text="DELETE", command=self.delete, font=("goudy old style", 18), bg="red", fg="white", activebackground="red", activeforeground="white", cursor="hand2").place(x=520, y=170, width=150, height=30)

        # ------- Category Details -------
        # ------- Create a style for the Treeview -------
        style = ttk.Style()
        style.configure("Treeview.Heading",
                        background="lightblue",
                        foreground="black",
                        font=("goudy old style", 10, "bold"),
                        relief="solid",
                        borderwidth=1)
        

        category_frame = Frame(self.root, bd=3, relief=RIDGE)
        category_frame.place(x=700, y=100, width=380, height=100)

        scrolly = Scrollbar(category_frame, orient=VERTICAL)
        scrollx = Scrollbar(category_frame, orient=HORIZONTAL)

        self.categoryTable = ttk.Treeview(category_frame, columns=("category_id", "category_name"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)

        self.categoryTable.heading("category_id", text="Category ID")
        self.categoryTable.heading("category_name", text="Category Name")

        self.categoryTable["show"] = "headings"

        self.categoryTable.column("category_id", width=150)
        self.categoryTable.column("category_name", width=150)

        self.categoryTable.pack(fill=BOTH, expand=1)
        self.categoryTable.bind("<ButtonRelease-1>", self.get_data)

        # ------- Images -------
        self.im1 = Image.open("images/cat.jpg")
        self.im1 = self.im1.resize((500, 250), Image.Resampling.LANCZOS)
        self.im1 = ImageTk.PhotoImage(self.im1)

        self.lbl_im1 = Label(self.root, image=self.im1, bd=4, relief=RIDGE)
        self.lbl_im1.place(x=50, y=220)

        self.im2 = Image.open("images/category.jpg")
        self.im2 = self.im2.resize((500, 250), Image.Resampling.LANCZOS)
        self.im2 = ImageTk.PhotoImage(self.im2)

        self.lbl_im2 = Label(self.root, image=self.im2, bd=4, relief=RIDGE)
        self.lbl_im2.place(x=580, y=220)

        self.show()

    # ------- Functions -------
    def add(self):
        con = sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
            if self.var_category_name.get() == "":
                messagebox.showerror("Error", "Category Name must be required", parent=self.root)
            else:
                c.execute("SELECT * FROM category WHERE category_name=?", (self.var_category_name.get(),))
                row = c.fetchone()

                if row is not None:
                    messagebox.showerror("Error", "This Category is already present, try different.", parent=self.root)
                else:
                    c.execute("INSERT INTO category (category_name) VALUES(?)", (self.var_category_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Category Added Successfully", parent=self.root)

                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)




    def show(self):
        con=sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
            c.execute("Select * from category")
            rows=c.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())

            for row in rows:
                self.categoryTable.insert("", END, values=row)
            


        except Exception as ex:
            messagebox.showerror("Error:", f"Error due to {str(ex)}", parent=self.root)



    def get_data(self, ev):
        f = self.categoryTable.focus()  
        content = self.categoryTable.item(f)
        row = content["values"]
        
        self.var_category_id.set(row[0])
        self.var_category_name.set(row[1])
        


    def delete(self):
        con = sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
            if self.var_category_id.get() == "":
                messagebox.showerror("Error", "Please Select Category From the List", parent=self.root)
            else:
                c.execute("Select * from category where category_id=?", (self.var_category_id.get(),))
                row = c.fetchone()

                if row == None:
                    messagebox.showerror("Error", "Error, Please Try Again", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you want to delete this Category?", parent=self.root)
                    if op == True:

                        c.execute("delete from category where category_id=?",(self.var_category_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Category Deleted Successfully",parent=self.root)
                        self.show()


                        self.var_category_id.set("")
                        self.var_category_name.set("")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()
