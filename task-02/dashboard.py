from tkinter import *
from PIL import Image, ImageTk
from users import usersClass
from product import productClass
from category import categoryClass
from sales import salesClass
from tracking import inventoryClass
from reports import reportClass
import sqlite3
from tkinter import messagebox
from datetime import datetime
import os



class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+70+50")
        self.root.title("INVENTORY MANAGEMENT SYSTEM! Developed by Nadeem")
        self.root.config(bg="#51bb57")

        # ------- Title -------
        self.icon_title = PhotoImage(file="images\\logo1.png")
        title = Label(self.root, text="INVENTORY MANAGEMENT SYSTEM", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 40, "bold"), bg="green", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        # ------ Logout Button ------
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), command=self.logout, bg="yellow", cursor="hand2").place(x=1200, y=10, height=50, width=120)

        # ------ Clock -------
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System \t\t Date: DD-MM-YYYY \t\t Time:HH:MM:SS",
                               font=("times new roman", 15), bg="gray", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # ------ Left Menu ------
        # Load and resize the image using Pillow
        self.MenuLogo = Image.open("images/menu_im.png")
        self.MenuLogo = self.MenuLogo.resize((150, 130), Image.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        # Create the left menu frame
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=565)

        # Place the resized image in the left menu
        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)


        # ------ Menu Buttons ------
        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20, "bold"),
                            bg="#009688").pack(side=TOP, fill=X)
        

        btn_users = Button(LeftMenu, text="Users", font=("times new roman", 13, "bold"),
                            bg="purple", fg="white", activebackground="purple", activeforeground="white", cursor="hand2", command=self.users)
        btn_users.pack(side=TOP, fill=X, padx=10, pady=10 )
        

        btn_products = Button(LeftMenu, text="Products", font=("times new roman", 13, "bold"),
                            bg="purple", fg="white", activebackground="purple", activeforeground="white", cursor="hand2", command=self.products)
        btn_products.pack(side=TOP, fill=X, padx=10, pady=10 )


        btn_category = Button(LeftMenu, text="Category", font=("times new roman", 13, "bold"),
                            bg="purple", fg="white", activebackground="purple", activeforeground="white", cursor="hand2", command=self.category)
        btn_category.pack(side=TOP, fill=X, padx=10, pady=10 )


        btn_sales = Button(LeftMenu, text="Sales", font=("times new roman", 13, "bold"),
                            bg="purple", fg="white", activebackground="purple", activeforeground="white", cursor="hand2", command=self.sales)
        btn_sales.pack(side=TOP, fill=X, padx=10, pady=10 )


        btn_track = Button(LeftMenu, text="Track Inventory", font=("times new roman", 13, "bold"),
                            bg="purple", fg="white", activebackground="purple", activeforeground="white", cursor="hand2", command=self.inventory)
        btn_track.pack(side=TOP, fill=X, padx=10, pady=10 )


        btn_report = Button(LeftMenu, text="Report", font=("times new roman", 13, "bold"),
                            bg="purple", fg="white", activebackground="purple", activeforeground="white", cursor="hand2", command=self.report)
        btn_report.pack(side=TOP, fill=X, padx=10, pady=10 )


        btn_exit = Button(LeftMenu, text="Exit", font=("times new roman", 13, "bold"),
                            bg="purple", fg="white", activebackground="purple", activeforeground="white", cursor="hand2", command=root.quit)
        btn_exit.pack(side=TOP, fill=X, padx=10, pady=10 )




        # ------ Content -------
        
        self.lbl_users= Label(self.root, text="Total Users\n [ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style",20, "bold"))
        self.lbl_users.place(x=300, y=180, height=150, width=300)

        self.lbl_product= Label(self.root, text="Total Products\n [ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style",20, "bold"))
        self.lbl_product.place(x=625, y=180, height=150, width=300)

        self.lbl_category= Label(self.root, text="Total Categorys\n [ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style",20, "bold"))
        self.lbl_category.place(x=950, y=180, height=150, width=300)


        self.lbl_sales= Label(self.root, text="Total Sales\n [ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style",20, "bold"))
        self.lbl_sales.place(x=300, y=400, height=150, width=300)



        # ------- Footer -------
        lbl_footer = Label(self.root, text="Inventory Management System | Developed by Nadeem \n For Any Technical Issue mail our support team : sk.nadeem040402@gamil.com",
                               font=("times new roman", 11), bg="gray", fg="white")
        lbl_footer.pack(side=BOTTOM, fill=X)


        self.update_function()

    # # # -----------------------------------------------------
    def users(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=usersClass(self.new_win)
    
    
    def products(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)
    

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)


    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)


    def inventory(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=inventoryClass(self.new_win)


    def report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)
    

    def update_function(self):
        con = sqlite3.connect(database=r"inventory.db")
        c = con.cursor()

        try:
            c.execute("select * from users")
            users=c.fetchall()
            self.lbl_users.config(text=f"Total Users\n[ {str(len(users))} ]")


            c.execute("select * from product")
            product=c.fetchall()
            self.lbl_product.config(text=f"Total Products\n[ {str(len(product))} ]")


            c.execute("select * from category")
            category=c.fetchall()
            self.lbl_category.config(text=f"Total Categorys\n[ {str(len(category))} ]")


            self.lbl_sales.config(text=f"Total Sales\n[ {str(len(os.listdir('bill')))} ]")


            current_time=datetime.now().strftime("%I:%M:%S %p")
            current_date=datetime.now().strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Inventory Management System \t\t Date: {str(current_date)} \t\t Time: {str(current_time)}")
            self.lbl_clock.after(200, self.update_function)




        except Exception as ex:
            messagebox.showerror("Error:", f"Error due to {str(ex)}", parent=self.root)




    def logout(self):
        self.root.destroy()
        os.system("python login.py")
    

if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()

